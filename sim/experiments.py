"""
Experiments against the flow model.

Each experiment holds the seed and the backlog constant and varies ONE policy,
so the difference is attributable. Every result is averaged over many seeds -
a single run of a stochastic model tells you nothing.

Run:  python3 sim/experiments.py  >  sim/RESULTS.md
"""

from __future__ import annotations

import random
import statistics
import sys
from dataclasses import replace

sys.path.insert(0, __file__.rsplit("/", 1)[0])

from flowsim import (SPRINT_DAYS, Config, aging_band_test, calibration_percentile,
                     percentile, simulate, summarise)

SEEDS = list(range(20))


def mean_over_seeds(cfg: Config, key_fn, seeds=SEEDS):
    vals = [key_fn(simulate(replace(cfg, seed=s))) for s in seeds]
    if isinstance(vals[0], dict):
        vals = [v for v in vals if v]
        keys = vals[0].keys()
        return {k: statistics.mean(v[k] for v in vals) for k in keys}
    return statistics.mean(vals)


def row(*cells) -> str:
    return "| " + " | ".join(str(c) for c in cells) + " |"


def f(x, n=1) -> str:
    return f"{x:.{n}f}"


# --------------------------------------------------------------------------

def exp_wip():
    print("## 1 · WIP limit\n")
    print("Same backlog, same effort, same blockers. Only the WIP limit changes.\n")
    print(row("WIP limit", "Days to clear 400 items", "Cycle time p50",
              "p85", "p95", "p50–p95 spread", "Mean WIP"))
    print(row("---", "---", "---", "---", "---", "---", "---"))
    base = Config(sprints=60)
    for limit in [3, 4, 6, 9, 12, 18]:
        cfg = replace(base, wip_limit=limit)
        s = mean_over_seeds(cfg, summarise)
        print(row(limit, f(s["days_to_clear_backlog"], 0), f(s["ct_p50"]),
                  f(s["ct_p85"]), f(s["ct_p95"]), f(s["ct_spread"]), f(s["wip_mean"])))
    print()


def exp_slicing():
    print("## 2 · Horizontal slicing (WIP-in-disguise)\n")
    print("A fraction of items are paired: each is individually finishable, but "
          "neither is *releasable* until its partner is done. Item count and "
          "effort are unchanged.\n")
    print(row("Paired items", "Days to clear 400 items", "Cycle time p85",
              "p50–p95 spread", "Rework days incurred"))
    print(row("---", "---", "---", "---", "---"))
    base = Config(sprints=60, wip_limit=6)
    for frac in [0.0, 0.2, 0.4, 0.6, 0.8]:
        cfg = replace(base, horizontal_fraction=frac)
        s = mean_over_seeds(cfg, summarise)
        print(row(f"{int(frac*100)}%", f(s["days_to_clear_backlog"], 0),
                  f(s["ct_p85"]), f(s["ct_spread"]), f(s["rework_days_total"], 0)))
    print()


def exp_expedites():
    print("## 3 · Expedites\n")
    print("Expedites pre-empt: they start immediately regardless of the WIP limit. "
          "Unplanned work queues instead. Both add the same amount of effort.\n")
    print(row("Scenario", "Days to clear 400 items", "Cycle time p85",
              "p50–p95 spread", "Mean WIP"))
    print(row("---", "---", "---", "---", "---"))
    base = Config(sprints=60, wip_limit=6)
    scenarios = [
        ("No extra demand", replace(base)),
        ("2 unplanned /sprint (queued)", replace(base, unplanned_per_sprint=2)),
        ("2 expedites /sprint (pre-empt)", replace(base, expedite_per_sprint=2)),
        ("5 expedites /sprint", replace(base, expedite_per_sprint=5)),
    ]
    for name, cfg in scenarios:
        s = mean_over_seeds(cfg, summarise)
        print(row(name, f(s["days_to_clear_backlog"], 0), f(s["ct_p85"]),
                  f(s["ct_spread"]), f(s["wip_mean"])))
    print()


def exp_pull_order():
    print("## 4 · Pull order\n")
    print("Oldest-first versus newest-first, everything else identical. "
          "Cycle time is measured start-to-finish; backlog wait is how long an "
          "item sat before anyone started it.\n")
    print(row("Pull rule", "Days to clear 400 items", "Cycle time p95",
              "Backlog wait p50", "Backlog wait p95"))
    print(row("---", "---", "---", "---", "---"))
    # Arrivals over time, otherwise LIFO and FIFO are mathematically symmetric.
    base = Config(sprints=60, wip_limit=6, arrivals_per_sprint=14, initial_ready=20)
    for label, oldest in [("Oldest first", True), ("Newest first", False)]:
        s = mean_over_seeds(replace(base, pull_oldest_first=oldest), summarise)
        print(row(label, f(s["days_to_clear_backlog"], 0), f(s["ct_p95"]),
                  f(s["queue_wait_p50"], 0), f(s["queue_wait_p95"], 0)))
    print()


def _calibration_run(base: Config, window: int, target: int = 30):
    landed = {"<50th": 0, "50-85th": 0, ">85th": 0}
    for seed in SEEDS:
        res = simulate(replace(base, seed=seed))
        weekly = res.throughput_per_week()
        cum, total = [], 0
        for t in weekly:
            total += t
            cum.append(total)
        for origin in range(window, len(weekly) - 12, 4):
            hist = weekly[max(0, origin - window):origin]
            if not hist or sum(hist) == 0:
                continue
            start_done = cum[origin - 1]
            actual = None
            for w in range(origin, len(weekly)):
                if cum[w] - start_done >= target:
                    actual = w - origin + 1
                    break
            if actual is None:
                continue
            p = calibration_percentile(hist, target, actual)
            if p < 50:
                landed["<50th"] += 1
            elif p < 85:
                landed["50-85th"] += 1
            else:
                landed[">85th"] += 1
    return landed


def _print_calibration(label: str, landed: dict):
    n = sum(landed.values())
    if not n:
        print(f"**{label}** — no valid forecasts\n")
        return
    print(f"**{label}** — {n} forecasts\n")
    print(row("Actual landed", "Share", "Expected if calibrated"))
    print(row("---", "---", "---"))
    print(row("Below 50th pct", f"{100*landed['<50th']/n:.0f}%", "50%"))
    print(row("50th–85th", f"{100*landed['50-85th']/n:.0f}%", "35%"))
    print(row("Beyond 85th pct", f"{100*landed['>85th']/n:.0f}%", "15%"))
    print()


def exp_regime_and_forecast():
    print("## 5 · Forecast calibration\n")
    print("Monte Carlo forecasts made every 4 weeks for the next 30 items, using "
          "only throughput the team could have observed at that moment. A "
          "well-calibrated forecast puts 50% of actuals below its 50th "
          "percentile and 15% beyond its 85th.\n")
    print("The backlog is enlarged to 1200 items so it never runs dry — "
          "otherwise the end of the backlog is mistaken for a capacity change.\n")

    print("### 5a · Stable capacity — is the method itself calibrated?\n")
    stable = Config(sprints=40, wip_limit=6, backlog_size=1200)
    tps = simulate(stable).throughput_per_sprint()
    print(f"Realised throughput per sprint (one run): `{tps[:12]}…`\n")
    for window in [6, 12, 24]:
        _print_calibration(f"Trailing window {window} weeks", _calibration_run(stable, window))

    print("### 5b · Capacity shifts — ~20/sprint, then ~25, then ~8\n")
    profile = [1.08] * 12 + [1.38] * 12 + [0.42] * 30
    shifting = replace(stable, capacity_profile=profile)
    tps = simulate(shifting).throughput_per_sprint()
    print(f"Realised throughput per sprint (one run): `{tps[:30]}…`\n")
    for window in [6, 12, 24]:
        _print_calibration(f"Trailing window {window} weeks", _calibration_run(shifting, window))


def exp_aging():
    print("## 6 · What an aging chart actually buys you\n")
    print("Flagging at the 70th percentile band. Note that asking whether the "
          "70th band *predicts* passing the 85th is tautological — any item past "
          "the 70th was by definition open when it crossed it. So this measures "
          "attention allocation instead.\n")
    print(row("Scenario", "Items flagged", "Share of total delay in flagged items",
              "Days still to run once flagged"))
    print(row("---", "---", "---", "---"))
    scenarios = [
        ("WIP 6, clean slicing", Config(sprints=60, wip_limit=6)),
        ("WIP 12, clean slicing", Config(sprints=60, wip_limit=12)),
        ("WIP 6, 60% paired items", Config(sprints=60, wip_limit=6,
                                           horizontal_fraction=0.6)),
    ]
    for name, cfg in scenarios:
        a = mean_over_seeds(cfg, aging_band_test)
        print(row(name, f"{100*a['flagged_share']:.0f}%",
                  f"{100*a['delay_share_in_flagged']:.0f}%",
                  f(a["mean_remaining_once_flagged"])))
    print()


def main():
    print("# Simulation results\n")
    print("Generated by `sim/experiments.py`. 3 engineers, 400-item backlog, "
          "15-day sprints, averaged over 20 seeds per configuration.\n")
    print("**These are properties of a model, not evidence about your teams.** "
          "See `sim/README.md` for what the model does and does not represent.\n")
    print("---\n")
    exp_wip()
    exp_slicing()
    exp_expedites()
    exp_pull_order()
    exp_regime_and_forecast()
    exp_aging()


if __name__ == "__main__":
    main()
