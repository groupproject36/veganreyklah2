# Pass 9960 · cutPrefix and cutSuffix — prefix/suffix chop stays in-range

**Corpus:** 43 programs (grew from 42)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.174312`

## What this pass covers

**`std.mem.cutPrefix`** and **`cutSuffix`** — return the remainder after a verified prefix or suffix. Build on `startsWith` / `endsWith` (9993); used in CLI flag parsing patterns.

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
