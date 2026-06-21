# Pass 9935 · SHA3 ShakeLike squeeze @memcpy — buffered slice bounds

**Witnesses:** 68 programs (grew from 67)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.204212`

## What this pass covers

**`ShakeLike.squeeze` in `sha3.zig`** — slice bounds on the rate-sized buffer between sponge squeezes. Sits above `keccak_p` (`9936`) on every SHAKE/XOF call.

## Rye std surface

**`std.crypto.sha3`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.crypto.sha3`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/crypto/sha3.zig` | `sha3` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/sha3_shake_buffered_memcpy_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9935_sha3_shake_buffered_memcpy.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9935 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.crypto.sha3` — [`rye/lib/std/crypto/sha3.zig`](../rye/lib/std/crypto/sha3.zig)

## Postconditions

- `self.offset <= self.buf.len` on entry and via `defer` on every return path
- Before each `@memcpy`: copy length fits destination; partial drain keeps `self.offset + n <= self.buf.len`
- Tail copy: `out.len <= self.buf.len` before copying from the freshly squeezed block

## What the test asserts

- Split `update` + multi-call `squeeze` matches one-shot `Shake128.hash` for the first 100 bytes
