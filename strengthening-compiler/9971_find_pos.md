# Pass 9971 · findPos — offset needle entry states the fit contract

**Corpus:** 32 programs (grew from 31)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.164312`

## What this pass covers

**`std.mem.findPos`** (`indexOfPos`) — unified forward search from `start_index`. Delegates to `findScalarPos`, `findPosLinear`, or Boyer-Moore-Horspool; this pass adds cold-wrapper postconditions where the wrapper returns directly.

## Rye std surface

Live implementation from `rye/lib/std` (strengthened):

**`std..mem.findPos`**

```zig
pub fn findPos(comptime T: type, haystack: []const T, start_index: usize, needle: []const T) ?usize {
    if (needle.len > haystack.len) return null;
    if (needle.len < 2) {
        if (needle.len == 0) {
            assert(start_index <= haystack.len);
            return start_index;
        }
        // findScalarPos is significantly faster than findPosLinear
        const scalar = findScalarPos(T, haystack, start_index, needle[0]);
        if (scalar) |i| assert(i + needle.len <= haystack.len);
        return scalar;
    }

    if (!std.meta.hasUniqueRepresentation(T) or haystack.len < 52 or needle.len <= 4)
        return findPosLinear(T, haystack, start_index, needle);

    const haystack_bytes = sliceAsBytes(haystack);
    const needle_bytes = sliceAsBytes(needle);

    var skip_table: [256]usize = undefined;
    boyerMooreHorspoolPreprocess(needle_bytes, skip_table[0..]);

    var i: usize = start_index * @sizeOf(T);
    while (i <= haystack_bytes.len - needle_bytes.len) {
        if (i % @sizeOf(T) == 0 and mem.eql(u8, haystack_bytes[i .. i + needle_bytes.len], needle_bytes)) {
            const result = @divExact(i, @sizeOf(T));
            // Postcondition at cold wrapper: a found index fits the needle (data-plane economy).
            assert(result + needle.len <= haystack.len);
            return result;
        }
        i += skip_table[haystack_bytes[i + needle_bytes.len - 1]];
    }

    return null;
}
```

## Width notes

**`std.mem.findPos`** — Public signature inherits Zig `usize` for slice lengths and indices — keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` only for named bounds inside the body (`max_*_check`, loop counters) with `assert` before `@intCast`.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |





## usize explicit audit

Tiger Style: *use explicitly-sized types like `u32`; avoid architecture-specific `usize`* ([`gratitude/TIGER_STYLE.md`](../gratitude/TIGER_STYLE.md) § Safety).

TAME: **`usize` is a boundary type, not a design type** — [`context/TAME_STYLE.md`](../context/TAME_STYLE.md), [`10024`](../expanding-prompts/10024_explicit_width_audit.md), [`992`](../work-in-progress/992_usize_width_baseline.md).

Lexicon ✅ requires every row **`done`** and zero **`fail`** rows.
### `std..mem.findPos`

| Check | Type | Tiger/TAME policy | Status |
|-------|------|-------------------|--------|
| slice params / `.len` | inherited `usize` (Tier C) | Tiger: avoid `usize` in APIs we publish — this surface is inherited Zig `std`; unchanged per `10024` rule 3 | done |
| Tier | C — inherited `std` | `992` Phase 4 — touch named bounds only; do not rename public seam | done |

### Witness `rye/tests/find_pos_test.rye`

| Check | Type | Tiger/TAME policy | Status |
|-------|------|-------------------|--------|
| Tier | B — witness `.rye` | `992` — `usize` only at `buf[0..n]` slice edge | done |
| witness body | slice edge only | Stack buffers + `.len` at seam — no authored `usize` fields | done |


## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `misc` | `findPos` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/find_pos_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9971_find_pos.md` | pass record + audited surfaces | done |
| `## usize explicit audit` | per-surface locus table — gates lexicon ✅ | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9971 | done |

## Audited surfaces

Checkmark requires **`## usize explicit audit`** all `done`, zero `fail` (Tiger/TAME — [`992`](../work-in-progress/992_usize_width_baseline.md)). Full implementation from `rye/lib/std`:
- [x] `std..mem.findPos` — [`misc`](../misc)

```zig
pub fn findPos(comptime T: type, haystack: []const T, start_index: usize, needle: []const T) ?usize {
    if (needle.len > haystack.len) return null;
    if (needle.len < 2) {
        if (needle.len == 0) {
            assert(start_index <= haystack.len);
            return start_index;
        }
        // findScalarPos is significantly faster than findPosLinear
        const scalar = findScalarPos(T, haystack, start_index, needle[0]);
        if (scalar) |i| assert(i + needle.len <= haystack.len);
        return scalar;
    }

    if (!std.meta.hasUniqueRepresentation(T) or haystack.len < 52 or needle.len <= 4)
        return findPosLinear(T, haystack, start_index, needle);

    const haystack_bytes = sliceAsBytes(haystack);
    const needle_bytes = sliceAsBytes(needle);

    var skip_table: [256]usize = undefined;
    boyerMooreHorspoolPreprocess(needle_bytes, skip_table[0..]);

    var i: usize = start_index * @sizeOf(T);
    while (i <= haystack_bytes.len - needle_bytes.len) {
        if (i % @sizeOf(T) == 0 and mem.eql(u8, haystack_bytes[i .. i + needle_bytes.len], needle_bytes)) {
            const result = @divExact(i, @sizeOf(T));
            // Postcondition at cold wrapper: a found index fits the needle (data-plane economy).
            assert(result + needle.len <= haystack.len);
            return result;
        }
        i += skip_table[haystack_bytes[i + needle_bytes.len - 1]];
    }

    return null;
}
```

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
