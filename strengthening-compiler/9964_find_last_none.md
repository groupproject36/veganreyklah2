# Pass 9964 · findLastNone — backward strspn search stays outside the set

**Corpus:** 39 programs (grew from 38)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.171512`

## What this pass covers

**`std.mem.findLastNone`** (`lastIndexOfNone`) — find the last scalar not in a set. Pairs with `findNonePos` (9965) and `findLastAny` (9966).

## Rye std surface

**`std.mem.findLastNone`**

```zig
pub fn findLastNone(comptime T: type, slice: []const T, values: []const T) ?usize
```

## Width notes

**`std.mem.findLastNone`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postcondition

On match:

```zig
assert(i < slice.len);
for (values) |v| assert(slice[i] != v);
```

## What the test asserts

- Last letter before trailing digits (upstream case)
- Last letter at end of digit prefix
- All-in-set returns null
- Last non-digit in mixed alphanumeric string
