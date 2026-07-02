# The Active-Designing Stack

**Language:** EN
**Last updated:** 2026-07-02 (design sitting companion)
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Status:** Foundation

---

## What This Folder Is

This is the clean room. The `active-designing/` folder holds the living design of our own work — the modules we are actually building, reasoned from first principles, in our own words. Where the external-research stack studies the world and thanks the works that taught us, this stack does something different and complementary: it designs.

This file, `README.md`, is the foundation stone. It rests at the bottom of the stack and explains how the stack works and what rule keeps it clean, so anyone who opens this folder understands its shape and its discipline at a glance.

---

## The silo principle

One rule governs everything here, and it is the reason this folder stands apart: **active-designing names only what is ours, and one fixed external.**

The names we may use are our own chosen modules — **TAME, Aurora, Rye, Brix, Tablecloth, Tally, Caravan, Weave, Mantra, Pond, Rishi, Comlink, Brushstroke, Dexter, Kumara, Bookie**, and any future names we coin — together with **RISC-V**, the open instruction set we build upon and treat as solid ground. No other project, product, language, or person is named here. Not the systems that inspired us, not the tools we admire, not even the languages our work descends from. Those belong elsewhere.

This is silo as a kindness to clarity. Outside ideas enter only as **concepts**, stripped of their origin and weighed on their own merits — a region of memory, a content-addressed store, a supervision tree, a lawful combinator. By refusing the borrowed name, we force ourselves to understand the idea well enough to restate it plainly, and we keep our design space free of any genealogy that might quietly smuggle in assumptions we never chose. What grows here grows on its own roots.

The discipline is simple to check: read any line aloud, and if it names something outside our own work or RISC-V, it belongs in the external-research stack instead.

---

## Two Folders, Two Purposes

The project keeps two design-adjacent stacks, and the boundary between them is deliberate — they differ in temper as much as in content.

The **external-research** stack is open to the world. It studies other systems, names them precisely, draws inspiration, and cites its sources — with the original works kept whole in the `gratitude/` folder. It is allowed to be experimental, informal, and overgrown at times, the way a field of inquiry should be: many threads, freely followed, some left to tangle. External research is where we learn, compare, and honor.

The **active-designing** stack is closed and self-contained. It carries only our own design, isolated from any non-TAME-style project or concept, so the work can mature undivided. Its temper is the opposite of the field's wildness: clear, thought-through, confirmed, directional, and intentional, accruing slowly and only when a change earns its place by serving — in our designs themselves — safety above performance, and performance above the joy of the craft. Active designing is where we decide and build.

Ideas flow one way across the boundary: a concept learned in external research, once understood, may cross into active-designing only after it has shed every borrowed name and been restated as our own. The citation and the gratitude stay behind; the distilled idea comes forward clean, and is admitted only once we are sure it makes the design safer, then faster, then kinder to work in.

---

## One clock, one order

Dated briefs carry `YYYYMMDD-HHMMSS_short-slug.md` filenames; this README is the living foundation and reverse-chron index. Full naming law: [`../context/specs/20260627-102012_one-clock-naming-law.md`](../context/specs/20260627-102012_one-clock-naming-law.md).

## Design briefs (newest first)

| Stamp | Brief | Meaning |
|-------|-------|---------|
| `20260702-031312` | [Modules, aspects, and mailable money](20260702-031312_modules-aspects-and-mailable-money.md) | Module/aspect vocabulary and graduation rule; Weave's trigger; MALA M0–M4; Mycelium and road-keeper; Amber contract; Brix packaging through Pond; opening lines; manual's four rooms |
| `20260630-030312` | [SLC-2a — the drawn terminal](20260630-030312_slc-2a-the-drawn-terminal.md) | Three-ring scope: value-driven viewer, redraw on change, live session mirror; Rings 1–3 witness landed |
| `20260630-014012` | [Lotus — the DAW](20260630-014012_lotus-the-daw.md) | Our studio: REAPER workflow shape, AP Mastering surface craft, Genesis hot-loop discipline; horizon after SLC-2a |
| `20260630-001812` | [The stack and the surface](20260630-001812_the-stack-and-the-surface.md) | Acyclic module order; Weave as substrate; Brushstroke draws values; Dexter/Kumara/Bookie named; SLC-2a the live rung |
| `20260629-004912` | [SLC-1 Step 2 · Version](20260629-004912_slc-1-step-2-version.md) | Hammock scope: session ring + transcript; `:history` and `:version`; Rishi drives Mantra by composition |
| `20260628-120912` | [Brix — the composer and the system around it](20260628-120912_brix-the-composer.md) | sixos mapping: Brix composes; bond overrides; Tablecloth holds; Mantra weaves; Comlink seals; Caravan supervises |
| `20260628-071012` | [SLC-1 · Rishi-and-Mantra hosted shell](20260628-071012_slc-1-rishi-mantra-shell.md) | Hammock scope: four verbs (type, run, version, recall); history in `.mantra/`; terminal-complete first ring |
| `20260628-043542` | [Thin frontend — direction adopted](20260628-043542_thin-frontend-slc-direction.md) | Rye as thin frontend; SLC order; strengthening arc complete |
| `20260622-232912` | [967 · Caravan — Improving Upon the State of the Art](20260622-232912_caravan-kernel-improvements.md) | A siloed design brief for how Caravan's microkernel improves upon what formal verification and safe-language kernels achieved separately. Th |
| `20260621-070712` | [968 · The Compiler Fork — Rye Becomes Its Own Language](20260621-070712_the-compiler-fork.md) | A siloed design brief for the moment Rye stops being a derivative and starts compiling its own types. The fork replaces the inherited slice  |
| `20260621-063912` | [969 · Bron — Token-Efficient Data Notation for the Rye OS Family](20260621-063912_bron-notation.md) | A siloed design brief for Bron (`.bron`), the data notation that carries values between modules, between forges, and between agents — human- |
| `20260621-051312` | [970 · Explicit Width in Rye — The Language Model](20260621-051312_explicit-width-in-rye.md) | A siloed design brief for Rye's width model after the language fork: no `usize` in Rye-authored types; `u32` for bounded in-memory lengths a |
| `20260620-042812` | [971 · Tally and Who — Gardens for Every Role at the Seam](20260620-042812_tally-and-who.md) | `972` named four **whos** — executor, sealer, opener, router — and one **what**, the datagram. Tally is none of those. Tally is **where work |
| `20260620-042612` | [972 · Who — Executor, Sealer, Opener, and Router](20260620-042612_who-executor-sealer-opener.md) | In conversation we said a hart names **who executes** and a datagram names **what moves** — and a fair question followed: what do we mean by |
| `20260620-041612` | [973 · Sealed Datagrams — A Value With a Wire Shape](20260620-041612_sealed-datagrams.md) | Comlink does not begin with sockets. It begins with a **datagram**: a bounded byte layout that carries who sealed a message, what name the c |
| `20260620-041512` | [974 · Harts — Parallel Execution on One Machine](20260620-041512_harts-parallel-on-one-machine.md) | Before Comlink carried a sealed datagram between two machines, it carried one between two harts — two hardware threads on the same RISC-V si |
| `20260620-041412` | [975 · Virtio — The Parity Device at the Emulated Wire](20260620-041412_virtio-the-device-wire.md) | Comlink's wire grew in three rungs: shared memory between two harts, localhost datagrams between two processes, and next — a true device bet |
| `20260620-021212` | [977 · Flow of Values — How the System Moves Without Braiding](20260620-021212_flow-of-values.md) | A siloed foundation brief for the compositional law beneath the whole family: values transformed, moved, routed, and remembered — kept apart |
| `20260620-020712` | [978 · Scribble, Lantern, and Lattice — Horizon Modules on One Value Grammar](20260620-020712_scribble-lantern-and-lattice.md) | A siloed design brief for the modules that extend our stack toward human-readable docs, GPU-aware editing, local inference, and honest tenso |
| `20260620-012112` | [979 · Comlink Remoting — Value-Based State Sync Over the Bounded Network](20260620-012112_comlink-remoting.md) | A siloed design brief for remote access in the TAME Rye OS: Comlink carries terminal state as values over UDP, authenticated by owner keys,  |
| `20260620-012012` | [980 · The Editor — Select, Then Act, Configured in Brix and Rishi](20260620-012012_the-editor.md) | A siloed design brief for the TAME editor: modal text editing that follows the select-then-act model, configured through Brix (settings) and |
| `20260620-011412` | [981 · The Desktop — Brushstroke, Skate, and Rishi Composed for the Screen](20260620-011412_the-desktop.md) | A siloed design brief for the TAME desktop: Brushstroke as the compositor, Skate as the terminal, Rishi as the keybinding language, and ever |
| `20260620-005112` | [982 · The Forge — Mantra Served, Brushstroke Drawn, Group Projects Welcome](20260620-005112_the-forge.md) | A siloed design brief for the forge we mean to build: a place where Mantra repositories are served, Brushstroke draws the surface, Comlink r |
| `20260619-225712` | [983 · The Whole System — Every Module Composed on Its Own Ground](20260619-225712_the-whole-system.md) | A siloed design brief that names the complete system we are building: language, kernel, supervision, composition, memory, store, boot, shell |
| `20260619-223712` | [Caravan as a Microkernel — Siloed Design Brief](20260619-223712_caravan-microkernel.md) | Caravan is the supervision and isolation layer of the family. This brief silos the microkernel decision — reached through external research  |
| `20260619-160312` | [985 · The Native System Interface — TAME at the OS Boundary](yonder/20260619-160312_native-system-interface.md) | Before Brushstroke can draw, before Rishi can open a file, before Pond can bound a process, our code must speak the native system interface  |
| `20260619-154912` | [986 · The Living Desktop — Pond, Brushstroke, Rishi, and Mantra Composed for Our Own Machine](yonder/20260619-154912_living-desktop.md) | A design brief for the next composed whole: a native desktop application, drawn by Brushstroke, running a Rishi shell whose Mantra commands  |
| `20260619-084412` | [The First Seeds — Caravan, Tally, and Reading Before the Wire Widens](20260619-084412_the-first-seeds.md) | Counsel received after Horizon 0 closed: the gate runs in Rishi, a sealed datagram crosses between two harts, and design still runs a little |
| `20260619-072600` | [Brushstroke — a Surface Drawn from Values](20260619-072600_brushstroke.md) | A clean-room distillation of the drawn-interface study. **Brushstroke** is the surface of the family: the place where Rye's values meet a pe |
| `20260619-051312` | [The Faithful Hand — the Design of Rishi](20260619-051312_the-faithful-hand.md) | Rishi is the shell of the family: the hand a person works with, and the seer who hears them and speaks faithfully to the machine. This brief |
| `20260619-051212` | [Correctness by Construction — the Design of Rye](20260619-051212_correctness-by-construction.md) | Rye is the language the whole family is written in, so this brief designs what Rye is meant to be: what it grows toward. The way we grew it  |
| `20260618-225712` | [Aurora — How a Machine Wakes into a Living System](20260618-225712_aurora.md) | Aurora is the dawn a machine wakes into: the passage from a cold processor to a living system, on open hardware. We design it as a relay — c |
| `20260618-224812` | [Shape-Casting, and the Two Layers of Safety](20260618-224812_shape-casting.md) | Before we trust raw bytes, we prove their shape: a shape-cast checks that a run of bytes truly holds a declared Rye type, validates it in pl |
| `20260618-224712` | [The Bounded Network — A Flow of Named, Sealed Values](20260618-224712_bounded-network.md) | A network should carry meanings, rather than guard pipes. Each message is a typed value, named by its own content, sealed to the one it is f |
| `20260618-224612` | [Rooted Identity — One Root, a Derived Tree](yonder/20260618-224612_rooted-identity.md) | Horizon — unified identity kin; in `yonder/` |
| `20260618-184912` | [996 · How We Grow a Language — Rishi on Rye, and One Style for the Family](20260618-184912_growing-a-language.md) | We have grown one language already, Rye, and the way we did it is a method we can reuse. This brief draws that method out plainly, applies i |
| `20260618-184912` | [997 · The Recommended Path for the Core Names](20260618-184912_recommended-architecture.md) | A clean-room architecture brief for our core modules — TAME, Rye, Brix, Tablecloth, Tally, Caravan, and Aurora — reasoning the recommended d |
| `20260618-182412` | [995 · Single-Stranded — The Enclosure and the Family, Read for What Stands Free](20260618-182412_single-stranded.md) | We hold a distinction worth keeping close: the **simple** and the **easy** are different things. This brief takes the architecture we have b |
| `20260618-085812` | [998 · A Strategy for Strengthening Rye, and the Next Step to Take](yonder/20260618-085812_strengthening-strategy.md) | The standing strategy for our strengthening work. Gates realized; effort dormant in `yonder/`. |
## Redirect stubs

When a design brief **supersedes** research or an executed prompt, the old file in another stack becomes a stub (see `../external-research/README.md`). In **this** stack, revise briefs in place when the design matures (see [`yonder/20260618-085812_strengthening-strategy.md`](yonder/20260618-085812_strengthening-strategy.md)) rather than leaving duplicate architecture docs.

**Current width law:** [`20260621-051312_explicit-width-in-rye.md`](20260621-051312_explicit-width-in-rye.md) — literal `usize` ban in Rye types. Interim Zig-ground seam audit: research `968` until fork F3.

**Retired patterns in new design prose:** Bash gates, `ArenaAllocator` in authored modules (use `init.garden`), `usize` in APIs we publish, vendor Zig parity as permanent contract.

---

*May this room stay clean. May every idea that enters earn its place on its own merit, undivided from where it came. May our names — and the ones still to come — grow here on their own roots, safe and swift and a joy, woven into the open grain of the machine we build upon.*
