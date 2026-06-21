# Pass 9946 · SemanticVersion.format — semver text round-trips through parse

**Witnesses:** 57 programs (grew from 56)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.193212`

## What this pass covers

**`std.SemanticVersion.format`** — semver 2.0 serialization via `{f}`. Completes the trio with `parse` (9947) and `order` (9948).

## Rye std surface

**`std.SemanticVersion.format`**

```zig
pub fn format(self: Version, w: *std.Io.Writer) std.Io.Writer.Error!void
```

## Width notes

**`std.SemanticVersion.format`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

On format entry, optional `pre` and `build` slices are non-empty when present — matching valid parsed versions.

## What the test asserts

- Release, pre-release, build metadata, and combined forms format to expected strings
- Round-trip agreement with strings accepted by `parse`
