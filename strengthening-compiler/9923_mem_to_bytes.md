# Pass 9923 · mem.toBytes — byte array length matches value size

**Witnesses:** 80 programs (grew from 79)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.023112`

## What this pass covers

**`std.mem.toBytes`** — copies a value's underlying bytes into a fixed array. Pairs with `asBytes` (9925), `bytesToValue`, and the slice view family (9924–9926).

## Rye std surface

**`std.mem.toBytes`**

```zig
pub fn toBytes(value: anytype) [@sizeOf(@TypeOf(value))]u8
```

## Width notes

**`std.mem.toBytes`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `toBytes` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_to_bytes_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9923_mem_to_bytes.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9923 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.toBytes` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

Returned array length equals `@sizeOf(@TypeOf(value))`.

## What the test asserts

- `u32` yields four bytes matching `asBytes`
- Two-byte struct yields two bytes
