# Pass 9924 · mem.bytesAsSlice — typed slice length matches byte span

**Witnesses:** 79 programs (grew from 78)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.022612`

## What this pass covers

**`std.mem.bytesAsSlice`** — reinterprets `[]u8` as `[]T` preserving pointer attributes. Inverse of `sliceAsBytes` (9926); pairs with `asBytes` (9925).

## Rye std surface

**`std.mem.bytesAsSlice`**

```zig
pub fn bytesAsSlice(comptime T: type, bytes: anytype) BytesAsSliceReturnType(T, @TypeOf(bytes))
```

## Width notes

**`std.mem.bytesAsSlice`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

Empty bytes or zero-sized `T` returns `len == 0`. Otherwise `result.len * @sizeOf(T) == bytes.len` and `bytes.len % @sizeOf(T) == 0`.

## What the test asserts

- Four bytes as two `u16` values; round-trip via `sliceAsBytes`
- Empty byte slice
- Zero-sized element type
