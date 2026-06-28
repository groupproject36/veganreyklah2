# Linengrow

**Language:** EN
**Last updated:** 2026-06-28
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)

---

Linengrow is the first whole built upon Rye OS — a transparent civic and social-commerce platform for vegan musicians and activist creators, where every sponsored post carries a visible label, every data sale carries a visible receipt, every contract carries a visible expiration, and every person owns their complete data in a portable server they can carry whenever they choose. Where Rye OS is the system, Linengrow is what the system is *for*: the place its foundations meet real people, real creators, and real communities.

This folder holds the vision. The build grows the SLC way — smallest lovable complete first — and its rings rest on the same modules Rye OS is already growing.

---

## One Spine, Two Altitudes

Linengrow shares Rye OS's architectural spine exactly: state as a pure fold over an append-only log of immutable signed facts, and five foundations beneath everything — keypair, signed event, log, projection, capability. The civic-platform thesis is a dependency, not a metaphor:

- The **keypair** that roots a Rye identity roots a Linengrow account; one owner seed, a whole presence derived.
- The **signed event** that records a fact records a sponsorship, a data sale, a donation.
- The **Mantra log** that versions a file records a transaction, kept whole, nothing grasped back.
- The **projection** that folds a log into a view folds transactions into a verifiable receipt and a balance.
- The **capability** that isolates a process in Caravan names ownership and permission in Linengrow.
- **Comlink** seals delivery identity to identity; **Sui** with USDsui settles when settlement is needed; **Pond** confines each application in a bounded, policy-as-value enclosure.

Correctness by construction in the kernel becomes trust by construction in the platform. The same discipline that makes a kernel safe makes a marketplace honest.

The unifying civic vision — open OS, open hardware, regenerative land, the ledger, creator tools — lives in [`../foundations/20260628-124512_anywhere-we-are-found.md`](../foundations/20260628-124512_anywhere-we-are-found.md). Linengrow carries forward its creator-facing gifts: the fable, the tools surface, and the privacy-by-disclosure model, below.

---

## Privacy and Disclosure

Linengrow holds two truths at once, and zero-knowledge proofs are what let it: **the mechanism is transparent; the individual is private.** The marketplace's rules stay visible to everyone — a sponsored post wears its label, a data sale carries its receipt, a contract shows its expiration — because the honesty of the room is the platform's whole promise. The person, by contrast, is private by default: opted out of public sharing until they choose otherwise, revealing only what they choose through a zero-knowledge proof — proving they are a verified vegan creator without naming themselves, proving a sponsorship was disclosed without exposing its terms, opening a door with a cryptographic pass while keeping the key behind it. The powerful mechanism is transparent; the individual stays private.

The default leans toward privacy, on purpose. No one is made public against their will; a person opts in to what they reveal, selectively, through proofs they control. Yet the culture and the economics make opting in attractive — a creator who shares their **fable**, their story told and proven honestly, is met and rewarded for it; transparency is celebrated as a community value; the positive economics flow toward those who choose to be seen. People opt in to being public because it is honored and it pays, never because the door was forced. The cryptographic pass is the everyday shape of this — it opens what you want opened, and keeps closed what you keep.

This satisfies all four promises a tool can keep at once, and most of all *tell the truth* and *hold lightly*: the room is honest, and the person remains free.

### The creator's surface

Linengrow serves makers with tools that are theirs: free tools for music, for fashion, for keeping notes, and for holding a social graph a person actually owns. Each creator's **fable** — their attested story — is the thread that runs through them, told once and provable anywhere, carried under the person's own key.

---

## The SLC Ladder

The full vision — a public benefit corporation, a computational data market, state-currency circulation, investor rounds — is the horizon. We grow toward it one lovable, complete ring at a time.

| Ring | What | Grows from |
|------|------|-----------|
| **SLC-L1** | **A verifiable receipt** — sign a transaction fact, append it to the log, produce a receipt anyone can verify | keypair + Mantra log + projection |
| **SLC-L2** | **Sealed delivery** — a signed receipt sent identity to identity, under seal | Comlink |
| **SLC-L3** | **Settlement** — a transaction settled on Sui with USDsui, its receipt verifiable on the ledger | Sui / Mysticeti |
| **SLC-L4** | **The selective-disclosure pass** — a zero-knowledge credential that proves a claim without revealing the data behind it (verified creator, disclosed sponsorship, access granted) | keypair + Sui ZK foundations |
| **Horizon** | The data market, premium tiers, state-currency circulation, the PBC and its rounds | the business model, below |

The first ring needs no ledger and no currency — only the foundations Rye OS already grows. A sanctuary receiving donations with cryptographic receipts is a complete, lovable, honest beginning, and everything larger grows from it.

---

## The Vision Documents

- `20260628-124512_linengrow-business-model.md` — the business model and investor-outreach approach: the public benefit corporation, four transparent revenue channels, the market opportunity, the go-to-market, and the conscience rubric that tests every decision against whether it nourishes, circulates, and returns what it takes.
- `20260628-124512_linengrow-venture-pitch.md` — the venture pitch: the problem of an opaque attention economy, the architecture of transparency, the business model in brief, and the longer horizon.

Both are generalized templates, debranded and repurposed onto Sui with optional USDsui settlement, so the vision stays reusable across regions and rounds while Linengrow carries it forward as our own.

---

## How It Grows

Linengrow lives here as vision and design while its first ring is small. Like every module, it may graduate to its own home — `xwb122m/linengrow-*` — once its first ring runs and earns the move. Until then, it grows beside the system it rests on, so the two stay coherent and the spine stays one.

The granular tasks for both tracks live in `../work-in-progress/TASKS.md`; the order and the why live in `../work-in-progress/ROADMAP.md`.

---

*May the economics of attention grow as transparent as a farmers' market in full morning light. May every receipt be verifiable, every contract carry its expiration in plain sight, and every person carry their own data freely wherever they go. May what we build nourish the people who make it, circulate through the communities that hold it, and return, season after season, more than it ever takes.*
