# Pass 9940 · allEqual — every element matches the scalar

**Witnesses:** 63 programs (grew from 62)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.195612`

## What this pass covers

**`std.mem.allEqual`** — tests whether every element in a slice equals a scalar. Complements `eql` (9941) and `count` (9951).

## Rye std surface

**`std.mem.allEqual`**

```zig
pub fn allEqual(comptime T: type, slice: []const T, scalar: T) bool
```

## Width notes

**`std.mem.allEqual`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `allEqual` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_all_equal_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9940_mem_all_equal.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9940 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.allEqual` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

- `false` ⇒ found element differs from scalar
- `true` ⇒ every element equals scalar (vacuous when empty)

## What the test asserts

- Uniform run, mixed run, empty slice
- Single-element match and mismatch
- Whitespace uniformity
