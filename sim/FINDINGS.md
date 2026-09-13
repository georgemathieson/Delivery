# What the simulation found

Numbers from `RESULTS.md`. Read `README.md` first for what the model does not represent.

**Six findings. Four of them contradict or qualify something in `docs/`.**

---

## 1 · A WIP limit can be too tight — the playbook doesn't say so

| WIP limit | Days to clear 400 items |
|---|---|
| 3 | 373 |
| **4** | **338** |
| 6 | 347 |
| 9 | 416 |
| 12 | 558 |
| 18 | 718 |

Three engineers. The optimum is around 4–6, not 3. At a limit of 3, a blocked item idles
a person — there is nothing else to pick up — so the system starves.

**The contradiction.** `docs/04-policies.md` says *"a limit that is never hit is not a
limit. If it hasn't bound in three weeks, lower it."* Followed without a floor, that
drives a team past the optimum into starvation, and the chart it would need to notice
(blocked-while-idle) isn't in the measure set.

**Correction made:** the policy now states a floor of roughly one item per person plus a
small buffer, and says to stop lowering when throughput falls.

The magnitude is worth keeping in view though: going from 12 to 6 nearly halves delivery
time with the same people. The direction of the playbook's advice is strongly supported;
only the unbounded version of it is wrong.

## 2 · Horizontal slicing costs ~29% of delivery time, invisibly

| Paired items | Days to clear 400 | Cycle time p85 | Rework days |
|---|---|---|---|
| 0% | 347 | 8.1 | 0 |
| 40% | 391 | 9.2 | 63 |
| 80% | 442 | 10.0 | 132 |

Same 400 items, same base effort. The only change is that paired items cannot be released
until both halves are done, with a chance of a mismatch when they meet.

This **confirms** `docs/10-story-slicing.md`, including the mechanism: the cost surfaces
as rework inside the second half, so the first half stays on record as fast and clean.

Note the p50–p95 spread barely moves (7.5 → 7.8) while delivery time rises 29%. A team
watching only the spread would not see this.

## 3 · Expedites are not much worse than queued work — until volume rises

| Scenario | Days to clear 400 |
|---|---|
| No extra demand | 347 |
| 2 unplanned/sprint (queues) | 390 |
| 2 expedites/sprint (pre-empts) | 392 |
| 5 expedites/sprint | 484 |

At two per sprint, pre-empting costs almost exactly what queueing costs — 392 vs 390.

**The contradiction.** `docs/04-policies.md` presents expedites as categorically more
damaging than unplanned work because they pre-empt. In this model that is not true at low
volume: **the harm is in the volume, not the pre-emption.** The queue-jumping matters for
fairness and for predictability of *individual* items, but the delivery cost is
essentially the added demand.

**Correction made:** the expedite policy no longer claims pre-emption is the primary harm.
It still recommends limiting the lane — because tracking frequency is what surfaces the
volume — but for the honest reason.

## 4 · "Pull the oldest first" makes the median slightly *worse*

| Pull rule | Backlog wait p50 | Backlog wait p95 |
|---|---|---|
| Oldest first | 131 | **247** |
| Newest first | **118** | 322 |

Newest-first wins on the median and loses badly on the tail. Delivery time and cycle time
are unchanged either way.

This is the classic FIFO/LIFO trade, and it means **oldest-first is a predictability
choice, not a speed choice**. Anyone who adopts it expecting things to get faster, and
then measures the median, will conclude it made things worse — and they will be right on
that measure.

**Correction made:** `docs/04-policies.md` now says this explicitly.

## 5 · The core four cannot see starvation — a real gap in the measure set

In the experiment above, cycle time p95 was 11.6 (oldest-first) versus 11.8
(newest-first): indistinguishable. Backlog wait p95 differed by **75 days**.

Cycle time is measured start-to-finish. Everything that happens to an item *before*
someone starts it is invisible to every one of the core four in `docs/02-measures.md`.

A team could have items rotting in the backlog for a year and see nothing but healthy
charts. This is the same blind spot as the sprint-boundary problem, one stage upstream.

**Correction made:** `docs/02-measures.md` adds backlog wait (age in the ready queue) as a
fifth measure, and notes that the core four are a *system* view, not a *customer* view.

## 6 · Monte Carlo is honest when stable — and more history makes it worse in a shift

**Stable capacity** (expected: 50 / 35 / 15)

| Window | Below 50th | 50–85th | Beyond 85th |
|---|---|---|---|
| 6 weeks | 54% | 33% | 14% |
| 12 weeks | 48% | 42% | 10% |
| 24 weeks | 47% | 46% | 7% |

**Capacity shifting** — ~20/sprint, then ~25, then ~8

| Window | Below 50th | 50–85th | Beyond 85th |
|---|---|---|---|
| 6 weeks | 54% | 23% | **23%** |
| 12 weeks | 52% | 25% | **22%** |
| 24 weeks | 46% | 21% | **33%** |

Two things:

**The method is sound.** Under stable capacity, a 6-week window is nearly perfectly
calibrated. Longer windows drift slightly conservative — which is safe.

**Longer history is more dangerous, not safer.** When capacity shifts, a 24-week window
puts a third of actuals beyond its own 85th percentile: it is still averaging in a
regime that no longer exists. The intuition that more data is better is wrong here.

This also gives the calibration record in `docs/12-success-criteria.md` a specific job:
**a run of actuals beyond the 85th is the signature of a regime change, not of bad luck.**
Shorten the window rather than apologising for the forecast.

**Correction made:** `docs/04-policies.md` now recommends a rolling window of roughly 6–12
weeks, and says what a cluster of late actuals means.

## 7 · The aging chart does not predict — and that is fine

| Scenario | Items flagged at 70th band | Share of total delay in them | Days still to run |
|---|---|---|---|
| WIP 6 | 25% | 83% | 3.9 |
| WIP 12 | 28% | 88% | 10.0 |

First, a caveat that applies to any aging chart anywhere: asking whether crossing the 70th
band predicts passing the 85th is **tautological**. Any item past the 70th percentile was
by definition still open when it crossed it. Recall is always 1.0 and precision is always
about 0.5, in every system. An aging chart has no predictive skill in the statistical
sense.

What it has is **attention allocation**, and that is genuinely strong: a quarter of items
carry over four-fifths of the excess delay. Looking at that quarter is an excellent use
of thirty minutes.

**The qualification.** `docs/02-measures.md` said an item past the 85th band is
*"statistically, in trouble now"*. That overclaims. It is not a prediction — it is a
report that the item is already unusual, which is useful for a different reason.

Note the third column: a worse system (WIP 12) gives you *more* warning time. Comfortable
aging charts in a high-WIP team are not a sign of health.

---

## What this does not test

The simulated team never swarms, splits an aged item, escalates a blocker or removes a
constraint. So this tests the **standing policies** and says nothing about the **cadence**
— the weekly review, the constraint hour, the whole of `docs/03-operating-cadence.md`.

Given the constraint hour is the thing most likely to be dropped and most likely to
matter, the highest-value part of the playbook remains untested. That is a limitation of
simulation, not an oversight: you would have to model human attention, and any result
would be a property of your assumptions about people.
