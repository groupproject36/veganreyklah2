# Pass 9967 · findAnyPos and findAny — any-delimiter search stays in-range

**Corpus:** 36 programs (grew from 35)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.165812`

## What this pass covers

**`std.mem.findAnyPos`** and **`std.mem.findAny`** — search for any of a set of scalar delimiters. Backs `splitAny` inside `SplitIterator`; pairs with `findScalarPos` (9974).

## Rye std surface

**`std.mem.findAnyPos`**

```zig
pub fn findAnyPos(comptime T: type, slice: []const T, start_index: usize, values: []const T) ?usize
```

**`std.mem.findAny`**

```zig
pub fn findAny(comptime T: type, slice: []const T, values: []const T) ?usize
```

## Width notes

**`std.mem.findAnyPos`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

**`std.mem.findAny`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `findAnyPos` — inherited `usize` seam; assertions only | done |
| `rye/lib/std/mem.zig` | `findAny` — inherited `usize` seam; assertions only | done |
| `rye/tests/find_any_pos_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9967_find_any_pos.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9967 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.findAnyPos` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)
- [x] `std.mem.findAny` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

**findAnyPos** on match:

```zig
assert(i < slice.len);
assert(slice[i] == value);
assert(i >= start_index);
```

**findAny** cold wrapper:

```zig
assert(i < slice.len);
assert(slice[i] matches one of values);
```

## What the test asserts

- First delimiter from zero
- Next delimiter from offset
- Past end returns null
- Whitespace set for trim-adjacent scans
- findAny from start finds vowel
- findAny absent set returns null
