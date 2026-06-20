# TAME Style — Code

Full guide: `context/specs/tame-style.md`. Apply when writing or reviewing Rye source (`.rye`), Brix descriptors (`.brix`), and Rishi scripts (`.rish`).

## When this rule is active

- Writing or editing any `.rye` source file
- Writing or editing any `.brix` descriptor
- Writing or editing any `.rish` script
- Reviewing, suggesting changes to, or explaining any of the above

## Core moves (root — all family languages)

- State invariants **before** implementing: write `assert` calls at construction, mutation, and postcondition, each preceded by a `// invariant:` comment.
- Bounds on everything: every allocation, collection, and pipeline names a maximum. Name the budget at construction; enforce at the edge.
- Say why: every assertion, every named constant, every surprising design choice earns a comment that names the reason.
- Accrete, never break: a name once given is a promise. Add beside it; do not replace it silently.
- One value model: string, integer, bool, list, record — composed side by side, never tangled.

## Supplement cheatsheet

| Language | Key discipline |
|----------|----------------|
| **Rye** | Explicit widths (`u32` bounded, `u64` wire); `usize` only at inherited slice boundaries. `std.debug.assert` at every invariant. Named errors, propagated with `try`. Short functions named with a verb. Constants named with type and comment. **Never use `ArenaAllocator` in authored `.rye`** — use `init.garden.allocator()`; see `inherited-names.md`. |
| **Brix** | Declarative only — no commands, no conditions. One field per line. Comments name what the brick *is*. Plain key-value; readable by hand. |
| **Rishi** | `run` always returns `{ status, out, err }`. Check `status` before trusting `out`. `assert` as a pipeline gate at every stage boundary. Effects come last and are visible. Named `let` bindings. |

## Explicit widths (Rye only)

Tiger Style: **`usize` is a boundary type, not a design type.** Inherited Zig `std` still uses `usize` at slice edges — convert explicitly at our API boundary.

| Width | Use |
|-------|-----|
| `u32` | Bounded in-memory counts, indices, lengths (named `MAX_*`) |
| `u64` | Wire offsets, timestamps, cross-target persistent sizes |
| `usize` | Only at `buf.len`, slice indexing, inherited `std` calls — always with `@intCast` + assert |

- **Never** `usize` in struct fields, public parameters, or return types we publish.
- Pair every narrow cast: `assert(buf.len <= std.math.maxInt(u32))` before `@intCast`.
- Charter: `expanding-prompts/10024_explicit_width_audit.md`; inventory: `work-in-progress/992_usize_width_baseline.md`.

## Garden memory (Rye only)

- **Never** construct or name `std.heap.ArenaAllocator` in authored `.rye` (seeds, Rishi, Skate, witnesses, tools).
- **Always** reach for the season allocator via `const garden = init.garden.allocator()` (or pass `allocator` from that garden).
- Do **not** add `GardenAllocator` as a std rename of `ArenaAllocator`. The owned wrapper lives at `rye.garden` / `tally/heap-garden.rye` when we build it — beside inherited names, not in their place.
- Full policy: `context/specs/inherited-names.md`.

## The priority order

Safety first — structural, not by convention. Performance second — measure before optimizing. Joy third — clarity, named things, the habit of saying why.

When these pull against each other, safety wins. When safety and performance are equal, joy earns the vote.
