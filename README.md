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

**[One-page overview →](OVERVIEW.md)**

## What's here

| Path | Purpose |
|---|---|
| `OVERVIEW.md` | The one-pager — the system, its three loops, and what it makes possible |
| `docs/00-start-here.md` | **Read first** — who each document is for, and the 90-day plan |
| `docs/01-diagnosis.md` | Why the current practices haven't moved delivery, and the live hypotheses |
| `docs/02-measures.md` | What to measure, what each measure tells you, and what to stop measuring |
| `docs/03-operating-cadence.md` | The rhythm: what happens daily, weekly, monthly, quarterly |
| `docs/04-policies.md` | Explicit policies — WIP limits, age limits, ready, blocked, unplanned work |
| `docs/05-azure-devops.md` | Getting the data out of Azure DevOps |
| `docs/06-stakeholder-communication.md` | How to hold a probabilistic conversation without losing trust |
| `docs/07-tooling-shortlist.md` | Software that can help, and what to build vs buy |
| `docs/08-diagnostic-decision-tree.md` | Routing: which hypothesis to chase, and how to triage an aged item |
| `docs/09-sprint-goals.md` | Writing sprint goals that don't reinstate scope commitment |
| `docs/10-story-slicing.md` | Thin vertical slices — why "small" and "deliverable" aren't in tension |
| `docs/11-demand-and-intake.md` | Portfolio WIP — the layer where you have authority and the teams don't |
| `docs/12-success-criteria.md` | Checkpoints, what determines success, and how you'd know it failed |
| `templates/` | Fillable packs for each cadence event |
| `teams/` | One folder per team: running log, policies, current state |
| `sharing/` | Talking to other teams — the talk, the pushback, the small ask |

## How to start

**Read `docs/00-start-here.md`.** It says who each document is for, what to do in your
first week, and the 90-day sequence.

The short version: decide the sprint-boundary question, pick **one** team, baseline for
four weeks without changing anything, then run one experiment at a time.

Do not roll all of this out to all teams at once. You will not be able to tell what
worked.

Most of this repo is for you, not the teams. Only `docs/04-policies.md` and
`docs/09-sprint-goals.md` are team-facing.
