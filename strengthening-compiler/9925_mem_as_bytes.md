# Pass 9925 · mem.asBytes — byte view length matches value size

**Witnesses:** 78 programs (grew from 77)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.021112`

## What this pass covers

**`std.mem.asBytes`** — reinterprets a pointer to one value as its underlying bytes. Pairs with `sliceAsBytes` (9926).

## Rye std surface

**`std.mem.asBytes`**

```zig
pub fn asBytes(ptr: anytype) AsBytesReturnType(@TypeOf(ptr))
```

## Width notes

**`std.mem.asBytes`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `asBytes` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_as_bytes_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9925_mem_as_bytes.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9925 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.asBytes` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

Returned byte slice length equals `@sizeOf(@TypeOf(ptr.*))` (zero for zero-sized types).

## What the test asserts

- `u32` yields four bytes; zeroing bytes clears the word
- Zero-sized type yields zero bytes
- Packed two-byte struct yields two bytes
