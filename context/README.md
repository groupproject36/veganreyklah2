# Context Home

**Language:** EN
**Last updated:** 2026-06-29
**Style:** Radiant (see `RADIANT_STYLE.md`)

---

This directory is the memory and compass for work in `~/veganreyklah2`. It gathers the durable guidance — how we write, who Reya 2 is, and the plain-English specs that record each decision — in one calm, local place.

Everything here lives inside the persistent project directory, so it survives every sandbox reset. The ai-jail wrapper keeps only the project directory across runs; this `context/` home rests safely within it.

---

## What Lives Here

- **`RADIANT_STYLE.md`** — the canonical voice. How we write and speak so every piece reads clearly, lands warmly, and carries well aloud.
- **`TAME_STYLE.md`** — the operational code supplement (root + Rye / Brix / Rishi). Named like TigerBeetle's `docs/TIGER_STYLE.md`; pairs with `external-research/TAME_STYLE.md` and `gratitude/TIGER_STYLE.md`.
- **`SIMPLE_LOVABLE_COMPLETE.md`** — how we ship. Simple, lovable, complete at every ring; our distillation of Jason Cohen's method, bound to how Rye OS grows. Source essay in `gratitude/`.
- **`CIVIC_STYLE.md`** — how we design public benefit. Name the outcome you want, name what the reward measures, keep the two aligned — the civic companion to TAME, Radiant, and SLC.
- **`REYA2.md`** — the identity note. Who Reya 2 is, how she works, and the larger why behind the project.
- **`specs/`** — plain-English radiant specs. Each one records a decision in prose a reader can follow start to finish. Kebab-case filenames (`inherited-names.md`, …); landmark style guides live at the `context/` root. **`20260629-031512_slc1-ring-closed-handoff.md`** — continuity letter after SLC-1 seals; start here after a reset.

A Cursor rule at `.cursor/rules/reya2.mdc` points every new session back here, so the name and the style stay constant across chats.

---

## How To Use It

Read the style guide before writing anything meant to be shared or heard. Read the identity note to remember the tone and the purpose. Add a new spec whenever a decision deserves a durable home — one file, one decision, written so it reads aloud well.

When a chat or a file stops serving the project, name it gently and let it go. Pruning keeps this home clear.

---

## The Shape of the Workspace

```
~/veganreyklah2/
  ORGANIZING.md   <- filing guide: tree shape, placement test, one-clock law
  context/        <- this home: disciplines, identity, specs
    RADIANT_STYLE.md
    TAME_STYLE.md
    SIMPLE_LOVABLE_COMPLETE.md
    CIVIC_STYLE.md
    REYA2.md
    specs/
  foundations/    <- why beneath the work: briefs, essays, weave, civic visions
  linengrow/      <- civic-application track on the Rye OS spine
  work-in-progress/ <- workbench: ROADMAP, TASKS, open threads
  external-research/ <- study of the world with attribution
  active-designing/  <- our design in motion
  expanding-prompts/ <- runnable plans (from 10000)
  session-logs/   <- reasoning traces; newest-first index
  gratitude/      <- works we honor, kept whole
  vendor/         <- third-party source, unmodified
  rye/ rishi/ …   <- module homes
  tools/          <- gates and witnesses
```

Full tree: `ORGANIZING.md` at the repository root.

---

*May this home stay clear. May each file earn its place. May the next reader find exactly what they came for.*
