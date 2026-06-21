# Pass 9947 · SemanticVersion.parse — parsed fields stay within input text

**Witnesses:** 56 programs (grew from 55)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.192712`

## What this pass covers

**`std.SemanticVersion.parse`** and **`parseNum`** — semver 2.0 parsing. Pairs with `order` (9948); feeds capability table and future **RyeVersion** accretion.

## Rye std surface

Live implementation from `rye/lib/std` (strengthened):

**`std..SemanticVersion.parse`**

```zig
pub fn parse(str: []const u8) !WindowsVersion {
            return std.meta.stringToEnum(WindowsVersion, str) orelse
                @enumFromInt(std.fmt.parseInt(u32, str, 0) catch
                    return error.InvalidOperatingSystemVersion);
        }
```

## Width notes

**`std.SemanticVersion.parse`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |





## usize explicit audit

Tiger Style: *use explicitly-sized types like `u32`; avoid architecture-specific `usize`* ([`gratitude/TIGER_STYLE.md`](../gratitude/TIGER_STYLE.md) § Safety).

TAME: **`usize` is a boundary type, not a design type** — [`context/TAME_STYLE.md`](../context/TAME_STYLE.md), [`10024`](../expanding-prompts/10024_explicit_width_audit.md), [`992`](../work-in-progress/992_usize_width_baseline.md).

Lexicon ✅ requires every row **`done`** and zero **`fail`** rows.
### `std..SemanticVersion.parse`

| Check | Type | Tiger/TAME policy | Status |
|-------|------|-------------------|--------|
| slice params / `.len` | inherited `usize` (Tier C) | Tiger: avoid `usize` in APIs we publish — this surface is inherited Zig `std`; unchanged per `10024` rule 3 | done |
| Tier | C — inherited `std` | `992` Phase 4 — touch named bounds only; do not rename public seam | done |

### Witness `rye/tests/semantic_version_parse_test.rye`

| Check | Type | Tiger/TAME policy | Status |
|-------|------|-------------------|--------|
| Tier | B — witness `.rye` | `992` — `usize` only at `buf[0..n]` slice edge | done |
| witness body | slice edge only | Stack buffers + `.len` at seam — no authored `usize` fields | done |


## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `misc` | `parse` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/semantic_version_parse_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9947_semantic_version_parse.md` | pass record + audited surfaces | done |
| `## usize explicit audit` | per-surface locus table — gates lexicon ✅ | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9947 | done |

## Audited surfaces

Checkmark requires **`## usize explicit audit`** all `done`, zero `fail` (Tiger/TAME — [`992`](../work-in-progress/992_usize_width_baseline.md)). Full implementation from `rye/lib/std`:
- [x] `std..SemanticVersion.parse` — [`misc`](../misc)

```zig
pub fn parse(str: []const u8) !WindowsVersion {
            return std.meta.stringToEnum(WindowsVersion, str) orelse
                @enumFromInt(std.fmt.parseInt(u32, str, 0) catch
                    return error.InvalidOperatingSystemVersion);
        }
```

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
