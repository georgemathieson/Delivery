# 05 — Getting the data out of Azure DevOps

Azure DevOps holds everything you need, but not all of it is exposed in the built-in
widgets. This is what's available out of the box, what isn't, and how to get the rest.

> These queries are written against standard Azure Boards Analytics and have not been
> run against your instance. Field names vary with process template (Agile / Scrum /
> Basic / custom) and with any custom states you've added. Treat them as a starting
> point and expect to adjust state names.

---

## What you get out of the box

Azure DevOps Analytics provides these dashboard widgets with no setup:

| Widget | Gives you | Good enough? |
|---|---|---|
| **Cycle Time** | Scatterplot with percentile lines | Yes — this is your measure 4 |
| **Lead Time** | Same, from creation | Yes |
| **Cumulative Flow Diagram** | WIP by state over time | Partly — see below |
| **Burndown / Burnup** | Sprint scope progress | Not used here (scope-boundary thinking) |
| **Velocity** | Points or count per sprint | Do not use |

**The CFD is your WIP measure**, but read it correctly: you want the *vertical
thickness* of the in-progress bands over time, not the shape of the top line. Widening
bands mean growing WIP. It is a serviceable WIP chart and an unhelpful anything-else
chart.

**The significant gap: there is no built-in Work Item Age chart.** That is your most
important measure, and you will have to build or buy it.

---

## Getting Work Item Age

Three options, in increasing order of effort.

### Option A — A board query plus a spreadsheet (start here)

A saved WIQL query returning all in-progress items with the date they entered the active
state, exported to CSV and charted against percentile bands you calculate once a quarter.

```sql
SELECT [System.Id], [System.Title], [System.State], [System.AssignedTo],
       [Microsoft.VSTS.Common.StateChangeDate], [System.Tags]
FROM WorkItems
WHERE [System.TeamProject] = @project
  AND [System.WorkItemType] IN ('User Story', 'Bug')
  AND [System.State] IN ('Active', 'In Progress', 'Code Review', 'Ready for Test')
ORDER BY [Microsoft.VSTS.Common.StateChangeDate] ASC
```

**Important caveat:** `StateChangeDate` is the date of the *most recent* state change,
not the date the item first became active. An item that moves In Progress → Blocked →
In Progress will show an age that has silently reset. For a weekly review it is usually
close enough to be useful; for anything you report on, use Option B.

Sorted ascending, the top of that list *is* your review agenda — oldest first.

### Option B — Analytics OData (the accurate version)

The Analytics OData endpoint exposes historical snapshots, so you can reconstruct when
an item genuinely first entered each state, and how long it spent there.

```
https://analytics.dev.azure.com/{org}/{project}/_odata/v4.0-preview/WorkItemRevisions
  ?$filter=WorkItemType eq 'User Story' and RevisedDate ge 2026-01-01Z
  &$select=WorkItemId,State,ChangedDate,RevisedDate,Title
  &$orderby=WorkItemId,ChangedDate
```

From the revision stream you can derive, per item: first entry into each state, total
days per state, active vs waiting split, blocked duration, and a true age that survives
state round-trips. This is the dataset that answers hypotheses H2, H4 and H5 — none of
which the built-in widgets can address.

There is also a `WorkItemBoardSnapshot` entity giving daily board position, which is a
convenient way to compute WIP per day without reconstructing it from revisions.

Authenticate with a PAT scoped to **Analytics (read)** only.

### Option C — Buy it

Several tools plug into ADO and give you aging, WIP and Monte Carlo without building
anything. See `docs/07-tooling-shortlist.md`. Given two to three teams, this is a very
defensible choice — the build cost here is real and it is not your core job.

---

## Fields you need to add

| Field / mechanism | Purpose | Notes |
|---|---|---|
| `Blocked` (tag or field) | Blocked-days measure | ADO Scrum template has a Blocked field; Agile template does not — use a tag |
| `BlockedReason` | Aggregating blocker causes | Custom picklist with the fixed values from `docs/04-policies.md` |
| `unplanned` tag | Unplanned work % | Tag is enough; a field is tidier if you'll report on it |
| Explicit waiting states | Wait-state breakdown | Add `Code Review` and `Ready for Test` as real board columns if they aren't already |

That last row does the most work. If review and test-wait are sub-states of a single
"In Progress" column, the queue that is probably causing your problem is mathematically
invisible. Splitting the column is a small change with an outsized diagnostic payoff.

---

## Suggested dashboard, per team

One ADO dashboard per team, same layout for all:

1. Work Item Age (built or embedded — the most prominent tile)
2. Cycle Time scatterplot with 50/70/85/95 percentile lines
3. Throughput run chart, 12 weeks
4. CFD, 12 weeks
5. Blocked items with days blocked, sorted descending
6. Query tile: items past the 85th percentile band

Same layout for every team so you can move between them without re-orienting, and so
teams can read each other's without explanation.

---

## A caution on the data

Board data reflects what people record, not what happens. Before drawing conclusions,
spot-check a handful of items against what the team says actually occurred. Common
distortions:

- Items moved to done in a batch at sprint end, compressing the cycle-time left tail
- Items sitting in In Progress while the person is actually on something else
- Blocked never recorded because it "wasn't worth updating the ticket"
- Work that never got a ticket at all

Fixing the recording is part of the work, not a prerequisite to starting it. Begin with
the data you have, note where it lies, and improve it as you go.
