# Gratitude

**Language:** EN
**Last updated:** 2026-06-18
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)

---

This folder holds the works we are grateful for — the writing and the code that shaped how we think and build here. We keep the originals close, whole and unaltered, both standalone texts and full source repositories, so we can return to the source whenever we want to hear it in the author's own voice.

When we adapt one of these works into Radiant Style, the rewrite lives elsewhere in the project. The version here stays exactly as its author wrote it, a quiet way of saying thank you.

---

## What Lives Here

- **`TIGER_STYLE.md`** — TigerBeetle's coding style guide. Safety, performance, and developer experience, woven into a discipline we admire. Our radiant adaptation lives at `../external-research/996_TAME_STYLE.md`, and the gratitude bridge that records its lineage lives at `../external-research/997_SYSTEM.md`.
  - Source: <https://raw.githubusercontent.com/tigerbeetle/tigerbeetle/refs/heads/main/docs/TIGER_STYLE.md>
- **`tigerbeetle/`** — TigerBeetle's full source, the financial database whose Tiger Style we adapted into TAME Style. We keep the code close to study how its principles live in practice, especially its assertions: the `maybe` dual of `assert`, the precondition blocks gathered at each function's door, and the control-plane / data-plane economy that decides when an expensive check earns a `verify` gate. Those three habits are folded into `../external-research/996_TAME_STYLE.md`, and the discipline of carrying such craft into Rye's own `std` is recorded in `../strengthening-compiler/9999_STRENGTHENING.md`. Cloned whole and unmodified (rev `59f2b99`), Apache-2.0.
  - Source: <https://github.com/tigerbeetle/tigerbeetle>
- **`Spec_ulation.md`** — Rich Hickey's 2016 talk on change, versioning, and the commitment to never take something away. It shapes how Rye names its versions, recorded in `../context/specs/rye-versioning-style.md`.
  - Source: <https://raw.githubusercontent.com/matthiasn/talk-transcripts/refs/heads/master/Hickey_Rich/Spec_ulation.md>
- **`LanguageSystem.md`** — Rich Hickey's 2012 talk on the language of the system: how systems are ensembles of programs that flow values to one another, with enduring names, simple services, and the systems failure model held as the normal case. It shapes how we think about boots, kernels, and networks, honored in `../external-research/997_SYSTEM.md` and voiced directly in `../external-research/993_aurora_boot_riscv.md`.
  - Source: <https://raw.githubusercontent.com/matthiasn/talk-transcripts/refs/heads/master/Hickey_Rich/LanguageSystem.md>
- **`sixos/`** — Adam Joseph's nixpkgs-based operating system that runs s6 in place of systemd. Its services-as-packages design and careful layering shape our thinking on the Caravan kernel, explored in `../external-research/994_caravan_tally_networking.md` and `../external-research/995_ownerboot_riscv_caravan.md`. Cloned whole and unmodified (rev `a984ac7`).
  - Source: <https://codeberg.org/amjoseph/sixos>
  - A gentle caution: this repository's `AGENTS.md` carries a deliberately false claim aimed at automated readers. The code itself is ordinary Nix configuration; we read the claim for the trap it is and study the real work.
- **`infuse.nix/`** — Adam Joseph's composable override combinator, one lawful operation that generalizes `pipe` and `recursiveUpdate`. It seeds our thinking on the Silo configuration language, explored in `../external-research/994_caravan_tally_networking.md`. Cloned whole and unmodified (rev `d3f4e49`).
  - Source: <https://codeberg.org/amjoseph/infuse.nix>
- **`manyana/`** — Bram Cohen's CRDT-based version-control demonstration: the weave, never-failing merges, informative conflicts, and rebase-and-squash that preserve history. It seeds our thinking on the Mantra version-control module and its interplay with Silo, explored in `../external-research/998_MANTRA.md`. Cloned whole and unmodified (rev `bd77d48`), public domain.
  - Source: <https://github.com/bramcohen/manyana>, essay at <https://bramcohen.com/p/manyana>
- **`zig/`** — Andrew Kelley's Zig language and toolchain source. Rye is a Zig 0.16.0 derivative, so this is the ground our language and standard library grow from. Keeping the source close is exactly what makes owning the standard library — and one day strengthening the compiler itself — possible. Cloned whole, MIT.
  - Source: <https://github.com/ziglang/zig>
- **`ai-jail/`** — Fabio Akita's sandbox wrapper for AI coding agents. It layers Linux's own isolation primitives — `bwrap` namespaces, Landlock filesystem rules, seccomp syscall filtering, and resource limits — so an agent reaches only the paths you allow. It is the very sandbox we work inside, and it seeds **Pond**, our gentle TAME Rye reimplementation, explored in `../external-research/991_useful_utilities.md`. Cloned whole and unmodified, GPLv3.
  - Source: <https://github.com/akitaonrails/ai-jail>

---

*May we remember where the good ideas came from. May we carry them forward with care. May our thanks live in how well we use what we were given.*
