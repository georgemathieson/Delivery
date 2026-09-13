# 07 — Tooling shortlist

You chose to build the operating cadence first, which is right — a tool will not tell
you what conversation to have. This is a starting shortlist to pick up once you have a
few weeks of baseline and know which measures you actually use.

Everything below integrates with Azure DevOps. Verify current pricing and feature sets
directly; both change.

---

## The gap you're buying against

Azure DevOps gives you cycle time, lead time and a CFD for free. What it doesn't give
you is **Work Item Age** — your most important chart — or Monte Carlo forecasting, or
a clean wait-state breakdown. That is the shopping list.

---

## Candidates

### Lighthouse — *start here*

Open source, free, self-hosted (Windows, macOS, Linux, Docker), no cloud connection
required. Connects to Azure DevOps and Jira using their native query languages, and runs
continuous Monte Carlo forecasts — including the harder cases of multiple teams
contributing to one feature, and features not yet broken down.

Built by Benjamin Huser-Berta, who writes in the same tradition you're already drawing
on. The "no cloud connection" property also makes the internal approval conversation
much shorter.

**Why start here:** it's free, it directly replaces the spreadsheet-driven Monte Carlo
you're presumably running by hand, and it costs you nothing to abandon if it doesn't
fit. Trial it on one team.

**Watch for:** it is forecasting-led. Check how much of the aging/flow charting you need
it covers before assuming it replaces everything.

### ActionableAgile Analytics (55 Degrees)

The reference implementation of flow metrics. Cycle time scatterplot, **Aging Work in
Progress**, CFD, throughput run chart and Monte Carlo — the exact set in
`docs/02-measures.md`. Available as an Azure DevOps Marketplace extension, so it lives
inside the tool your teams already use, which matters a lot for adoption.

Paid, per-user. Daniel Vacanti's work underpins it, which means the metric definitions
are the rigorous ones rather than convenient approximations.

**Why consider it:** it is the shortest path from zero to every chart in this repo, and
the in-ADO placement means teams see the charts without navigating anywhere.

**Watch for:** per-user cost across three teams; confirm whether you need seats for
everyone or only for people opening the charts.

### Agile Analytics (Azure DevOps extension)

An ADO-native extension covering sprint health, flow metrics, DORA metrics and Monte
Carlo forecasting. Worth a look if you also want DORA alongside flow.

**Watch for:** breadth can mean shallower flow metrics. Check the aging chart
specifically — it is the one you cannot compromise on.

### FlowPulse

A Python package that runs queries against Azure DevOps or Jira and generates flow
metric charts plus Monte Carlo forecasts. Scriptable, automatable, free.

**Why consider it:** if you want charts generated on a schedule into a report rather
than a dashboard people must visit, this is the lowest-friction option — and it produces
the Monday-morning refresh in `docs/03-operating-cadence.md` automatically.

**Watch for:** no UI. Fine for you, less good for teams self-serving.

### Build it yourself (Analytics OData)

`docs/05-azure-devops.md` Option B. Everything is reachable through the Analytics
endpoint, and a script producing aging, WIP, throughput and wait-state charts is perhaps
a week of work plus ongoing maintenance.

**Recommendation: don't, initially.** With two to three teams the tools above cover it,
and your scarce resource is your attention, not licence budget. Revisit only if you find
a measure none of them provide — the most likely candidate being the wait-state
breakdown by blocker reason, which is specific to your tagging scheme.

---

## Suggested sequence

1. **Weeks 1–4:** no new tools. Run the cadence on ADO's built-in widgets plus the WIQL
   query and a spreadsheet for aging. Learn which measures you actually use.
2. **Week 5:** trial Lighthouse on one team — free, and it replaces hand-run Monte Carlo.
3. **Week 8:** if aging and flow charting are still the painful part, trial
   ActionableAgile on one team and compare.
4. **Week 12:** decide, and standardise across all teams.

Deliberately slow. Tools adopted before you know what question you're asking become
dashboards nobody reads, and you only get one credible rollout per year.

---

## Sources

- [ActionableAgile Analytics — 55 Degrees](https://www.55degrees.se/products/actionableagileanalytics)
- [ActionableAgile Analytics for Azure DevOps — Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=actionableagile.aa-analytics-paid)
- [Comparing Flow Metrics Tools — ProKanban](https://prokanban.org/blog/comparing-flow-metrics-tools-find-the-right-one-for-your-needs)
- [Lighthouse — Getting Started](https://blog.letpeople.work/p/lighthouse-getting-started)
- [How Lighthouse Forecasts](https://blog.letpeople.work/p/how-lighthouse-forecasts)
- [How to Visualize Work Item Age in Azure DevOps](https://medium.com/@benjihuser/how-to-visualize-work-item-age-in-azure-devops-c6304f3c4333)
- [Running Monte Carlo Simulations in Azure DevOps](https://medium.com/@benjihuser/running-monte-carlo-simulations-in-azure-devops-728746ef15be)
- [Agile Analytics for Azure DevOps](https://ado-analytics.baytekdev.com/)
- [FlowPulse](https://pypi.org/project/flowpulse/1.0.6)

---

## Further reading

Beyond the sources above, one article covers much of the same ground as this repo,
reached independently:

- Paul Brown, ["The Dirty Secret Behind Agile
  Failure"](https://thrivve.partners/the-dirty-secret-behind-agile-failure) — argues that
  Agile is incomplete rather than wrong, because it never taught flow. Names the same four
  metrics used here. Three ideas borrowed into this repo: *WIP-in-disguise*
  (`docs/10-story-slicing.md`), the expedite policy and ongoing prioritisation
  (`docs/04-policies.md`), and cycle time as time-to-feedback and therefore risk exposure
  (`docs/02-measures.md`).

  Worth reading with the caveat that it is argued from experience rather than evidence —
  it tells you what is wrong, where this repo makes you measure whether it is. It also
  stops at the team boundary: it has no equivalent of `docs/11-demand-and-intake.md`, no
  forecast calibration, and does not confront the sprint-as-commitment-container problem
  in `docs/01-diagnosis.md`.
