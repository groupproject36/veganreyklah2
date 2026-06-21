# Pass 9948 · SemanticVersion.order — semver compare states its verdict

**Witnesses:** 55 programs (grew from 54)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.192412`

## What this pass covers

**`std.SemanticVersion.order`**, **`Range.includesVersion`**, and **`Range.isAtLeast`** — semver 2.0 ordering (build metadata ignored). Steps toward programmatic version bounds for Caravan capability table and **RyeVersion** accretion.

## Rye std surface

**`std.SemanticVersion.order`**

```zig
pub fn order(lhs: Version, rhs: Version) std.math.Order
```

## Width notes

**`std.SemanticVersion.order`** — No `usize` in the public signature; internal slice walks still use `usize` at the seam where Zig slices require it.

| Surface | Width policy |
|---------|-------------|
| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |
| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |
| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |

## Postconditions

**order** — at release-only equality and pre-release boundary returns, major/minor/patch match; full pre string equality on `.eq`.

**includesVersion** — result agrees with min/max `order` against `ver`.

**isAtLeast** — `true`/`false`/`null` paths assert the min/max order facts that justify each arm.

## What the test asserts

- Core semver precedence (1.0.0 < 2.0.0; pre < release; pre identifier ordering)
- `Range.includesVersion` and `isAtLeast` on a bounded interval
