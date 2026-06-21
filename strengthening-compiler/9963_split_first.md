# Pass 9963 · SplitIterator.first — opening field stays within the buffer

**Corpus:** 40 programs (grew from 39)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.172012`

## What this pass covers

**`SplitIterator.first`** (via `splitScalar`, `splitAny`, `splitSequence`) — returns the first field and advances. Completes the split iterator quartet beside `next` (9993), `peek` (9969), and `rest` (9968).

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

After `next()` yields the first field:

```zig
assert(start <= self.buffer.len);
assert(field.len <= self.buffer.len);
assert(start + field.len <= self.buffer.len);
```

Index-based only — `SemanticVersion.parse` calls `first()` at comptime; pointer checks are runtime-only.

## What the test asserts

- Scalar, any, and sequence delimiters
- Leading delimiter yields empty first field
- Single field with no delimiter consumes whole buffer
