---
name: TAME Style — Operational Supplement
description: Checkable coding rules for Rye, Brix, and Rishi — root plus one supplement per language. Pairs with the voiced canon in external-research/996_TAME_STYLE.md.
type: reference
---

# TAME Style — Operational Supplement

**Language:** EN
**Last updated:** 2026-06-21 (`043312` — usize policy aligned with Tiger; tools in Rye)
**Style:** Radiant (see `RADIANT_STYLE.md`)
**Status:** Active — grow by supplement, earned when the language is ready

---

## Document Stack

Three layers, one discipline — filenames follow TigerBeetle's `docs/TIGER_STYLE.md` pattern (landmark guides at `context/TAME_STYLE.md`, beside `RADIANT_STYLE.md`):

| Layer | Path | Role |
|-------|------|------|
| **Source** | `gratitude/TIGER_STYLE.md` | TigerBeetle team's guide, kept whole and unaltered |
| **Voiced canon** | `external-research/996_TAME_STYLE.md` | Our radiant adaptation; Safety, Performance, DX, and the full why |
| **Operational supplement** | this document | Checkable root + Rye / Brix / Rishi rules for authors and agents |

Read **996** for philosophy and expert Tiger discipline. Read **this file** at the keyboard for what to assert, name, and bound. Organization prose lives in `active-designing/20260618-184912_growing-a-language.md`.

Cursor and Claude rules (`.cursor/rules/tame-style.mdc`, `.claude/rules/tame-style.md`) point here.

---

## What This Is

TAME names the order of values that governs every line we write: **safety first, performance second, the joy of the craft third.** That order is a priority — when they pull against each other, safety wins; when safety and performance are equal, joy earns the vote.

This guide makes those values concrete for code. It is organized as **one root** — rules that hold across the whole family — and **a supplement for each language**, added when that language has earned distinct idioms of its own. A supplement that does not exist yet is not overdue: it waits for the language to be real enough to need it.

---

## Root — Universal Across the Family

These disciplines hold for Rye, Brix, Rishi, and every module written in them. A language that has no supplement of its own still keeps the root. Where the root is silent, **996** and `gratitude/TIGER_STYLE.md` are authoritative.

### 1. State invariants before implementing

Write the assertions before you write the algorithm. An invariant written before the loop is an invariant the loop was built to preserve. An invariant written after the loop is a hope wearing a check's clothes.

A structural invariant lives in a comment block immediately before the type it governs:

```
// Invariant: pos <= buf.len; all bytes in buf[0..pos] are committed.
const Region = struct { ... };
```

A behavioral invariant lives immediately before the function that enforces it:

```
// Precondition: name.len == Sha3.digest_length * 2 (64 hex chars).
fn read_blob(...) ...
```

### 2. Bounds on everything

Every allocation, every collection, every pipeline names its maximum size. Name the budget at construction; check it at the edge; fail with a named error, not a silent corruption.

A bound is not a hedge. It is the honest answer to "how large can this grow?" stated up front, before the machine runs.

### 3. Say why

Every assertion earns a comment: `// invariant: ...`. Every named constant earns a comment if the name alone does not make the reason obvious. Every design choice that will surprise a reader earns a sentence that names the reason.

The next reader meets the reason, not only the rule.

### 4. Accrete, never break

A name once given is a promise. Add beside it; do not replace it silently. When a better shape is found, the old name keeps working while the new one grows. Rename only with a migration path; deprecate before removing.

A version once published does not change.

### 5. One value model

A value is: a string, an integer, a boolean, a list of values, a record of named values — or a composite of these. Values are composed (placed side by side); they are never tangled (woven together so that reading one requires holding the others).

A value crosses module boundaries without being serialized to text and reparsed on the other side. When that seam would open, close it.

---

## Rye Supplement

Rye carries the family. The safety Rye offers is the safety every module written in it inherits. These rules are specific to Rye code (`.rye` source files). Naming, performance habits, and assertion density defer to **996** unless this supplement states a Rye-specific seam.

### Typed and sized

Use explicitly sized integer types: `u8`, `u16`, `u32`, `u64`, `i8`, `i16`, `i32`, `i64`. Use `f32` or `f64` for floating-point. Never use `c_int`, `c_uint`, or `anyopaque` without a stated, commented reason.

**`usize` is BANNED in Rye. No exceptions.** Every occurrence in authored `.rye` is technical debt to be eliminated by the compiler fork (F1–F5). See [`active-designing/20260621-070712_the-compiler-fork.md`](../active-designing/20260621-070712_the-compiler-fork.md) and [`active-designing/20260621-051312_explicit-width-in-rye.md`](../active-designing/20260621-051312_explicit-width-in-rye.md). The gate `tools/width-check.rish` enforces zero tolerance.

| Width | Role in authored Rye |
|-------|----------------------|
| **`u32`** | All in-memory counts, indices, and lengths **bounded by a named constant** (garden capacity, grid dimension, stack depth, frame size). Default width for “how many in this region.” |
| **`u64`** | Wire-persistent sizes, timestamps, content offsets, and any quantity that must mean the same thing on every target. |
| **`usize`** | **BANNED.** Every existing occurrence is technical debt. The compiler fork (F1) rejects it; the std rewrite (F3) eliminates it from `rye/lib`. |

Name the bound when you pick `u32`:

```zig
const max_frame_bytes: u32 = 4096;
pos: u32, // invariant: pos <= max_frame_bytes
```

Width audit: `work-in-progress/992_usize_width_baseline.md`. Fork plan: `active-designing/20260621-070712_the-compiler-fork.md`.

**Existing Zig seam casts** (`const x: usize = @intCast(...)`) are **technical debt**, not an acceptable pattern:

```zig
// DEBT — eliminated when Rye's slice type carries u32 len (fork F3)
std.debug.assert(buf.len <= std.math.maxInt(u32));
const cap: u32 = @intCast(buf.len);
// ... arithmetic in u32 ...
const start: usize = @intCast(self.pos);
std.debug.assert(start <= buf.len);
return buf[start .. start + @as(usize, @intCast(n))];
```

### Naming (Tiger Style)

**`snake_case`** for functions, variables, and file names — per `gratitude/TIGER_STYLE.md` and `external-research/996_TAME_STYLE.md`. The underscore is the closest thing we have to a space; descriptive names read aloud well.

- Name functions with a verb: `compute_diff`, `serialize_weave`, `load_weave`, `read_brix`.
- Name constants in `snake_case` with units and qualifiers last when helpful: `max_depth`, `digest_hex_len`.
- Early seeds may still carry `camelCase` from before this rule landed; migrate names opportunistically when you touch a file — do not rename silently across the tree in one sweep.

For everything else, follow the Zig style guide as filtered through **996** (line length, braces, `zig fmt`, and the rest).

### Assertions as first-class design

`std.debug.assert(cond)` is not a debugging tool; it is the design written down where the machine can check it.

- **Preconditions** — at the top of a function, before any work: the conditions the caller must have arranged.
- **Invariants** — after every mutation of a data structure: the conditions the structure must always keep.
- **Postconditions** — after a computation: the conditions the result must honor.

Prefer a narrow assertion over a wide one. `assert(len <= max)` is more informative than `assert(ok)`.

In tests, use `std.testing.expect` and `std.testing.expectEqual` rather than `std.debug.assert`.

### Named errors

Error types are named descriptively: `error.OutOfBounds`, `error.InvalidFormat`, `error.NotFound`. Names are chosen to name the *fault*, not the *operation* that discovered it.

Propagate errors with `try`. Catch only at the boundary where the program can act: a command entry point, a test body. Never swallow an error silently with a discard pattern.

### Short functions

One function, one idea. If a function needs a section comment divider (`// ---`), it is doing more than one thing and should be split.

The name says what the function *does*; the comment says *why it exists* and *what invariants it keeps*.

Parameters: declare the tightest type you can. Prefer slices over pointers when ownership is not transferred.

### Named constants

No magic numbers inline. Name constants with their type:

```zig
const max_depth: u32 = 1024; // chain length above which we stop and warn
const digest_hex_len: u32 = 64; // SHA3-256 digest rendered as hex
```

The comment names why the bound exists, not just what it is.

### Structs carry their invariant

The comment block immediately before a struct declaration states what must hold at all times:

```zig
// Invariant: pos <= buf.len.
// Invariant: every byte in buf[0..pos] was written by this Region's put call.
const Region = struct {
    buf: []u8,
    pos: u32,
};
```

A mutation function on the struct asserts the invariant holds on entry and on exit.

### Garden memory — never `ArenaAllocator` directly

In **authored** Rye programs (`.rye` seeds, tools, witness tests, Skate, Rishi source), reach for the process season allocator through **`init.garden`**, not through `std.heap.ArenaAllocator`:

```zig
const garden = init.garden.allocator();
```

Name the local `garden` (or `allocator` when the role is generic). Do not construct `ArenaAllocator` in our code, do not name the type in our APIs, and do not add `std.heap.GardenAllocator` as a rename of the inherited type.

**Why:** `ArenaAllocator` is Zig's inherited name — we keep it in `std` untouched (`context/specs/inherited-names.md`). Our warm vocabulary names what we own: `Init.garden` today; `rye.garden` or `tally/heap-garden.rye` when the owned wrapper graduates to Tally. Inherited `std` internals may still use `ArenaAllocator`; that is out of scope for authored programs.

**Freestanding / no `Init`:** use `std.heap.FixedBufferAllocator`, Tally `Region`, or an explicit child allocator passed in — still not `ArenaAllocator` in authored code unless you are strengthening inherited `std` itself.

---

## Brix Supplement

Brix is the composing language: it describes what a system is made of. A `.brix` file is a declaration, not a program. These rules govern `.brix` descriptors.

### Declarative only

A `.brix` file describes what exists. It contains no commands, no conditions, no loops, no expressions. The format is plain key-value: one field per line, a single space separating key from value, `#` for comments.

### Each brick is individually simple

A `file` entry names one source file. A brick makes no claim about other bricks. Simplicity here is structural: a brick that depends on knowing about its neighbors is not yet a brick.

### Comments name what the brick is

A comment above a `file` entry says what that source file *is* — its role in the system — rather than what it does or how it works:

```
# Rishi — the shell that speaks commands
file rishi/src/main.rye
```

### The descriptor is a value

Any tool that reads a `.brix` file should be able to do so with `splitLines` and the first-space split. No grammar, no parser, no special characters. A descriptor readable by hand is readable by any tool.

---

## Rishi Supplement

Rishi is the shell: typed pipelines, process results as structured values, assertions as gates. These rules govern `.rish` scripts.

### Run returns a structured value

`run` produces a structured result: `{ status, out, err }`. Never treat `out` as reliable until `status` has been checked. A pipeline that discards `status` silently is a pipeline that has decided faults do not matter.

```
let result = run "zig" ["build"]
assert result.status == 0  // invariant: build succeeded before we run tests
```

### Assertions as gates

An `assert` in a Rishi pipeline stops the pipeline loudly when the condition fails. Place assertions at stage boundaries: after a `run`, before a write, before a conditional branch. The assert is the cheapest correctness check available; use it freely.

### Effects are visible and ordered

A pipeline stage that has side effects — writing a file, sending a message, modifying state — comes last in its group and is named or commented to say so. A reader moving left to right through a pipeline should encounter effects after the computations that justify them.

### Terseness that never costs safety

Short pipelines are good. A pipeline longer than roughly ten stages earns a name and a comment block explaining its purpose. A pipeline whose stages are individually unclear earns intermediate `let` bindings with named values.

### Bindings are named

`let` binds a named value. Name bindings for what they *are*, not for how they were computed: `let commit_hash = ...` rather than `let result_of_sha3_over_blob = ...`.

---

*May the root hold firm across every language we grow. May each supplement stay small — exactly as small as the language has earned, and no larger. May the rules serve the work, and the work serve what is true.*
