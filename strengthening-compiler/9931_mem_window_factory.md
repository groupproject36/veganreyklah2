# Pass 9931 · mem.window factory — sliding window starts at buffer front

**Witnesses:** 72 programs (grew from 71)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.212412`

## What this pass covers

**`mem.window`** — factory postconditions beside strengthened `WindowIterator` (`9954`) and sibling factories (`9932`–`9934`).

## Postconditions

On return from `window`:

- `size != 0` and `advance != 0` (precondition, unchanged)
- Non-empty buffer: `index == 0` and `index <= buffer.len`
- Empty buffer: `index == null`
- `size` and `advance` match arguments

## What the test asserts

- Chunk and slide modes yield expected first windows at creation
- Empty buffer yields null immediately
- Window larger than buffer returns the whole buffer once
