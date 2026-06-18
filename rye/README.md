# Rye

**Language:** EN
**Version:** `20260618.043012` (Rye chronological stamp)
**Last updated:** 2026-06-18
**Style:** Radiant prose (see `../context/RADIANT_STYLE.md`); code in TAME Style (`../external-research/996_TAME_STYLE.md`)
**Status:** Living

---

## What Rye Is

Rye is the systems language we are growing from Zig 0.16.0. This first version is honest about what it is: a careful front-end that runs `.rye` source through the Zig 0.16.0 toolchain, on a standard library that is now Rye's own. A `.rye` file is Zig source at heart for now, so every capability the toolchain offers — including SHA3-512 in the standard crypto library — is Rye's too, by construction. But Rye has begun to diverge: it carries its own copy of the standard library, and it counts its versions in its own way. Over time, it grows further into its own shape.

The `rye` command speaks two verbs:

- `rye version` — print Rye's chronological version and the backend it stands upon.
- `rye run <file.rye>` — compile and run a single `.rye` source file, against Rye's own standard library.

Because the toolchain's front-end reads only the `.zig` extension, `rye run` bridges: it copies the `.rye` source to an adjacent `.zig` file, hands that to the compiler — pointed at Rye's standard library — and clears the bridge away so the tree stays tidy.

---

## The Shape of the Folder

```
rye/
  README.md                 <- this introduction
  lib/                      <- Rye's library directory (passed via --zig-lib-dir)
    std/                    <- our std: a copy of Zig 0.16.0's, under our care
    (others)                <- relative symlinks back to the pinned toolchain
  src/
    main.zig                <- the `rye` command, written in TAME Style
  tests/
    sha3_512_test.rye       <- proves SHA3-512 parity with Zig 0.16.0
    version_test.rye        <- shows the backend version via builtin.zig_version
  bin/
    rye                     <- the built command (after building)
```

The lessons learned while building Rye live in their own home, `../rye-learning-process/`, with the growing reference in `998_ALMANAC.md`.

---

## Owning the Standard Library

A language is not wholly its own until it owns its standard library. Rye does. The folder `lib/` is Rye's library directory: its `std/` began as a **bit-for-bit copy of Zig 0.16.0's** standard library, now under our care to tend and grow; the rest of the directory links back to the pinned toolchain, unchanged. The `rye` command points the compiler at this library with `--zig-lib-dir`, so `@import("std")` in a `.rye` program means *Rye's* std.

The command **insists** on it. Before compiling, it confirms our library sits at the expected path and refuses to run against anything else, so a successful `rye run` is, by construction, a run against Rye's own standard library. The assurance lives in the path, not in any marker written into the code — which lets `std` stay a faithful copy that we diverge from deliberately, a clean diff at a time.

---

## How Rye Counts Time

Rye's first deliberate divergence from Zig is the way it names its versions. Where Zig counts semantically (`0.16.0`), Rye counts **chronologically** — `YYYYMMDD.HHMMSS`, where later is always larger — so a version says *when*, and carries only the one semantic worth keeping. The first running, divergent version is `20260617.213112`.

Rye carries this all the way down. The backend keeps its own honest semantic version, reported live through `builtin.zig_version`; Rye also reads that same pinned snapshot on its own clock — Zig 0.16.0 was committed at `20260413.181917` UTC, so that is the backend's name in Rye's time. `rye version` prints both, side by side. The fuller reasoning lives in `../context/specs/rye-versioning-style.md`.

---

## Building and Running

Rye stands on the prebuilt Zig 0.16.0 toolchain kept at `../vendor/zig-toolchain`, fetched from the official release and verified against its published checksum before we trusted a byte of it.

Build the `rye` command — pointed at Rye's own standard library, so the command dogfoods the `std` it ships:

```sh
../vendor/zig-toolchain/zig build-exe src/main.zig -femit-bin=bin/rye --zig-lib-dir lib
```

Point `rye` at its backend and run the SHA3-512 test; the command finds `lib/` beside its own binary, so `.rye` programs compile against Rye's `std` automatically:

```sh
export RYE_ZIG="$PWD/../vendor/zig-toolchain/zig"
./bin/rye run tests/sha3_512_test.rye
```

The test hashes the bytes `"Rye"` with SHA3-512 and asserts the digest against a value computed independently beforehand. When it prints the digest and confirms parity, SHA3-512 in Rye is working exactly as it does in Zig 0.16.0 — the very same code, under a new name.

---

## A Note on Memory

The `rye` command allocates from the process arena — a single garden the runtime clears whole on exit — so a short-lived command needs no finer bookkeeping and leaves nothing behind. This is the region model our designs name Tally, lived in the smallest place.

---

## Rye's Garden

Rye is the language at the bottom of a wider ecosystem we are designing in the open: **Tally**, the garden allocator; **Caravan**, the supervisor-kernel; **Silo**, configuration; **Mantra**, version control; **Aurora**, boot; and **Pond** — a gentle, TAME-style reimplementation of the `ai-jail` sandbox we work inside, a bounded enclosure where an agent can build in safety. The explorations behind these names live in `../external-research/`, and the from-scratch setup that ties the tools together lives in `../SOURCE.md`.

---

*May the first command be sure, and the language grow surely from it. May every `.rye` file we run leave the tree as tidy as it found it, and may Rye become, in time, wholly its own — safe, swift, and a joy to write.*
