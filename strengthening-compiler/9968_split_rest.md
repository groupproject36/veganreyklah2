# Pass 9968 · SplitIterator.rest — tail slice stays within the buffer

**Corpus:** 35 programs (grew from 34)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.165512`

## What this pass covers

**`SplitIterator.rest`** — returns the unprocessed tail without advancing. Mantra uses it after `next()` on tab-separated weave rows and newline-split lines.

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
