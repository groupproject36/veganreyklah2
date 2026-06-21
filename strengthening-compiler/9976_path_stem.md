# Pass 9976 · path.stem — basename without extension stays within the input

**Corpus:** 27 programs (grew from 26)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.161812`

## What this pass covers

**`std.fs.path.stem`** — returns the final path component without its extension. Completes the path naming family beside `extension` (9977), `basename` (9978), and `dirname` (9980).

## Rye std surface

**`std.fs.path.stem`**

```zig
pub fn stem(path: []const u8) []const u8
```

## Width notes

**`std.fs.path.stem`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

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
