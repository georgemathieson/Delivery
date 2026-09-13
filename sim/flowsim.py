"""
Flow simulation: a delivery system you can run policies against.

Deliberately separates three things that are conflated in real life:

  ground truth  - hidden effort, real blockers. The simulation knows these.
  observation   - what a team could actually measure (start/finish dates).
  policy        - what the team does (WIP limits, pull order, slicing).

That separation is the point. It lets us ask not only "did the policy help"
but "would the team's own instruments have told them the truth" - which is
untestable in a real organisation, because you never see ground truth.

Pure standard library. No dependencies.
"""

from __future__ import annotations

import math
import random
import statistics
from dataclasses import dataclass, field

SPRINT_DAYS = 15


# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

@dataclass
class Config:
    # System
    engineers: int = 3
    backlog_size: int = 400
    sprints: int = 30
    seed: int = 7

    # Item effort (hidden ground truth), lognormal - right-skewed like real work
    effort_median: float = 1.6           # median engineer-days of touch time
    effort_sigma: float = 0.55           # spread; higher = more variable work

    # Blocking (hidden ground truth)
    block_prob_per_day: float = 0.06     # chance an in-progress item blocks today
    block_days_mean: float = 2.2         # mean duration of a block

    # Policy: work in progress
    wip_limit: int | None = None         # None = unlimited (pull whenever free)
    max_effort_per_item_per_day: float = 1.0   # 1.0 = no swarming

    # Policy: context switching penalty when WIP exceeds people
    switching_penalty: bool = True

    # Policy: pull order
    pull_oldest_first: bool = True       # else: newest / shiniest first

    # Policy: slicing. Fraction of items that cannot finish alone -
    # they are paired and both must complete before either is releasable.
    horizontal_fraction: float = 0.0
    # Late integration: when the two halves finally meet, chance they disagree
    # (the API returns an id, the UI needed a name). Rework lands on both.
    pair_rework_prob: float = 0.45
    pair_rework_effort: float = 0.9      # engineer-days added to EACH half

    # Demand: expedites that pre-empt, and unplanned work that queues
    expedite_per_sprint: float = 0.0
    unplanned_per_sprint: float = 0.0

    # Continuous arrivals. With a static backlog, LIFO and FIFO are symmetric
    # and pull order cannot matter; real backlogs are fed over time.
    arrivals_per_sprint: float = 0.0
    initial_ready: int | None = None      # rest of the backlog arrives over time

    # Capacity regime per sprint (multiplier on engineer-days).
    # Models holidays, incidents, attrition, onboarding.
    capacity_profile: list[float] = field(default_factory=list)

    def capacity_on(self, day: int) -> float:
        base = float(self.engineers)
        if not self.capacity_profile:
            return base
        sprint = day // SPRINT_DAYS
        mult = self.capacity_profile[min(sprint, len(self.capacity_profile) - 1)]
        return base * mult


# --------------------------------------------------------------------------
# Items
# --------------------------------------------------------------------------

@dataclass
class Item:
    id: int
    effort: float                  # hidden: engineer-days of touch time required
    partner: int | None = None     # horizontal slice: both must finish together
    expedite: bool = False
    unplanned: bool = False

    started: int | None = None     # observable
    finished: int | None = None    # observable
    remaining: float = 0.0         # hidden
    blocked_until: int = -1        # hidden until observed as "blocked"
    blocked_days: int = 0          # observable if the team tags blockers
    code_complete: int | None = None  # hidden: effort exhausted, may await partner
    arrived: int = 0               # observable: when it entered the backlog
    reworked: bool = False         # hidden: has late integration already bitten?
    rework_days: float = 0.0       # hidden: extra effort caused by late integration

    def __post_init__(self) -> None:
        self.remaining = self.effort

    @property
    def queue_wait(self) -> int | None:
        """Days sitting in the backlog before being started. Invisible to a
        cycle-time chart, which only starts counting once work begins."""
        return (self.started - self.arrived) if self.started is not None else None

    @property
    def cycle_time(self) -> int | None:
        if self.started is None or self.finished is None:
            return None
        return self.finished - self.started

    def age_at(self, day: int) -> int | None:
        if self.started is None or (self.finished is not None and self.finished <= day):
            return None
        return day - self.started


# --------------------------------------------------------------------------
# Simulation
# --------------------------------------------------------------------------

@dataclass
class Result:
    items: list[Item]
    wip_by_day: list[int]
    finished_by_day: list[int]
    days: int
    config: Config

    def completed(self) -> list[Item]:
        return [i for i in self.items if i.finished is not None]

    def cycle_times(self) -> list[int]:
        return [i.cycle_time for i in self.completed() if i.cycle_time is not None]

    def throughput_per_sprint(self) -> list[int]:
        n = self.days // SPRINT_DAYS
        out = []
        for s in range(n):
            lo, hi = s * SPRINT_DAYS, (s + 1) * SPRINT_DAYS
            out.append(sum(self.finished_by_day[lo:hi]))
        return out

    def throughput_per_week(self) -> list[int]:
        out = []
        for w in range(self.days // 5):
            out.append(sum(self.finished_by_day[w * 5:(w + 1) * 5]))
        return out


def percentile(values: list[float], p: float) -> float:
    """Nearest-rank percentile. p in 0..100."""
    if not values:
        return float("nan")
    s = sorted(values)
    k = max(0, min(len(s) - 1, math.ceil(p / 100 * len(s)) - 1))
    return float(s[k])


def build_backlog(cfg: Config, rng: random.Random) -> list[Item]:
    items: list[Item] = []
    mu = math.log(cfg.effort_median)
    for i in range(cfg.backlog_size):
        effort = rng.lognormvariate(mu, cfg.effort_sigma)
        items.append(Item(id=i, effort=effort))

    # Horizontal slicing: pair up a fraction of items so neither can finish alone.
    n_pairs = int(cfg.backlog_size * cfg.horizontal_fraction / 2)
    pool = list(range(cfg.backlog_size))
    rng.shuffle(pool)
    for p in range(n_pairs):
        a, b = pool[2 * p], pool[2 * p + 1]
        items[a].partner = b
        items[b].partner = a
    return items


def simulate(cfg: Config) -> Result:
    rng = random.Random(cfg.seed)
    backlog = build_backlog(cfg, rng)
    by_id = {i.id: i for i in backlog}

    if cfg.arrivals_per_sprint and cfg.initial_ready is not None:
        ready = list(backlog[:cfg.initial_ready])
        pending = list(backlog[cfg.initial_ready:])
    else:
        ready = list(backlog)      # not yet started
        pending = []
    in_progress: list[Item] = []
    wip_by_day: list[int] = []
    finished_by_day: list[int] = []

    total_days = cfg.sprints * SPRINT_DAYS
    next_expedite_id = cfg.backlog_size

    for day in range(total_days):
        # --- new backlog items arriving over time ---------------------------
        if pending and cfg.arrivals_per_sprint:
            n = 0
            while pending and rng.random() < cfg.arrivals_per_sprint / SPRINT_DAYS:
                it = pending.pop(0)
                it.arrived = day
                ready.append(it)
                n += 1
                if n > 5:
                    break

        # --- demand arriving from outside -----------------------------------
        if cfg.expedite_per_sprint and rng.random() < cfg.expedite_per_sprint / SPRINT_DAYS:
            it = Item(id=next_expedite_id,
                      effort=rng.lognormvariate(math.log(cfg.effort_median), cfg.effort_sigma),
                      expedite=True)
            next_expedite_id += 1
            by_id[it.id] = it
            backlog.append(it)
            it.started = day                 # expedites pre-empt: they start now
            in_progress.append(it)

        if cfg.unplanned_per_sprint and rng.random() < cfg.unplanned_per_sprint / SPRINT_DAYS:
            it = Item(id=next_expedite_id,
                      effort=rng.lognormvariate(math.log(cfg.effort_median), cfg.effort_sigma),
                      unplanned=True)
            next_expedite_id += 1
            by_id[it.id] = it
            backlog.append(it)
            ready.insert(0, it)              # unplanned work queues, at the front

        # --- pull new work --------------------------------------------------
        while ready:
            if cfg.wip_limit is not None and len(in_progress) >= cfg.wip_limit:
                break
            if cfg.wip_limit is None and len(in_progress) >= cfg.engineers:
                break                        # unlimited policy still needs a hand free
            # A team facing a half-finished pair pulls the other half next -
            # otherwise the first half sits in WIP forever. Modelling that
            # avoids an artificial deadlock while keeping the real cost:
            # the pair is effectively one larger batch.
            idx = None
            for j, cand in enumerate(ready):
                if cand.partner is not None and by_id[cand.partner] in in_progress:
                    idx = j
                    break
            if idx is None:
                idx = 0 if cfg.pull_oldest_first else len(ready) - 1
            nxt = ready.pop(idx)
            nxt.started = day
            in_progress.append(nxt)

        # --- blocking -------------------------------------------------------
        for it in in_progress:
            if it.blocked_until >= day:
                it.blocked_days += 1
                continue
            if it.code_complete is None and rng.random() < cfg.block_prob_per_day:
                dur = max(1, int(rng.expovariate(1 / cfg.block_days_mean)))
                it.blocked_until = day + dur
                it.blocked_days += 1

        # --- allocate effort ------------------------------------------------
        workable = [i for i in in_progress
                    if i.blocked_until < day and i.code_complete is None]
        capacity = cfg.capacity_on(day)

        if cfg.switching_penalty and len(in_progress) > cfg.engineers:
            # Weinberg-style loss: ~20% per concurrent stream beyond one per person
            excess = len(in_progress) / max(1, cfg.engineers)
            capacity *= max(0.35, 1.0 - 0.18 * (excess - 1))

        if workable:
            share = capacity / len(workable)
            per_item = min(share, cfg.max_effort_per_item_per_day)
            for it in workable:
                it.remaining -= per_item
                if it.remaining <= 0:
                    it.code_complete = day

        # --- late integration -----------------------------------------------
        # The moment both halves are code-complete is the first time anything
        # is actually proven. This is where a mismatch surfaces - at its most
        # expensive point, and the cost lands silently inside the second half.
        for it in list(in_progress):
            if it.partner is None or it.code_complete is None or it.reworked:
                continue
            p = by_id[it.partner]
            if p.code_complete is None:
                continue
            if rng.random() < cfg.pair_rework_prob:
                for half in (it, p):
                    half.reworked = True
                    half.code_complete = None
                    half.remaining = cfg.pair_rework_effort
                    half.rework_days += cfg.pair_rework_effort
            else:
                it.reworked = p.reworked = True

        # --- finish ---------------------------------------------------------
        done_today = 0
        for it in list(in_progress):
            if it.code_complete is None:
                continue
            if it.partner is not None:
                p = by_id[it.partner]
                if p.code_complete is None:
                    continue                 # WIP-in-disguise: waits for its other half
            it.finished = day + 1
            in_progress.remove(it)
            done_today += 1

        finished_by_day.append(done_today)
        wip_by_day.append(len(in_progress))

    return Result(items=backlog, wip_by_day=wip_by_day,
                  finished_by_day=finished_by_day, days=total_days, config=cfg)


# --------------------------------------------------------------------------
# Monte Carlo forecasting - exactly what a team would do with observed data
# --------------------------------------------------------------------------

def monte_carlo_days(weekly_history: list[int], items_remaining: int,
                     trials: int = 3000, rng: random.Random | None = None) -> list[int]:
    """How many WEEKS to finish `items_remaining`, sampling observed weekly throughput."""
    rng = rng or random.Random(1)
    hist = [h for h in weekly_history] or [1]
    out = []
    for _ in range(trials):
        done, weeks = 0, 0
        while done < items_remaining and weeks < 500:
            done += rng.choice(hist)
            weeks += 1
        out.append(weeks)
    return out


def forecast_percentiles(weekly_history: list[int], items_remaining: int,
                         ps=(50, 85, 95)) -> dict[int, float]:
    sims = monte_carlo_days(weekly_history, items_remaining)
    return {p: percentile(sims, p) for p in ps}


def calibration_percentile(weekly_history: list[int], items_remaining: int,
                           actual_weeks: int) -> float:
    """Where did the actual outcome land in the forecast distribution? 0-100."""
    sims = monte_carlo_days(weekly_history, items_remaining)
    # Mid-rank for ties. Forecasts are in whole weeks, so ties are common;
    # counting them as "not below" biases every percentile downwards and
    # makes a perfectly calibrated method look optimistic.
    below = sum(1 for s in sims if s < actual_weeks)
    equal = sum(1 for s in sims if s == actual_weeks)
    return 100.0 * (below + 0.5 * equal) / len(sims)


# --------------------------------------------------------------------------
# Observation helpers - what the team's charts would show
# --------------------------------------------------------------------------

def aging_band_test(res: Result, flag_pct: float = 70.0) -> dict:
    """
    What does flagging an item at the `flag_pct` band actually buy you?

    NOTE, and this is a real limitation of the technique: "does crossing the
    70th band predict ending beyond the 85th?" is TAUTOLOGICAL. Any item whose
    cycle time exceeds the 70th percentile was, by definition, open when it
    crossed that band - so it is flagged. Recall is always 1.0 and precision is
    always ~(100-85)/(100-70) = 0.5, in any system whatsoever. An aging chart
    does not predict. It reports that an item is already unusual.

    So measure what it is actually for - attention allocation:
      - how many items get flagged (the cost of looking)
      - what share of total delay sits in flagged items (the value of looking)
      - how long a flagged item still has to run (the window you have to act)
    """
    cts = res.cycle_times()
    if not cts:
        return {}
    band = percentile(cts, flag_pct)
    med = percentile(cts, 50)

    flagged = [c for c in cts if c > band]
    excess_total = sum(max(0, c - med) for c in cts)
    excess_flagged = sum(max(0, c - med) for c in flagged)

    return {
        "flag_band_days": band,
        "flagged_share": len(flagged) / len(cts),
        "delay_share_in_flagged": (excess_flagged / excess_total) if excess_total else 0.0,
        "mean_remaining_once_flagged": (statistics.mean([c - band for c in flagged])
                                        if flagged else 0.0),
    }


def summarise(res: Result) -> dict:
    cts = res.cycle_times()
    tps = res.throughput_per_sprint()
    comp = res.completed()
    original = [i for i in comp if i.id < res.config.backlog_size]
    all_done = (max(i.finished for i in original)
                if len(original) == res.config.backlog_size else float("nan"))
    return {
        "completed": len(comp),
        "days_to_clear_backlog": all_done,
        "throughput_sprint_mean": statistics.mean(tps) if tps else 0,
        "throughput_sprint_stdev": statistics.pstdev(tps) if len(tps) > 1 else 0,
        "ct_p50": percentile(cts, 50),
        "ct_p85": percentile(cts, 85),
        "ct_p95": percentile(cts, 95),
        "ct_spread": percentile(cts, 95) - percentile(cts, 50),
        "wip_mean": statistics.mean(res.wip_by_day),
        "blocked_days_total": sum(i.blocked_days for i in comp),
        "rework_days_total": sum(i.rework_days for i in comp),
        "queue_wait_p50": percentile([i.queue_wait for i in comp
                                      if i.queue_wait is not None], 50),
        "queue_wait_p95": percentile([i.queue_wait for i in comp
                                      if i.queue_wait is not None], 95),
    }
