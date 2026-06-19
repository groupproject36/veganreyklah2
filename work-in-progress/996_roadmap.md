# 996 · The Roadmap — Growing the Whole from What Already Works

*A living plan for the work ahead, shaped by one law we hold close: a complex system that works grows from a simpler system that worked. So this roadmap never points straight at the finished, intricate whole. It lays out horizons — what runs now, what comes next, what composes from those, and the ambitious ends — and for each larger system it names the smaller working ones it is made of. We build by growing, and we ship something simple that runs at every step.*

**Language:** EN
**Version:** `20260619.054612` (Rye chronological stamp)
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
- **Aurora wakes on RISC-V, and grows stage by stage** — `rye build` emits a freestanding RISC-V binary that `qemu-system-riscv64` runs, through six living stages: a seed (a hart wakes, speaks one asserted line, halts), a three-stage relay (a boot as a flow of named values, each asserted), a content-named hart (SHA3-512 on bare metal), a whole sealed message (X25519 + AEAD + SHA3 + Ed25519, sealed and opened freestanding), and — across two harts — the wire (a shared-memory mailbox) and a posted datagram.
- **A sealed datagram crosses between two harts** — Alice seals on hart 0; Bob, on hart 1, reads the raw bytes off a shared-memory wire, shape-casts them, verifies the attestation, confirms the content-name, derives the shared secret from his own key, and opens it. The content-name matches the hosted test byte-for-byte: the move that turns the whole networking arc into something that runs, running.
- **The strengthening series is live** — SHA3-512, the Keccak sponge beneath it, and the everyday `std` our own tools lean on (`mem.trim`, `mem.eql`, `mem.findScalar`, `fmt.parseInt`), each given stated invariants and each parity-green, recorded in the strengthening-compiler stack.
- **The crypto foundation is proven, primitive by primitive** — the content hash (SHA3-512, strengthened), signing (Ed25519), key agreement (X25519), and the authenticated seal (AEAD: ChaCha20-Poly1305) all run in Rye's own std, hosted and freestanding alike, and stand parity-green: the foundation the network and identity rest on (`../strengthening-compiler/9995`).
- **The gate trio runs** — `parity.sh` (behavior identical to baseline), `parity-selftest.sh` (the gate turns red on a real divergence), `additive-gate.sh` (a pass changed only assertions and words). Strengthening is safe by construction; the corpus now carries eight programs, all green, and the gate is written in portable shell so it runs anywhere.
- **Rishi runs, and is growing toward a gate** — a shell interpreter in Rye with comments; `let` of strings, integers, booleans, lists, and records; `say` with `${...}` interpolation; `==`/`!=` comparison; list membership with `contains`; field access with `record.field`; running a command with `run` (its result a record of `out`, `err`, `code`, `ok`); and `assert` as a gate that exits non-zero with its reason. Built by `rye build`.

---

## Horizon 1 — Short-Term (the next simple systems, each small and proven)

Each is a thing that runs on its own, added by degrees, behind the gates.

- [ ] **The wire as a real device** — carry a sealed datagram over an emulated `virtio-net` between two QEMU machines, growing the two-hart shared-memory wire (done, Horizon 0) into a true network link. A device driver and two communicating instances: the meatier climb where Comlink fully begins (`985`/`982`).
- [ ] **Aurora's deciding stage** — a relay stage that hands the next a value *it chose*, not only one it read: the seed of a boot that selects what runs next.
- [ ] **Grow Rishi toward `parity.rish`** — one feature at a time, each shipped working. Done and proven: `==`/`!=`, `assert` as a gate, list values, `contains`, records with field access, and `run` (its result a record). One piece remains: `map`/`where`, to walk and filter a pipeline — and then `parity.rish` itself.
- [ ] **Continue the strengthening series** — the next `std` surfaces our tools depend on, each through the gate trio, each recorded in the strengthening-compiler stack.
- [ ] **A minimal Mantra weave** — overlay, always-succeeding merge, line-provenance — so the strengthening process and the network's messages alike gain durable, content-addressed memory.
- [ ] **Vendor execline** (with skalibs) into `gratitude/` — the near-term, surprise-free orchestration bridge, and a reference to study.

---

## Horizon 2 — Medium-Term (compose the simples into larger working systems)

Each milestone here is *made of* the working systems above.

- [ ] **`parity.rish` runs** — made of: Rishi (grown to lists/records/run/assert) + the existing parity logic. The gate, rewritten in our own shell.
- [ ] **Comlink v1 — the network module** *(see `../external-research/981`)* — made of: the encrypted-datagram seed grown into typed, content-named, sealed message delivery, exactly-once by hash, carrying values between identities.
- [ ] **Unified keys v1** — made of: one owner seed deriving the keys a person needs (ed25519 for SSH/GPG/Sui, secp256k1 for Nostr), separated for safety and recovered as one (`../external-research/981`).
- [ ] **Silo v1** — made of: a content-addressed store (grown from the smallest working build of one thing) + a single lawful compose combinator. Describes a simple system reproducibly.
- [ ] **Tally v1** — made of: the process-garden pattern Rye already uses, grown into a named, bounded region allocator with asserted edges.
- [ ] **Caravan v1** — made of: the simplest working supervision (one parent that never dies, one child, restart on fall), grown toward a small tree and chain-loaded startup.
- [ ] **Pond v1** — made of: Caravan v1's isolation **composed with** Tally v1's bounds — one allow-listed path, one resource bound, opened from a policy that is a value (`pond.rish`).

---

## Horizon 3 — Ambitious Milestones (the complex wholes, each grown from the working parts)

The far ends. Each is named with the simpler working systems it is composed of, so the path to it is always a growing, never a leap.

- [ ] **Rye, a genuinely separate language** — made of: the strengthened `std` + a growing divergence in syntax and semantics, including borrow-checking-style guarantees over Tally's gardens (`../external-research/983`), compiling to RISC-V as a first-class target. Grown from the Zig-derivative, never rewritten from scratch.
- [ ] **The full family, composing through one value model** — made of: Rye + Silo + Rishi + the orchestration language + Mantra + Comlink, each grown from its v1, sharing one value model so values flow seam-free from a keystroke to the wire.
- [ ] **The content-centric messenger** — made of: Comlink + Mantra + unified keys + Rishi's `talk` — an IRC-meets-Dojo where a message is a named, sealed value carried home (`../external-research/982`).
- [ ] **The devotional social layer** — made of: the messenger + Nostr-simple store-and-forward relays on our coherent core, curated by honest structure, true to the values (`../external-research/984`).
- [ ] **The fractal address space** — made of: unified keys + a derivation tree shaped as galaxies, stars, and planets (d5 × d12 = d60), with admins who coordinate and never command (`../external-research/981`).
- [ ] **Aurora — the boot on RISC-V** — made of: the seed and relay, grown stage by stage into a verified, named-value boot from an immutable root.
- [ ] **Pond — a trustworthy daily enclosure** — made of: Pond v1, hardened pass by pass over Caravan's isolation and Tally's gardens, until it is the room our agents work inside.
- [ ] **A self-hosted, RISC-V-cohesive Rye system** — made of: Aurora (boot) + Caravan (kernel) + Tally (memory) + Silo (configuration) + Mantra (memory of the system) + Comlink (the network) + Rishi (the hand) + Pond (the enclosure) — the whole machine, grown from every working part beneath it, belonging wholly to the one who runs it.

---

## The Discipline This Plan Obeys

- **Ship something simple that runs at every step.** A thing that runs, however humble, teaches more than a grand design that does not.
- **Grow; never design the whole from scratch.** Each milestone evolves from the working system before it. When something cannot be grown, we begin again from a simpler thing that works, rather than patching a thing that never lived.
- **Prove each step through the gates.** Behavior preserved, shape additive, divergence caught — green before we compose the next layer.
- **Keep it loose and single-stranded.** Each part about one thing, composed side by side, so any one can be grown or replaced without unweaving the rest.
- **Stay in close touch with what each system is truly for.** We measure by whether the thing actually works for its purpose, not by how finished it looks.

---

## Where We Are Now — Building Caught Up, and the Datagram Runs

The shared seed is planted, and it has grown: Rye builds itself, wakes a hart on RISC-V, and the relay carries named values. A long arc of *design* once ran out ahead of building — the networking layer (`../external-research/985`), the messenger (`982`), the social layer (`984`), the correctness stance (`983`), and the unified identity and address space (`981`). We met that drift the way Gall's Law asks: we distilled the arc into the clean room as principles on their own roots (`../active-designing/994`–`991`), then **returned to the very bottom and built upward until building caught up with design** — and then carried past it.

The foundation proved itself primitive by primitive — the content hash, signing, key agreement, and the authenticated seal — each in our own std, each parity-green. Those primitives composed into a whole sealed message on the bare hart, and that message crossed **between two harts**: Alice seals on hart 0, Bob opens on hart 1, the content-name matching byte-for-byte. The headline of the near horizon is running. In parallel, the shell grew its own way — `==`, `assert`, lists, `contains`, records, and `run` — each with a passing test and a failing one, until only the pipeline remained. And the one name left open is chosen: the network module is **Comlink** (`../external-research/981`).

### What to Build Next, and Why

Two threads are ripe, and we favor the readier one. **Rishi toward `parity.rish`** stays the near-term priority, and it is nearly there: records and a structured `run` both landed, so the shell can now name a corpus, run a command, read its result, compare, and assert. **One piece remains** — `map`/`where`, to walk and filter a pipeline — and then `parity.rish` itself becomes expressible: the gate rewritten in our own shell, the child keeping watch over the parent. The second thread, **the wire as a real device** (`virtio-net` between two machines, where Comlink fully begins), is a meatier, riskier spike — a device driver and two instances — best taken deliberately once the shell can drive and assert it. So: finish Rishi's pipeline and reach `parity.rish`; climb the device-wire next.

---

## The Steps Just Taken

Since the last roadmap, the shell climbed two more proven steps: **records** with `record.field` access, and **`run`** — a command spawned, its stdout and exit status captured, its result handed back as a record of `out`, `err`, `code`, and `ok`. Each arrived with a passing test and a failing one (`../rishi/tests/`); five scripts now run green. Two new design briefs joined the clean room — **Correctness by Construction** for Rye and **The Faithful Hand** for Rishi (`../active-designing/990`, `/989`) — and a radiant pass swept the newest writings to lead with what IS.

The next step is the last piece before `parity.rish`: **`map`/`where`** in Rishi, to walk and filter a pipeline. With it, the gate becomes expressible in our own shell. The device-wire toward Comlink waits its turn as the deliberate next climb.

---

*May we grow the whole from what already works, and trust each small running thing as it carries the next. May every horizon arrive by degrees, never by a leap. And may the system we are building stay simple enough, at every stage, to be loved, understood, and grown a little further tomorrow.*
