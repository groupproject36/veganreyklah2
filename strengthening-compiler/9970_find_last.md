# Pass 9970 · findLast — backward search entry states the fit contract

**Corpus:** 33 programs (grew from 32)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.164812`

## What this pass covers

**`std.mem.findLast`** (`lastIndexOf`) — unified backward sub-slice search. Delegates to `findLastLinear` (9972) or reverse Boyer-Moore-Horspool; complements `find` / `findPos` (9971).

## Rye std surface

**`std.mem.findLast`**

```zig
pub fn findLast(comptime T: type, haystack: []const T, needle: []const T) ?usize
```

## Width notes

**`std.mem.findLast`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `findLast` — inherited `usize` seam; assertions only | done |
| `rye/tests/find_last_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9970_find_last.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9970 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.findLast` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postcondition

On reverse BMH match:

```zig
assert(result + needle.len <= haystack.len);
```

`findLastLinear` path already strengthened (9972). Empty needle returns `haystack.len` per std semantics.

## What the test asserts

- Last repeated needle wins
- Single-char last match
- Not found
- Empty needle at haystack.len
- Long haystack exercises reverse BMH path
