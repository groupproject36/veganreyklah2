# 9996 · Strengthening the Functions Our Tools Call

*The first two passes hardened the crypto core — SHA3-512 and the Keccak sponge beneath it. This one turns to the everyday: the standard-library functions the `rye` CLI and the Rishi shell call on every run. We traced our own call graph, found a small load-bearing cluster, and gave each function a stated invariant — without changing a single thing any of them returns.*

**Language:** EN
**Version:** `20260618.193812` (Rye chronological stamp)
**Last updated:** 2026-06-18
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME Style (`../external-research/996_TAME_STYLE.md`); the method in `9999_STRENGTHENING.md`

---

## Why These Functions

A strengthening compiler hardens the code we actually depend on, in the order we lean on it. So we followed the call graph of our own programs.

The `rye` CLI (`rye/src/main.rye`) compares command names with `std.mem.eql`, checks a file suffix with `std.mem.endsWith`, and finds a directory with `std.fs.path.dirname`. The Rishi shell (`rishi/src/main.rye`) does more on every line it runs: it trims whitespace with `std.mem.trim`, splits on a scalar, searches for `=`, `}`, and `$` with `std.mem.indexOfScalar` and `indexOfScalarPos`, compares names with `std.mem.eql`, and parses integers with `std.fmt.parseInt`.

That last cluster is the prize. It includes a clean example of the very thing this pass is named for — *functions that call other functions*: `indexOfScalar` and `indexOfScalarPos` are thin wrappers over `findScalarPos`, so strengthening the search means deciding **where** along that chain the invariant belongs.

## What We Strengthened

Four functions, each a different kind of TAME assertion, so the pass also reads as a small catalogue of the forms an invariant can take.

### `std.mem.trim` — a postcondition

`trim` walks two cursors inward from the ends and returns `slice[begin..end]`. The invariant that makes that slice valid is that the cursors close inward and never cross:

```
assert(begin <= end);
assert(end <= slice.len);
return slice[begin..end];
```

So the result is always a contiguous sub-slice of the input — never longer, never out of bounds. Rishi trims on nearly every line, around names, values, and statements.

### `std.mem.findScalar` — a postcondition, at the cold wrapper

`findScalar` (which `indexOfScalar` aliases) is a one-line wrapper over `findScalarPos`. We let it capture the result and state what a successful search must mean:

```
const result = findScalarPos(T, slice, 0, value);
if (result) |i| {
    assert(i < slice.len);
    assert(slice[i] == value);
}
return result;
```

A found index lands inside the slice and truly points at the value sought. We state this at the **cold wrapper**, deliberately, so the hot vectorized loop inside `findScalarPos` stays lean — the control-plane / data-plane economy we took from the TigerBeetle reading. The cheap, O(1) check rides the wrapper; the tight SIMD loop is left to run unburdened.

### `std.mem.eql` — a `maybe`, the dual of assert

`eql` answers a question rather than requiring an answer in advance: both equal and unequal lengths are expected inputs. So we name that variable space rather than constrain it:

```
maybe(a.len == b.len);
```

`maybe` is always true (`ok or !ok`) and compiles to nothing; it stands as living documentation that the length relationship here is free to vary. (We added `maybe` to `mem.zig`'s imports beside `assert`.)

### `std.fmt.parseInt` — a precondition

A base is either `0` (detect it from a `0x`/`0o`/`0b` prefix) or a true radix in 2…36. Anything else is the caller's mistake, so we name it at the door of `parseIntWithGenericCharacter`, where `parseInt` enters:

```
assert(base == 0 or (base >= 2 and base <= 36));
```

Rishi parses its integer literals with base 10, well inside the contract.

## The Discipline Held

Each change adds what the code *says*, never what it *does*. To prove it, a new witness program — `rye/tests/call_paths_test.rye` — exercises all four functions across found and not-found searches, equal and unequal comparisons, trims that strip everything, and several bases. The differential-parity gate (`tools/parity.sh`) runs it against the pristine baseline `std` and against our strengthened `std` and finds the output and exit code identical to the byte:

```
PARITY    call_paths_test.rye
GREEN: Rye's std is behavior-identical to the baseline across the witnesses.
```

And because `rye run` builds in Debug, the assertions are **live** every time we run Rishi — so each `.rish` script we run now actively checks these invariants as it goes, and would stop loudly, near the cause, if one were ever false.

## What We Left for Later, on Purpose

`indexOfScalarPos` is a *direct* alias to the hot `findScalarPos`, with no wrapper between. Giving it the same postcondition therefore means touching the hot core — which the data-plane economy asks us not to do lightly. That waits for a later pass dedicated to hot paths, behind a `verify` flag: checks too costly for the data plane, compiled in only when we ask for them. Naming the deferral is part of the honesty; we strengthened where it was cheap and clear, and we said plainly where we did not.

---

*May the small functions we lean on each day carry their invariants quietly and well. May every result stay within the bounds it promises, and may the gate stay green as our library grows a little more its own.*
