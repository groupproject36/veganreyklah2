# Pass 9965 · findNonePos and findNone — strspn search stays outside the set

**Corpus:** 38 programs (grew from 37)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.171112`

## What this pass covers

**`std.mem.findNonePos`** and **`std.mem.findNone`** — find the first scalar not in a set (`strspn`-like). Pairs with `findAnyPos` (9967).

## Rye std surface

**`std.mem.findNonePos`**

```zig
pub fn findNonePos(comptime T: type, slice: []const T, start_index: usize, values: []const T) ?usize
```

**`std.mem.findNone`**

```zig
pub fn findNone(comptime T: type, slice: []const T, values: []const T) ?usize
```

## Width notes

**`std.mem.findNonePos`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

**`std.mem.findNone`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `findNonePos` — inherited `usize` seam; assertions only | done |
| `rye/lib/std/mem.zig` | `findNone` — inherited `usize` seam; assertions only | done |
| `rye/tests/find_none_pos_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9965_find_none_pos.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9965 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.findNonePos` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)
- [x] `std.mem.findNone` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

**findNonePos** on match:

```zig
assert(i < slice.len);
assert(i >= start_index);
for (values) |v| assert(slice[i] != v);
```

**findNone** cold wrapper:

```zig
assert(i < slice.len);
for (values) |value| assert(slice[i] != value);
```

## What the test asserts

- First non-digit in mixed string
- Skip leading digits
- All-in-set returns null
- Absent set returns null
- Positional search past tail returns null
- Positional search from offset finds first outside set
