# 996 · The Roadmap — Growing the Whole from What Already Works

*A living plan for the work ahead, shaped by one law we hold close: a complex system that works grows from a simpler system that worked. So this roadmap never points straight at the finished, intricate whole. It lays out horizons — what runs now, what comes next, what composes from those, and the ambitious ends — and for each larger system it names the smaller working ones it is made of. We build by growing, and we ship something simple that runs at every step.*

**Language:** EN
**Version:** `20260619.024512` (Rye chronological stamp)
**Last updated:** 2026-06-19
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME — safety, performance, the joy of the craft; and Gall's Law, that working wholes grow from working parts
**Status:** Living roadmap

---

## The Shape of This Plan

This plan draws its discipline from the active-designing stack: simplicity as single-stranded parts composed (`995`), the method of growing a language from proven ground (`996`), the gates that prove each step (`998`), the architecture the parts compose into (`997`), and the decision that Rye is its own language (`../context/specs/rye-as-its-own-language.md`). Above all it keeps Gall's Law: we reach for the smallest version that works, and let it become the larger one by degrees. No milestone here is built whole from scratch; each grows from the working systems beneath it.

---

## Horizon 0 — What Already Works (the ground we stand on)

These are the simple systems that run today. Everything ahead grows from them.

- **Rye runs, and is written in Rye** — a Zig-0.16 derivative with its own standard library and its own chronological versioning. The `rye` command (`run` and `build`) is itself a `.rye` program; Rye bootstraps once, then self-hosts its own build.
- **Aurora wakes on RISC-V** — `rye build` emits a freestanding RISC-V binary that `qemu-system-riscv64` runs: a seed (a hart wakes, speaks one asserted line, halts) and a three-stage relay (a boot as a flow of named values, each stage asserted). Rye's open-hardware cohesion and Aurora's first life, proven together.
- **The strengthening series is live** — SHA3-512, the Keccak sponge beneath it, and the everyday `std` our own tools lean on (`mem.trim`, `mem.eql`, `mem.findScalar`, `fmt.parseInt`), each given stated invariants and each parity-green, recorded in the strengthening-compiler stack.
- **The crypto foundation is proven, primitive by primitive** — the content hash (SHA3-512, strengthened), signing (Ed25519), and key agreement (X25519) all run in Rye's own std and stand parity-green in the gate: the foundation the network and identity will rest on (`../strengthening-compiler/9995`).
- **The gate trio runs** — `parity.sh` (behavior identical to baseline), `parity-selftest.sh` (the gate turns red on a real divergence), `additive-gate.sh` (a pass changed only assertions and words). Strengthening is safe by construction; the corpus now carries six programs, all green, and the gate is written in portable shell so it runs anywhere.
- **Rishi runs** — a minimal shell interpreter in Rye (comments, `let` of strings and integers, `say` with `${name}` interpolation), built by `rye build`.

---

## Horizon 1 — Short-Term (the next simple systems, each small and proven)

Each is a thing that runs on its own, added by degrees, behind the gates.

- [ ] **A first networking seed** — one encrypted, content-named datagram between two harts: the smallest living piece of `985`/`982`, grown from Aurora's seed (which speaks, yet does not yet listen). Its crypto foundation is being laid and proven, seed by seed: signing (Ed25519) and key agreement (X25519) are done and parity-green; the authenticated seal (AEAD) comes next; then the datagram itself — identity at the owner key, named by SHA3-512, sealed and validated in place. This is the move that turns the whole networking arc into something that runs.
- [ ] **Aurora's deciding stage** — a relay stage that hands the next a value *it chose*, not only one it read: the seed of a boot that selects what runs next.
- [ ] **Grow Rishi toward `parity.rish`** — one feature at a time, each shipped working: list values → records → a `run` that returns a structured process result → `map`/`where` → `==` → `assert` as a gate.
- [ ] **Continue the strengthening series** — the next `std` surfaces our tools depend on, each through the gate trio, each recorded in the strengthening-compiler stack.
- [ ] **A minimal Mantra weave** — overlay, always-succeeding merge, line-provenance — so the strengthening process and the network's messages alike gain durable, content-addressed memory.
- [ ] **Vendor execline** (with skalibs) into `gratitude/` — the near-term, surprise-free orchestration bridge, and a reference to study.

---

## Horizon 2 — Medium-Term (compose the simples into larger working systems)

Each milestone here is *made of* the working systems above.

- [ ] **`parity.rish` runs** — made of: Rishi (grown to lists/records/run/assert) + the existing parity logic. The gate, rewritten in our own shell.
- [ ] **Setu v1 — the network module** *(name provisional; see `../external-research/981`)* — made of: the encrypted-datagram seed grown into typed, content-named, sealed message delivery, exactly-once by hash, carrying values between identities.
- [ ] **Unified keys v1** — made of: one owner seed deriving the keys a person needs (ed25519 for SSH/GPG/Sui, secp256k1 for Nostr), separated for safety and recovered as one (`../external-research/981`).
- [ ] **Silo v1** — made of: a content-addressed store (grown from the smallest working build of one thing) + a single lawful compose combinator. Describes a simple system reproducibly.
- [ ] **Tally v1** — made of: the process-garden pattern Rye already uses, grown into a named, bounded region allocator with asserted edges.
- [ ] **Caravan v1** — made of: the simplest working supervision (one parent that never dies, one child, restart on fall), grown toward a small tree and chain-loaded startup.
- [ ] **Pond v1** — made of: Caravan v1's isolation **composed with** Tally v1's bounds — one allow-listed path, one resource bound, opened from a policy that is a value (`pond.rish`).

---

## Horizon 3 — Ambitious Milestones (the complex wholes, each grown from the working parts)

The far ends. Each is named with the simpler working systems it is composed of, so the path to it is always a growing, never a leap.

- [ ] **Rye, a genuinely separate language** — made of: the strengthened `std` + a growing divergence in syntax and semantics, including borrow-checking-style guarantees over Tally's gardens (`../external-research/983`), compiling to RISC-V as a first-class target. Grown from the Zig-derivative, never rewritten from scratch.
- [ ] **The full family, composing through one value model** — made of: Rye + Silo + Rishi + the orchestration language + Mantra + Setu, each grown from its v1, sharing one value model so values flow seam-free from a keystroke to the wire.
- [ ] **The content-centric messenger** — made of: Setu + Mantra + unified keys + Rishi's `talk` — an IRC-meets-Dojo where a message is a named, sealed value carried home (`../external-research/982`).
- [ ] **The devotional social layer** — made of: the messenger + Nostr-simple store-and-forward relays on our coherent core, curated by honest structure, true to the values (`../external-research/984`).
- [ ] **The fractal address space** — made of: unified keys + a derivation tree shaped as galaxies, stars, and planets (d5 × d12 = d60), with admins who coordinate and never command (`../external-research/981`).
- [ ] **Aurora — the boot on RISC-V** — made of: the seed and relay, grown stage by stage into a verified, named-value boot from an immutable root.
- [ ] **Pond — a trustworthy daily enclosure** — made of: Pond v1, hardened pass by pass over Caravan's isolation and Tally's gardens, until it is the room our agents work inside.
- [ ] **A self-hosted, RISC-V-cohesive Rye system** — made of: Aurora (boot) + Caravan (kernel) + Tally (memory) + Silo (configuration) + Mantra (memory of the system) + Setu (the network) + Rishi (the hand) + Pond (the enclosure) — the whole machine, grown from every working part beneath it, belonging wholly to the one who runs it.

---

## The Discipline This Plan Obeys

- **Ship something simple that runs at every step.** A thing that runs, however humble, teaches more than a grand design that does not.
- **Grow; never design the whole from scratch.** Each milestone evolves from the working system before it. When something cannot be grown, we begin again from a simpler thing that works, rather than patching a thing that never lived.
- **Prove each step through the gates.** Behavior preserved, shape additive, divergence caught — green before we compose the next layer.
- **Keep it loose and single-stranded.** Each part about one thing, composed side by side, so any one can be grown or replaced without unweaving the rest.
- **Stay in close touch with what each system is truly for.** We measure by whether the thing actually works for its purpose, not by how finished it looks.

---

## Where We Are Now — Design Has Run Ahead, and We Re-Anchor on Building

The shared seed is planted: Rye builds itself, wakes a hart on RISC-V, and the relay carries named values. A long arc of *design* then ran out ahead of building — the networking layer (`../external-research/985`), the messenger (`982`), the social layer (`984`), the correctness stance (`983`), and the unified identity and address space (`981`) — learning from sources we honored and cloned into `gratitude/` (Urbit, Sui, Nostr, Primal, Damus). Since, we have done two quiet, load-bearing things: **distilled that arc into the clean room** as principles standing on their own roots — rooted identity, the bounded network, shape-casting, and Aurora itself (`../active-designing/994`–`991`) — and **begun building again at the very bottom**.

For Gall's Law asks that a working whole grow from a working *simple* one. So we returned to the foundation our new ideas lean on — the cryptography — and began proving it, seed by seed: **signing** (Ed25519) and **key agreement** (X25519) now run in our own std, deterministic and parity-green, the gate carrying six programs with none diverged. The next moves stay small and concrete: the authenticated **seal** (AEAD), then the first encrypted, content-named **datagram** between two harts — where Aurora's relay and the network meet — alongside Aurora's deciding stage and Rishi's list values. From that one sealed word, Setu and the messenger and the social layer all grow.

One decision waits on you: the network module's name — **Setu** is recommended, with Doota, Akasha, and Comlink in view (`../external-research/981`).

---

## The Steps Just Taken

Since the last roadmap, the work moved on two fronts. In **code**: Rye became written in Rye and now self-hosts its build; Aurora grew from a seed into a three-stage relay; and the strengthening series reached the everyday `std` our tools call — `mem.trim`, `mem.eql`, `mem.findScalar`, `fmt.parseInt` (`../strengthening-compiler/9996`) — each parity-green. In **design**: a research arc drew the networking, messaging, social, correctness, and identity layers (`../external-research/981`–`985`) in our own voice and through every lens; the expanding-prompts stack was born; the honored sources were cloned; and a radiant pass set the corpus to lead with what IS, with the stance of *correctness over debugging* written into both style guides.

The next step turns design back into something that runs: **a first encrypted, content-named datagram between two harts** — grown from Aurora's seed and `985`/`982` — alongside Aurora's deciding stage and Rishi's list values, each small, each proven, each a root the larger systems grow from.

---

*May we grow the whole from what already works, and trust each small running thing as it carries the next. May every horizon arrive by degrees, never by a leap. And may the system we are building stay simple enough, at every stage, to be loved, understood, and grown a little further tomorrow.*
