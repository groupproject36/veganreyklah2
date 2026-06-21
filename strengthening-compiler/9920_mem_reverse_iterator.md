# Pass 9920 · mem.reverseIterator — cursor starts at end, walks in range

**Witnesses:** 83 programs (grew from 82)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260621.024512`

## What this pass covers

**`mem.reverseIterator`** and **`ReverseIterator.next` / `nextPtr`** — factory and backward iteration. Pairs with `mem.reverse` (9921).

## Postconditions

Factory: `index == len == slice.len`. Each `next` / `nextPtr`: after decrement, `index < len`.

## What the test asserts

- String literal yields `c`, `b`, `a`, then null
- Array pointer `nextPtr` walks `7`, `3`, then null
