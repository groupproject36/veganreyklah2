# Pass 9977 · path.extension — suffix stays within the input

**Corpus:** 26 programs (grew from 25)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.161312`

## What this pass covers

**`std.fs.path.extension`** — returns the filename suffix after the last dot. Completes the path trio with `basename` (9978) and `dirname` (9980).

## Rye std surface

**`std.fs.path.extension`**

```zig
pub fn extension(path: []const u8) []const u8
```

## Width notes

**`std.fs.path.extension`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

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

- Normal extension on a file
- Last dot wins on multi-dot names
- No extension when absent
- Leading-dot hidden files return empty
- Nested path resolves through basename
- Empty path returns empty
