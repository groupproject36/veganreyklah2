# Pass 9971 · findPos — offset needle entry states the fit contract

**Corpus:** 32 programs (grew from 31)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.164312`

## What this pass covers

**`std.mem.findPos`** (`indexOfPos`) — unified forward search from `start_index`. Delegates to `findScalarPos`, `findPosLinear`, or Boyer-Moore-Horspool; this pass adds cold-wrapper postconditions where the wrapper returns directly.

## Postconditions

- Empty needle: `assert(start_index <= haystack.len)`
- Single-char needle via `findScalarPos`: `assert(i + needle.len <= haystack.len)`
- BMH match: `assert(result + needle.len <= haystack.len)`
- `findPosLinear` path: already strengthened (9973)

## What the test asserts

- Multi-byte match from zero and from offset
- Single-char from offset
- Not found
- Empty needle at start
- Long haystack exercises BMH path (len ≥ 52, needle len > 4)
