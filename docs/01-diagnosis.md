# 01 — Diagnosis: why the current practices haven't moved delivery

## What has been introduced, and what each one actually does

| Practice | What it genuinely improves | What it does **not** touch |
|---|---|---|
| 3 amigos sessions | Shared understanding; fewer defects from misread intent; fewer mid-flight scope reversals | How long an item waits between people |
| Removing hours, then points, in favour of right-sizing | Variability in item **size**; time spent estimating; the "points as productivity" trap | Variability in item **elapsed time**, which is dominated by waiting, not working |
| Monte Carlo simulation | Honesty of the forecast; replaces a single date with a distribution | The behaviour of the system being forecast. A simulation describes; it does not intervene |
| Lagging indicators on stories | After-the-fact confirmation of what happened | Any ability to act while the work is still in flight |

Every one of these is a good practice. Together they form a well-described system.
None of them form a **faster or less variable** system.

This is the central point: **Monte Carlo tells you the truth about a system you have
not yet changed.** If the forecast is uncomfortable, the correct response is to change
the system, not to re-run the simulation.

## The measurement gap

Lagging indicators can only tell you that a sprint ended badly. By then every decision
that caused it has already been made. Predictability work needs **in-flight** signals —
things you can see while an item is still open and still influenceable:

- How old is each in-progress item, right now?
- How many items are in progress at once, right now?
- How long has each blocked item been blocked, right now?

None of these require the item to finish. All of them are actionable today. This is the
single biggest change in this repo: move the centre of gravity from *what happened* to
*what is happening*.

## The sprint-boundary contradiction

Stakeholders already receive probabilistic ranges. That is the harder half of the
change and it is already done. But if the internal scorecard is still "did we finish
what we pulled into the sprint", two incompatible units of account are running at once:

- The **forecast** is probabilistic, continuous, and about a body of work reaching done.
- The **sprint** is deterministic, batched, and about a fixed scope reaching a fixed date.

A flow system measured against a fixed-scope boundary will fail that boundary
indefinitely, however good the stories are. Nicolas Brown's point — that there is no
such thing as a committed outcome — applies internally as much as externally. You have
retired the committed outcome for stakeholders; it is still in force for the teams.

**Decide explicitly which unit you are managing by.** Recommendation: keep the sprint
as a *cadence* for planning, review and retrospective, and retire it as a *commitment
container*. Sprint success stops being "we finished what we said" and becomes "flow was
stable and aging stayed inside policy". If a team needs a scoreboard, give them
throughput stability and aging — not scope completion.

A tell worth checking: if sprints routinely end with carryover but the Monte Carlo
forecast remains roughly accurate, the teams are not unpredictable. Only the sprint
boundary is.

## Live hypotheses

Ordered by likelihood for 2–3 mostly-independent teams with right-sized stories.
Each has a falsification test — do not debate these, measure them.

H3, H4, H7 and H8 all corrupt or exclude data the others rely on, so rule them out first
(`docs/08-diagnostic-decision-tree.md`). A confident diagnosis built on a polluted
throughput history is worse than no diagnosis.

### H1 — Too much work in progress
Items are started faster than they are finished, so everything is simultaneously
half-done and nothing lands inside the boundary. This is the most common cause by a
wide margin, and it is invisible in lagging indicators because finished items still
eventually finish.

*Test:* plot WIP per team per day against throughput per week. If WIP is drifting up
while throughput is flat, this is your answer. Also check average items in progress
divided by team size — anything above ~1 concurrent item per person warrants scrutiny.

*If true:* set a WIP limit below current average and hold it. Expect it to feel wrong
for two to three weeks.

### H2 — Work is started before it is genuinely ready
Right-sizing makes items small, but small is not the same as ready. An item pulled
without a decision, a dependency, an environment or an acceptance answer will sit
in-progress accruing age while the real constraint is elsewhere.

*Test:* measure time from "started" to first commit / first meaningful activity. A long
gap means the item was pulled before work could actually begin. Also measure how many
items are blocked within 48 hours of being started.

*If true:* an explicit definition of started (`docs/04-policies.md`) plus a ready buffer.

### H3 — Unplanned and interrupt work is eating capacity silently
Production support, escalations, "quick favours", and work that arrives directly to an
individual. If it isn't on the board it isn't in the forecast, and the Monte Carlo
simulation is being fed a systematically optimistic history.

*Test:* count items created *during* the sprint that were not in it at the start, as a
percentage of throughput. Ask each team to log interrupt time for two weeks. If
unplanned work is above ~20% of throughput and is not represented in the data feeding
the simulation, the forecast is structurally wrong.

*If true:* make it visible on the board, reserve explicit capacity for it, and include
it in the throughput history that feeds the forecast.

### H4 — Carryover masked by re-splitting
Items that don't finish get split at the sprint boundary so that "something" completes.
This corrupts both the throughput history and the cycle-time distribution — the data
feeding Monte Carlo now describes a system that doesn't exist.

*Test:* look for items created near a sprint boundary whose titles or parents duplicate
an item closed at the same boundary. Look for a cycle-time distribution with an
implausibly short left tail.

*If true:* stop splitting at boundaries. Let items age visibly across them.

### H5 — The delay is downstream of development
Code complete is not done. Review, QA, environment availability, release windows, and
change approval are all queues. If the team's "in progress" ends at development, the
delay simply relocates to somewhere the board doesn't show.

*Test:* break cycle time down by state. Compare time in active states against time in
waiting states (review, ready-for-test, ready-for-release, blocked).

*If true:* pull those states onto the board, then limit WIP in them specifically. Review
queues in particular respond very well to a WIP limit.

### H7 — Fractional allocation and team instability

People split across teams or projects at percentages, or team composition churning.
Someone at "50% on each of two teams" does not deliver half on each — context switching
takes a cut off the top, and they are a shared resource both teams queue behind.

This one matters disproportionately because **Monte Carlo assumes a stable system**. If
membership changed three months ago, the throughput history describes a team that no
longer exists, and the forecast is confidently describing fiction.

*Test:* how many people are allocated at less than 100% to one team? Overlay team
composition changes on the throughput run chart — steps in throughput usually line up
with joiners and leavers rather than with anything the team did.

*If true:* often the single largest lever available, and the hardest to pull, because it
is an organisational allocation decision rather than a team practice. Worth the fight.
Consolidating two half-people into one whole one reliably beats any process change in
this repo.

### H8 — Rework and defect loops

Items that come back: returned from review, reopened after test, or fixed post-release.
This is **invisible WIP**. If cycle time is measured to first "done", the rework loop is
excluded entirely, and the team looks faster than it is while capacity silently drains.

*Test:* count items reopened or returned from a later state, as a percentage of
throughput. Compare "first marked done" against "finally done" for the same item. Count
defects found after release, by originating item.

*If true:* a quality problem wearing a speed problem's clothes — and the important
consequence is that **pressure makes it worse**. Any intervention aimed at going faster
will increase the rework rate and reduce net throughput. Fix the loop before touching
anything else.

### H6 — Dependency and decision wait
Lower probability given mostly-independent teams, but decisions still queue. Waiting on
a product decision, a security sign-off, or a third party looks identical to being slow.

*Test:* tag blocked reasons. Count blocked days per reason per month.

## A note on flow efficiency

Flow efficiency (active time ÷ elapsed time) is an intuitive measure and a poor
management one. It depends entirely on how honestly and granularly "active" is
recorded, which makes it easy to game and near-impossible to compare across teams. It
also collapses two different problems — long waits and slow work — into one number.

Use the underlying breakdown instead: **time in waiting states, by state, in days**.
Same diagnostic value, no false precision, and it names the queue you need to attack.

There is a ninth cause that sits above all of these and is not a team problem at all:
more initiatives running concurrently than the teams can carry. Team-level WIP limits
cannot fix it, because the demand arrives from outside the team. See
`docs/11-demand-and-intake.md` — for a delivery lead running several projects, this is
usually the highest-leverage thing available, and the only one on this page you can
act on alone.

A decision tree for routing between these hypotheses — in an order where the answers can
be trusted — is in `docs/08-diagnostic-decision-tree.md`.

## What to do with this document

Pick the two hypotheses you believe most. Set up the measures that test them
(`docs/02-measures.md`). Run four weeks of baseline before changing anything. Then run
one intervention at a time and log it in `templates/experiment-log.md`.

Resist the urge to fix all six at once. If you change three things and delivery
improves, you have learned nothing you can reuse on the next team.
