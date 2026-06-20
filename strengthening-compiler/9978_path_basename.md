# Pass 9978 · path.basename — final component stays within the input

**Corpus:** 25 programs (grew from 24)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.160312`

## What this pass covers

**`std.fs.path.basename`** — returns the final path component. Complements `path.dirname` (9980) on the path pair the rye bridge and Pond policy will compose.

## Postcondition

At `basenameInner` return:

```zig
assert(result.len <= path.len);
if (result.len > 0) assert(mem.indexOf(u8, path, result) != null);
```

## What the test asserts

- Nested path yields the filename
- Absolute path yields the last segment
- Bare filename returns itself
- Empty path and root return empty
- Parity holds against baseline std
