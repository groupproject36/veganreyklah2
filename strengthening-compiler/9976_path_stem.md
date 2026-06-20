# Pass 9976 · path.stem — basename without extension stays within the input

**Corpus:** 27 programs (grew from 26)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.161812`

## What this pass covers

**`std.fs.path.stem`** — returns the final path component without its extension. Completes the path naming family beside `extension` (9977), `basename` (9978), and `dirname` (9980).

## Postcondition

```zig
assert(result.len <= path.len);
if (result.len > 0) assert(mem.indexOf(u8, path, result) != null);
```

## What the test asserts

- Multi-dot filename strips only the last extension
- Simple `name.ext` yields `name`
- No extension returns full basename
- Leading-dot files keep the hidden name
- Empty path returns empty
