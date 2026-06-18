# 999 · The Active-Designing Stack

**Language:** EN
**Last updated:** 2026-06-17
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Status:** Foundation

---

## What This Folder Is

This is the clean room. The `active-designing/` folder holds the living design of our own work — the modules we are actually building, reasoned from first principles, in our own words. Where the external-research stack studies the world and thanks the works that taught us, this stack does something different and complementary: it designs.

This file, `999_DESIGN.md`, is the foundation stone. It rests at the bottom of the stack and explains how the stack works and what rule keeps it clean, so anyone who opens this folder understands its shape and its discipline at a glance.

---

## The Quarantine Principle

One rule governs everything here, and it is the reason this folder stands apart: **active-designing names only what is ours, and one fixed external.**

The names we may use are our own chosen modules — **TAME, Aurora, Rye, Silo, Tally, Caravan**, and any future names we coin — together with **RISC-V**, the open instruction set we build upon and treat as solid ground. No other project, product, language, or person is named here. Not the systems that inspired us, not the tools we admire, not even the languages our work descends from. Those belong elsewhere.

This is quarantine as a kindness to clarity. Outside ideas enter only as **concepts**, stripped of their origin and weighed on their own merits — a region of memory, a content-addressed store, a supervision tree, a lawful combinator. By refusing the borrowed name, we force ourselves to understand the idea well enough to restate it plainly, and we keep our design space free of any genealogy that might quietly smuggle in assumptions we never chose. What grows here grows on its own roots.

The discipline is simple to check: read any line aloud, and if it names something outside our own work or RISC-V, it belongs in the external-research stack instead.

---

## Two Folders, Two Purposes

The project keeps two design-adjacent stacks, and the boundary between them is deliberate — they differ in temper as much as in content.

The **external-research** stack is open to the world. It studies other systems, names them precisely, draws inspiration, and cites its sources — with the original works kept whole in the `gratitude/` folder. It is allowed to be experimental, informal, and overgrown at times, the way a field of inquiry should be: many threads, freely followed, some left to tangle. External research is where we learn, compare, and honor.

The **active-designing** stack is closed and self-contained. It carries only our own design, isolated from any non-TAME-style project or concept, so the work can mature undivided. Its temper is the opposite of the field's wildness: clear, thought-through, confirmed, directional, and intentional, accruing slowly and only when a change earns its place by serving — in our designs themselves — safety above performance, and performance above the joy of the craft. Active designing is where we decide and build.

Ideas flow one way across the boundary: a concept learned in external research, once understood, may cross into active-designing only after it has shed every borrowed name and been restated as our own. The citation and the gratitude stay behind; the distilled idea comes forward clean, and is admitted only once we are sure it makes the design safer, then faster, then kinder to work in.

---

## The Counting-Down Convention

Like the external-research stack, this folder counts **down**. This foundation claims `999`. The next design document takes `998`, the one after `997`, and so the sequence descends. Sort the folder alphabetically — the default nearly everywhere — and the smallest number rises to the top, so the newest design greets the reader first while the foundation holds at the base.

```
active-designing/
  997_<next-design>.md     <- most recent, sorts first
  998_recommended_architecture.md
  999_DESIGN.md            <- this foundation, sorts last
```

To add a design, take the next number down from the lowest present, name the file for its subject, write it self-contained in Radiant Style, and keep faith with the quarantine principle: our own names, and RISC-V, and nothing else.

---

*May this room stay clean. May every idea that enters earn its place on its own merit, undivided from where it came. May our six names — and the ones still to come — grow here on their own roots, safe and swift and a joy, woven into the open grain of the machine we build upon.*
