# Pass 9979 · trimStart — leading strip stays within the input

**Corpus:** 24 programs (grew from 23)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.152712`

## What this pass covers

**`std.mem.trimStart`** — removes leading characters from a slice. Rishi calls it indirectly through `trim` on every line; the arithmetic parser and `let` binder trim leading whitespace before names and values.

Completes the trim family alongside `trim` (9996) and `trimEnd` (9982).

## Rye std surface

**`std.mem.trimStart`**

```zig
pub fn trimStart(comptime T: type, slice: []const T, values_to_strip: []const T) []const T
```

## Width notes

**`std.mem.trimStart`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `trimStart` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/trim_start_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9979_trim_start.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9979 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.trimStart` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postcondition

```zig
assert(begin <= slice.len);
assert(result.len <= slice.len);
```

## What the test asserts

- Leading whitespace removed
- No-op when nothing to strip
- Empty input returns empty
- Result length never exceeds input length
- Trailing characters left untouched

## Design notes

Same contract as `trimEnd`: the cursor advances inward from the start and the returned slice never extends past the input bounds.
