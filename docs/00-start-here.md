# 00 — Start here

## Who each document is for

The single most common way this fails is treating the repo as a handbook to distribute.
Most of it is **yours**, not the teams'.

| Document | Audience | How it's used |
|---|---|---|
| `01-diagnosis` | You only | Your working theory. Never circulate — it reads as a charge sheet |
| `02-measures` | You, then leads | You build them; leads learn to read them over time |
| `03-operating-cadence` | You | The rhythm you personally run |
| `04-policies` | **Team-facing** | Adapted and agreed by each team. They own the copy in `teams/<team>/` |
| `05-azure-devops` | You | Setup reference |
| `06-stakeholder-communication` | You | Your own language discipline |
| `07-tooling-shortlist` | You | Later. Weeks 5+ |
| `08-decision-tree` | You | Weekly routing aid |
| `09-sprint-goals` | **Team-facing** | Share when you introduce goals — not in week 1 |
| `10-story-slicing` | **Team-facing** | Share with 09. Goals don't work on a layer-cut backlog |
| `11-demand-and-intake` | You, then your sponsor | The portfolio layer. Your highest-leverage work |
| `12-success-criteria` | You | Checkpoints. Read it now, before anything is invested |

Only **04** and **09** go to teams, and not at the same time. Everything else is your
own instrumentation. Handing a team `01-diagnosis` reads as "here are six theories about
what you're doing wrong", however it's framed.

---

## The 90-day plan

### Before anything — three decisions only you can make (2 hours, this week)

**1. Decide the sprint-boundary question, privately, and write down your answer.**

Is sprint-scope completion still the internal scorecard? If yes, you have decided to
keep a measure you've concluded is arbitrary, and nothing downstream will work. Make
this call before you instrument anything, because it determines what the instrumentation
is *for*. Don't announce it yet.

**2. Pick one team.** The one where you have the best relationship and the most access —
not the one with the worst delivery. You are learning how to run this, and you want your
mistakes to land somewhere forgiving. Resist starting with all three.

**3. Count concurrent initiatives across your teams** (`11-demand-and-intake`). One hour,
needs nobody's permission. If the count exceeds the number of teams, that matters more
than anything the flow charts will tell you.

**4. Answer the four open questions.** Roughly 30 minutes in Azure DevOps:

- Are the Monte Carlo forecasts roughly accurate while sprints carry over? *(If yes, this
  is a boundary problem, not a flow problem — and that changes everything below.)*
- Are review and test-wait separate board columns, or buried inside "In Progress"?
- What is WIP per person right now?
- Does "done" mean in production, or merged?

Write the answers in `teams/<team>/baseline.md`. They'll steer which hypothesis you chase.

---

### Weeks 1–4 — baseline. Change nothing.

This is the hardest instruction in the repo and the one most likely to be skipped.

| # | Action | Effort |
|---|---|---|
| 1 | Build the ADO dashboard for team 1 (`05-azure-devops`, "Suggested dashboard") | 2 hrs, once |
| 2 | Save the aging WIQL query; export to a sheet weekly | 1 hr setup, 10 min/wk |
| 3 | Calculate cycle-time percentiles — 50/70/85/95. These set your age bands | 1 hr |
| 4 | Check unplanned work % and boundary-splitting **first** (Tree 1 gates on both) | 1 hr |
| 5 | Start the weekly flow review with team 1 (`templates/weekly-team-review.md`) | 30 min/wk |
| 6 | Change the standup to a right-to-left board walk, oldest item first | one conversation |
| 7 | At week 4, fill in `teams/<team>/baseline.md` | 1 hr |

**Say nothing about chart shapes for four weeks.** The moment you comment, people start
managing the chart instead of the work, and your baseline is contaminated.

Item 6 is the exception to "change nothing" — it's free, it's reversible, and it's often
worth more on its own than anything else here.

**How to introduce the review** — say roughly this, and mean it:

> "I want to understand where work actually spends its time. For the next month I'm just
> collecting — I'm not going to comment on the numbers, and none of this is about
> individuals. If it turns out the problem is something I own, that's a useful result."

Then honour it. If the first aged item becomes a conversation about a person, you will
not get honest data again.

---

### Weeks 5–8 — first intervention, and widen the cadence

| # | Action |
|---|---|
| 8 | Run Tree 1 (`08-decision-tree`) against the baseline. Pick **one** hypothesis |
| 9 | Write it up in `templates/experiment-log.md` before starting. Predict the effect |
| 10 | Agree `teams/<team>/policies.md` **with** team 1 — they edit it, you don't |
| 11 | Run the experiment. Minimum three weeks before judging |
| 12 | Start the weekly flow review with teams 2 and 3 — baseline only, no changes |
| 13 | Trial Lighthouse on team 1 (free, self-hosted, replaces hand-run Monte Carlo) |
| 14 | Protect one hour a week for the systemic constraint. This gets dropped first and matters most |

If in genuine doubt at step 8, pick the WIP limit. It's the cheapest intervention, the
fastest to show an effect, and the most likely to be the real cause.

Warn the team in advance that weeks 1–2 of a WIP limit feel *worse*. People feel idle
before they feel fast. Unwarned teams abandon it in week two.

---

### Weeks 9–12 — second wave, and start measuring predictability properly

| # | Action |
|---|---|
| 15 | Conclude experiment 1. Record the result even if it's "no effect" — especially then |
| 16 | Start the first experiment on team 2, informed by what transferred |
| 17 | Start the monthly delivery review (`templates/monthly-delivery-report.md`) |
| 18 | Begin the forecast-calibration record — `teams/<team>/forecasts.md`, every forecast, logged when made |
| 19 | Reshape the monthly review into the stakeholder pack (`06`). Never two sets of numbers |
| 20 | Decide on tooling (`07`) now you know which measures you actually use |

Step 18 is the one with the longest payback and the shortest window to start. You cannot
measure calibration retrospectively, and in twelve months it is the evidence that
settles whether probabilistic forecasting is working. **Start it now even if nothing
else on this list happens.**

---

### Month 4+ — make it stick

- Introduce sprint goals (`09`) **together with** slicing (`10`), once scope commitment
  is genuinely dead. Not before — introduced too early they get written as scope lists
  and the practice is spoiled. Introduced without `10`, they can't be written at all on a
  layer-cut backlog, and the team will conclude goals don't work here.
- Announce the boundary decision from step 1 explicitly to the teams. Ambiguity here is
  worse than either answer.
- Hand weekly review facilitation to each team lead. Target: within six months you
  attend, you don't run it.
- Quarterly recalibration (`03`): re-baseline percentiles, ratchet WIP limits down,
  delete any measure nobody has acted on.

---

## Your first week, concretely

1. Decide the boundary question. Write the answer down. Don't announce it.
2. Pick the team.
3. Half an hour in ADO answering the four questions.
4. Check unplanned work % and boundary-splitting — if either is live, that's your whole
   first month and everything else waits.
5. Book a recurring 30-minute slot with team 1 and send the paragraph above.

That's it. About three hours. If week one ends with a dashboard and a booked meeting,
you're on track.

---

## The four ways this fails

1. **Rolling out to all three teams at once.** You'll learn nothing transferable and
   won't be able to attribute any improvement.
2. **Skipping the baseline.** You'll argue about whether things improved, with no way to
   settle it.
3. **Dropping the systemic-constraint hour.** You'll build excellent reporting and change
   nothing. This is the most likely failure.
4. **The measures becoming a scorecard.** The first time an aging chart is used to
   question a person's output, the data stops being honest and never recovers.
