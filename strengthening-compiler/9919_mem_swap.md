# Pass 9919 · mem.swap — locations exchange values

**Witnesses:** 84 programs (grew from 83)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.030412`

## What this pass covers

**`std.mem.swap`** — exchange contents of two memory locations. Pairs with `mem.reverse` (9921), which calls `swap` for each mirrored pair.

## Rye std surface

**`std.mem.swap`**

```zig
pub fn swap(comptime T: type, noalias a: *T, noalias b: *T) void
```

## Width notes

**`std.mem.swap`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `swap` — max_reverse_check `u32`; public `usize` unchanged | done |
| `rye/tests/mem_swap_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9919_mem_swap.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9919 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.swap` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

After swap at runtime, each pointer holds the other's original bytes (`eql(u8, asBytes(...))`). Comptime swaps skip byte asserts — same rule as the existing comptime branch (undefined layout).

## What the test asserts

- `u8` pair exchanges
- `i32` pair exchanges
- anonymous struct pair exchanges field-wise
