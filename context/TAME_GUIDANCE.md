---
name: TAME Guidance — Operational Supplement
description: Checkable coding rules for Rye, Brix, and Rishi — root plus one supplement per language. Pairs with the voiced canon in external-research/TAME_GUIDANCE.md.
type: reference
---

# TAME Guidance — Operational Supplement

**Language:** EN
**Last updated:** 2026-06-29 (TH-7 freestanding width; width-check in parity; POSIX seam note)
**Style:** Radiant (see `RADIANT_STYLE.md`)
**Status:** Active — grow by supplement, earned when the language is ready

---

## Document Stack

Three layers, one discipline — filenames follow TigerBeetle's `docs/TIGER_STYLE.md` pattern (landmark guides at `context/TAME_GUIDANCE.md`, beside `RADIANT_STYLE.md`):

| Layer | Path | Role |
|-------|------|------|
| **Source** | `gratitude/TIGER_STYLE.md` | TigerBeetle team's guide, kept whole and unaltered |
| **Voiced canon** | `external-research/TAME_GUIDANCE.md` | Our radiant adaptation; Safety, Performance, DX, and the full why |
| **Operational supplement** | this document | Checkable root + Rye / Brix / Rishi rules for authors and agents |

Read the voiced canon (`external-research/TAME_GUIDANCE.md`) for philosophy and expert Tiger discipline. Read **this file** at the keyboard for what to assert, name, and bound. Organization prose lives in `active-designing/20260618-184912_growing-a-language.md`.

Cursor and Claude rules (`.cursor/rules/tame-guidance.mdc`, `.claude/rules/tame-guidance.md`) point here.

---

## What This Is

TAME names the order of values that governs every line we write: **safety first, performance second, the joy of the craft third.** That order is a priority — when they pull against each other, safety wins; when safety and performance are equal, joy earns the vote.

This guide makes those values concrete for code. It is organized as **one root** — rules that hold across the whole family — and **a supplement for each language**, added when that language has earned distinct idioms of its own. A supplement that does not exist yet is not overdue: it waits for the language to be real enough to need it.

The rules here that a machine can check are gathered near the end, in **What We Check, and When** — each one matched to the tool that catches it today, or named as a horizon when it waits for a Zig parser. The checkable rules and the idioms behind them are drawn faithfully from TigerBeetle's own enforcement, `src/tidy.zig`, kept in our gratitude for the team that wrote it.

---

## Root — Universal Across the Family

These disciplines hold for Rye, Brix, Rishi, and every module written in them. A language that has no supplement of its own still keeps the root. Where the root is silent, **996** and `gratitude/TIGER_STYLE.md` are authoritative.

### 1. State invariants before implementing

Write the assertions before you write the algorithm. An invariant written before the loop is an invariant the loop was built to preserve. An invariant written after the loop is a hope wearing a check's clothes.

A structural invariant lives in a comment block immediately before the type it governs:

```zig
// Invariant: pos <= buf.len; all bytes in buf[0..pos] are committed.
const Region = struct { ... };
```

A behavioral invariant lives immediately before the function that enforces it:

```zig
// Precondition: name.len == Sha3.digest_length * 2 (64 hex chars).
fn read_blob(...) ...
```

### 2. Bounds on everything, and simple control flow

Every allocation, every collection, every pipeline names its maximum size. Name the budget at construction; check it at the edge; fail with a named error, rather than a silent corruption.

A bound is the honest answer to "how large can this grow?" stated up front, before the machine runs. Everything has a limit, so every loop and every queue carries a fixed upper bound. Where a loop genuinely cannot terminate — an event loop — that fact is asserted, so the reader meets the intent. Control flow stays simple and explicit; recursion stays out, so that everything which should be bounded stays bounded.

### 3. Say why

Every assertion earns a comment: `// invariant: ...`. Every named constant earns a comment if the name alone does not make the reason obvious. Every design choice that will surprise a reader earns a sentence that names the reason.

The next reader meets the reason, not only the rule. Always motivate, always say why — a stated rationale shares with the reader the very criteria by which to weigh the decision.

### 4. Accrete, never break

A name once given is a promise. Add beside it; do not replace it silently. When a better shape is found, the old name keeps working while the new one grows. Rename only with a migration path; deprecate before removing.

A version once published does not change.

### 5. One value model

A value is: a string, an integer, a boolean, a list of values, a record of named values — or a composite of these. Values are composed (placed side by side); they are never tangled (woven together so that reading one requires holding the others).

A value crosses module boundaries without being serialized to text and reparsed on the other side. When that seam would open, close it.

POSIX interop at the process boundary is a seam, not the model — see [`active-designing/20260629-203012_posix-a-seam-not-a-model.md`](../active-designing/20260629-203012_posix-a-seam-not-a-model.md).

### 6. State invariants positively

Lead with what holds. The affirmative form is easier to get right and easier to read aloud, and it is the same instinct Radiant Style keeps for prose:

```zig
if (index < length) {
    // The invariant holds.
} else {
    // The invariant does not hold.
}
```

Split compound conditions into simple ones with nested `if/else`, rather than a wall of booleans joined by `and`. A single `if` often wants a matching `else`, so the positive and the negative space are both handled or both asserted.

### 7. Smallest scope, fewest variables

Declare each variable at the smallest scope that serves it, and keep the number of variables in scope small. Fewer names in flight means fewer ways to reach for the wrong one.

### 8. Explicit options at the call site

Pass options to library functions explicitly, rather than leaning on their defaults. `@prefetch(a, .{ .cache = .data, .rw = .read, .locality = 3 })` reads more clearly than `@prefetch(a, .{})`, and it stays correct even if the library changes a default tomorrow.

---

## Rye Supplement

Rye carries the family. The safety Rye offers is the safety every module written in it inherits. These rules are specific to Rye code (`.rye` source files). Naming, performance habits, and assertion density defer to **996** unless this supplement states a Rye-specific seam.

### Typed and sized

Use explicitly sized integer types: `u8`, `u16`, `u32`, `u64`, `i8`, `i16`, `i32`, `i64`. Use `f32` or `f64` for floating-point. Never use `c_int`, `c_uint`, or `anyopaque` without a stated, commented reason.

**Prefer fixed widths; avoid `usize` in authored Rye.** Tiger Style: use explicitly-sized types like `u32` for everything; avoid architecture-specific `usize`. In authored `.rye`, `tools/width-check.rish` flags authored `usize` while blessing sanctioned seam casts (`@intCast`, `@as(usize`). At the **inherited-std seam** (calling Zig's `std` through pristine symlinks), assert the bound and cast — that is correct Tiger code, rather than debt awaiting a compiler fork.

| Width | Role in authored Rye |
|-------|----------------------|
| **`u32`** | All in-memory counts, indices, and lengths **bounded by a named constant** (garden capacity, grid dimension, stack depth, frame size). Default width for "how many in this region." |
| **`u64`** | Wire-persistent sizes, timestamps, content offsets, and any quantity that must mean the same thing on every target. |
| **`usize`** | **Only at the cast site, never as an authored field or flowing variable.** At the inherited-std boundary: assert `len <= maxInt(u32)` (or named bound), do arithmetic in `u32`, `@intCast` to `usize` for the Zig API call. |

**Three widths, one boundary rule.** Authored Rye holds counts and indices in fixed widths; `usize` appears only where Zig's slice and allocator APIs require it — at the cast, not in a variable that flows through the module.

Two seam moves cover nearly everything:

1. **Index a slice with an authored `u32`:** cast at the index — `buf[@intCast(pos)]` or `buf[@as(usize, pos)]`. Assert the value is in range first when the bound is not already guaranteed.
2. **Take a std-provided length into authored arithmetic:** assert `len <= std.math.maxInt(u32)`, then `@intCast` down to `u32` — reuse Tally's `bufLenU32` shape rather than re-rolling the assert-and-cast at every call site.

**Worked example:** Mantra's SLC-1 path (`mantra/src/diff.rye`, `main.rye`) — seven in-memory indices migrated to `u32` with seam casts at slice indices; `store.rye` and `weave.rye` were already clean. Comlink wire formats lean on **`u64`** at persistence boundaries; Rishi REPL buffers follow the same **`u32` + seam cast** pattern as Mantra in TH-5.

**Freestanding width (Aurora).** On bare metal, `usize` is the machine word, and it is the correct, honest type for addresses, for control-and-status register values, for register-width hardware bit masks, and for local indices at the slice-access site. These are not debt; they are the kernel naming the hardware in the hardware's own width. What stays disciplined even here: a long-lived stored *count* still earns a named `u32` bound, so its ceiling is documented rather than left to the word size. The hosted authored-`usize` gate, `width-check`, governs the hosted corpus; `aurora/*` is freestanding and keeps this policy instead.

Name the bound when you pick `u32`:

```zig
const max_frame_bytes: u32 = 4096;
pos: u32, // invariant: pos <= max_frame_bytes
```

Width audit: [`work-in-progress/20260620-212126_usize-width-baseline.md`](../work-in-progress/20260620-212126_usize-width-baseline.md). **Mantra**, **Rishi**, and **Comlink** are green under the hosted policy (TH-3 through TH-6). **`width-check.rish`** is a blocking parity witness for the hosted corpus; **`aurora/*`** is scoped out and governed by the freestanding policy above.

**Seam pattern at inherited `std` (correct, not debt):**

```zig
const assert = std.debug.assert;

assert(buf.len <= std.math.maxInt(u32));
const cap: u32 = @intCast(buf.len);
// ... arithmetic in u32 ...
const start: usize = @intCast(self.pos);
assert(start <= buf.len);
return buf[start .. start + @as(usize, @intCast(n))];
```

**Compiler fork (F1–F5):** deferred **horizon** — deliberated only from a mature whole. See [`active-designing/20260628-043542_thin-frontend-slc-direction.md`](../active-designing/20260628-043542_thin-frontend-slc-direction.md). Prior fork-plan notes remain in [`active-designing/20260621-070712_the-compiler-fork.md`](../active-designing/20260621-070712_the-compiler-fork.md) as research, rather than the active primary track.

### Naming (Tiger Style)

**`snake_case`** for functions, variables, and file names — per `gratitude/TIGER_STYLE.md` and `external-research/TAME_GUIDANCE.md`. The underscore is the closest thing we have to a space; descriptive names read aloud well.

- Name functions with a verb: `compute_diff`, `serialize_weave`, `load_weave`, `read_brix`.
- Name constants in `snake_case` with units and qualifiers last when helpful: `max_depth`, `digest_hex_len`.
- Early seeds may still carry `camelCase` from before this rule landed; migrate names opportunistically when you touch a file — rather than renaming silently across the tree in one sweep.

**Types and receivers.** A function that returns a `type` carries a `CamelCase` name ending in `Type` — `StackType`, `BitSetType` — so the reader sees a type constructor at a glance. When a method aliases its own type, give the alias the **real type name**, `const Stack = @This();`, rather than the bare `Self`. For the receiver itself, name it after the type in non-generic structs — `file: SourceFile`, `counter: *IdentifierCounter` — which reads more clearly than a generic `self`; the plain `self` stays welcome inside generic wrappers where the type name is a parameter.

For everything else, follow the Zig style guide as filtered through **996** (line length, braces, `zig fmt`, and the rest).

### The opening lines

Every hosted `.rye` file that speaks or checks begins with the same three lines — the canonical head, tutorial one's first breath:

```zig
const std = @import("std");
const assert = std.debug.assert;
const print = std.debug.print;
```

A one-line prelude was weighed and set aside: Rye removed the namespace-splat long ago, so a single import would force qualified calls and collide with bare `assert` (gated by tidy) and bare `print` (ruled this week). A prelude file would spend the same three lines plus an indirection. **Canonize these three** until the shared head outgrows four names — the day indirection starts paying rent. A gentle textual check for the canonical head waits on the horizon beside `tame-check`.

### Assertions as first-class design

`assert(cond)` is not a debugging tool; it is the design written down where the machine can check it. Import it unqualified once per file — `const assert = std.debug.assert;` — and call it bare, the way TigerBeetle does throughout. Assertions detect programmer errors, which are unexpected; the correct response to corrupt code is to crash, and so an assertion downgrades a catastrophic correctness bug into a loud, findable liveness bug.

- **Density.** Assert all function arguments and return values, preconditions, postconditions, and invariants. Aim for an average of at least **two assertions per function** — a function that checks nothing operates blindly on data it has not verified.
- **Preconditions** — at the top of a function, before any work: the conditions the caller must have arranged.
- **Invariants** — after every mutation of a data structure: the conditions the structure must always keep.
- **Postconditions** — after a computation: the conditions the result must honor.
- **Pair your assertions.** For each property worth enforcing, find two different code paths to assert it on — validity right before a write and again right after the matching read, a count checked on both `push` and `pop`. The boundary between valid and invalid is where the interesting bugs live, so guard both sides of it.
- **Assert positive space and negative space.** Assert what you expect to be true, and also assert what you expect to be false. Tests follow the same rule: exercise valid data, invalid data, and data crossing from one to the other.
- **Split compound assertions.** Prefer `assert(a); assert(b);` over `assert(a and b)` — the split form reads more simply and names exactly which half failed.
- **Assert implications on one line.** `if (a) assert(b)` states "a implies b" plainly.
- **Assert at compile time.** Use `comptime assert(...)` to check the relationships of compile-time constants and the sizes of types, so a design flaw is caught before the program ever runs.
- **Gate the expensive check.** When a thorough assertion costs too much for the hot path, place it behind a verify flag rather than dropping it: `if (constants.verify and verify_push) assert(!contains(link));`. This mirrors our verify-flag hot-path thread.

A small, complete example — a bounded stack, asserting its invariant on two paths and naming its bound:

```zig
const assert = std.debug.assert;

fn push(stack: *StackAny, link: *Link) void {
    assert((stack.count == 0) == (stack.head == null)); // structural invariant
    assert(link.next == null);
    assert(stack.count < stack.capacity);              // the bound

    link.next = stack.head;
    stack.head = link;
    stack.count += 1;
}

fn pop(stack: *StackAny) ?*Link {
    assert((stack.count == 0) == (stack.head == null)); // same invariant, second path
    const link = stack.head orelse return null;
    stack.head = link.next;
    stack.count -= 1;
    return link;
}
```

In tests, reach for `std.testing.expect` and `std.testing.expectEqual` rather than `assert`.

### Diagnostic output (`print`)

For hosted seeds and modules, mirror the assert import: bind once per file — `const print = std.debug.print;` — and call bare `print(...)`. TigerBeetle's `tidy.zig` bans qualified `debug.assert(` and expects unqualified `assert`; it does **not** ban qualified `debug.print(`, yet the same once-per-file binding keeps diagnostic lines short and consistent across the hosted corpus.

- **As-you-touch.** Migrate when a file is already open for other work — the same discipline as assertion-density hygiene, rather than a tree-wide sweep.
- **No gate yet.** `tools/tame-check.rish` does not flag `std.debug.print(`; add that rule only if the need is proven, the way we defer AST-tier lints.
- **Separate layers.** Rishi `.rish` pipelines speak through `say`; freestanding Aurora may grow its own logging seam when the boot path matures; `rye/tests/*` witnesses may keep the qualified form until touched.

### Named errors

Error types are named for the **fault**, rather than the operation that discovered it: `error.OutOfBounds`, `error.InvalidFormat`, `error.NotFound`.

Propagate errors with `try`. Catch only at the boundary where the program can act: a command entry point, a test body. When you must compare an error, **switch on it** rather than writing `err == error.Foo` or `err != error.Foo` — the equality form silently widens to `anyerror` and lets a new error slip through unhandled, while a `switch` makes every case visible. Never swallow an error silently with a discard pattern. Handle every error: most catastrophic failures trace back to mishandled non-fatal errors.

### Short functions

One function, one idea. We keep a **hard limit of 70 lines per function** — the point where a function stops fitting on a screen and starts asking the reader to scroll. Art is born of constraints, and most walls of code have a natural seam at this length.

We bring the rule in by **ratcheting from the bottom up**, rather than sweeping the whole tree at once: the greatest value is in keeping a small function from quietly growing into a large one, so a function newly crossing the line is the one to split. This is accrete-never-break applied to length.

When you split, **push the `if`s up and the `for`s down**: keep the branching in one parent function, and move the non-branchy work into leaf helpers that stay pure. Centralize control flow and state in the parent; let the helpers compute what changes rather than applying it. A function that needs a `// ---` section divider is doing more than one thing and wants splitting.

Parameters: declare the tightest type you can. Prefer slices over pointers when ownership stays put.

### Named constants

No magic numbers inline. Name constants with their type:

```zig
const max_depth: u32 = 1024; // chain length above which we stop and warn
const digest_hex_len: u32 = 64; // SHA3-256 digest rendered as hex
```

The comment names why the bound exists, rather than only what it is.

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

### Season memory — never `ArenaAllocator` directly

In **authored** Rye programs (`.rye` seeds, tools, witness tests, Skate, Rishi source), reach for the process season allocator through **`init.arena`** at the pristine std seam, rather than through `std.heap.ArenaAllocator`:

```zig
const garden = init.arena.allocator();
```

Name the local `garden` (warm vocabulary — Tally's future owned concept) or `allocator` when the role is generic. Do not construct `ArenaAllocator` in our code, do not name the type in our APIs, and do not add `std.heap.GardenAllocator` as a rename of the inherited type.

**Why:** `ArenaAllocator` is Zig's inherited name — we keep it in `std` untouched (`context/specs/inherited-names.md`). At the thin-frontend seam, Zig names the field `arena`; we honor that name in code. `garden` lives as a local binding and as Tally's future owned vocabulary (`rye.garden` or `tally/heap-garden.rye` when the wrapper graduates). Inherited `std` internals may still use `ArenaAllocator`; that is out of scope for authored programs.

**Freestanding / no `Init`:** use `std.heap.FixedBufferAllocator`, Tally `Region`, or an explicit child allocator passed in — still not `ArenaAllocator` in authored code unless you are strengthening inherited `std` itself.

**On static allocation.** TigerBeetle allocates all memory at startup and frees nothing after, a discipline its database domain rewards with zero latency spikes and no use-after-free. We adopt the spirit fully — bound everything, name every budget — and we adopt the letter where the domain matches: freestanding Aurora paths favor `FixedBufferAllocator` and Tally regions sized up front. For hosted seeds and tools, the bounded `init.arena` season is our deliberate, honest choice: a single arena, released at the end of its season, rather than per-call churn. We name this difference plainly rather than claim a rule we do not yet keep.

---

## Brix Supplement

Brix is the composing language: it describes what a system is made of. A `.brix` file is a declaration, rather than a program. These rules govern `.brix` descriptors.

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

`let` binds a named value. Name bindings for what they *are*, rather than for how they were computed: `let commit_hash = ...` rather than `let result_of_sha3_over_blob = ...`.

---

## What We Check, and When

These are the machine-checkable rules — the lint surface. The discipline is the distinctiveness we chose when we made Rye a thin frontend, so we grow these checks the way we grow everything: as small, demand-driven increments beside the work, rather than one large sweep. Each line names the rule, and the tool that catches it today or the horizon it waits for.

**Enforced now — textual checks in Rishi** (grow these first, each with a witness, alongside SLC-1 and the width migration):

| Rule | Check |
|------|-------|
| **No authored `usize` in published `.rye`** (seam casts blessed) | `tools/width-check.rish` (live, TH-1) |
| **Unqualified assert** | `tools/tame-check.rish` (live gate, TH-2c) |
| **No `Self = @This()`** | `tools/tame-check.rish` (gate) |
| **No tabs, no trailing whitespace** | `tools/tame-check.rish` (gate) |
| **Line length ≤ 100 columns** | flag lines past 100, allowing a URL or a multiline-string result that itself fits |
| **One `# Title` per markdown** | flag any `.md` with zero or more than one top-level `#`, fenced code ignored — directly serving our doc-heavy tree |
| **No leftover `FIXME` or `dbg(`** | flag both before merge; `FIXME` is welcome while iterating, gone before main |

**Horizon — wait for a Zig parser** (build when Rye's own tooling can parse, or when the need is proven; do not clone `tidy.zig` ahead of the need):

| Rule | Why it waits |
|------|--------------|
| **70 lines per function, ratcheted** | needs the AST to find function spans |
| **Parenthesize bitwise-with-arithmetic mixes** | needs the AST to read operator nodes |
| **`defer` followed by a blank line** | needs token positions |
| **Dead declarations and dead files** | needs identifier and import analysis |
| **Switch on errors, not `== error.`** | a textual flag is a fair first pass; the AST makes it exact |

The full enforcement we are learning from lives in TigerBeetle's `src/tidy.zig`. We borrow its rules in our own voice and at our own pace, and we keep its file in gratitude.

---

*May the root hold firm across every language we grow. May each supplement stay small — exactly as small as the language has earned, and no larger. May the rules serve the work, and the work serve what is true.*
