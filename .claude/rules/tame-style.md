# TAME Style — Code

**Canon:** `external-research/TAME_STYLE.md` (voiced Tiger Style) · **Source:** `gratitude/TIGER_STYLE.md`
**Operational supplement:** `context/TAME_STYLE.md`. Apply when writing or reviewing Rye source (`.rye`), Brix descriptors (`.brix`), Bron notation (`.bron`), and Rishi scripts (`.rish`).

## When this rule is active

- Writing or editing any `.rye` source file
- Writing or editing any `.brix` descriptor or `.bron` notation
- Writing or editing any `.rish` script
- Reviewing, suggesting changes to, or explaining any of the above

## Core moves (root — all family languages)

- State invariants **before** implementing: write `assert` calls at construction, mutation, and postcondition, each preceded by a `// invariant:` comment.
- Bounds on everything: every allocation, collection, and pipeline names a maximum. Name the budget at construction; enforce at the edge.
- Say why: every assertion, every named constant, every surprising design choice earns a comment that names the reason.
- Accrete, never break: a name once given is a promise. Add beside it; do not replace it silently.
- One value model: string, integer, bool, list, record — composed side by side, never tangled.

## ABSOLUTE: No `usize` in Rye

**`usize` is banned in Rye. No exceptions. No seam casts. No boundary patterns.**

Rye is forking from Zig. The Zig slice type `[]T` with `len: usize` is an inherited constraint we are replacing. In Rye:

- **`u32`** for all lengths, indices, counts, offsets bounded by a named constant
- **`u64`** for wire-persistent sizes, timestamps, MMIO addresses, cross-target quantities
- **Never `usize`** — not in struct fields, not in function parameters, not in return types, not in local variables, not at slice boundaries, not anywhere

Where Zig's `std` currently requires `usize` (slice `.len`, `@intCast`), the Rye compiler fork (F1–F5) replaces the slice type. Until the fork lands, existing seam casts (`const start: usize = @intCast(...)`) are **technical debt to be eliminated**, not an acceptable pattern.

The width-check gate (`tools/width-check.rish`) enforces this. Every authored `.rye` file must pass.

## Supplement cheatsheet

| Language | Key discipline |
|----------|----------------|
| **Rye** | `u32` bounded, `u64` wire. **Zero `usize` — absolute ban.** `std.debug.assert` at every invariant. Named errors, propagated with `try`. Short functions named with a verb. |
| **Brix** | Composition language — declares systems. Evaluates to Bron. Interfaces with Mantra, targets Aurora + Tally. |
| **Bron** | Data notation — plain key-value, one field per line. Parsed, not evaluated. Token-efficient. |
| **Rishi** | `run` always returns `{ status, out, err }`. Check `status` before trusting `out`. `assert` as a pipeline gate. `if/then/else` for conditionals. `for-each` for iteration. |

## Garden memory (Rye only)

- **Never** construct or name `std.heap.ArenaAllocator` in authored `.rye`.
- **Always** reach for the season allocator via `const garden = init.garden.allocator()`.
- Full policy: `context/specs/inherited-names.md`.

## The priority order

Safety first — structural, not by convention. Performance second — measure before optimizing. Joy third — clarity, named things, the habit of saying why.

When these pull against each other, safety wins. When safety and performance are equal, joy earns the vote.
