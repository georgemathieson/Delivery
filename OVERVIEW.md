# Delivery, on one page

> **Predictability isn't a promise you make. It's a property of a system — one you can
> measure, and change.**

---

## The system

```mermaid
flowchart LR
    DEMAND["<b>Demand</b><br/>Fewer things<br/>started at once"]
    TEAMS["<b>Teams</b><br/>Work finishes<br/>instead of piling up"]
    VALUE["<b>Delivered</b><br/>Small, whole,<br/>in production"]
    STAKE["<b>Stakeholders</b><br/>Never surprised"]

    DEMAND ==> TEAMS ==> VALUE ==> STAKE

    SEE["<b>See it happening</b><br/>Age · WIP<br/>Throughput · Cycle time"]
    DIAG["<b>Name the cause</b><br/>Which constraint<br/>is actually binding?"]
    ACT["<b>Remove one</b><br/>One change,<br/>measured"]

    TEAMS -.-> SEE
    SEE --> DIAG
    DIAG --> ACT
    ACT -. "changes the system" .-> TEAMS

    HIST["<b>What we actually did</b><br/>Throughput history"]
    FC["<b>Forecast</b><br/>A range, with<br/>a confidence level"]
    CAL["<b>Calibration record</b><br/>Where actuals landed<br/>in the distribution"]

    VALUE -.-> HIST
    HIST --> FC
    FC ==> STAKE
    STAKE -.-> CAL
    CAL -. "proves it's honest" .-> FC

    VALUE -. "frees capacity to start the next thing" .-> DEMAND

    classDef spine fill:#1f2937,stroke:#111827,color:#ffffff,font-weight:bold
    classDef loop fill:#eef2ff,stroke:#4f46e5,color:#1e1b4b
    classDef fore fill:#ecfdf5,stroke:#059669,color:#064e3b

    class DEMAND,TEAMS,VALUE,STAKE spine
    class SEE,DIAG,ACT loop
    class HIST,FC,CAL fore
```

**Three loops, and that's the whole idea.**

| Loop | What it does | Why it was missing |
|---|---|---|
| **Improvement** | See → diagnose → remove a constraint → the system changes | Previous practices described the system. None fed back into it |
| **Forecast** | What we did → a range → what happened → proof it was honest | Forecasts were made, but never scored, so trust stayed an opinion |
| **Demand** | Finishing frees capacity to start the next thing | Nothing limited what could be started, so everything was |

---

## What this makes possible

Six things you couldn't do before.

| | Before | Now |
|---|---|---|
| **1** | You found out at the end of the sprint | **You see trouble while you can still act on it** |
| **2** | Theories about why delivery is slow | **You know which constraint is actually binding** |
| **3** | "It feels better" | **You can tell whether a change worked** |
| **4** | Everything started, everything late | **Start fewer things, and the first one lands in a third of the time** |
| **5** | Layers that prove nothing until they meet | **Something whole and usable, every few days** |
| **6** | "Trust us" | **Evidence the forecast is honest** |

---

## What we stopped doing

Not everything here is an addition. Some of it is removal.

```mermaid
flowchart LR
    A["Estimating in hours"] --> B["Story points"] --> C["Right-sized stories"] --> D["<b>Counting what finishes</b>"]
    E["Sprint scope commitment"] --> F["<b>A sprint goal<br/>and a forecast</b>"]
    G["Velocity as a target"] --> H["<b>Throughput as an observation</b>"]
    I["Reporting what happened"] --> J["<b>Seeing what's happening</b>"]

    classDef old fill:#f3f4f6,stroke:#9ca3af,color:#6b7280
    classDef new fill:#1f2937,stroke:#111827,color:#ffffff
    class A,B,E,G,I old
    class C,F,H,J new
    class D new
```

---

## The one number

Everything else is diagnosis. This is the score:

> ### The gap between your 50th and 95th percentile cycle time.
>
> Narrowing = becoming predictable. Not moving = you've built reporting, not change.

Not throughput. Not velocity. Not how many sprints hit their scope. **The spread.**
Predictability is a narrow distribution, and nothing else.

---

## What it costs

**Three hours a week**, across three teams.

| | |
|---|---|
| 30 min | Refresh the charts |
| 90 min | One 30-minute flow review per team |
| **60 min** | **Removing the constraint you found** |
| 20 min | Notes |

The hour in bold is the one that changes anything. The rest only makes problems visible.

---

## How it could fail

Named in advance, so they're recognisable when they happen.

1. **All three teams at once** — no way to tell what worked
2. **No baseline** — no way to settle whether it improved
3. **The constraint hour gets dropped** — excellent reporting, unchanged system *(most likely)*
4. **A chart gets used to question a person** — the data stops being honest, and doesn't recover

---

*Full model: [`README.md`](README.md) · Start at [`docs/00-start-here.md`](docs/00-start-here.md)*
