# Pass 9951 · mem.count — non-overlapping needle tally stays in bounds

**Witnesses:** 52 programs (grew from 51)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.184712`

## What this pass covers

**`std.mem.count`** and **`countScalar`** — tally non-overlapping needle occurrences (or scalar elements). Complements `findPos` (9971) and `contains` patterns in string builtins.

## Rye std surface

**`std.mem.count`**

```zig
pub fn count(comptime T: type, haystack: []const T, needle: []const T) usize
```

## Width notes

**`std.mem.count`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

**count** — each match and final state:

```zig
assert(idx >= i);
assert(idx + needle.len <= haystack.len);
assert(i <= haystack.len);
assert(found <= haystack.len);
```

**countScalar**:

```zig
assert(found <= list.len);
```

## What the test asserts

- Empty haystack, single and double scalar hits
- Multi-byte needle non-overlap (`foo`, `ff`, `abc`)
- `countScalar` on spaced `abc` string
