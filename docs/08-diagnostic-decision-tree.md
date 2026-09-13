# 08 — Diagnostic decision tree

Two decision aids: one for diagnosing a **team**, one for triaging an **aged item** in
the weekly review.

Use them as routing, not as a script. Their job is to stop you defaulting to whichever
cause you found last time, and to make sure you check things in an order where the
answers can be trusted. If the tree points somewhere your judgement says is wrong,
follow your judgement — then work out which question the tree is missing.

---

## Tree 1 — Diagnosing a team

**Check data integrity first.** Hypotheses H3 and H4 corrupt the very measures you'd use
to test H1, H2, H5 and H6. Diagnosing WIP from a throughput history polluted by
boundary-splitting wastes a month and produces a confident wrong answer.

```mermaid
flowchart TD
    A["Team not delivering predictably"] --> B{"Is all work on the board?<br/>Unplanned work under 20%<br/>and included in forecast history?"}
    B -->|"No"| H3["<b>H3 — Unplanned work</b><br/>Forecasts are structurally optimistic.<br/>Make it visible, tag it, feed it into<br/>the throughput history.<br/><i>Fix before diagnosing anything else.</i>"]
    B -->|"Yes"| C{"Any items split at a sprint<br/>boundary, or age reset<br/>to zero on carryover?"}
    C -->|"Yes"| H4["<b>H4 — Carryover masked by splitting</b><br/>Cycle-time and throughput history<br/>describe a system that doesn't exist.<br/>Stop boundary splitting, let items<br/>age visibly.<br/><i>Re-baseline after 4 weeks.</i>"]
    C -->|"No"| D["Data is trustworthy.<br/>Now diagnose flow."]

    D --> E{"Arrivals consistently<br/>exceed departures?<br/>Or WIP above ~1 per person?"}
    E -->|"Yes"| H1["<b>H1 — Too much WIP</b><br/>Set a limit 20% below current average.<br/>Highest-leverage, cheapest fix.<br/><i>Start here if in doubt.</i>"]
    E -->|"No"| F{"What share of cycle time<br/>is spent in waiting states?"}

    F -->|"Over half"| G{"Waiting where?"}
    G -->|"Review / test / release"| H5["<b>H5 — Downstream queues</b><br/>Make those states explicit columns,<br/>then WIP-limit them specifically.<br/>Review queues respond very well."]
    G -->|"Blocked on dependency<br/>or decision"| H6["<b>H6 — Dependency / decision wait</b><br/>Aggregate blocked days by reason tag.<br/>Systemic ones are yours to remove."]

    F -->|"Under half"| I{"Long gap between 'started'<br/>and first real activity?"}
    I -->|"Yes"| H2["<b>H2 — Started before ready</b><br/>Tighten the Definition of Started.<br/>Queue is being hidden as age."]
    I -->|"No"| J{"Is the 50th–95th<br/>cycle-time gap narrowing<br/>over the last quarter?"}
    J -->|"Yes"| K["System is improving.<br/>Hold the cadence, keep baselining.<br/>Check the sprint boundary isn't<br/>the only thing 'failing'."]
    J -->|"No"| L["No single dominant cause.<br/>Look at throughput run chart shape:<br/>saw-tooth peaking at the boundary<br/>means batching, not slowness."]
```

### The question the tree can't ask

If you reach the bottom with nothing conclusive, ask this one by hand:

> **Are the Monte Carlo forecasts roughly accurate while sprints routinely carry over?**

If yes, the teams are predictable and only the boundary is failing. No amount of flow
work will fix that, because nothing is broken — the scoreboard is measuring the wrong
unit. That's `docs/01-diagnosis.md`, "the sprint-boundary contradiction", and the fix is
a conversation, not an intervention.

---

## Tree 2 — Triaging an aged item in the weekly review

For each item past the 85th percentile band, oldest first. Every item leaves the meeting
with a named next action and an owner.

```mermaid
flowchart TD
    A["Item past 85th percentile band"] --> B{"Is it blocked?"}
    B -->|"Yes"| C{"Blocked more<br/>than 2 days?"}
    C -->|"Yes"| D["Tag the reason.<br/>Escalate with a named owner<br/>and a date.<br/><i>Log the reason tag — repeats<br/>across weeks are systemic<br/>and are yours to fix.</i>"]
    C -->|"No"| E["Name who is chasing it<br/>and when it gets re-checked."]

    B -->|"No"| F{"Is anyone actually<br/>working on it today?"}
    F -->|"No"| G["Why was it started?<br/><b>This is an H2 signal.</b><br/>Either start it properly now,<br/>or move it back and record<br/>that it was pulled too early."]
    F -->|"Yes"| H{"Has it been actively<br/>worked longer than<br/>a typical item?"}
    H -->|"Yes"| I{"Is it bigger than<br/>we thought?"}
    I -->|"Yes"| J["Split it.<br/><b>Keep the original start date<br/>on the remainder</b> — resetting<br/>age to zero is how carryover hides."]
    I -->|"No"| K["Swarm it.<br/>Who else can join today<br/>to get it finished?"]
    H -->|"No"| L["It's waiting on something<br/>not yet named.<br/>Find it — that's the whole<br/>point of the question."]

    A --> M{"Past the 95th?"}
    M -->|"Yes"| N["<b>Unblock, split, or stop.</b><br/>Stopping is a real option and<br/>is used far too rarely.<br/>Four times typical cycle time<br/>is the item telling you something<br/>about its value or readiness."]
```

### The one question

Every branch above is a way of answering a single question, asked of the **item** and
never of the person:

> **What is stopping this finishing today?**

Not "how's it going". "How's it going" gets you a status update and a feeling. The
question above gets you an obstacle with a name, which is the only thing you can
actually act on.
