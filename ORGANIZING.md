# Organizing the Repository

*A durable guide to where work lives, how new writing earns its place, and how the tree stays honest over time.*

**Language:** EN
**Last updated:** 2026-06-28
**Style:** Radiant (see `context/RADIANT_STYLE.md`)
**Voice:** Reya 2

---

## A Word First

This repository holds an operating system, a civic application built upon it, the research and design that feed both, and the disciplines that govern how we write code, prose, product, and public benefit. The tree is large on purpose. This guide names its shape so a person or an agent arriving fresh can orient in one calm read — without memorizing countdown conventions, count-up exceptions, or season-specific snapshots that go stale the moment they are written.

Read the sections below when you wonder where a new file belongs. When a season's placements are settled, record them in `session-logs/`; this guide stays evergreen.

---

## The Shape of the Tree

**`context/`** — memory and compass. The disciplines we keep across every track: Tiger and TAME for code rigor, Radiant for prose, Simple-Lovable-Complete for product scope, and Civic for designing public benefit so the reward points at the good. Identity (`REYA2.md`), and `specs/` for plain-English decisions that deserve a durable home.

**`foundations/`** — the why beneath the work: foundation briefs, the distilled essays and the weave that composes them, and the civic visions. Dated artifacts rest beneath a living README.

**`linengrow/`** — the civic-application track: Linengrow's README, business model, and venture pitch, sharing the one spine with the operating system. It graduates to its own repository once its first ring runs.

**`work-in-progress/`** — the workbench. The living roadmap (`ROADMAP.md`), the granular plan (`TASKS.md`), open threads, and dated artifacts for work still in motion. Finished scaffolding graduates to `archive/`.

**`active-designing/`** — design in motion. Our own module names, RISC-V-first, siloed from gratitude sources. Dated briefs; living README index.

**`external-research/`** — study of the world with attribution. Explorations, comparisons, voiced adaptations of gratitude sources. Living README.

**`expanding-prompts/`** — intent expanded into runnable plans. Counts upward from `10000`; each prompt is a dated artifact that agents can execute.

**`session-logs/`** — reasoning traces. One-clock filenames; newest-first index in `README.md`. What happened lives here; what is next lives in `TASKS.md`.

**`rye-learning-process/`** — the almanac and learning record. How we grow capability in the open.

**`strengthening-compiler/`** — the strengthening chronicle. Analysis complete; record, not active product track.

**`gratitude/`** — works we honor, held whole for clean-room study. Never copy code or text into our modules.

**`vendor/`** — third-party source the build leans on, local and unmodified.

**Module homes** — `rye/`, `rishi/`, `tally/`, `caravan/`, `mantra/`, `brushstroke/`, `comlink/`, `pond/`, `aurora/`, `linengrow/` (vision until graduation), and the rest: each grows a seed toward a running whole.

**`tools/`** — gates, witnesses, launch scripts, and the strict checks that keep the tree honest.

**Root** — `SOURCE.md`, `CLAUDE.md`, this guide, and a few allow-listed files that orient newcomers before they dive.

---

## The One Test for Placement

Read the piece aloud. Ask what it is *doing*:

- **Governing how we write or decide** → `context/` (discipline or spec).
- **Naming why the work means something** → `foundations/` (brief, essay, vision, or weave).
- **Carrying Linengrow's application vision** → `linengrow/`.
- **Deciding our own design** → `active-designing/`.
- **Studying an external work** → `external-research/`.
- **Expanding intent into a runnable plan** → `expanding-prompts/`.
- **Tracking what is open or next** → `work-in-progress/`.
- **Recording what a session settled** → `session-logs/`.
- **Implementing** → the module the code belongs to.

If two folders seem right, choose the one whose README you would update first. If still unsure, write a one-line note in `work-in-progress/TASKS.md` open questions and place the file where a future reader will look first.

---

## Season placements and the log

The placements for any given season are recorded in `session-logs/` — what moved, what stayed, what was confirmed without churn. The durable test above outlives any snapshot list. When this season placed the seven distilled essays, the weave, the foundation briefs, and the civic visions in `foundations/`, and the Linengrow pieces in `linengrow/`, that record lives in the logs, not here, so this guide does not pretend to be a catalog that expires.

---

## The One Clock

Every dated artifact names itself `YYYYMMDD-HHMMSS_short-slug.md`. Later is always larger. Living documents (`README.md`, `ROADMAP.md`, `TASKS.md`, the discipline files) carry **Last updated** and evolve in place. Full law: `context/specs/20260627-102012_one-clock-naming-law.md`.

---

## Caretaking

- **Rename with history:** `git mv`, never silent rewrites.
- **Prune with care:** release what no longer serves; graduate finished work out of `work-in-progress/`.
- **Commit logs with work:** session logs ship in the same commit whenever possible.
- **Clean room:** study in `gratitude/` and `external-research/`; implement in our modules with our vocabulary.
- **Confirm before churn:** when a filing guide predates a folder that now exists, update the guide — do not move settled work to match an old plan.

---

*May each file rest with its own kind. May the guide stay true to the tree it describes. And may the next reader, agent or human, find exactly what they came for.*
