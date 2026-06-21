# Pass 9920 · mem.reverseIterator — cursor starts at end, walks in range

**Witnesses:** 83 programs (grew from 82)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.024512`

## What this pass covers

**`mem.reverseIterator`** and **`ReverseIterator.next` / `nextPtr`** — factory and backward iteration. Pairs with `mem.reverse` (9921).

## Rye std surface

**`std.mem.reverse_iterator`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.reverse_iterator`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

Factory: `index == len == slice.len`. Each `next` / `nextPtr`: after decrement, `index < len`.

## What the test asserts

- String literal yields `c`, `b`, `a`, then null
- Array pointer `nextPtr` walks `7`, `3`, then null
