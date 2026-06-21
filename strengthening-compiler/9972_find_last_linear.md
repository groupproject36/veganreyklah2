# Pass 9972 · findLastLinear — backward needle search stays in-range

**Corpus:** 31 programs (grew from 30)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.164012`

## What this pass covers

**`std.mem.findLastLinear`** (`lastIndexOfLinear`) — linear backward sub-slice search. `findLast` delegates here on small inputs; pairs with `findPosLinear` (9973).

## Rye std surface

**`std.mem.findLastLinear`**

```zig
pub fn findLastLinear(comptime T: type, haystack: []const T, needle: []const T) ?usize
```

## Width notes

**`std.mem.findLastLinear`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `findLastLinear` — inherited `usize` seam; assertions only | done |
| `rye/tests/find_last_linear_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9972_find_last_linear.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9972 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.findLastLinear` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postcondition

On match:

```zig
assert(i + needle.len <= haystack.len);
```

## What the test asserts

- Last occurrence wins on repeated needle
- Single-char last match
- Multi-byte last match
- Missing needle returns null
