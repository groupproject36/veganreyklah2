# Pass 9947 · SemanticVersion.parse — parsed fields stay within input text

**Witnesses:** 56 programs (grew from 55)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.192712`

## What this pass covers

**`std.SemanticVersion.parse`** and **`parseNum`** — semver 2.0 parsing. Pairs with `order` (9948); feeds capability table and future **RyeVersion** accretion.

## Rye std surface

**`std.SemanticVersion.parse`**

```zig
pub fn parse(text: []const u8) !Version
```

## Width notes

**`std.SemanticVersion.parse`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

**parse** — on success:

- Release-only versions have no `pre` or `build`
- `pre` and `build` slices are found within the input `text`

**parseNum**:

```zig
assert(text.len > 0);
```

## What the test asserts

- Plain release, pre-release, build metadata, and combined forms
- Major/minor/patch and metadata substring equality
