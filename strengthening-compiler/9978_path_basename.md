# Pass 9978 · path.basename — final component stays within the input

**Corpus:** 25 programs (grew from 24)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.160312`

## What this pass covers

**`std.fs.path.basename`** — returns the final path component. Complements `path.dirname` (9980) on the path pair the rye bridge and Pond policy will compose.

## Rye std surface

**`std.fs.path.basename`**

```zig
pub fn basename(path: []const u8) []const u8
```

## Width notes

**`std.fs.path.basename`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/fs/path.zig` | `path.basename` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/path_basename_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9978_path_basename.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9978 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.fs.path.basename` — [`rye/lib/std/fs/path.zig`](../rye/lib/std/fs/path.zig)

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
