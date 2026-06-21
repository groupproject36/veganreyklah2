# Pass 9945 · sliceTo — sentinel slice length agrees with terminator search

**Witnesses:** 58 programs (grew from 57)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.193612`

## What this pass covers

**`std.mem.sliceTo`** and **`lenSliceTo`** (slice branch) — slice sentinel-terminated pointers and buffers up to a terminator. Pairs with `findSentinel` (9952) and `orderZ` (9952).

## Rye std surface

**`std.mem.sliceTo`**

```zig
pub fn sliceTo(ptr: anytype, comptime end: std.meta.Elem(@TypeOf(ptr))) SliceTo(@TypeOf(ptr), end)
```

## Width notes

**`std.mem.sliceTo`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `sliceTo` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_slice_to_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9945_mem_slice_to.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9945 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.sliceTo` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

**sliceTo** — returned slice length matches `lenSliceTo`.

**lenSliceTo** (slice inputs) — when a terminator is found inside the slice, the index is in bounds and points at `end`.

## What the test asserts

- NUL-terminated string literals and embedded NUL
- Scalar delimiter before sentinel
- `[*:0]const u8` C string via `sliceTo` and `len`
- Optional null pointer returns null
