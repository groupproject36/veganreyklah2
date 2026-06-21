# Pass 9960 · cutPrefix and cutSuffix — prefix/suffix chop stays in-range

**Corpus:** 43 programs (grew from 42)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.174312`

## What this pass covers

**`std.mem.cutPrefix`** and **`cutSuffix`** — return the remainder after a verified prefix or suffix. Build on `startsWith` / `endsWith` (9993); used in CLI flag parsing patterns.

## Rye std surface

**`std.mem.cutPrefix`**

```zig
pub fn cutPrefix(comptime T: type, slice: []const T, prefix: []const T) ?[]const T
```

## Width notes

**`std.mem.cutPrefix`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

**cutPrefix** on match:

```zig
assert(prefix.len <= slice.len);
assert(rest.len + prefix.len == slice.len);
```

**cutSuffix** on match:

```zig
assert(suffix.len <= slice.len);
assert(rest.len + suffix.len == slice.len);
```

## What the test asserts

- Prefix chop on flag-style string
- Absent prefix returns null
- Suffix chop and absent suffix
- Empty needle preserves whole slice
