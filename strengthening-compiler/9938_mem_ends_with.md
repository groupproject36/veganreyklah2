# Pass 9938 · endsWith — suffix verdict agrees with eql

**Witnesses:** 65 programs (grew from 64)
**Gate:** GREEN — parity confirmed
**Stamp:** `20260620.201912`

## What this pass covers

**`std.mem.endsWith`** — suffix test on slices. The `rye` CLI checks `.rye` suffixes; pairs with `startsWith` (9939) on the Aurora metal lane (`995`).

## Postconditions

- `false` when `needle.len > haystack.len` ⇒ length ordering stated
- `true` ⇒ `needle.len <= haystack.len`
- `false` otherwise ⇒ empty needle or suffix `eql` fails

## What the test asserts

- Normal suffix match and mismatch
- Empty needle (always true)
- Needle longer than haystack
- Equal-length exact match
