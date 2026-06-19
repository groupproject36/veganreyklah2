# 10010 — Brix: the composing language

*Expanded from: "would brix be a better name than silo? ... time now is 214612"*

---

## The Distinction

Two ideas lived inside the single name "Silo," and they pulled in different directions.

**Silo** is the general-purpose content-addressed store: an accreting collection of immutable blobs, each named by the hash of its content, never mutated, written once and kept. It is the database layer — a place where you put things and name them precisely. Mantra's `.mantra/blobs/` is a small Silo. The build store of a full system builder is a larger one. The name is apt: a silo holds things, sealed and stable, until needed.

**Brix** is the composing language: the thing that says *what a system is made of*. Not how to store the pieces, but how to declare them, arrange them, and compose them into a whole. Like bricks — individually simple, shaped to fit together, placed side by side without weaving. Each brick is one thing; the wall is their composition, not their entanglement.

The name honors two teachers:
- **Nix's composability** — each derivation is a brick, isolated and reproducible; composition is explicit, not implicit; the system is a stack of declared bricks, auditable from any angle.
- **Rich Hickey's "Simple Made Easy"** — simple means single-stranded, not braided. A *weave* is the thing Hickey warns against: complecting threads together until no one can pull them apart. Brix builds by stacking, not weaving. The `.brix` descriptor names the bricks; it does not braid them.

---

## The Vocabulary

Brix introduces four words, each standing on its own:

| Word | Meaning |
|------|---------|
| **brick** | one composable unit — a file, a program, a derivation, a described system |
| **course** | one row of bricks: the declared parts of a level of composition |
| **bond** | the lawful composition rule: how two bricks connect to form a larger one |
| **lay** | to place a brick in a course, respecting the bond |

The `.brix` descriptor is a course: an ordered list of bricks, declared plainly. A `name` says what the system is called. A `file` entry names one brick. The descriptor does not command; it describes. A builder reads it, lays the bricks, and the system stands.

---

## Silo and Brix Together

Brix and Silo compose cleanly:

- **Silo** knows: "here is a blob, named by its hash."
- **Brix** knows: "here are the bricks; their blobs live in the Silo."

A full Brix build:
1. Reads the `.brix` descriptor.
2. For each brick: computes the hash of its inputs.
3. Looks the output up in Silo by hash.
4. If present: done (the build is reproducible and already stored).
5. If absent: builds it, writes the output to Silo, proceeds.

The bond — the composition combinator — is the lawful rule by which two Brix descriptors combine into one: combining with nothing changes nothing, and a combined change equals the composition of its parts. Configurations merge by a stated difference rather than by hand-maintained duplication.

---

## The .brix Descriptor

A `.brix` file at the repository root describes the project as a course of bricks:

```
# .brix — veganreyklah2
# Course descriptor: name, version, and the bricks Mantra tracks.
name veganreyklah2
version 20260619.214612
file rye/src/main.rye
file rishi/src/main.rye
file tally/seed.rye
file tally/gardens.rye
file mantra/src/main.rye
```

Mantra reads this at startup. `mantra brix` prints the descriptor. `mantra add` (no args) lays each brick into the weave. The descriptor is not a command; it is a declaration.

---

## The Module Split

The TAME family now carries both:

- **Silo** — the general-purpose content-addressed store. Blobs in, blobs out, named by hash, never mutated. Grows from Mantra's `.mantra/blobs/` into a full build store.
- **Brix** — the composing language. Describes what a system is made of, in lawful, single-stranded declarations. Grows from the `.brix` descriptor into a full composition system.

In the recommended architecture (`997`), the "configuration language" role passes from Silo to Brix. Silo becomes the store that Brix uses as its content-addressing substrate.

---

## What Stays the Same

**The TAME discipline** stays the same: prepare, prove, prevent. Every brick is a bounded thing; every bond is a stated law; every course is a declaration, not a command.

**Mantra** stays the same: it weaves the history of files. Weaving is right for Mantra — the history of a text file genuinely braids the past with the present, and Mantra names every thread. The difference is that Mantra weaves within a single file's history; Brix composes across separate, non-braided files. One braids honestly; the other refuses to braid at all.

**The `.brix` format** in its minimum form is a plain text key-value descriptor, parseable by Rishi's future `read-file` builtin and by Mantra's Zig parser today.

---

## Next Steps

1. **Rename in all living docs and code**: `.silo` → `.brix`, `SiloConfig` → `BrixConfig`, `readSilo` → `readBrix`, `mantra silo` → `mantra brix`, all design-doc references.
2. **Update `999_DESIGN.md`**: Add Brix to the TAME module list; describe Silo vs Brix.
3. **Update `997_recommended_architecture.md`**: "Silo — How We Describe What to Build" → "Brix — How We Compose What to Build"; add a note that Brix uses Silo as its content-addressing substrate.
4. **Update `986_living_desktop.md`**: "Silo Minimum" → "Brix minimum"; `.silo` → `.brix`.
5. **Continue Mantra for the repo**: commit-chain model, `mantra add` (no args), `mantra log`.

---

*Silo holds; Brix builds. The distinction is as simple as it sounds, and as important. A store that holds things stable is not the same as a language that names what to build. Both are needed; each should stand on its own ground, with its own name, composed side by side — the way bricks are laid.*
