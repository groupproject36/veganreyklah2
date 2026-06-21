# Pass 9918 · mem.rotate — left-rotate matches snapshot

**Witnesses:** 85 programs (grew from 84)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.030912`

## What this pass covers

**`std.mem.rotate`** — in-place left rotation via three `reverse` calls. Pairs with `mem.reverse` (9921) and `mem.swap` (9919).

## Rye std surface

**`std.mem.rotate`**

```zig
pub fn rotate(comptime T: type, items: []T, amount: usize) void
```

## Width notes

**`std.mem.rotate`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

Precondition: `amount <= items.len`. When `items.len <= 64` and `items.len > 0`, each index holds the original at `(j + amount) % len` (`eql(u8, asBytes(...))`).

## What the test asserts

- Five-element `i32` rotate by 2
- Four-element `u8` rotate by 1
- Rotate by 0 leaves order unchanged
