# Pass 9961 · mem.join — separator join fills the allocated buffer

**Corpus:** 42 programs (grew from 41)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.173212`

## What this pass covers

**`std.mem.join`** and **`joinMaybeZ`** — allocate and concatenate slices with a separator. Backs Rishi `join` and complements `path.join` (9983).

## Rye std surface

**`std.mem.join`**

```zig
pub fn join(allocator: Allocator, separator: []const u8, slices: []const []const u8) Allocator.Error![]u8
```

## Width notes

**`std.mem.join`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postcondition

After the memcpy loop:

```zig
assert(buf.len == total_len);
assert(buf_index + @as(usize, @intFromBool(zero)) == total_len);
```

## What the test asserts

- Multi-slice join with separators
- Single slice (no separator inserted)
- Empty middle slices preserved
- Zero-length input slice list
- `joinZ` null terminator
