# Pass 9940 · allEqual — every element matches the scalar

**Witnesses:** 63 programs (grew from 62)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.195612`

## What this pass covers

**`std.mem.allEqual`** — tests whether every element in a slice equals a scalar. Complements `eql` (9941) and `count` (9951).

## Rye std surface

**`std.mem.allEqual`**

```zig
pub fn allEqual(comptime T: type, slice: []const T, scalar: T) bool
```

## Width notes

**`std.mem.allEqual`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

- `false` ⇒ found element differs from scalar
- `true` ⇒ every element equals scalar (vacuous when empty)

## What the test asserts

- Uniform run, mixed run, empty slice
- Single-element match and mismatch
- Whitespace uniformity
