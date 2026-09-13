# Flow simulation

A model of a delivery system you can run policies against, to find out where the
playbook in `docs/` is weak.

```
python3 sim/experiments.py > sim/RESULTS.md
```

Pure standard library, ~25 seconds, deterministic per seed.

## Why simulate at all

In a real organisation you never see ground truth. You cannot know how long an item
"should" have taken, so you cannot tell whether your instruments are telling you the
truth. A simulation can, because it controls the ground truth.

That makes the interesting question not *"does the policy work"* but **"would the team's
own measures have revealed what was happening?"** Several of the findings in
`FINDINGS.md` are about measures failing to see things, and none of them could have been
established from real data.

## Design

Three things are deliberately separated:

| Layer | Contents |
|---|---|
| **Ground truth** | Hidden effort per item (lognormal), blocker occurrence and duration, late-integration rework |
| **Observation** | Start and finish days only — exactly what a board records |
| **Policy** | WIP limit, pull order, slicing, expedites, arrivals, capacity regime |

Every metric reported is computed **from the observation layer only**, the same way a
team would compute it from Azure DevOps. Ground truth is used only to judge whether
those metrics were right.

## Mechanisms modelled

- **Effort** is lognormal — right-skewed, like real cycle times. Not normal.
- **Capacity sharing**: available engineer-days are spread across items in progress,
  capped at 1 day per item per day. This reproduces Little's Law without being told to.
- **Context switching**: when WIP exceeds headcount, capacity is reduced ~18% per
  excess concurrent stream (floor 35%). A Weinberg-style heuristic, not a measurement.
- **Blocking**: a daily hazard with exponential duration.
- **Horizontal slicing**: paired items, neither releasable until both are code-complete,
  with a probability of late-integration rework landing on both when they finally meet.
- **Expedites** pre-empt the WIP limit; **unplanned work** joins the front of the queue.
- **Capacity regimes**: per-sprint multipliers, for modelling incidents and attrition.

## What it does NOT model

Be sceptical of anything that would depend on these:

- **People.** No individuals, skills, holidays, morale, or learning. Capacity is fungible.
- **Quality.** No escaped defects, no rework except late integration on paired items.
- **Dependencies between teams.** Single team only.
- **Demand management.** The portfolio layer in `docs/11-demand-and-intake.md` is absent.
- **Discovery.** Items don't change scope or get cancelled once started.
- **Feedback.** Nothing that is delivered changes what should be built next — which is
  precisely the mechanism `docs/02-measures.md` calls cycle-time-as-risk-exposure.
- **Human response.** The simulated team never swarms, splits, or escalates, so the
  *interventions* the playbook recommends in a review are not represented. Only the
  standing policies are.

That last one matters most: this tests the **policies**, not the **cadence**. It can tell
you whether a WIP limit helps. It cannot tell you whether a weekly flow review helps.

## Parameters are invented

`effort_median`, `block_prob_per_day`, the switching penalty and the rework probability
are plausible, not measured. Directions of effect are trustworthy where they are large
and monotonic; magnitudes are not. Treat any single number here as a hypothesis to check
against your own data, never as a result.

## Files

| File | Purpose |
|---|---|
| `flowsim.py` | The model, the Monte Carlo forecaster, and the observation helpers |
| `experiments.py` | Six experiments, each varying one policy over 20 seeds |
| `RESULTS.md` | Generated output |
| `FINDINGS.md` | What it found, including where it contradicts `docs/` |
| `app.html` | The same model as an interactive page — presets, live charts, pin-and-compare |

## The interactive version

`app.html` runs the model in the browser. Open the file directly, or use the published
version if one has been shared with you.

Six presets jump to the findings in `FINDINGS.md`. **Pin this run** freezes the current
configuration as a dashed baseline on every chart, so you can change one control and read
the difference rather than remembering two sets of numbers.

Two things worth doing first:

- Pin *Balanced*, then drag WIP from 5 to 14. The delivery curve bends away from the
  baseline and days-to-clear rises by more than half — same people, same work.
- Pin *Balanced*, then set horizontal slicing to 80%. Watch what **doesn't** move: the
  p50–p95 spread barely changes while delivery slides out by weeks. That is finding 2 made
  visible — a team watching only percentiles would not see it.

The page carries the same caveats as the rest of this folder. Every chart on it is
computed from start and finish dates only; the ground truth the model holds is withheld
from the charts deliberately, which is the whole reason a simulation can say something
real data cannot.
