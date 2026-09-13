# Talk 1 — the problem, and what we're trying

**Length:** 20 minutes, plus as long as the questions run
**Audience:** curious, uncommitted, other teams
**Goal:** they look at their own work differently. *Not* adoption.

If they leave wanting to check something about their own team, it worked. If they leave
having agreed to a process, be suspicious — that's compliance, and it won't survive
contact with their next busy fortnight.

---

## Structure

### 1 · Shared pain — 3 min

Open with the honest version. No preamble about frameworks.

> "Over the last couple of years we introduced 3 amigos. We dropped hours for points, then
> dropped points for right-sizing. We run Monte Carlo simulations. We give stakeholders
> probability ranges instead of dates.
>
> Every one of those is a good practice. Work still didn't land when we expected it to.
>
> Anyone else recognise that?"

Then **stop and let them answer.** This is the most important pause in the talk. You are
establishing that this is a shared problem before offering any view about it — and you
may learn something that changes the rest of your talk.

### 2 · The uncomfortable bit — 4 min

Two realisations. Keep them short; they do the work.

**One: everything we'd introduced acted on the inputs.** How well-formed a story is, how
honestly we describe the forecast. None of it changed how work *moves*. Monte Carlo is
an honest description of a system nobody has changed yet.

**Two — the one that stung: every measure we had could only tell us a sprint had already
ended badly.** By the time a lagging indicator moves, every decision that caused it has
been made. We had no way to see trouble while we could still do something about it.

> "We'd built a really good system for finding out afterwards."

### 3 · Something they'll recognise, right now — 5 min

Pick **one**. The aim is a visible flicker of recognition in the room, not coverage.

**Option A — horizontal slicing** *(strongest if their backlog looks like this)*

Put up two tickets:

```
001  Add API to get endpoints
002  Add UI to display endpoints
```

> "That's not two small stories. It's one story cut in half the wrong way — and neither
> half delivers anything or proves anything. When 002 finds out the API returns a group
> ID and the UI needs a name, the rework happens silently inside 002. 001 is on record
> as fast and clean.
>
> Here's the part that got us: on every measure we had, that looks like good
> right-sizing. Small items. High count. Short cycle times. The chart applauds."

**Option B — work item age** *(strongest for a metrics-minded room)*

> "Every chart we had described finished work. So we started asking one question about
> the unfinished work instead: how old is it, right now? And in a review, of the oldest
> item: what is stopping this finishing today?
>
> Not 'how's it going'. That gets you a status update. The other question gets you an
> obstacle with a name."

### 4 · What we're trying — 4 min

Brief, and explicitly an experiment.

> "So we're doing three things. Measuring work in flight rather than work finished —
> mainly how old things are and how many we've got on at once. Cutting stories so each
> one delivers something on its own. And recording every forecast when we make it, so in
> a year we can tell you objectively whether our forecasts are honest, rather than
> asking you to take our word for it.
>
> That's it. We're not rolling anything out. It's one team."

Optionally show `OVERVIEW.md`'s loop diagram here — **once**, without walking through it.
It's a picture of the shape, not a syllabus.

### 5 · What we don't know — 2 min

Do not skip this. It's where the credibility is.

> "We might find the teams were already fine and the problem was the sprint boundary all
> along. We might find it's how work gets allocated, which isn't a team problem at all.
> We genuinely don't know yet.
>
> We've written down what we expect to see and by when. If it doesn't happen, I'll come
> back and tell you that too."

### 6 · The ask — 2 min

One thing. See `03-the-invitation.md`.

> "I'm not asking you to adopt anything. One thing, free, and you can stop next week if
> you hate it: in your standup, walk the board right to left, oldest item first, and ask
> what's stopping the oldest thing finishing. Don't go round the people.
>
> And if you're curious — come and sit in on one of our reviews. No commitment, just come
> and watch."

---

## Things to hold back

**Don't show the full document set.** Sixteen files reads as a programme, and programmes
get resisted or mandated — both fatal.

**Don't show your teams' numbers.** They'll be read as a comparison however you frame
it, and it puts the other teams on the defensive for the rest of the session.

**Don't use "predictability" as the headline.** It sounds like a demand for commitment,
which is the opposite of the point. "Finding out earlier" lands better in a room that
hasn't heard the argument yet.

**Don't promise speed.** You don't know, and it's not what this is for. If asked, see
`02-questions-and-pushback.md`.

---

## If you only get five minutes

Cut to: the shared pain, the "we'd built a good system for finding out afterwards" line,
one concrete example, and the standup ask. That version works fine — it's the whole
argument, and everything else is elaboration.
