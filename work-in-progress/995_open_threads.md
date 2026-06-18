# 995 · Open Threads — the Networking and Social Turn

*A fresh snapshot of where we are and what is live, taken after a turn that reached outward: encrypted networking from the boot upward, a devotional social layer, and five new honored sources. It supersedes `997_open_threads.md`, carrying its still-open items forward.*

**Language:** EN
**Version:** `20260618.195712` (Rye chronological stamp)
**Last updated:** 2026-06-18
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2

---

## What Just Landed

- **A new way of working.** The `expanding-prompts/` stack is born (`9999_EXPANDING`), where a request becomes an expanded, structured prompt I run; its first entry, `10000`, is my reading of this turn's request.
- **Two research pieces.** `external-research/985` (encrypted networking from the boot upward → Aurora/Caravan/Tally/Silo/Mantra/Rye on RISC-V, learning from Urbit's Ames/Jael and Sui's Mysticeti/Move) and `984` (a simple, non-harming social layer for a devotional vegan community, learning from Nostr, with Sui-style validation and DAG curation).
- **Five honored sources, cloned.** `gratitude/urbit`, `gratitude/sui`, `gratitude/nips`, `gratitude/primal`, `gratitude/damus` — added as shallow submodules, for study and provenance.

## New Threads These Open

- **The owner-key PKI.** `985` roots network identity in the owner key (Ames's lesson without Azimuth). The hard, unanswered part is rotation, revocation, and recovery — what happens when a key is lost or stolen. The QR key-cards and master-key rotation in `SOURCE.md` are the first thread, not the whole answer.
- **The encrypted-datagram seed.** The smallest network that works: two harts, two owner keys, one authenticated, content-named datagram, verified with asserted invariants. This is Aurora's networking seed, several honest stages past today's "wake and speak."
- **Curation by structure, not by engine.** Both `985` and `984` lean on a DAG of named values (Mantra + Mysticeti's lesson). The live question: the smallest honest ranking — chronology, explicit follows, a web of trust — that needs no hidden model.
- **Spam without a central filter.** Nostr's known weakness. Our candidate answer: a web of trust among keys plus Tally-bounded relays, possibly Pond-enclosed. Untested.
- **The smallest social layer.** A note signed by an owner key, stored on one relay, read by a friend's key. What is the least we build first, and what grows from it?
- **Critical reading still owed.** We gathered essences by web and clone; a close read of the cloned sources (Ames's packet format, Mysticeti's commit rule, the core NIPs, Primal's caching, Damus's NIP set) would sharpen `985`/`984` and may earn their own research entries.

## Carried Forward (still live)

- **Aurora's next stage:** a stage that hands the next a value *it chose* — a real decision, not only a reading (`aurora/`, the roadmap).
- **Rishi toward `parity.rish`:** the next feature is list values; the climb continues on its own track.
- **The verify-flag hot-path strengthening pass:** `indexOfScalarPos` and other hot data-plane functions await postconditions compiled in only behind a `verify` flag (`strengthening-compiler/9996`).
- **The unbuilt modules:** Tally, Caravan, Silo, Mantra remain designs; `985`/`984` lean on them and so raise the value of growing their first working seeds.

## The Through-Line

One value model, all the way down: a packet (`985`), a post (`984`), a Mantra line, a Silo build, a Rye value — the same kind of thing, signed, named, bounded, owned. Each new study tightens that line; each clone tests it against how others actually did it. We keep it simple, we keep it kind, and we grow the whole from the smallest part that already works.

---

*May the threads stay visible while they are open, and be tied off honestly when they close. May we read what we cloned closely, build what we imagined slowly, and keep the network — like the values it carries — small enough to love.*
