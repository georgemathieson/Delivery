# 03 — The operating cadence

This is how you stay on top of 2–3 teams without becoming the bottleneck or the
police. Total cost to you: roughly **3 hours a week**, plus 2 hours a month.

The principle throughout: **you attend to the flow of work, the teams attend to the
work.** If you find yourself discussing the content of a ticket, you have drifted.

---

## Daily — team-owned, you don't attend

**The board walk (10–15 min, the team's own standup)**

Walk the board **right to left, oldest item first**. Not person by person.

Two questions only:
- What do we need to do to finish the item on the right?
- Is anything blocked, and for how long?

No status round-robin. If a team's standup is "what I did yesterday", this change alone
is often worth more than anything else in this repo — it reorients the team from
individual activity to collective completion.

**Your involvement:** none, routinely. Drop in once a month, unannounced, to see whether
the format has survived contact. It usually decays back within six weeks without
occasional reinforcement.

---

## Weekly — the flow review (30 min per team, you facilitate)

The centrepiece. Template: `templates/weekly-team-review.md`.

Same slot, same day, every week. With three teams this is 90 minutes.

**Agenda**

| Time | Item |
|---|---|
| 0–5 | Aging chart: every item past the 85th percentile band, oldest first |
| 5–15 | For each aged item — what is stopping this finishing? Who owns the next action? |
| 15–20 | WIP vs limit; arrival vs departure rate |
| 20–25 | Blocked items: reason, days blocked, escalation needed |
| 25–30 | Current experiment: what are we running, what have we seen |

**Rules that make it work**

- Attendance is the team, not a representative. If only a lead attends, this becomes a
  status report to you and loses all of its value.
- You ask about **items**, never about people. "What is holding this item?" not "how are
  you getting on with this?"
- Every aged item leaves the meeting with a named next action and an owner. Not "we'll
  keep an eye on it".
- Timebox hard. It must not become a second planning meeting.
- Say nothing about the chart shapes for the first four weeks. You are baselining, and
  early commentary makes people manage the chart instead of the work.

**What you are listening for**

The same blocker reason appearing in two consecutive weeks, or across two teams. That
is a systemic constraint and it is yours to remove — it is the highest-value thing you
personally do all week.

---

## Fortnightly / sprint boundary — planning and review, unchanged in form

Keep the ceremony, change its content.

- **Planning** stops being "what will we commit to". It becomes "what is this sprint
  for?" (the sprint goal — `docs/09-sprint-goals.md`), then "what is the smallest set of
  work that gets us there, and do we have the WIP headroom to start it?"
- **Review** stops being "did we finish the sprint". It becomes "did we achieve the goal,
  what did we learn, and what is the current forecast?" A goal missed because we learned
  it was the wrong goal is a good sprint — say so out loud.
- **Retrospective** gets one standing agenda item: the flow charts. What do they show
  that we didn't feel, and what did we feel that they don't show?

Explicitly retire the sprint-scope commitment as the measure of sprint success. Say it
out loud to the teams, once, clearly. Ambiguity here is worse than either answer: teams
will default to the old scoreboard and privately conclude the new measures are theatre.

---

## Monthly — the delivery review (90 min, all teams + you)

Template: `templates/monthly-delivery-report.md`.

- Throughput run chart per team, 12 weeks rolling
- Cycle time percentiles per team — is the 50th-to-95th gap narrowing?
- Forecast accuracy: where did last month's actuals land in their forecast distributions?
- Unplanned work percentage
- Experiments: what ran, what happened, what next
- Systemic constraints: what is blocking more than one team, and who owns removing it

**This is also your stakeholder input.** The monthly report is what gets reshaped for
`docs/06-stakeholder-communication.md` — do not maintain two sets of numbers.

---

## Quarterly — recalibration (half a day, you + team leads)

- Are the measures still driving action, or have they become wallpaper? Delete any that
  aren't used.
- Re-baseline percentiles. Your bands should move as the system improves; stale bands
  quietly stop flagging anything.
- Review the forecast-accuracy record across the quarter. Are forecasts calibrated?
- Review policies in `docs/04-policies.md`. WIP limits in particular should ratchet down
  over time as flow improves.

---

## Your own weekly rhythm

| When | What | Time |
|---|---|---|
| Mon AM | Pull the data, refresh charts for all teams | 30 min |
| Mon–Wed | Three flow reviews, one per team | 90 min |
| Thu | Work on the one systemic constraint you identified | 60 min |
| Fri | Update `teams/<team>/log.md` for each team; note anything for the monthly | 20 min |

The Thursday hour is the part that gets dropped first and matters most. Facilitating
reviews makes problems **visible**; only that hour makes them **go away**. If you never
protect it, you will have built an excellent reporting system and changed nothing.

---

## Anti-patterns to watch for in yourself

- **Becoming the reporting layer.** If the teams don't look at the charts between your
  meetings, they are your charts, not theirs. Aim to hand the weekly review to each team
  to facilitate within six months.
- **Adding a practice when a measure gets uncomfortable.** The instinct will be to
  introduce a new ceremony. Prefer removing a constraint.
- **Comparing teams.** Different work, different contexts, different distributions. Each
  team is compared only against its own past. Stakeholders will ask for a cross-team
  league table; don't build one.
- **Running three experiments at once.** You will learn nothing transferable.
