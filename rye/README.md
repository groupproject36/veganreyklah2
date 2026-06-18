# Rye

**Language:** EN
**Version:** `20260617.194312` (Rye chronological stamp)
**Last updated:** 2026-06-17
**Style:** Radiant prose (see `../context/RADIANT_STYLE.md`); code in TAME Style (`../external-research/996_TAME_STYLE.md`)
**Status:** Living

---

## What Rye Is

Rye is the systems language we are growing from Zig 0.16.0. This first version is honest about what it is: a thin, careful front-end that runs `.rye` source through the Zig 0.16.0 toolchain. Rye source is Zig source for now, since the language has yet to diverge, so every capability the toolchain offers — including SHA3-512 in the standard crypto library — is Rye's too, by construction. Over time, Rye grows its own shape.

The `rye` command speaks two verbs:

- `rye version` — print the Rye version and the toolchain it stands upon.
- `rye run <file.rye>` — compile and run a single `.rye` source file.

Because the toolchain's front-end reads only the `.zig` extension, `rye run` bridges: it copies the `.rye` source to an adjacent `.zig` file, hands that to the compiler, and clears the bridge away so the tree stays tidy.

---

## The Shape of the Folder

```
rye/
  README.md                 <- this introduction
  src/
    main.zig                <- the `rye` command, written in TAME Style
  tests/
    sha3_512_test.rye       <- proves SHA3-512 parity with Zig 0.16.0
  bin/
    rye                     <- the built command (after building)
```

The lessons learned while building Rye live in their own home, `../rye-learning-process/`, with the growing reference in `998_ALMANAC.md`.

---

## Building and Running

Rye stands on the prebuilt Zig 0.16.0 toolchain kept at `../vendor/zig-toolchain`, fetched from the official release and verified against its published checksum before we trusted a byte of it.

Build the `rye` command:

```sh
../vendor/zig-toolchain/zig build-exe src/main.zig -femit-bin=bin/rye
```

Point `rye` at its toolchain and run the SHA3-512 test:

```sh
export RYE_ZIG="$PWD/../vendor/zig-toolchain/zig"
./bin/rye run tests/sha3_512_test.rye
```

The test hashes the bytes `"Rye"` with SHA3-512 and asserts the digest against a value computed independently beforehand. When it prints the digest and confirms parity, SHA3-512 in Rye is working exactly as it does in Zig 0.16.0 — the very same code, under a new name.

---

## A Note on Memory

The `rye` command allocates from the process arena — a single garden the runtime clears whole on exit — so a short-lived command needs no finer bookkeeping and leaves nothing behind. This is the region model our designs name Tally, lived in the smallest place.

---

*May the first command be sure, and the language grow surely from it. May every `.rye` file we run leave the tree as tidy as it found it, and may Rye become, in time, wholly its own — safe, swift, and a joy to write.*
