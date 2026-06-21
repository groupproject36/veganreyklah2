# Pass 9962 · SplitBackwardsIterator — backward split fields stay in-range

**Corpus:** 41 programs (grew from 40)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.172612`

## What this pass covers

**`SplitBackwardsIterator`** (`splitBackwardsScalar`, `splitBackwardsAny`, `splitBackwardsSequence`) — `next`, `first`, and `rest`. Mirrors forward `SplitIterator` strengthening (9993, 9963, 9968).

## Rye std surface

**`std.mem.split`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.split`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/mem.zig` | `split` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/split_backwards_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9962_split_backwards.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9962 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.mem.split` — [`rye/lib/std/mem.zig`](../rye/lib/std/mem.zig)

## Postconditions

**next** on every yielded field:

```zig
assert(start <= end);
assert(end <= self.buffer.len);
```

**first** after `next()`:

```zig
assert(field.len <= self.buffer.len);
assert(end <= self.buffer.len);
```

**rest**:

```zig
assert(end <= self.buffer.len);
```

Index-based only — comptime-safe like forward `first` (9963).

## What the test asserts

- Scalar backward walk with empty field (`||`)
- `rest()` tracks unprocessed prefix
- Any and sequence delimiters
- Single field with no delimiter
