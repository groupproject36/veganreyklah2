# Pass 9971 · findPos — offset needle entry states the fit contract

**Corpus:** 32 programs (grew from 31)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.164312`

## What this pass covers

**`std.mem.findPos`** (`indexOfPos`) — unified forward search from `start_index`. Delegates to `findScalarPos`, `findPosLinear`, or Boyer-Moore-Horspool; this pass adds cold-wrapper postconditions where the wrapper returns directly.

## Rye std surface

**`std.mem.findPos`**

```zig
pub fn findPos(comptime T: type, haystack: []const T, start_index: usize, needle: []const T) ?usize
```

## Width notes

**`std.mem.findPos`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `findPos` — inherited `usize` seam; assertions only | done |
| `rye/tests/find_pos_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9971_find_pos.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9971 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.findPos` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

- Empty needle: `assert(start_index <= haystack.len)`
- Single-char needle via `findScalarPos`: `assert(i + needle.len <= haystack.len)`
- BMH match: `assert(result + needle.len <= haystack.len)`
- `findPosLinear` path: already strengthened (9973)

## What the test asserts

- Multi-byte match from zero and from offset
- Single-char from offset
- Not found
- Empty needle at start
- Long haystack exercises BMH path (len ≥ 52, needle len > 4)
