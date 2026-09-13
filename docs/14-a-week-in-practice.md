# 14 — A week in practice

A worked example of the rhythm in `docs/03-operating-cadence.md`. Names and numbers are
invented; the shape is what it actually looks like.

**Scene:** week 7. Team 1 (Catalogue) is past baseline with a WIP-limit experiment
running. Teams 2 and 3 (Onboarding, Billing) are in week 3 of baseline, so no commentary
on their numbers yet.

---

## Monday 08:45 — refresh the charts · 30 min

| | WIP | Limit | Finished last wk | Started | 85th %ile | Oldest open |
|---|---|---|---|---|---|---|
| **Catalogue** | 9 | 7 | 11 | 14 | 9 days | **14 days** |
| **Onboarding** | 5 | 6 | 14 | 13 | 6 days | 7 days |
| **Billing** | 12 | — | 8 | 11 | 16 days | **23 days** |

Two things are visible before any meeting: Catalogue is over its limit and started more
than it finished, and Billing's 85th percentile is nearly three times Onboarding's.
Billing is still baselining, so that gets written down, not raised.

Ten minutes looking, twenty exporting the aging list sorted oldest-first. **That sorted
list is the agenda.**

---

## Tuesday 10:00 — Catalogue flow review · 30 min

Three items past the 85th band. Oldest first.

### #4412 · 14 days · "Employee can page through the catalogue"

> **You:** What's stopping this finishing today?
> **Dev:** I lost Monday morning getting enough data locally to test pagination. Dev's
> only got about forty rows.
> **You:** Is it finishable this week now?
> **Dev:** Yeah, it's basically done.

No ticket raised. One line in the facilitator's notes: **dev data — 2nd time this month,
2nd team.** (`docs/13-friction-and-delay.md`)

### #4398 · 11 days · blocked 4 days, tagged `decision`

Waiting on whether deprecated endpoints appear in the list.

> **You:** Who can answer that?
> **PO:** Me — I've just not got to it.
> **You:** Can you get to it today?

Owner named, action named, meeting moves on. You do not chase it yourself; it is the
PO's to own.

### #4405 · 10 days

Bigger than thought. Team agrees to split, **keeping the original start date on the
remainder** so the age doesn't reset (`docs/04-policies.md`).

### WIP

9 against a limit of 7. Started 14, finished 11.

> **You:** You're two over, and you started three more than you finished. What would it
> take to hold the limit this week?
> **Team:** We'd have to not start the search story until pagination lands.
> **You:** Is that worse?
> *(pause)*
> **Team:** …no, probably not.

**That pause is the intervention.** It is not mandated — they reached it. A limit the
team concludes is right survives the next busy fortnight; one you imposed does not.

---

## Wednesday 10:00 — Onboarding · 30 min

Healthy. WIP under limit, finished more than started, nothing past the 85th band. Ten
minutes and done.

One item blocked 3 days on a security review, tagged `dependency`. Noted: **security
review — 3rd time this month.**

Short reviews are fine. Do not pad them to fill the slot, and do not go hunting for
problems — you will find some, and they will not be real.

---

## Wednesday 14:00 — Billing · 30 min

WIP 12 across five people. Oldest item 23 days. Every instinct says say something.

**Don't.** They are baselining, and the agreement was four weeks without commentary. Ask
the aged-item questions, take notes, leave.

> *Facilitator's notes: WIP 2.4 per person. Almost certainly H1. Hold until week 5.*

Comment now and they begin managing the number rather than the work, and the baseline you
will need to prove anything later is gone.

---

## Thursday 14:00 — the constraint hour · 60 min

This week: **dev environment data.** Three sightings, two teams.

The hour is not spent fixing it. It is spent making it someone's problem:

| Time | What |
|---|---|
| 15 min | Check whether a seeded dataset exists anywhere. It doesn't. Establish that the platform team owns the environment |
| 20 min | Quantify: 3 known instances at ~half a day ≈ 1.5 days this month — **and that's only what surfaced in reviews.** Assume double |
| 10 min | Write four sentences: what's happening, how often, what it costs, the likely fix |
| 15 min | Send to the platform lead, book 20 minutes next week |

**Nothing is fixed on Thursday, and that is normal.** The hour converts a grumble into a
costed request with an owner. Landing it will take three or four weeks.

Note what was *not* done: writing a seeding script yourself. Tempting, quick, and it
fixes one team while the platform carries on generating the problem for everyone else.

---

## Friday 16:00 — logs · 20 min

Three entries in `teams/<team>/log.md`, four lines each. Then the monthly list:

- Dev data — 3 sightings, 2 teams, ~1.5 days/month, with platform
- Security review — 3rd blocked instance this month, watch it
- Catalogue WIP experiment — week 2, held the limit once

**Weekly total: 2 hours 50 minutes.**

---

## The same week, gone wrong

Thursday 14:00 is taken by a steering meeting. Entirely reasonable — steering matters,
and the constraint hour has no external deadline, no attendees, and nobody chasing it.

You still ran three good reviews. The charts are current. The notes are excellent.

And in four weeks a developer loses another morning to the same thin dev data, because
nobody took it to the platform team.

Repeat for a quarter and you will have the best-instrumented teams in the building and
delivery that has not moved. This is failure mode 3 in `docs/00-start-here.md`, and it is
the most likely one precisely because every single week, sacrificing that hour is the
most sensible-looking decision on the table.

---

## What this week shows

| Principle | Where it appears |
|---|---|
| The aging list is the agenda | Monday |
| Ask about items, never people | #4412, #4398 |
| Small friction needs no ticket, only a note | #4412 |
| Name an owner and an action, don't take it on | #4398 |
| Splits keep the original start date | #4405 |
| The team concludes; you ask the question | WIP exchange |
| Silence during baseline is discipline, not neglect | Billing |
| The constraint hour moves problems, it rarely solves them | Thursday |
| Don't fix it yourself if that leaves the system unchanged | Thursday |
