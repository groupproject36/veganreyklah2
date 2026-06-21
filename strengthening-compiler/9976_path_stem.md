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

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/fs/path.zig` | `path.stem` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/path_stem_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9976_path_stem.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9976 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.fs.path.stem` — [`rye/lib/std/fs/path.zig`](../rye/lib/std/fs/path.zig)

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
