# Pass 9921 · mem.reverse — reversed order matches snapshot

**Witnesses:** 82 programs (grew from 81)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.024012`

## What this pass covers

**`std.mem.reverse`** — in-place order reversal of a slice. Pairs with `reverseIterator` and the mem mutation arc.

## Rye std surface

**`std.mem.reverse`**

```zig
pub fn reverse(comptime T: type, items: []T) void
```

## Width notes

**`std.mem.reverse`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `reverse` — max_reverse_check `u32`; public `usize` unchanged | done |
| `rye/tests/mem_reverse_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9921_mem_reverse.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9921 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.reverse` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

When `items.len <= 64`, after reversal each element's bytes match the mirrored original (`eql(u8, asBytes(...))` — works for any `T` with defined layout, including structs used by `mem.sort`).

## What the test asserts

- `u8` five-element reversal
- `i32` three-element ends swap
