# 02 — Measures

Three rules before any of the specifics.

1. **Every measure must have an owner and an action.** If nobody would do anything
   differently based on the number, delete the number.
2. **Measure the system, not the people.** The moment a measure is used to compare
   individuals, it stops measuring anything real. Say this out loud when you introduce
   them, and then behave accordingly.
3. **Distributions, not averages.** Average cycle time is close to meaningless — the
   distribution is right-skewed, so the average sits somewhere nobody actually
   experiences. Always quote percentiles.

---

## The core four

### 1. Work Item Age — *the most important chart you will run*

For every item currently in progress: calendar days since it entered the first active
state. Plotted against the cycle-time percentile bands of finished work.

**Why it matters:** it is the only leading indicator in this list. It tells you an item
is in trouble while you can still do something about it. An item at the 85th percentile
of your historical cycle time and still open is, statistically, in trouble now.

**Action it drives:** in the weekly review, walk items from oldest to newest and ask a
single question of each — *what is stopping this finishing today?* Not "how's it going".

**Policy:** any item past the 85th percentile band gets an owner and a named next action
before the meeting ends. Past the 95th, it gets escalated to you.

**Be precise about what the band means.** It is *not* a prediction. Asking whether
crossing the 70th band predicts passing the 85th is tautological — any item past the 70th
percentile was by definition open when it crossed it, in any system whatsoever. An aging
chart has no predictive skill.

What it has is **attention allocation**, and that is strong enough on its own:
simulation (`sim/FINDINGS.md`, finding 7) found roughly a quarter of items carry over
four-fifths of the excess delay. Looking at that quarter is an excellent use of thirty
minutes. The chart reports that an item is *already* unusual — which is useful for a
different reason than prediction, and worth saying accurately, because a team that is
promised prediction will notice it isn't getting one.

### 2. Work in Progress (WIP)

Count of items in any active or waiting state, per team, per day.

**Why it matters:** WIP is the lever with the most direct, most immediate effect on
cycle time (Little's Law: cycle time = WIP ÷ throughput). Halve WIP at constant
throughput and you halve cycle time. It is the cheapest intervention available and
almost always the right first one.

**Action it drives:** set an explicit limit; when the limit is hit, the team finishes
something before starting something.

**Watch for:** WIP that looks flat because items sit in a state the board doesn't count.

### 3. Throughput

Count of items finished per week, per team. A run chart, not an average.

**Why it matters:** this is the input to Monte Carlo. Its **stability** matters more
than its level. A team finishing 6–8 items every week is far more valuable than one
averaging 10 with a range of 2–20, because the first can be forecast and the second
cannot.

**Action it drives:** if the run chart is spiky, find the spikes' causes before trying
to raise the level. And check the spikes aren't sprint-boundary artefacts — a saw-tooth
pattern that peaks on the last day of every sprint is a batching signal, not a
performance signal.

### 4. Cycle Time distribution

Elapsed calendar days from started to done, for finished items. Report as a scatterplot
over time with 50th / 70th / 85th / 95th percentile lines.

**Why it matters:** it defines the age bands in measure 1, and the spread is your
predictability. A shrinking spread is the goal. The 85th percentile is the number to
quote to stakeholders — "most items land within N days" — not the average.

**Action it drives:** track the **gap** between 50th and 95th percentile over time. That
gap narrowing is the single clearest evidence that predictability work is working.

**The second reason cycle time matters — worth using with stakeholders:**

> **Cycle time is time to feedback. In the absence of knowable ROI, it is your risk
> exposure.**

Most of what gets built is a bet. Value is unconfirmed until someone on the receiving end
says it helped. So every day an item is open is a day spent without learning whether the
bet was right — and the only thing worse than being wrong is being wrong slowly.

This reframes cycle time from a delivery metric into a **risk metric**, which is a
language stakeholders already speak. You cannot measure return on work that hasn't
landed; you can control how long you are exposed before finding out.

*(Framing from Paul Brown, ["The Dirty Secret Behind Agile
Failure"](https://thrivve.partners/the-dirty-secret-behind-agile-failure).)*

---

### 5. Backlog wait — the one the core four cannot see

Days between an item entering the backlog and someone starting it.

**Why it matters:** everything above measures start-to-finish. Whatever happens to an item
*before* work begins is invisible to all four. Simulation (`sim/FINDINGS.md`, finding 5)
found two pull policies with cycle-time 95th percentiles of 11.6 and 11.8 days —
indistinguishable — whose backlog waits differed by 75 days at the 95th percentile.

A team can have items rotting in the backlog for a year and see nothing but healthy
charts. This is the sprint-boundary blind spot one stage upstream: **the core four are a
system view, not a customer view.** From outside, the wait is part of the wait.

**Action it drives:** if backlog wait has a long tail, either the backlog contains work
nobody intends to do — delete it, it is costing you honesty — or intake exceeds capacity
(`docs/11-demand-and-intake.md`).

---

## Supporting measures

| Measure | Definition | What it tells you | Tests |
|---|---|---|---|
| Wait-state breakdown | Days per item split by state, active vs waiting | Where the delay actually is | H5 |
| Blocked days by reason | Total days blocked, grouped by tagged reason | Whether blockers are systemic or one-off | H6 |
| Started-to-first-activity | Days from "started" to first commit/PR/real activity | Work pulled before it was ready | H2 |
| Unplanned work % | Items created mid-sprint not in the plan ÷ total throughput | Hidden capacity drain, and whether the forecast history is honest | H3 |
| Expedite frequency | Count of items that pre-empted work in progress, per month | Whether urgency is running the system | H3 |
| Arrival vs departure rate | Items started per week vs finished per week | Whether WIP is structurally growing | H1 |
| Aging carryover | Items open across 2+ sprint boundaries | Whether the boundary is hiding age | H4 |
| Forecast accuracy | Actual delivery date vs the forecast distribution it fell in | Whether the forecast is calibrated | — |

### Forecast accuracy, specifically

This is how you objectively measure predictability rather than asserting it. For each
completed forecast, record which percentile of the original forecast distribution the
actual outcome landed in.

Over many forecasts, those percentiles should be **uniformly distributed**. If actuals
consistently land above the 85th percentile, your forecasts are optimistic and the
input history is unrepresentative (look hard at H3 and H4). If they consistently land
below the 30th, you are sandbagging and burning credibility in the other direction.

Track this. It converts "are we predictable?" from an opinion into a number, and it is
the thing that will most directly earn stakeholder trust over a year.

---

Where the organisation requires a risk register, these measures are what it should be
scored from — `docs/15-risk-register.md` maps each signal to the register entry it
generates, so likelihood and impact are read off data rather than guessed in a workshop.

---

## What to stop measuring

| Stop | Why |
|---|---|
| Velocity | Already retired. Don't let it return under a new name (e.g. "items per sprint" used as a target). |
| Say/do ratio, sprint commitment % | Measures conformance to a boundary you have decided is arbitrary. Rewards under-committing. |
| Flow efficiency as a headline | Gameable, needs suspiciously precise activity data, and conflates two distinct problems. Use the wait-state breakdown instead. |
| Average cycle time | The distribution is skewed; the average describes nobody. Use percentiles. |
| Individual throughput | Guarantees local optimisation and kills the collaboration that actually reduces cycle time. |
| Estimate accuracy | You removed estimates deliberately. Measuring their accuracy reintroduces them. |

---

## Baseline first

Before changing anything: collect four to six weeks of the core four, per team, and
write the numbers into `teams/<team>/baseline.md`. Without a baseline you cannot tell
improvement from noise, and you will end up arguing about whether things got better.
