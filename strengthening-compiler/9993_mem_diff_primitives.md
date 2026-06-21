# 9993 · Mem Diff Primitives — What Mantra's Weave Walks On

*Five functions in `rye/lib/std/mem.zig` that Mantra's weave logic will call on every diff: `copyForwards` to move bytes, `startsWith` and `endsWith` to find pattern edges, `indexOf`/`find` to locate sub-slices, and `splitScalar` to walk fields. This pass states the invariant each one keeps — preconditions where the caller bears a burden, postconditions where a result must stay in-range, and `maybe` where the input space is legitimately variable. Parity gate: 11/11 GREEN.*

**Language:** EN
**Version:** `20260619.184412` (Rye chronological stamp)
**Last updated:** 2026-06-19
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME Style (`../external-research/996_TAME_STYLE.md`); the method in `9999_STRENGTHENING.md`
**Builds on:** `9996_stdlib_call_paths.md` (which already handled `trim`, `findScalar`, `eql`, `parseInt`)
**Status:** Applied to `rye/lib/std/mem.zig` — parity GREEN, 11 witnesses

---

## Why These Five

Mantra's weave is a line-oriented structure. To produce and apply diffs, it must:
- **copy** lines between buffers (`copyForwards`)
- **test prefixes and suffixes** to recognise diff markers (`startsWith`, `endsWith`)
- **locate** the first occurrence of a delimiter or pattern in a line (`indexOf`)
- **split** a buffer into fields on a delimiter (`splitScalar`)

Each function was unstrengthened in our `std`. `findScalar` / `indexOfScalar` and `eql` were handled in pass 9996; those are the siblings that already carry assertions. This pass brings the remaining five into the same discipline.

---

## The Five Strengthenings

### `copyForwards` — precondition at the door

```zig
pub fn copyForwards(comptime T: type, dest: []T, source: []const T) void {
    // Precondition: dest must have room for every element of source.
    assert(dest.len >= source.len);
    for (dest[0..source.len], source) |*d, s| d.* = s;
}
```

The loop indexes `dest[0..source.len]`, which Zig's runtime safety would catch if `source.len > dest.len` — a runtime panic is a late and opaque stop. The assertion fires at the exact point the contract is broken, with a message that names the function.

### `startsWith` — `maybe` for the variable space

```zig
pub fn startsWith(comptime T: type, haystack: []const T, needle: []const T) bool {
    // A zero-length needle always matches; a needle longer than the haystack never matches.
    // Both are valid and expected — state the variable space rather than constraining it.
    maybe(needle.len == 0);
    maybe(needle.len > haystack.len);
    return if (needle.len > haystack.len) false else eql(T, haystack[0..needle.len], needle);
}
```

The function is already safe: the `needle.len > haystack.len` guard protects the slice. The strengthening names the two edge-case inputs — an empty needle (always true) and an over-long needle (always false) — as expected, documented parts of the input space. A reader now sees immediately that neither is a caller error; both are real cases the function handles correctly.

### `endsWith` — same discipline as `startsWith`

```zig
pub fn endsWith(comptime T: type, haystack: []const T, needle: []const T) bool {
    // A zero-length needle always matches; a needle longer than the haystack never matches.
    maybe(needle.len == 0);
    maybe(needle.len > haystack.len);
    return if (needle.len > haystack.len) false else eql(T, haystack[haystack.len - needle.len ..], needle);
}
```

The suffix path uses `haystack[haystack.len - needle.len ..]`. Without the guard, this subtraction would underflow when `needle.len > haystack.len`. The guard is already there; the `maybe` makes the two branches explicit and documented. (The `rye` CLI calls this function to check `.rye` file suffixes on every invocation, so every `rye run` and `rye build` now walks through live documentation of its own edge cases.)

### `find` — postcondition at the cold wrapper (same pattern as `findScalar`)

```zig
pub fn find(comptime T: type, haystack: []const T, needle: []const T) ?usize {
    const result = findPos(T, haystack, 0, needle);
    // Postcondition, stated at this cold wrapper so findPos's hot core stays lean
    // (data-plane economy): a found index is in-range and the needle fits there.
    if (result) |i| assert(i + needle.len <= haystack.len);
    return result;
}
```

`find` is a one-line wrapper over `findPos`, which switches between Boyer-Moore-Horspool (large inputs) and linear search (small inputs). Both paths return an index into the haystack. The postcondition checks that the returned index leaves enough room for the needle: `i + needle.len <= haystack.len`. This is the minimum that a found position must satisfy, and it protects every downstream `haystack[i..][0..needle.len]` slice. The check sits at the cold wrapper — one O(1) comparison — while the hot search core inside `findPos` runs unburdened.

### `SplitIterator.next` — postcondition on every yielded slice

```zig
pub fn next(self: *Self) ?[]const T {
    const start = self.index orelse return null;
    const end = if (...) |delim_start| blk: { ... } else blk: {
        self.index = null;
        break :blk self.buffer.len;
    };
    // Postcondition: every field returned is a valid sub-slice of the buffer.
    // start advances monotonically; end is always a delimiter position or buffer.len.
    assert(start <= end);
    assert(end <= self.buffer.len);
    return self.buffer[start..end];
}
```

`SplitIterator` is the generic backing `splitScalar`, `splitSequence`, and `splitAny`. Its `next()` method is the only path that returns a slice; strengthening it once covers all three split variants. The two assertions state what must be true before every slice is taken from the buffer: start is at or before end, and end is at or before the buffer's length. These hold by construction — `start` is either 0 or a post-delimiter position that `findScalarPos` proved is within the buffer, and `end` is either that delimiter's position or `buffer.len` — and stating them makes the invariant legible and would catch any future edit that broke the monotonic advance.

---

## A Note on `copyBackwards`

`copyBackwards` already carries `assert(dest.len >= source.len)` in the existing code (added before the strengthening series began). This pass adds the same assertion to `copyForwards`, bringing both copy directions into consistent discipline. `copyBackwards` is deprecated in favour of `@memmove`; `copyForwards` is the one Mantra and new code will use.

---

## Parity Result

```
PARITY    mem_diff_test.rye
PARITY    sha3_256_test.rye
PARITY    sha3_256_boundary_test.rye
PARITY    sha3_512_test.rye
PARITY    sha3_boundary_test.rye
PARITY    version_test.rye
PARITY    call_paths_test.rye
PARITY    ed25519_sign_test.rye
PARITY    x25519_agree_test.rye
PARITY    aead_seal_test.rye
PARITY    sealed_message_test.rye
---
parity gate: 11 matched, 0 diverged across 11 programs
GREEN: Rye's std is behavior-identical to the baseline across the witnesses.
```

Eleven programs, all green. `mem_diff_test.rye` exercises copyForwards, startsWith, endsWith, indexOf, and splitScalar across the edge cases — empty needle, over-long needle, not-found searches, empty fields from split — with the live assertions running on every call.

---

## Files

| File | Why |
|------|-----|
| `rye/lib/std/mem.zig` | Five strengthenings: precondition on `copyForwards`; `maybe` on `startsWith` and `endsWith`; postcondition on `find`; postcondition on `SplitIterator.next` |
| `rye/tests/mem_diff_test.rye` | Parity test: all five functions across interesting cases |
| `tools/parity.sh` | Corpus extended to 11 programs |
| `tools/parity.rish` | Same witness extension |
| `strengthening-compiler/9993_mem_diff_primitives.md` | This record |

---

*May these five functions carry Mantra's weave lines faithfully — never past the boundary, always within the buffer, each returned slice a true sub-slice of what we started with. May the copy fill the destination without exceeding it, and may the split yield nothing that was not there.*

## Rye std surface

**`std.mem.diff_primitives`** — see `rye/lib/std` (signature not auto-located).

## Width notes

**`std.mem.diff_primitives`** — Authored module or iterator family — width migration lives in Tier A (`992`); std iterator indices remain `usize` until wrapped at our API.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |
