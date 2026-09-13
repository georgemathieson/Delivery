# 13 — Friction, and where delay actually comes from

## The claim

**Most delay is not a few big blockers. It is a long tail of small friction.**

Slow local setup. Thin data in the dev environment. A flaky test. A pipeline that takes
forty minutes. A pull request sitting for two days. Each one individually beneath the
threshold at which anyone would complain. Together, they *are* the cycle time.

This matters because it changes where to look. Chasing the big, visible blockers has
poor returns — they are few, they are already known, and someone is usually already on
them. The tail is larger, entirely invisible, and nobody owns it.

---

## Why it stays invisible

**Every individual instance is rationally not worth reporting.**

A developer loses an hour getting enough data locally to test something. Raising it costs
ten minutes, feels like whinging, and sounds like an excuse for being slow. Absorbing it
is the locally rational choice — every time, for everyone, forever.

Two consequences follow, and both are design constraints:

1. **Any mechanism costing more than about thirty seconds will not be used.** A ticket, a
   form, or a category taxonomy guarantees silence.
2. **The barrier is social before it is mechanical.** People do not report friction
   because it sounds like making excuses for their own slowness.

The second is the one that needs your attention. Say it explicitly and often — *"telling
me you lost a morning to the environment is the most useful thing you can do today"* —
and then prove it by how you react the first time someone does. React badly once and you
will not hear it again, and you will be back to guessing.

---

## What is actually achievable

**You cannot prevent the first occurrence.** Nobody knew the dev environment had too
little data until someone needed to test pagination against it. No process catches that
in advance, and one claiming to is ceremony for a fantasy.

**The target is occurrences two through thirty.** This is a recurrence problem, not a
prediction problem. The first lost morning is unavoidable; the next twelve are entirely
avoidable, and in most organisations they are paid — by everyone, indefinitely — because
nobody adds them up.

So the question to hold yourself to is not *"did we catch it in time?"* It is:

> **How many times did we pay for the same thing?**

---

## Three jobs, three frequencies

The existing cadence does this, provided the jobs are kept separate.

| Job | When | Mechanism |
|---|---|---|
| **Detect** | Daily | The standup question — "what is stopping this finishing today?" One day's latency, not a week's |
| **Aggregate** | Weekly | Facilitator's notes in the flow review. One instance is noise; the third is a pattern |
| **Remove** | The weekly constraint hour | Fix it once, for everyone (`docs/03-operating-cadence.md`) |

The weekly review is not where friction is *caught* — the standup is. Weekly is where it
is **counted**, which is the step almost nobody does, and the one that converts anecdote
into a case somebody can act on.

### In the moment, absorb it

The developer who hits friction should fix it, carry on, and mention it the next morning.

Do not build a process that requires people to stop working in order to report having
been stopped from working. The reporting must be cheaper than the friction, or it will
correctly be skipped.

---

## Seeing it in data you already have

Two proxies from the existing measures (`docs/02-measures.md`):

- **Started to first commit** — catches "pulled it, then couldn't actually begin"
- **Time in review / waiting states** — catches the queue half of the tail

Neither is complete. For the rest, **ask people directly**: *"what wasted your time this
week?"* Self-reported friction is a legitimate instrument rather than a soft one — for
this class of problem it is frequently the only instrument, because the cost never lands
anywhere a system records it.

Ask it monthly, keep it to one question, and count the answers rather than discussing
them individually.

---

## Developer experience is a predictability lever

The implication is larger than any single example.

If cycle time is dominated by a tail of small friction, then the quality of a team's
tooling, environments, test data and pipelines is not a morale question or an engineering
indulgence. **It is one of the larger available levers on delivery predictability**, and
plausibly a bigger one than anything in this repo's process guidance.

It is also chronically underfunded, for exactly the reason above: the cost is real,
continuous, and invisible, so it never competes successfully against visible feature work.

Counting it is what changes that. Not arguing for it.

---

## The honest limit

Some friction will not be fixed. It belongs to another team's system, or the fix costs
more than it saves. That is a legitimate outcome.

When it happens, the job stops being *fix it* and becomes **make the cost visible and let
someone decide**:

| Not this | This |
|---|---|
| "The dev environment is a pain" | "We spend about four days a month working around thin dev data. The fix is roughly a week. Here's the trade." |

The first is a complaint and will be absorbed. The second is a decision, and someone can
make it. The only way to have the second conversation is to have been counting.
