# Aurora — the dawn a machine wakes into

**Version:** `20260618.194012` (Rye chronological stamp)
**Style:** Radiant prose (see `../context/RADIANT_STYLE.md`); code in TAME Style (`../external-research/996_TAME_STYLE.md`)
**Status:** First seed and first relay — small, runnable, and growing

---

## What Aurora Is

Aurora is the dawn a machine wakes into: the boot, the first light between a cold
processor and a living system. The fuller vision — RISC-V cohesion, a flow of
named values, content-addressed stages, owner keys — lives in
`../external-research/993_aurora_boot_riscv.md`, read forward through the rethink
in `../external-research/986_decided_design_aurora_mantra.md`. This folder holds
the part that already breathes.

## The First Seed

Following Gall's Law — a working complex system grows from a working simple one —
Aurora begins with the smallest boot that runs. In `src/seed.rye`, one hart wakes
on a freestanding RISC-V machine, gives itself a stack, speaks a single line over
the console, and asks the machine to rest. No operating system sits beneath it
and no standard library above it: only Rye's own toolchain, aimed at bare metal,
and an emulator to wake in.

It is also the step where Rye and Aurora meet. Rye's north star asks it to cohere
with open hardware (`../context/specs/rye-as-its-own-language.md`); a freestanding
RISC-V binary, built by Rye and run on a real emulator, is that coherence made
concrete — and the same artifact is Aurora's first living stage. One step, two
roots fed.

## The Second Stage — a Relay

The seed grows by one true step into the first *relay*. In `src/relay.rye`, the
boot becomes a flow of named values: stage one wakes and reads the machine's
identity, packing it into a small `Machine` value; stage two receives that value,
proves an invariant of it — the base integer ISA must be present, or this code
could not run — and speaks what it found; stage three rests. Each handoff is a
tail call, and a value travels with it: the boot-as-flow-of-named-values idea
(`../external-research/993_aurora_boot_riscv.md`, `/986`) at its smallest honest
size. It reads real registers (`mhartid`, `misa`), proves what it must, and hands
off — the shape every later stage will take.

## Build and Run

```sh
aurora/run.sh          # the seed (the default stage)
aurora/run.sh relay    # the second stage: the first relay
```

`run.sh` asks `rye build` to emit a freestanding RISC-V ELF for the chosen stage
— Rye building its own bare-metal artifact, against its own standard library —
and then wakes it on `qemu-system-riscv64 -machine virt`. The seed prints:

```
Aurora seed: a hart woke on RISC-V, spoke this line, and halted.
```

and the relay prints what it learned and proved along its three stages:

```
Aurora relay:
  stage 1 -> woke hart 0
  stage 2 -> proved RV with base integer + compressed
  stage 3 -> resting.
```

Both end with a clean exit (status 0), because the last stage writes the
machine's test finisher to power itself down. The script uses the vendored Zig
0.16.0 toolchain beside the project, so it needs no extra setup; an emulator
(`qemu-system-riscv64`) is the one thing it expects to find.

## The Shape of the Folder

```
aurora/
  README.md          <- this introduction
  src/
    seed.rye         <- the first seed: a hart wakes, speaks, and halts
    relay.rye        <- the second stage: a value flows across asserted stages
  layout.ld          <- where a stage lives in memory (RAM base, _start first)
  run.sh             <- build a stage with rye, wake it in qemu (default: seed)
  .build/            <- the emitted ELFs (built on demand, untracked)
```

## How It Grows

The seed is the simple system that works, and the relay is the first grown from
it, never bolted on. The near steps from here: a stage that hands the next a
value *it chose* — a real decision, not only a reading; then, as the other
modules ripen, Tally's bounded gardens for the boot's own memory, Caravan's hand
on what runs next, and Silo describing the stages as values rather than code.
Mantra will give each stage an enduring, content-addressed name, so a boot can
say exactly what it ran. The roadmap that holds these steps lives in
`../work-in-progress/996_roadmap.md`.

---

*May the first light be gentle and sure: a hart waking, a single true line
spoken, and a clean rest — the dawn the rest of the system grows into.*
