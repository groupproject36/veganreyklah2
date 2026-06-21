# Pass 9926 · mem.sliceAsBytes — byte view length matches element width

**Witnesses:** 77 programs (grew from 76)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.015612`

## What this pass covers

**`std.mem.sliceAsBytes`** — reinterprets a typed slice as `[]u8` preserving pointer attributes. Pairs with `asBytes` on single items and the copy/compare mem arc.

## Rye std surface

**`std.mem.sliceAsBytes`**

```zig
pub fn sliceAsBytes(slice: anytype) SliceAsBytesReturnType(@TypeOf(slice))
```

## Width notes

**`std.mem.sliceAsBytes`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

Returned byte slice length is `slice.len * @sizeOf(Elem)` on the main path; zero-bit elements and empty non-sentinel slices return `len == 0`.

## What the test asserts

- `u16` array yields four bytes with correct endian layout
- Empty sentinel `u8` string yields zero bytes
- Zero-bit element slice yields zero bytes
