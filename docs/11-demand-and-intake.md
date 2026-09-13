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

## Fractional allocation

The same problem one altitude down: instead of a team carrying too many initiatives, a
*person* is carrying too many. "Sarah is 80% on the catalogue and 20% on payments."

### Where the 20% came from

A funding or headcount spreadsheet, essentially always. Someone needed the columns to sum
to 100% and 80/20 made them sum. It is a **financial allocation reported as a capacity
plan**, and it has never been checked against what the person actually did.

Two questions retire it:

- What evidence is there that it was ever 20%? (There will be none.)
- What would have to be true for it to be exactly 20%? The person would have to switch on
  a schedule, lose nothing in the switch, and neither stream would ever be urgent.

### It isn't 80/20

The commonly cited rule of thumb (Weinberg) is roughly a 20% loss per additional
concurrent stream:

| Streams | Nominal each | After switching loss |
|---|---|---|
| 1 | 100% | 100% |
| 2 | 50% | ~40% |
| 3 | 33% | ~20% |
| 4 | 25% | ~10% |

Treat the figures as illustrative rather than measured — it is a heuristic, not a
finding. The direction is not in doubt. 80/20 behaves more like 65/15, with a fifth of a
person disappearing into the switch. Because the loss is invisible, it never appears in
anyone's plan, which is exactly why the plan keeps looking achievable.

### Parallelism is not interleaving

A fast-food kitchen handles many orders at once, so "we can't do two things at once" is
easy to rebut. The precise version survives:

> **They split the work across stations. They don't split a person across orders.**

The grill cook is not 80% burgers and 20% fries. Each station does one thing, the *work*
moves between people, and nobody pauses an order at 60% to start another.

| | What it is | Verdict |
|---|---|---|
| **Parallelism** | Several items in flight, each person doing one thing | Fine — this is how teams work |
| **Interleaving** | One person divided across several items | This is fractional allocation |

Nobody works on two things at once. Fractional allocation is **switching between two
things and calling the switching a percentage.**

### What it is actually for

This is the part to lead with in any conversation about it.

80/20 exists because it lets **two sponsors both hear yes.** It converts a hard
prioritisation decision into an arithmetic fiction in which nobody loses. That is why it
survives despite everyone privately knowing it does not work: it is not a capacity
decision that happens to be wrong, it is a **conflict-avoidance device wearing a capacity
decision's clothes.**

So the counter is not a better percentage. It is the queue conversation above, at the
level of a person:

> *Which of these two matters more? Whichever you say, that one happens first and the
> other happens next — and both finish sooner this way than if we split someone across
> them.*

That is not a refusal. It is a sequencing decision, offered to the person whose decision
it actually is.

### Measure it before you argue it

Compare cycle time for items owned by people allocated wholly to one team against items
owned by people split across two. Same board, same period, no new tooling — this is the
H7 test in `docs/01-diagnosis.md`.

"Fractional allocation costs us" is an opinion. "Items owned by split people take 2.4×
longer to finish here" is not. Get the number before the conversation, not after.

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
| Week 3 | Count people allocated at less than 100% to one team. Measure their cycle times against everyone else's |
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
