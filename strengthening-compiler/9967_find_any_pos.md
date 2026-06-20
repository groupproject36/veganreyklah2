# Pass 9967 · findAnyPos and findAny — any-delimiter search stays in-range

**Corpus:** 36 programs (grew from 35)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.165812`

## What this pass covers

**`std.mem.findAnyPos`** and **`std.mem.findAny`** — search for any of a set of scalar delimiters. Backs `splitAny` inside `SplitIterator`; pairs with `findScalarPos` (9974).

## Postconditions

**findAnyPos** on match:

```zig
assert(i < slice.len);
assert(slice[i] == value);
assert(i >= start_index);
```

**findAny** cold wrapper:

```zig
assert(i < slice.len);
assert(slice[i] matches one of values);
```

## What the test asserts

- First delimiter from zero
- Next delimiter from offset
- Past end returns null
- Whitespace set for trim-adjacent scans
- findAny from start finds vowel
- findAny absent set returns null
