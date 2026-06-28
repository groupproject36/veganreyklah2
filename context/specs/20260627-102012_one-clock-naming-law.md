# Starting Rye Over: One Clock, One Order, One Clean Re-Fork

**Stamp:** 20260627.102012
**Status:** Adopted
**Voice:** Reya 2
**Style:** Radiant (see `context/RADIANT_STYLE.md`)
**By:** Reya 2, with **Kaeden Reyklah** as coauthor

---

## One Clock Names Everything

Rye already keeps time by a single chronological stamp. This memo carries that one clock outward — from the version numbers, where it already lives, into the filenames themselves. When the same stamp that orders a release also names the file, the filesystem sorts by time on its own, and the order on disk becomes the order of the work. One clock, one order, all the way down.

The decision is simple to state and steady to follow: a single chronological stamp governs the naming of every dated artifact, so the names sort honestly and the history reads as it happened.

---

## Two Tiers Share Each Folder

Every folder holds two kinds of file, and each kind keeps its own discipline.

**Living documents hold steady and carry no stamp.** These are the files a reader returns to — `README.md` for the foundation and its index, and `STRATEGY.md`, `ROADMAP.md`, and `LEXICON.md` where they fit. They grow and revise in place, always current, always at the same path. Their name is their address, and the address stays put.

**Dated artifacts form the append-only stream and take the stamp.** These are the memos, the session logs, the records of a decision made at a moment. Each one carries the stamp in its filename form — `YYYYMMDD-HHMMSS_short-slug.md` — ascending and unique. Once written, a dated artifact rests; the stream only grows forward.

The two tiers meet in one place. Each folder's `README.md` carries a **reverse-chronological index** — newest first, a row per entry with stamp, title, and one line of meaning. So the filesystem stays purely chronological, ascending and honest, while the newest-first view lives exactly where it can hold summaries and greet a reader. The clock orders the files; the index welcomes the reader.

---

## Keep the History, Reorganize on a Branch

One path is chosen and settled: **keep history, reorganize with `git mv` on a branch named `reorg/one-clock`, and never force-push.** Every rename preserves provenance and blame across the move. No submodule needs re-registration. And the work honors aparigraha at the git level — non-grasping applied even to history, which we carry forward rather than rewrite.

The clean record of the old layout comes from the frozen archive, not from a rewrite. The repository was sealed at a known-good tip and pushed off-sandbox, so the past is preserved whole in its own place. The branch, then, is free to reshape the present without disturbing the record of what came before. When the branch is ready, it merges into `main` by an ordinary fast-forward — no rewrite, no force.

---

## The Rollout: Smallest Complete Thing First

The order of work follows the smallest-complete-thing discipline, one whole piece at a time.

**The session logs are the easy win.** Each already holds its stamp beneath a countdown prefix, so dropping that prefix turns the sort honest in a single pass. This is the natural first chunk: mechanical, low-judgment, and complete on its own.

**The design folders are the judgment-heavy work, taken one folder fully at a time** — `active-designing/`, `external-research/`, `expanding-prompts/`, `work-in-progress/`, `rye-learning-process/`, `strengthening-compiler/`. Within each folder, read the header stamp to name the file; derive a missing stamp from the file's first-commit date; anchor the foundation to `README.md` and any charter to `STRATEGY.md`; and turn genuine duplicates into one-line redirect stubs rather than second copies. One folder complete before the next begins.

**The Zig 0.16.0 clean re-fork waits beyond all of this.** It is the funded frontier, opened once the new order has settled — proven ground first, the frontier funded later. The vendored standard library slims to an overlay in that later pass, after the naming and the folders stand firm.

---

## Why This Holds

This naming law is one decision wearing several faces. The single clock that already versions Rye now also names its files, so order on disk and order in time become the same thing. Living documents stay reachable at steady addresses while dated artifacts stream forward untouched. History carries through every rename, and the frozen archive keeps the old shape safe. Each piece lands complete before the next opens. The whole arrangement is aparigraha made structural — a place for everything, nothing grasped, the order kept true by the clock rather than by effort.

---

*May the clock keep our order true. May each file earn its place and rest where it belongs. May the work move forward one complete piece at a time, and leave the project a little clearer than we found it.*

---

*Written together by Kaeden and Reya 2.*
