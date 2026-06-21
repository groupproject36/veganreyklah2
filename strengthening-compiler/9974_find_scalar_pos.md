# Pass 9974 · findScalarPos — offset search stays in-range from start_index

**Corpus:** 29 programs (grew from 28)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.163112`

## What this pass covers

**`std.mem.findScalarPos`** (`indexOfScalarPos`) — scalar search from a start offset. Rishi calls it on every interpolated string (`$`, `}`) and on `let` lines (`=`).

Postcondition lands on the **scalar tail loop** only — vectorized paths stay lean per data-plane economy (9996); the tail loop is where small inputs and remainder scans complete.

## Rye std surface

**`std.mem.findScalarPos`**

```zig
pub fn findScalarPos(comptime T: type, slice: []const T, start_index: usize, value: T) ?usize
```

## Width notes

**`std.mem.findScalarPos`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `findScalarPos` — inherited `usize` seam; assertions only | done |
| `rye/tests/find_scalar_pos_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9974_find_scalar_pos.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9974 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.findScalarPos` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postcondition

On match in the scalar tail:

```zig
assert(j < slice.len);
assert(slice[j] == value);
assert(j >= start_index);
```

## What the test asserts

- Search from zero finds first match
- Search from middle finds next match
- No match past last occurrence returns null
- start_index at len returns null
- Interpolation-shaped slice finds closing `}`
- `let` line finds `=`
