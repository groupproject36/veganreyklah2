# Pass 9952 · orderZ — NUL-terminated compare agrees with slice order

**Witnesses:** 51 programs (grew from 50)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.184412`

## What this pass covers

**`std.mem.orderZ`**, **`boundedOrderZ`**, and **`findSentinel`** — C-string lexicographic compare and sentinel search. Pairs with `mem.order` (9953).

## Rye std surface

**`std.mem.orderZ`**

```zig
pub fn orderZ(comptime T: type, lhs: [*:0]const T, rhs: [*:0]const T) math.Order
```

## Width notes

**`std.mem.orderZ`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `orderZ` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_order_z_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9952_mem_order_z.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9952 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.orderZ` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

**orderZ**:

```zig
assert(result == order(T, lhs[0..lhs_len], rhs[0..rhs_len]));
```

**boundedOrderZ** — equal-through-bound path:

```zig
assert(i <= bound);
```

**findSentinel**:

```zig
assert(p[i] == sentinel);
```

## What the test asserts

- `orderZ` less, equal, greater; shared pointer self-compare
- `findSentinel` on `"hello"` and `""`
- `boundedOrderZ` respects compare bound
