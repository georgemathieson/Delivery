# Delivery

A delivery operating model for making teams predictable and reliable to stakeholders.

## The thesis

Predictability is a **property of a system**, not a behaviour you can ask a team to
exhibit. You cannot instruct a team into predictability, and you cannot estimate your
way there. You get it by reducing the variability of how long work takes to flow
through the system, and by measuring honestly whether that variability is shrinking.

Practices already in place — 3 amigos, right-sized stories, Monte Carlo forecasting,
probabilistic ranges to stakeholders — are all sound. They act on the **inputs** to the
system (how well-formed work is, and how honestly it is described). None of them act on
the **flow** of work through the system, which is where predictability is actually won
or lost.

This repository is the instrumentation and the operating rhythm for acting on flow.

## What's here

| Path | Purpose |
|---|---|
| `docs/01-diagnosis.md` | Why the current practices haven't moved delivery, and the live hypotheses |
| `docs/02-measures.md` | What to measure, what each measure tells you, and what to stop measuring |
| `docs/03-operating-cadence.md` | The rhythm: what happens daily, weekly, monthly, quarterly |
| `docs/04-policies.md` | Explicit policies — WIP limits, age limits, ready, blocked, unplanned work |
| `docs/05-azure-devops.md` | Getting the data out of Azure DevOps |
| `docs/06-stakeholder-communication.md` | How to hold a probabilistic conversation without losing trust |
| `docs/07-tooling-shortlist.md` | Software that can help, and what to build vs buy |
| `templates/` | Fillable packs for each cadence event |
| `teams/` | One folder per team: running log, policies, current state |

## How to start

1. Read `docs/01-diagnosis.md`. Pick the two hypotheses you think are most likely.
2. Stand up the measures in `docs/02-measures.md` for **one** team first (`docs/05-azure-devops.md`).
3. Run the weekly review in `templates/weekly-team-review.md` for four weeks without
   changing anything else. You are establishing a baseline, not fixing yet.
4. Then run one experiment at a time from `templates/experiment-log.md`.

Do not roll all of this out to all teams at once. You will not be able to tell what
worked.
