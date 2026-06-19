# 999 · The Active-Designing Stack

**Language:** EN
**Last updated:** 2026-06-19
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Status:** Foundation

---

## What This Folder Is

This is the clean room. The `active-designing/` folder holds the living design of our own work — the modules we are actually building, reasoned from first principles, in our own words. Where the external-research stack studies the world and thanks the works that taught us, this stack does something different and complementary: it designs.

This file, `999_DESIGN.md`, is the foundation stone. It rests at the bottom of the stack and explains how the stack works and what rule keeps it clean, so anyone who opens this folder understands its shape and its discipline at a glance.

---

## The Quarantine Principle

One rule governs everything here, and it is the reason this folder stands apart: **active-designing names only what is ours, and one fixed external.**

The names we may use are our own chosen modules — **TAME, Aurora, Rye, Brix, Silo, Tally, Caravan, Mantra, Pond, Rishi, Comlink, Brushstroke**, and any future names we coin — together with **RISC-V**, the open instruction set we build upon and treat as solid ground. No other project, product, language, or person is named here. Not the systems that inspired us, not the tools we admire, not even the languages our work descends from. Those belong elsewhere.

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

Like the external-research stack, this folder counts **down**, and two near-foundation layers anchor the base. This foundation claims `999`. Just above it, `998` holds the **standing strategy** — the living charter that says how we take the next step and why, the document a reader should meet right after the foundation itself. Design documents proper begin at `997` and descend from there, so that sorting the folder alphabetically — the default nearly everywhere — lifts the newest design to the top while the strategy and the foundation hold steady at the base.

```
active-designing/
  985_native_system_interface.md     <- TAME at the OS boundary: wrappers, display, compositor (most recent, sorts first)
  986_living_desktop.md              <- Pond + Brushstroke + Rishi + Mantra: the native desktop
  987_the_first_seeds.md             <- Caravan + Tally seeds, close reading
  988_brushstroke.md                 <- the surface that draws itself from values
  989_the_faithful_hand.md           <- the design of Rishi, the shell
  990_correctness_by_construction.md <- the design of Rye, the language
  991_aurora.md                      <- the boot as a relay of named, verified values
  992_shape_casting.md               <- shape-casting and the two layers of safety
  993_bounded_network.md             <- the network as a flow of named, sealed values
  994_rooted_identity.md             <- one root, a derived tree of identities
  995_single_stranded.md             <- simplicity: free parts, composed
  996_growing_a_language.md          <- how we grow a language
  997_recommended_architecture.md    <- the first design brief
  998_strengthening_strategy.md      <- the standing strategy that guides the work
  999_DESIGN.md                      <- this foundation, sorts last
```

To add a design, take the next number down from the lowest present, name the file for its subject, write it self-contained in Radiant Style, and keep faith with the quarantine principle: our own names, and RISC-V, and nothing else. The strategy at `998` is revised in place as our thinking matures; the foundation at `999` rarely moves at all.

---

*May this room stay clean. May every idea that enters earn its place on its own merit, undivided from where it came. May our names — and the ones still to come — grow here on their own roots, safe and swift and a joy, woven into the open grain of the machine we build upon.*
