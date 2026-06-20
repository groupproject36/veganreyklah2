# Pass 9961 · mem.join — separator join fills the allocated buffer

**Corpus:** 42 programs (grew from 41)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.173212`

## What this pass covers

**`std.mem.join`** and **`joinMaybeZ`** — allocate and concatenate slices with a separator. Backs Rishi `join` and complements `path.join` (9983).

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
