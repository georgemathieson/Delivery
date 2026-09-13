# 04 — Explicit policies

Kanban's most underrated idea: **make policies explicit**. Most delivery variability
comes from implicit, differently-understood rules about when work starts, when it's
blocked, and what done means. Writing them down removes a surprising amount of
variation on its own.

These are defaults. Each team should adapt them in `teams/<team>/policies.md` and own
them. A policy the team didn't agree to is a rule, and rules get routed around.

---

## Definition of Started

An item moves to In Progress only when **all** of these are true:

- [ ] Someone is actively working on it today — not "assigned to"
- [ ] It has been through 3 amigos (or the team has explicitly waived it)
- [ ] No known unresolved dependency, decision, or access blocks the first step
- [ ] The team is under its WIP limit

**Why:** starting an item that cannot progress converts a queue you can see (the
backlog) into age you can't (in-progress time). This directly tests hypothesis H2.

---

## Definition of Done

Done means **in production, or in the hands of the user**. Not code complete, not merged,
not "done pending release".

If your release process genuinely prevents this, then represent the release queue on the
board as an explicit state and measure it. Do not hide it by redefining done — that
relocates the delay somewhere the data can't see, which is exactly hypothesis H5.

---

## WIP limits

**Starting point:** current average WIP, minus 20%. Set it, hold it for three weeks, then
review.

- Limits apply per state where a queue forms — particularly **code review** and **ready
  for test**, not just "in progress".
- A limit that is never hit is not a limit. If it hasn't bound in three weeks, lower it.
- When the limit is hit, the team **finishes something before starting something**. That
  usually means swarming on the oldest item, which is the point.

The uncomfortable few weeks after a WIP limit is introduced are the intervention
working, not failing. People feel idle before they feel fast. Say this to the teams in
advance or the limit will be quietly abandoned in week two.

---

## Age limits

Derived from your own cycle-time distribution, refreshed quarterly.

| Item age | What happens |
|---|---|
| Past the 70th percentile | Flagged on the board (colour/tag). Visible, no action required |
| Past the 85th percentile | Discussed at the next standup with a named next action and owner |
| Past the 95th percentile | Escalated to you. Either unblock it, split it, or explicitly stop it |

**"Explicitly stop it" is a real option** and is used far too rarely. An item that has
been in progress for four times the typical cycle time is telling you something about
its readiness or its value. Abandoning it is often the correct call, and normalising
that is one of the more valuable cultural changes available to you.

---

## Blocked

- Any item that cannot progress **today**, for any reason, is marked blocked. Including
  "waiting for review" and "waiting for someone to come back from leave".
- Blocked items carry a **reason tag** from a fixed list: `dependency`, `decision`,
  `environment`, `external-party`, `people`, `defect`, `unclear-requirement`.
- Blocked days are counted and reviewed monthly by reason.
- Anything blocked for more than 2 days is raised in the weekly flow review.

The fixed tag list matters more than it looks. Free-text blocker reasons cannot be
aggregated, and aggregation is the entire point — one item blocked on environments is
bad luck; thirty blocked days a month on environments is a business case.

---

## Unplanned work

**What this means: demand arriving from outside the team.** Production support, an
escalation, a favour for another team, "can you just look at this". *Not* the tasks
involved in delivering something already on the board.

- All unplanned work goes on the board. No exceptions, including work that takes an
  hour. Especially work that takes an hour — small interrupts are the ones that never get
  recorded, and they add up to a quarter of a team's capacity without anyone noticing.
- It is tagged `unplanned` so it can be counted.
- It counts against the WIP limit like anything else.
- Reserve explicit capacity for it based on the measured percentage — don't pretend
  it's zero and absorb it invisibly.

### The test

> **Is this new demand, or is it part of delivering something already on the board?**

Duration is not the test. A two-hour support request is unplanned work. A two-day
refactor needed to finish the story in progress is not — it is that story.

See "Tasks, items and enablers" in `docs/10-story-slicing.md` for the second half of
that distinction.

**And it must be included in the throughput history that feeds Monte Carlo.** If
unplanned work consumes 25% of capacity but is absent from the data, the simulation is
forecasting a team that has 33% more capacity than the one you actually have. This is
one of the most common reasons a technically correct Monte Carlo forecast is
consistently optimistic.

---

## Expedites

Different from unplanned work, and more damaging: an expedite **pre-empts** work already
in progress. Unplanned work joins the queue; an expedite jumps it, and everything it
jumped pays for it.

- **Limit the expedite lane — even if the limit is one.** A second expedite waits, or
  something gives way visibly.
- **Define entry criteria.** What genuinely qualifies? Write it down before the next one
  arrives, because in the moment everything qualifies.
- **Track the frequency.** If you are expediting weekly, it is not an exception, it is a
  process failure. Count them monthly alongside blocked days.
- **Make the cost visible.** Every expedite delays something else. Name what it delayed,
  in the review, out loud. Treat them like a credit card: usable, but paid off.

Expedites should be rare, deliberate, and slightly uncomfortable. That discomfort is the
signal they are being used responsibly — a frictionless expedite lane becomes the default
route within a quarter.

And ask the question underneath, which is the one that actually fixes it:

> **What are we doing wrong that makes so many things urgent?**

Recurring expedites are almost never a series of unrelated emergencies. They are a
symptom — of intake that isn't managed, of forecasts nobody believes, or of quality
problems surfacing late.

*(Policy shape from Paul Brown, ["The Dirty Secret Behind Agile
Failure"](https://thrivve.partners/the-dirty-secret-behind-agile-failure).)*

---

## Ongoing prioritisation

Most teams prioritise at intake and then never again. Once work is in progress it goes
out of sight, and old items linger while newer, shinier ones leapfrog them.

In a flow system prioritisation is continuous, and the daily decision is not *what to
start* but **what to finish next**.

- Visualise work item age, so the decision has information behind it.
- When all else is equal, **pull the oldest item first**.
- Have an explicit pull policy, so this isn't re-argued every morning.

Work waiting silently is not harmless. It is accruing risk and decay while looking like
nothing is happening.

---

## Right-sizing

Right-sizing is already in place. To keep it honest:

- The rule is a **time-based** one, not a complexity judgement: if the team believes an
  item will take more than N days of elapsed time, split it. Set N from the 85th
  percentile of your current cycle time.
- Splitting happens **before** starting, not at the sprint boundary. Splitting an
  in-flight item to make it "finish" corrupts the throughput history (H4).
- If an in-progress item turns out to be too big, that is a legitimate reason to split —
  but record it as a split, and keep the original start date on the remainder so the age
  doesn't reset to zero. **Resetting age to zero is how carryover hides.**

---

## Forecasting

- Forecasts are always ranges with a confidence level, never single dates. Already in
  place — protect it.
- The throughput history feeding the simulation must be from the **same system**:
  same team, same composition, includes unplanned work, no boundary-split artefacts.
- Re-forecast on a fixed schedule (monthly) and when scope materially changes. Do not
  re-forecast because someone dislikes the answer.
- Record every forecast in `teams/<team>/forecasts.md` **at the time it is made**, with
  the distribution. You cannot measure calibration retrospectively, and the temptation
  to remember a forecast as more accurate than it was is very strong.
