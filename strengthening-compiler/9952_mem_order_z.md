# Pass 9952 · orderZ — NUL-terminated compare agrees with slice order

**Witnesses:** 51 programs (grew from 50)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.184412`

## What this pass covers

**`std.mem.orderZ`**, **`boundedOrderZ`**, and **`findSentinel`** — C-string lexicographic compare and sentinel search. Pairs with `mem.order` (9953).

## Postconditions

**orderZ**:

```zig
assert(result == order(T, lhs[0..lhs_len], rhs[0..rhs_len]));
```

**boundedOrderZ** — equal-through-bound path:

```zig
assert(i <= bound);
```

**findSentinel**:

```zig
assert(p[i] == sentinel);
```

## What the test asserts

- `orderZ` less, equal, greater; shared pointer self-compare
- `findSentinel` on `"hello"` and `""`
- `boundedOrderZ` respects compare bound
