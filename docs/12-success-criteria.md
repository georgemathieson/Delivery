# 12 — Will this work, and how would you know?

A change programme without success criteria cannot be stopped, because there is never a
moment at which it has demonstrably failed. This document sets those criteria in advance,
while nobody has anything invested in the answer.

---

## What success actually means here

Two goals were set at the start: make teams **more predictable**, and make them **more
reliable to stakeholders**. They are not the same, and one is much closer to done than
the other.

| Goal | Definition | Status |
|---|---|---|
| Predictable | The spread of delivery times is narrow and stable — the 50th–95th cycle-time gap | The open problem |
| Reliable | Stakeholders are never surprised; forecasts are calibrated and update early | **Largely already achieved** by giving ranges |

Worth sitting with the second row. Reliability is not "hit the date" — it is "never be
surprised by you". Probabilistic ranges, honestly updated, deliver that. You may be
further along than it feels, and the frustration may be coming from measuring against a
sprint boundary that was never a reliability measure in the first place.

---

## Checkpoints

### 6 weeks — *you know what is actually wrong*

- [ ] Baseline recorded for at least one team
- [ ] Concurrent-initiative count established (`docs/11`)
- [ ] Data-integrity hypotheses ruled in or out (H3, H4, H7, H8)
- [ ] One hypothesis named as the primary cause, with evidence

**This is the near-certain outcome.** Instrumentation reliably produces a diagnosis, even
when it produces nothing else. If you get here and stop, you have still gained more than
the last two years of practice changes delivered.

*If not met:* almost always because the ADO data was worse than expected. Fix the
recording; don't abandon the method.

### 3 months — *one lever has moved, measurably*

- [ ] One experiment concluded on team 1, result recorded either way
- [ ] Weekly flow review running on all teams
- [ ] Forecast-calibration record started
- [ ] Cadence surviving without you chasing it

*If not met:* the usual cause is the systemic-constraint hour being lost to meetings.
Check your own calendar before concluding the method doesn't work.

### 6 months — *the system is measurably different*

- [ ] 50th–95th cycle-time gap narrowing on at least one team
- [ ] WIP limits in place and binding
- [ ] Six or more forecasts in the calibration record
- [ ] At least one systemic constraint removed
- [ ] At least one team lead facilitating their own review

*If not met, with the cadence genuinely running:* this is real evidence. Either the
constraint is outside the teams (go to `docs/11`), or it is organisational — allocation,
funding, priority churn — and no team-level intervention will touch it. That is a finding,
and it is worth more than another six months of trying harder.

### 12 months — *it belongs to them, not you*

- [ ] Forecast percentiles roughly uniform — objectively calibrated
- [ ] Teams run their own reviews; you attend
- [ ] Stakeholders ask for confidence levels rather than dates
- [ ] Your week is spent on constraints, not reporting

---

## What determines whether this works

Honestly, most of it is not in this repo.

**Strongly in favour**

- The instrumentation will produce a diagnosis. This is close to guaranteed
- WIP limits are one of the most reliable interventions in the field, and cheap
- Probabilistic forecasting is already established — the hardest cultural battle is won
- Two to three teams is a tractable scope for one person
- The existing practices are sound. Nothing here needs unpicking, only adding to

**Against, or uncertain**

- **Whether you can influence demand.** If initiatives keep being started, team-level
  work is bailing out a boat. This is the single biggest determinant and it depends on
  sponsorship you may not currently have
- **Whether you protect the constraint hour.** The most likely failure mode by a
  distance: excellent reporting, unchanged system
- **Change fatigue.** Teams have had several practice changes already, none of which
  visibly worked. "Here's another thing" is a reasonable reaction and needs answering —
  this one is instrumentation before intervention, which is genuinely different, but you
  have to say so
- **Whether the measures stay diagnostic.** The first time an aging chart is used to
  question a person, the data stops being honest and does not recover

---

## The result you should pre-commit to accepting

There is a real possibility that three months of measurement shows **the teams are
already predictable**, and that the apparent problem is the sprint boundary, or demand
management, or allocation — none of which the teams control.

Decide now that you will accept that answer if the data gives it. It is the outcome most
likely to be quietly discarded, because it is unsatisfying, it doesn't look like
leadership, and it points at people senior to the teams. It would also be the single most
valuable finding available, and acting on it would do more for delivery than anything in
this repo.

---

## An honest overall read

The probability of ending up **better informed** is very high — the instrumentation does
that almost regardless of what else happens.

The probability of **materially more predictable teams within a year** is good, conditional
on two things: that the cause turns out to be inside the teams, and that you keep
protecting the hour that removes constraints rather than the hours that describe them.

The probability of **stakeholders finding delivery more reliable** is high, and partly
already banked — provided you keep the calibration record, which is what converts
"trust us" into evidence.

The main risk is not that the method is wrong. It is that the diagnosis points somewhere
you cannot act alone, and the programme quietly becomes a reporting function instead. The
counter to that is written down in advance, here, and in the four ways this fails in
`docs/00-start-here.md`.
