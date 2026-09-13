# 11 — Demand and intake

## The gap this fills

Everything else in this repo acts on work that is **already inside** a team. That is the
wrong altitude for the most common cause of unpredictability in an organisation running
several projects at once.

A team-level WIP limit cannot hold against organisational demand. If three teams are
carrying six concurrent initiatives because six stakeholders each started one, every team
is context-switching, every initiative is progressing slowly, and no amount of board
discipline inside a team fixes it. The team didn't choose the six.

**This is the one layer where you have authority and the teams do not.** They can hold
a WIP limit inside a sprint. Only you can decline to start a seventh initiative. For a
delivery lead across multiple projects, this is usually the highest-leverage work
available — and it is not in the weekly flow review, because it doesn't happen there.

---

## Portfolio WIP

Little's Law works at every altitude. At the portfolio level:

> average time to deliver an initiative = initiatives in progress ÷ initiatives completed per period

Halve the number of concurrent initiatives and you halve time-to-delivery for each,
without anyone working differently. Three teams running two initiatives each will finish
both sooner than three teams running four each — and crucially, the **first** one lands
far sooner, which is when the value starts.

| | 6 concurrent | 3 concurrent, then 3 |
|---|---|---|
| First initiative delivered | month 6 | **month 3** |
| All six delivered | month 6 | month 6 |
| Value accruing from #1–3 | from month 6 | from month 3 |
| Chance to learn before starting #4–6 | none | three months of it |

Same people, same throughput, three months of earlier value and a feedback loop that
didn't exist before. The only cost is that initiatives 4–6 start later — which mainly
feels bad to whoever sponsors them.

### Count it

The number to establish first: **how many initiatives are in flight across your teams
right now?** Count anything a stakeholder would name as a thing they are waiting for,
including the ones nobody has worked on for three weeks.

If that count exceeds the number of teams, you have found something more significant than
anything the flow charts will tell you.

---

## Intake policy

Three questions to answer explicitly, and write down:

**1. Who can start work?** Not "who can request" — who can cause a team to begin. If the
answer is "several people, informally", that is the finding. Intake with no single point
of entry cannot be limited.

**2. What is the limit?** A number of concurrent initiatives, agreed in advance. Like a
WIP limit, one that is never reached isn't a limit.

**3. What happens when the limit is reached?** The answer must be "it waits in a visible
queue", not "we squeeze it in". If there is no answer, the limit is decorative.

### The "not yet" queue

The most effective stakeholder conversation available to you is not about dates. It is
showing someone the ordered queue and asking **which of these should your request go in
front of?**

This works because it moves the conversation from "is my thing important?" — to which the
answer is always yes — to a trade-off between named, real alternatives. It also makes
the cost of starting everything visible without you having to argue for it. Most people,
shown the queue, will place their own request lower than you would have.

Keep the queue ordered, visible, and honest. An initiative that has been queued for six
months should say so rather than being quietly relabelled.

---

## The started-equals-committed trap

An initiative that has been started is dramatically harder to stop than one that has not,
regardless of what has been learned since. Sunk cost, visible progress, and someone's
name on it all make stopping feel like failure.

Two consequences:

- **The decision to start is the real decision.** By the time doubt appears, the cost of
  stopping has already been manufactured. Scrutinise starts far harder than continuations.
- **Stopping must be normalised deliberately.** If nothing has ever been stopped, nothing
  will be. Stop something visibly, early, and describe it as the system working — the
  same move recommended for aged items in `docs/04-policies.md`, one altitude up.

---

## What to do about it

| When | Action |
|---|---|
| Week 1 | Count concurrent initiatives across your teams. Write the number down |
| Week 2 | Map who can start work, and how. Expect this to be informal and undocumented |
| Week 4 | Take the count to whoever owns the portfolio. Frame it with the table above, not as a complaint |
| Week 6 | Propose a concurrent-initiative limit, and the queue that goes with it |
| Ongoing | Nothing starts without something finishing. This is the whole intervention |

Start the count in week 1 alongside the team baselining. It costs an hour, needs nobody's
permission, and may be the most important number you collect.

---

## When this isn't the problem

If your teams are each running one initiative at a time and delivery is still
unpredictable, this document doesn't apply and the cause is inside the teams
(`docs/01-diagnosis.md`). Check before investing in a portfolio conversation you don't
need — arriving with a governance proposal for a problem you don't have costs credibility
you will want later.
