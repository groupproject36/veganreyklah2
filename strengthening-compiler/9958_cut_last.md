# Pass 9958 · cutLast and cutScalarLast — backward split-once stays in-range

**Corpus:** 45 programs (grew from 44)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.175312`

## What this pass covers

**`std.mem.cutLast`** and **`cutScalarLast`** — return before/after slices at the **last** needle occurrence. Pairs with `cut`/`cutScalar` (9959); use `findLast` / `findScalarLast` (9970, 9975).

## Rye std surface

**`std.mem.cutLast`**

```zig
pub fn cutLast(comptime T: type, haystack: []const T, needle: []const T) ?struct
```

## Width notes

**`std.mem.cutLast`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `cutLast` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/cut_last_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9958_cut_last.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9958 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.cutLast` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

Same contract as forward `cut`/`cutScalar` — index in range, parts reassemble haystack.

## What the test asserts

- Absent needle returns null
- Sequence and scalar last-split match upstream cases
