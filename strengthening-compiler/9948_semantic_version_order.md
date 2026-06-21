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

## Width audit (affected files)

| File | Audit | Status |
|------|-------|--------|
| `rye/lib/std/SemanticVersion.zig` | `order` — Phase 4 `usize` seam policy applied | done |
| `rye/tests/semantic_version_order_test.rye` | witness program | done |
| `tools/parity.rish` | witness registered | done |
| `strengthening-compiler/9948_semantic_version_order.md` | pass record + audited surfaces | done |
| `992_strengthening_width_crosswalk.md` | lexicon row 9948 | done |

## Audited surfaces

Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). Each surface this pass strengthens:

- [x] `std.SemanticVersion.order` — [`rye/lib/std/SemanticVersion.zig`](../rye/lib/std/SemanticVersion.zig)

## Postconditions

**order** — at release-only equality and pre-release boundary returns, major/minor/patch match; full pre string equality on `.eq`.

**includesVersion** — result agrees with min/max `order` against `ver`.

**isAtLeast** — `true`/`false`/`null` paths assert the min/max order facts that justify each arm.

## What the test asserts

- Core semver precedence (1.0.0 < 2.0.0; pre < release; pre identifier ordering)
- `Range.includesVersion` and `isAtLeast` on a bounded interval
