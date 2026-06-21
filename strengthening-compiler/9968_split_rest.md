# Pass 9968 · SplitIterator.rest — tail slice stays within the buffer

**Corpus:** 35 programs (grew from 34)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.165512`

## What this pass covers

**`SplitIterator.rest`** — returns the unprocessed tail without advancing. Mantra uses it after `next()` on tab-separated weave rows and newline-split lines.

## Rye std surface

**`std.mem.split`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.split`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postcondition

```zig
if (self.index) |idx| assert(idx <= self.buffer.len);
assert(start <= end);
```

## What the test asserts

- rest shrinks as fields are consumed
- rest is empty when iteration completes
- fresh iterator rest is the whole buffer
- Mantra-shaped tab field tail after first column
