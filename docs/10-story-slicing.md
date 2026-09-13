# 10 — Story slicing

## The tension that isn't

> "User stories feel like they're fighting between vertical slices of functionality that
> can be delivered, and making stories small so that we can reduce risk."

These only fight if you believe the way to make a story small is to **remove a layer**.
They stop fighting the moment you make it small by **removing scope**.

- **Horizontal slice** — "Add the API", "Add the UI". Small, but neither half delivers
  anything, can be demoed, or can be validated. Risk accumulates until the last piece
  lands.
- **Thin vertical slice** — a narrower capability, working end to end. Equally small,
  but deployable, demoable, and capable of being wrong in a way you find out about now.

### Why horizontal slicing increases risk while looking like right-sizing

Risk here means **the chance of being wrong and not finding out until it is expensive**.
Right-sizing reduces it by shortening the loop from decision to consequence: a small item
finishes, integrates, deploys, gets used, and you learn.

A horizontal cut shortens the **ticket** but not the **loop**. Nothing is learned when
"Add API to get endpoints" is marked done, because nothing has met anything yet. The loop
is still as long as the whole capability.

What that looks like in practice:

```
Day 3   001 "Add API to get endpoints"    -> Done. Throughput +1. Cycle time 3 days.
Day 6   002 "Add UI to display endpoints" -> in progress
Day 6   ...the API returns owner as a directory group ID.
        The UI needs a display name. No lookup exists.
```

Three consequences, in increasing order of damage:

1. **The cost lands on the wrong item.** The rework happens *inside* 002, silently — it is
   rarely raised as a new ticket. 002 gets a long, unexplained cycle time while 001 stays
   on record as fast and clean. The data misattributes the cost.
2. **The mismatch surfaced at the most expensive moment.** Had the story been "see a list
   of endpoints with owner name, end to end", the same problem appears on day one, when
   changing the API costs an hour.
3. **Nothing was deployable in between.** The larger risk — *is this the right thing at
   all?* — went entirely untested.

It looks like right-sizing because on everything easily visible, it is identical:

| | Horizontal slice | Thin vertical slice |
|---|---|---|
| Item size | small | small |
| Item count | high | high |
| **Risk over time** | **back-loaded** | **front-loaded** |

Only the last row differs, and it is not in the instrumentation.

It does the *opposite* of right-sizing because it makes the measures **report health while
risk increases**. Throughput counts an item that delivered nothing to anyone. Cycle time
records a short, clean completion. The aging chart stays calm, because horizontal items
genuinely do finish quickly.

A team can therefore slice horizontally, watch every flow metric improve, and accumulate
more unvalidated risk each sprint than before — with the instrumentation confirming the
practice causing the problem.

This is why the vertical constraint has to be checked **when the story is written**. No
chart in `docs/02-measures.md` will catch it afterwards.

---

## WIP-in-disguise

A story can pass every size check and still not flow, because it carries the full weight
of the epic it came from. The card is small; the work isn't.

Symptoms:

- Stories that **reference each other** to make sense
- Stories that **all have to ship together** to be useful
- A single story taking **multiple people across multiple sprints** to finish

The cleanest single test, which collapses both constraints in this document into one:

> **Treat *independently valuable* as the definition of right-sized.**
>
> If it can't move, be tested, or finish on its own, it is still too big — however small
> the card looks on the board.

*(Framing from Paul Brown, ["The Dirty Secret Behind Agile
Failure"](https://thrivve.partners/the-dirty-secret-behind-agile-failure).)*

---

## Two levels, both vertical

The most common overcorrection once a team learns to slice vertically: they stop cutting
by layer and start writing epics as stories.

| Level | Scope | Example | Role |
|---|---|---|---|
| **Capability / epic** | Days to weeks | "An API owner can keep their entries accurate without going through us" | **This is the sprint goal** (`docs/09-sprint-goals.md`) |
| **Story** | Under the right-sizing threshold | "An owner can edit the description of an endpoint they own" | This is what flows on the board |

They differ in **scope, not axis**. Both go all the way through the stack. A story is a
thin slice *within* a capability, never a layer of one.

So "an owner can manage and maintain the catalogue" is not a story to write. It is the
goal, and it splits into:

```
Owner can edit the description of an endpoint they own
Owner can add a new endpoint
Owner can mark an endpoint as deprecated
Owner can assign a system owner
```

### Two independent constraints

| | Question | "Add the API" | "Manage the catalogue" | "Edit an endpoint's description" |
|---|---|---|---|---|
| **Vertical** | Does it deliver anything on its own? | ✗ | ✓ | ✓ |
| **Small** | Under the right-size threshold? | ✓ | ✗ | ✓ |

Both, every time. Failing either produces the same symptom in the data — an item sitting
in progress accruing age — from opposite causes.

This matters because the overcorrection is often *more* damaging than the original
problem. Cycle times balloon, the aging chart goes red across the board, and the team
concludes vertical slicing doesn't work here — when what actually happened is they
stopped slicing.

### Spotting an epic wearing a story's clothes

1. **Contains "and" or "or".** "Manage *and* maintain" is two things minimum.
2. **Vague verb** — manage, maintain, handle, administer, support, deal with. These are
   category labels, not actions. Concrete verbs (edit, add, deprecate, submit, search,
   notify) are story-sized by nature.
3. **Collective object** — "the catalogue" rather than "an endpoint". Singular objects
   force singular scope.
4. **Fails the team's own right-sizing rule** (`docs/04-policies.md`) — more than N days
   elapsed.

The shape to aim for: **one actor, one concrete verb, one object.** If done can't be
described in a single sentence, it's a capability, not a story.

---

## The test

> **If this story were the last one we ever shipped, would anything be better than
> before?**

"Add API to get API endpoints" — no. Nobody can do anything they couldn't do yesterday.
"See a list of API endpoints, name only" — yes. Small, unglamorous, real.

A softer version for borderline cases: *could we demo this on its own without apologising
for what's missing?*

---

## Slicing patterns

Ways to make a story smaller **without** cutting off a layer.

| Pattern | Instead of | Do this |
|---|---|---|
| **Data richness** | API, then UI | List showing names only → add description → add owner |
| **Happy path first** | Form, then validation, then errors | Valid input works end to end → then validation → then error states |
| **One scenario** | Support all request types | One system, one access type → then the others |
| **Walking skeleton** | Build a 6-step wizard one step per story | Whole wizard with **one** step, working end to end → then add steps |
| **Hardcode then earn** | Full integration | Real UI against a fixed list → then the live API |
| **Manual then automate** | Build the notification system | Owner is emailed manually by an admin → then automate it |
| **One user type** | All roles | Employee view works → then owner view |

The walking-skeleton row is the one most often missed and the most valuable. Building a
multi-step flow one step at a time means **nothing works until the final step**, so all
the integration risk lands at the end — precisely the shape right-sizing exists to avoid.
Build the flow end to end with a single step, then thicken it.

"Manual then automate" is similarly underused. A capability delivered by a human doing
something tedious is still delivered, and it tells you whether automating it is worth it.

---

## Worked example

A real backlog, sliced by layer:

```
001  Add API to get API endpoints
002  Add UI to display endpoints
003  Add API to get details for an endpoint
004  Add UI for details slideout
005  Add API endpoint to request access
006  Add UI step 1 for request access
007  Add UI step 2 for request access
008  Add API for step 2 (fetch systems)
...  bunch of other UI steps
012  Add UI for final step (complete and submit)
013  Add API to submit request
014  Add notification to API owners
015  Add edit functionality for endpoint list
016  Add UI for edit API
017  Add UI to add system owner
```

Three problems, all caused by the same cut:

1. **Every odd item is half a story.** 001 delivers nothing until 002 lands. Age accrues
   against work that cannot be validated.
2. **The wizard (006–012) back-loads all the risk.** Nothing works until step six.
3. **Value ordering is destroyed.** 014 — notifying owners that a request is waiting — is
   plausibly the highest-value item in the list, because it is what stops requests dying
   in an inbox. Layer-ordering has put it fourteenth.

Re-cut by outcome:

### Capability 1 — Discover what exists

> **Goal: "An employee can find out what APIs exist and who owns them, without asking
> anyone."**

```
S1  See a list of API endpoints (name only, real data, full stack)
S2  ...with description and owner shown
S3  Open an endpoint to see its full details
S4  Search the list by name
```

### Capability 2 — Get access without chasing

> **Goal: "An API owner finds out about an access request without the employee chasing
> them."**

```
S5  Request access to an endpoint — single-step form, happy path, submits and persists
S6  Owner is notified when a request arrives     <-- the actual value, delivered early
S7  ...choose which system the access is for
S8  ...validation and error states
S9  ...remaining wizard steps
```

Note S6. Once ordered by outcome rather than layer, the most valuable item moves from
fourteenth to second, and it is *cheap* — a single-step request plus a notification is a
working system that someone can use on day three.

### Capability 3 — Keep the catalogue current

> **Goal: "An API owner can keep their own entries accurate without going through us."**

```
S10  Owner can edit an existing endpoint entry
S11  Owner can add a new endpoint
S12  Assign a system owner
```

Same work, same story count, roughly the same total effort. Every story is now
independently deployable, the risk is front-loaded instead of back-loaded, and each
capability has a goal that was **derived from the outcome, not reverse-engineered from
the list**.

---

## Tasks, items and enablers

A common question once a team starts taking the board seriously: *someone needs to spend
a morning getting the service running locally with enough data to test pagination — is
that a story?*

Usually **no**. It is part of doing the pagination story.

Nobody raises an item for "open the IDE", "write the test", "attach the debugger". This
is the same category, and giving it its own item does active harm:

- The pagination story looks cheaper than it was
- Throughput counts an item that delivered nothing to anyone
- It is a horizontal slice — the setup half proves nothing until the pagination half lands

That time **should** land inside the pagination story, because then that story's cycle
time honestly reflects what pagination cost. That number feeds the forecast.

### When it becomes an item

Three conditions, any one of which is enough:

| Condition | Why | Example |
|---|---|---|
| **Reusable** — the team will need it repeatedly | It has a real outcome and a real user | "Any developer can run the API locally against a realistic data volume" |
| **Blocking more than this story** | The constraint is the environment, not the story that surfaced it | Several stories stalled on thin dev data |
| **Breaches the right-size threshold** | The host story will blow its age band | Seeding realistic data turns out to be two days |

Rough rule: **under a day and only this story needs it → it is the work. Longer, or
others need it → it is an item.**

Enabler items are legitimate. The user is the team, which is fine — the test in this
document still applies unchanged: *if this were the last thing we shipped, would anything
be better than before?* For "any developer can run the API locally with realistic data",
yes.

When an enabler is split out of a story already in progress, record it as a split and
keep the original start date on the remainder (`docs/04-policies.md`). Otherwise the
split reads as two fast items rather than one that turned out to be bigger than expected.

### The signal that matters even without a ticket

Most of these never become items, and they are still worth seeing.

In the weekly flow review, the answer to *"what is stopping this finishing today?"* may
be "I spent the morning getting enough data locally to test pagination". One developer
for one hour is nothing. Three developers hitting the same thing in a month is thirty
hours, plus the ones who didn't bother and shipped untested.

No ticket is needed to catch that — only the question asked weekly and someone noticing
the repeat. That is what the facilitator's notes and the systemic-constraint hour in
`docs/03-operating-cadence.md` exist for. **Friction that recurs is a constraint; a
constraint is work for the delivery lead, not another ticket for the team.**

This class of problem — a long tail of small friction, each instance too small to be
worth reporting — is where most delay actually comes from. See
`docs/13-friction-and-delay.md`.

---

## Direction of travel

That last point is the whole thing.

| | |
|---|---|
| **Backwards** | Stories exist → find a sentence covering enough of them → that's the goal |
| **Forwards** | Outcome → what's the smallest set of work that reaches it? → those are the stories |

The artefacts look identical. Only the direction differs, and it determines whether the
goal can survive its plan being wrong.

If writing a sprint goal feels like reverse-engineering, the backlog is almost always
cut by layer. **Fix the backlog, not the goal.** No amount of goal-writing technique
extracts an honest outcome from a build plan.

---

## Where this connects to the rest

- **H2, started before ready** — horizontal stories are frequently pulled because they
  look ready, then stall waiting for their other half.
- **H1, too much WIP** — a layer-cut backlog encourages several capabilities in flight at
  once, because no single one has a natural sequence.
- **Cycle time distribution** — a story blocked on its counterpart shows up as a long
  right tail, which widens the 50th–95th gap. That gap is your predictability number.

Slicing is not a story-writing nicety. It is one of the more direct levers on the
measures in `docs/02-measures.md`.
