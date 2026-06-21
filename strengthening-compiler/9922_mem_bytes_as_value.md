# Pass 9922 · mem.bytesAsValue — byte buffer aliases at least one T

**Witnesses:** 81 programs (grew from 80)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.023612`

## What this pass covers

**`std.mem.bytesAsValue`** — reinterprets bytes as a pointer to `T`, preserving pointer attributes. Pairs with `asBytes` (9925), `toBytes` (9923), and `bytesToValue`.

## Rye std surface

**`std.mem.bytesAsValue`**

```zig
pub fn bytesAsValue(comptime T: type, bytes: anytype) BytesAsValueReturnType(T, @TypeOf(bytes))
```

## Width notes

**`std.mem.bytesAsValue`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `bytesAsValue` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_bytes_as_value_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9922_mem_bytes_as_value.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9922 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.bytesAsValue` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

Slice inputs satisfy `bytes.len >= @sizeOf(T)`; one-item pointers satisfy `@sizeOf(child) >= @sizeOf(T)`.

## What the test asserts

- `u32` round-trip through `asBytes` → `bytesAsValue`
- Two-byte struct round-trip
