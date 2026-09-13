# 09 — Sprint goals

## Why this matters more now, not less

Retiring the sprint-scope commitment (`docs/01-diagnosis.md`) removes the thing that
used to give the sprint its meaning. If nothing replaces it, the sprint becomes a timer:
work flows continuously, a fortnight elapses, everyone gathers to observe that a
fortnight has elapsed.

The sprint goal is what replaces it. It is the answer to *"what is this fortnight for?"*
— an intent, not a container. That makes it the load-bearing artefact of a flow system
that has kept its cadence.

## The failure this document exists to prevent

Most sprint goals are a scope list with a sentence wrapped round them:

> "Complete the payment stories: US-101, US-102 and US-103."

That is not a goal. It is a commitment container wearing a hat, and it reinstates
everything you have just spent months removing — the say/do scoreboard, the boundary
splitting, the pressure to pull work that isn't ready. If sprint goals get written this
way, you would genuinely be better off with no sprint goal at all.

**The test — the only one that really matters:**

> **Could this goal be achieved by a different set of stories than the ones we planned?**

If the answer is no, it's a scope list. Rewrite it.

A good goal survives its plan being wrong. That's the point of having one: when the team
discovers on day four that the approach doesn't work, the goal tells them what to do
instead. A scope list tells them only what they've failed to do.

**A second, softer test:**

> Could a stakeholder tell whether we achieved it, without looking at the board?

---

## What a good goal looks like

A sprint goal should express **one** of:

| Type | Shape | Example |
|---|---|---|
| Outcome | Something is true for a user that wasn't before | "A returning customer can check out without re-entering card details." |
| Risk reduction | A significant unknown becomes known | "We know whether the new provider can handle our peak volume — and if not, what we'd do instead." |
| Learning | A question gets answered | "We know which of the two onboarding flows converts better, from real traffic." |
| Enablement | Something becomes possible that wasn't | "Any engineer can deploy to staging without asking for help." |

Note that two of those four are satisfied by a **negative** answer. "The provider can't
handle peak volume" fully achieves the risk-reduction goal above. That's exactly right,
and it's the clearest illustration of the difference between a goal and a commitment: a
goal can be achieved by learning the answer is no.

### Good and bad, side by side

| Poor | Better | Why |
|---|---|---|
| "Complete US-101, 102, 103" | "A returning customer can check out without re-entering card details" | Scope list vs. outcome. Passes the different-stories test. |
| "Finish the migration" | "All read traffic is served from the new database, with a tested rollback" | "Finish" is unfalsifiable until someone argues about what finished means. |
| "Improve performance" | "The search page responds under 500ms at the 95th percentile for logged-in users" | No way to tell if you got there. |
| "Do the discovery work" | "We know whether to build or buy the reporting layer, and can defend the answer" | Activity vs. decision reached. |
| "Complete the spike and start the build" | "We know enough about the API limits to size the integration" | Two goals stapled together. |

---

## The goal does not fill the sprint

The most common misreading, and worth being explicit about.

A sprint goal is the **head of the queue, not the queue**. It answers "what is this
sprint *for*?" — not "what will we do?" Work outside the goal still flows: the next
capability, defects, unplanned work, small requests.

So this reasoning is a trap:

> "The goal only covers four stories, and we normally finish fifteen — so the team won't
> have enough to do. I'd better make the goal bigger."

That is a **utilisation** question: how do I fill the container? It is the model that
story points were retired to escape, returning in a new costume. The correct response to
"that's only four stories" is *"good — we'll finish it by day four and pull the next
thing."*

A goal that consumes the whole sprint is a **bad** goal, because a single blocker then
takes the goal down with it. Leave margin deliberately.

### If you need a three-clause goal to fill the sprint, that's a WIP signal

When a goal has to be stretched — *"...and owners can create and edit endpoints, and be
notified when a request arrives"* — it is telling you the team is running three or four
unrelated capabilities in parallel. Look at what sequencing them instead does:

| | Four in parallel | Sequenced, goal-led |
|---|---|---|
| Capability 1 done | day 14 | **day 4** |
| Capability 2 done | day 14 | day 7 |
| Throughput | 15 items | 15 items |

Identical throughput. A quarter of the cycle time on the first capability, and it is
deployable — and learnable from — ten days earlier. That is Little's Law, and it is
hypothesis H1 (`docs/01-diagnosis.md`) appearing in planning rather than in a chart.

**The sprint goal is the device that forces the sequencing.** Its "limiting" quality is
not a side effect to be worked around — it is the entire mechanism.

### If the goal feels reverse-engineered

Suspect the backlog, not your goal-writing. A backlog sliced by layer ("add the API",
"add the UI") is a **build plan**, and no honest outcome can be extracted from a build
plan — which is exactly what reverse-engineering feels like. See `docs/10-story-slicing.md`.

---

## Rules

**One goal per sprint.** Two goals is no goal — the moment they conflict, the team has
no basis for choosing, which is precisely when a goal would have been useful. If the
work genuinely doesn't share a theme, that is worth knowing: it usually means too many
concurrent initiatives, which is H1 arriving by a different route.

**The team writes it.** A goal handed down is a target, and targets get satisfied rather
than pursued. Your role is to ask whether it passes the two tests, not to author it.

**Write it before selecting the work, not after.** A goal reverse-engineered from a
pre-picked story list will always be a scope list, however it's phrased. Goal first, then
"what's the smallest set of work that gets us there?" The artefacts look the same either
way; only the direction of travel differs, and it decides whether the goal survives its
plan being wrong.

**Not every sprint needs one.** If a team is genuinely running a steady flow of unrelated
small items, an invented goal is worse than an honest "this sprint is flow — no single
theme". Manufacturing a goal to fill a template is how the practice dies.

**It doesn't constrain what else gets done.** Work outside the goal still flows. The goal
says what this fortnight is *for*, not what is permitted. It is the tiebreaker when two
things compete for attention, and the thing you protect when the sprint goes wrong.

---

## When the goal isn't met

This is information, not a failure, and how you respond the first two or three times
decides whether the practice survives. Distinguish three cases — they need opposite
responses:

1. **We learned the goal was wrong.** Best possible outcome. Say so explicitly, and
   celebrate it visibly, or nobody will ever admit it again.
2. **We were blocked.** The blocker is the finding. Tag it, aggregate it, and if the
   reason repeats across sprints it becomes your systemic constraint work
   (`docs/03-operating-cadence.md`).
3. **We never really worked on it.** The only one that warrants a hard conversation —
   and the conversation is about WIP and competing priorities, not effort. It usually
   means the team was pulled elsewhere, which is H1 or H3 showing up as a goal miss.

**Do not track a goal-achievement percentage.** The moment "% of sprint goals met"
becomes a number anyone reports upward, teams will write goals they're certain of, and
you will have rebuilt the say/do ratio with extra steps. The goal's value is in
directing decisions during the sprint, not in scoring the sprint afterwards.

---

## How this fits with forecasting

They answer different questions and should never be merged:

| | Sprint goal | Monte Carlo forecast |
|---|---|---|
| Horizon | This fortnight | Weeks to months |
| Question | What is this sprint for? | When will this body of work be done? |
| Audience | The team | Stakeholders |
| Form | An intent | A distribution |

A sprint goal is not a mini-forecast, and it is not a commitment you report on
externally. Keep it inside the team. The moment it appears in a stakeholder pack with a
tick or a cross next to it, it becomes a commitment, and everything on this page stops
being true.

---

## The one-line version, for the team wall

> **A sprint goal says what this sprint is for. If it can only be met by finishing exactly
> the stories we picked, it isn't a goal — it's a list.**

> **And it doesn't have to fill the sprint. It's the head of the queue, not the queue.**
