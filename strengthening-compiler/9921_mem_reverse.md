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

## Postconditions

When `items.len <= 64`, after reversal each element's bytes match the mirrored original (`eql(u8, asBytes(...))` — works for any `T` with defined layout, including structs used by `mem.sort`).

## What the test asserts

- `u8` five-element reversal
- `i32` three-element ends swap
