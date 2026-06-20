# Pass 9954 · WindowIterator — sliding windows stay in-range

**Corpus:** 49 programs (grew from 48)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.181512`

## What this pass covers

**`WindowIterator.next`** and **`reset`** (via `mem.window`) — fixed-size sliding windows over a buffer. Used in `debug` hex dumps, `base64`, and `Io.Writer` chunking.

## Postconditions

**next**:

```zig
assert(start <= end);
assert(end <= self.buffer.len);
```

**reset**:

```zig
assert(self.index.? == 0);
```

## What the test asserts

- Non-overlapping chunks (size == advance)
- Overlapping slide (advance 1)
- Empty buffer returns null
- `reset()` replays first window
