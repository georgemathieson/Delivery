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

Right-sizing was adopted to reduce risk. Horizontal slicing reduces *item size* while
**increasing** risk, because nothing is proven until the layers meet. It looks like
right-sizing and does the opposite.

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
