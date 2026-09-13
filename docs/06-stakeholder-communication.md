# 06 — Stakeholder communication

You already give probabilistic ranges. That is the hard part and it is done. This
document is about protecting it, because probabilistic forecasting fails in
organisations for social reasons far more often than mathematical ones.

---

## The three failure modes

### 1. The range gets collapsed back into a date

Someone takes "85% confident by 12 March" and writes "12 March" in the steering pack.
From then on you are accountable to a date you never gave.

**Counter:** never state a single percentile alone. Always give at least two points —
"50% by 20 February, 85% by 12 March". A pair cannot be collapsed without visibly
discarding information, and people are reluctant to be seen doing that.

### 2. The range is treated as a negotiation opening

"Can you do the 50% date?" The range gets read as padding to be haggled down.

**Counter:** be explicit that the percentile is a statement about **risk appetite**, not
effort. "We can plan to the 50% date if you're comfortable being late half the time.
For anything with an external dependency, I'd use the 85%." Put the choice back where it
belongs — with the person carrying the consequence.

### 3. The forecast is blamed when reality differs

The 15% case happens, and probabilistic forecasting is judged to have "not worked".

**Counter:** this is what the forecast-accuracy record is for. If you can show that over
twelve forecasts, actuals landed roughly uniformly across the distribution, then the
15% case occurring is the model working exactly as advertised. Without that record you
have only an argument; with it you have evidence. **Start keeping it now**, before you
need it.

---

## What to send monthly

Derived from the monthly delivery review — same numbers, reshaped. Never maintain two
sets of figures.

**Per initiative:**
- Forecast: two percentiles, with the date the forecast was made
- Movement since last month, and *why* it moved (scope added, throughput changed,
  blocker resolved) — movement without a cause reads as guessing
- Confidence trend: is the range narrowing as we get closer? It should be. A range that
  isn't narrowing means we're learning nothing, and that is worth saying out loud

**Per team, one line each:**
- Throughput stability, cycle time 85th percentile, and its direction of travel

**One section, program-wide:**
- The systemic constraint you're working on, and what you need from them to remove it

That last section is the most valuable thing in the report. It converts the pack from a
status update into a request, and it is what makes stakeholders participants rather than
an audience.

---

## Language that helps

| Instead of | Say |
|---|---|
| "We're committed to 12 March" | "We're 85% confident of 12 March" |
| "It'll take about 6 weeks" | "Most work like this lands within 4–9 weeks" |
| "We slipped" | "The forecast moved out by 2 weeks; here's what changed" |
| "The team underperformed" | "Cycle time widened; we're working on why" |
| "Can you commit?" | "What confidence level do you need for this decision?" |

That last one is the single most useful question available to you. Most date requests
are not really about dates — they are about a downstream decision someone needs to make.
Asking what the date is *for* very often reveals that an 85% date two weeks later is
completely acceptable, or that they needed a different answer entirely.

---

## On the word "commitment"

You will be asked for one. The honest position is that a team can commit to effort,
attention, priority and transparency — but an outcome that depends on unknowns cannot
be committed to, only forecast. Saying otherwise is a promise you'd have to break.

You don't have to win this argument philosophically. In practice it is enough to say:
*"I can give you the date I'm most confident about, and I'll tell you the moment that
changes — which is worth more than a promise I'd have to break later."* Most
stakeholders, given a forecast that updates honestly and early, stop asking for
commitments within a couple of quarters. The thing they actually wanted was **no
surprises**, and that is something you can genuinely deliver.

The reliability you're being asked for is not "hit the date". It is "never be surprised
by you". Build for that.
