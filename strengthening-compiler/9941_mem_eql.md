# Pass 9941 · mem.eql — equality verdict agrees with length and difference

**Witnesses:** 62 programs (grew from 61)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.195412`

## What this pass covers

**`std.mem.eql`** — slice equality. Rishi compares names on every line; complements `findDiff` (9949) and `order` (9953). Builds on the `maybe` documentation from 9996 with return-path postconditions.

## Rye std surface

**`std.mem.eql`**

```zig
pub fn eql(comptime T: type, a: []const T, b: []const T) bool
```

## Width notes

**`std.mem.eql`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `eql` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_eql_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9941_mem_eql.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9941 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.eql` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

**Vector path (`eqlBytes`):**

- `true` ⇒ `a.len == b.len`
- `false` ⇒ `a.len != b.len` or `findDiff(a, b) != null`

**Scalar path:**

- `false` on length mismatch ⇒ `a.len != b.len`
- `true` on empty or shared pointer ⇒ `a.len == b.len`
- `false` on element mismatch ⇒ differing element at that index
- final `true` ⇒ `a.len == b.len`

## What the test asserts

- Equal and unequal strings, length mismatch, empty slices
- Shared-pointer self-compare
- Mid-string inequality on longer inputs (exercises vector path on u8)
