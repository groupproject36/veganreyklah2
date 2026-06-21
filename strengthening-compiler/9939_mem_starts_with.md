# Pass 9939 · startsWith — prefix verdict agrees with eql

**Witnesses:** 64 programs (grew from 63)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.200012`

## What this pass covers

**`std.mem.startsWith`** — prefix test on slices. The `rye` CLI and Mantra weave logic depend on it; builds on the `maybe` documentation from 9993 with return-path postconditions pairing `eql` (9941).

## Rye std surface

**`std.mem.startsWith`**

```zig
pub fn startsWith(comptime T: type, haystack: []const T, needle: []const T) bool
```

## Width notes

**`std.mem.startsWith`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `startsWith` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/mem_starts_with_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9939_mem_starts_with.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9939 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.startsWith` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

- `false` when `needle.len > haystack.len` ⇒ length ordering stated
- `true` ⇒ `needle.len <= haystack.len`
- `false` otherwise ⇒ empty needle or prefix `eql` fails

## What the test asserts

- Normal prefix match and mismatch
- Empty needle (always true)
- Needle longer than haystack
- Equal-length exact match
