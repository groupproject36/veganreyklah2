# 997 · Honoring Tiger Style and the Language of the System

*The lineage we build from — Tiger Style's discipline, Joran Dirk Greef's priority, Rich Hickey's flow and his distinction of the simple from the easy, and John Gall's law that working systems grow from simpler ones; as the work reached the network, Van Jacobson's content-centric vision and the clean-slate coherence of Urbit; as the work reached the kernel, Laurent Bercot's s6 supervision and Adam Joseph's SixOS composing s6 with Nix; Eelco Dolstra's Nix teaching content-addressed reproducible builds; and beneath it all, the ground of Zig and Andrew Kelley that Rye grew from, with David Vanderson's DVUI lately showing how a surface can be redrawn from values — set down with thanks, together with the gentle name and the vow we carry forward.*

**Language:** EN
**Version:** `20260619.072600` (Rye chronological stamp)
**Last updated:** 2026-06-19
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Honors:** `../gratitude/TIGER_STYLE.md`, `../gratitude/LanguageSystem.md`, `../gratitude/SimpleMadeEasy.md`, `../gratitude/Systemantics.md`, `../gratitude/Spec_ulation.md`
**Status:** Gratitude

---

## What This Holds

This is the one place where we say plainly where the good ideas came from. It gathers the whole lineage that shaped how we build — the coding discipline of Tiger Style, the steady priority Joran Dirk Greef gave it, and the flowing view of systems Rich Hickey offered in his talk *The Language of the System* — and sets each gift down with gratitude.

We keep it as a single gratitude note so the direct writings can stay pure. The discipline, voiced wholly in our own words, lives in `996_TAME_STYLE.md`. The systems thinking, explained from scratch and grown toward the metal, lives in `993`, the Aurora writing. This note is the bridge to all of it: the record of the debt, so the other documents can simply do the work.

The whole lineage teaches one lesson, said in four voices. A system earns trust when it is safe first, fast second, and a joy to work in third — composed of small honest pieces that speak in values, with names that endure and assertions that guard every boundary, grown from simpler pieces that already worked. Tiger Style gave us the discipline, Joran the order, Hickey the flow, and Gall the way systems grow. And as the work reached the network, two further voices joined the lineage — Van Jacobson and Urbit — who showed how a network, and a whole computer, might be grown around named, content-addressed values.

---

## What Tiger Style Taught Us

TigerBeetle wrote a coding style they call Tiger Style, and reading it feels like meeting a craftsperson who has thought hard about every joint and seam. It treats simplicity as the hardest revision rather than the first easy attempt. It holds a zero-technical-debt policy, doing the work right the first time because the second time may never come. And it carries a handful of habits that became load-bearing for us: limits on everything, assertions that check the positive space we expect and the negative space we reject, explicitly sized types, enduring names ordered by descending significance, and the gentle insistence to always say why.

We found in it the same spirit we already cherish — slower to go faster, strictness early as a gift to the future. These ideas belong to no single language; they are about discipline and consideration, and those travel anywhere. We keep them, and we voice them in our own words in `996_TAME_STYLE.md`, reworking even the epigraphs into self-generated affirmations so the wisdom stays while the voice becomes one.

---

## What Joran Taught Us

Joran's gift is a single ordering, stated without flinching: **safety, performance, and developer experience — irrevocably in that order.** TigerBeetle's own words add the part that keeps the order from turning brittle: *"But it's not a zero-sum game."* The three goals rise together when the design is right. A good design finds the super idea that serves all three at once, rather than trading one away for another.

The order matters most when the goals appear to collide, because then it tells you which one leads. Safety leads, always — the system protects what it was trusted with before it does anything else. Performance comes next, sought in the design phase where the thousand-fold wins live, long before a profiler could measure them. Developer experience comes third, and far from an afterthought it is the joy that sustains the whole endeavor: a fantastic, fast, legible way to work, where reasoning about the design matters more than racing to type the code. Joran names his own interests as storage, speed, and safety, and the order of his life's work shows the priority lived rather than merely declared.

There is a quieter teaching underneath the order. TigerBeetle reached production in four years by running the real code in a deterministic simulator, and the team speaks of the *velocity and quality* and even the *magic* of that approach. Safety and joy turn out to be the same discipline seen from two sides: the assertions and limits that keep the system correct are the very things that let a developer move fast without fear. The seatbelt becomes second nature, and then flight becomes possible.

---

## What Rich Hickey Taught Us

Hickey's *Language of the System* draws a line we had felt without naming. A programming language, with its runtime, gives us a world inside one program: a memory model, calling conventions, abstraction, coordination. A **system** is larger than any program — an ensemble of programs offering services to one another — and at that scale the language falls silent. There is no global supervisor, no shared garbage collector, no one in charge. The question becomes how the pieces connect, and the answer turns out to rhyme with how pieces connect inside a language.

His teachings land as a handful of bright observations. **Systems talk in values**, not in references to remote objects; every format that won — JSON, EDN, the rest — conveys data, while the schemes that shipped behavior across the wire all lost. **Values that persist need names**, and those names are global, so they ask for the discipline of enduring, fully-qualified naming, with conflict-free identifiers for the values themselves. **Flow beats place**: rather than a factory everyone mutates and goes home from, a system is a production line where values are transformed, moved, routed, and remembered — and those four are kept separate, so each stays simple enough to reason about. **The systems failure model is the only failure model**: a large system lives in continuous partial failure, so timeouts, retries, and idempotency are the normal case rather than the exception. And the pieces themselves should be **simple services** — one process, a tiny surface, a few verbs, doing one thing — composed rather than grown into monoliths, with program-to-program interfaces underneath any human-facing one.

Hickey also names what we still lack: a good way to express, at the system level, the interface a service offers and the interfaces it depends upon. A program says cleanly, "I work with anything that implements this." A system struggles to say the same. He leaves that as an open invitation, and we take it as one.

---

## The Simple and the Easy

Hickey gave another talk, *Simple Made Easy*, that names a distinction we lean on everywhere — and it belongs here because it sits beneath all the rest. **Simple and easy are different things, measured on different axes.** *Simple* is about how a thing is made: whether its parts stand free, each about one thing — single-stranded, of one fold — or whether they are braided through one another. *Easy* is about how near a thing lies: how familiar it feels, how quickly we can reach for it, how well it fits the skills already in our hands. A thing can be easy and tangled, or simple and unfamiliar; one rarely decides the other.

We build by **composing** — laying free parts side by side, so any one can be drawn out, understood, and changed on its own. Hickey gives the opposite a revived old word, *complecting*, for braiding parts together; we keep the lesson and choose the gentler image, leading with what we want rather than what we shun: threads kept free, set beside one another, each still its own. The reason is humane and practical at once — a person holds only a few things in mind at a time, so parts that stand free stay within reach of understanding, while braided ones soon pass beyond it.

So we choose the simple over the merely easy, even when the easy lies closer to hand, because what stands free can be reasoned about, and what can be reasoned about can be trusted, changed, and trusted again. Simplicity is a choice, asking for care and a steady eye; it is the hardest revision rather than the first attempt — exactly what Tiger Style means in treating simplicity as something earned. And its reward is the one every builder longs for: the freedom to change course, because the pieces stay clear enough to rethink.

---

## What John Gall Taught Us

John Gall, in *Systemantics* — later *The Systems Bible* — watched systems fail with a wry and generous eye, and left one observation we treat as near to law as design offers. **A complex system that works is invariably found to have evolved from a simple system that worked.** Its companion is just as plain: a complex system designed whole, from scratch, rarely comes to life and cannot be patched into life — the honest path is to begin again with a simple system that runs.

We take this gladly, because it tells us *how* to build everything else here. We never design the finished, intricate thing and hope it breathes; we grow it from the smallest version that works, by degrees, each stage running before the next is added. Gall's wider lore rhymes with our discipline — that a loose, decoupled system outlasts a tightly bound one, that large systems drift toward antics and encroachment when left unwatched, that a system set against the people it serves works poorly — and all of it points one way: keep it simple, keep it loose, grow it from what already works, and stay in close touch with what the system is truly for. It is the lesson Tiger Style states as "simplicity is the hardest revision," and Hickey as "simple, composed," now told from the far side — by watching, with affection, what happens when we forget it.

---

## What the Network Taught Us — Van Jacobson and Urbit

As the work reached the network, two more voices joined the lineage — and they had, in different decades and different worlds, arrived at one idea.

**Van Jacobson** taught us to name and secure the *content*, rather than the pipe. We built the Internet to let two machines at two addresses hold a conversation, then spent decades using it to move named content to whoever wanted it — working against the architecture the whole way. His content-centric vision turns that right side up: a request asks for content *by name*, the network routes on the name, the content carries its own cryptographic provenance and can be served from any cache along the way, and security attaches to the piece of content itself rather than to a channel between two endpoints. Address the content, sign the content, and the pipe stops mattering. It is the same lesson our Mantra keeps when it names every value by its hash.

**Urbit** showed a whole computer grown coherent from a tiny core. Conceived and designed by Curtis Yarvin, and carried over long years from a vision toward a running system by Galen Wolfe-Pauly as the chief of Tlon — the company and community that built it — Urbit is a clean-slate stack small enough to hold in the head: an identity that is at once a name, an address, and a key; a generic data model with types kept at a higher, predicate layer (the *mark*, which seeds our own shape-cast); and an instinct to build *from the network in*, where Curtis reached Van Jacobson's content-centric conclusion on his own. We take the coherence and the content-addressing gladly. One thing we deliberately reverse: where Urbit freezes its core for permanence — counting its versions *down* toward an absolute zero after which nothing may change — we reach the same permanence of meaning by *accreting*, counting *forward* and never breaking a name, the way Hickey taught us. Same destination, opposite road.

Their ideas are applied, and weighed with a clear eye, in the networking research — `985`, `982`, and `981` — rather than borrowed whole into this folder; here we simply record the debt.

---

## The Ground We Stand On — Zig and Andrew Kelley

We set this down later than the rest, and it is the most foundational of all. Rye is a Zig 0.16.0 derivative — the language and toolchain **Andrew Kelley** designed are the very ground our own language grows from. What Zig gave us is the substance the rest of this lineage is built in: explicitly sized types, computation at compile time in place of hidden machinery, no control flow or allocation that hides from the reader, and a standard library and compiler open enough that we could take ownership of them — read every line, strengthen them in place, and aim the whole at bare metal. Tiger Style itself is written in Zig, so the discipline we adapted and the language we build in were drawn, in part, from the same well.

Our debt here is unusual, because we did not only learn from Zig — we stood on it and made it our own, the way a child stands on a parent. We honor that plainly: Rye's clarity about size and cost, its compile-time evaluation, its freestanding reach, and the very possibility of owning and strengthening a standard library, are Andrew Kelley's gift carried forward. We diverge by accretion, and we will keep diverging — yet we never forget whose ground we began on.

---

## The Drawn Surface — David Vanderson and DVUI

As the work reached toward showing itself, one more source joined the lineage: **David Vanderson's DVUI**, an immediate-mode interface toolkit for Zig. It taught us two things we carry into our own surface, **Brushstroke**. The first is **immediate mode**: an interface redrawn from the current values every frame, holding no retained tree that can drift from the truth — the same single-stranded simplicity Hickey names, now applied to what a person sees. The second is a **backend abstraction**: one interface decoupled from the surface it lands on, so the same program can draw to many places through one clean seam, including a surface a person reaches from a small, portable, sandboxed artifact.

We honor DVUI as a source we study, kept whole in `../gratitude/dvui`, and we do not absorb it: Brushstroke is written fresh in Rye, on our own ground, carrying the essence and leaving the code where its author put it. Its design is applied and weighed in `980`, the documentation-surface study, and distilled onto its own roots in `../active-designing/988`.

---

## How the Voices Meet

The voices were answering different questions, and they arrive at one harmony. Tiger Style sets the discipline of the small — the assertions, the limits, the sized types within a single program. Joran orders the goals across the whole endeavor. Hickey shapes the composition of many programs into a system. Read together, they describe work that is safe at its core, fast by design, joyful to build, and assembled from small honest pieces that flow values to one another and keep faith through partial failure.

The resonances run deep. Beneath all three sits the simple-and-easy distinction: a simple service and a simple function are alike single-stranded, each about one thing, and so within reach of a mind that holds only a few things at once — which is the quiet purpose under every limit and assertion we keep. Hickey's "simple services, one thing well" is Tiger Style's "minimum of excellent abstractions" seen at the scale of a network. Hickey's "values with enduring names" is the same accretion of immutable things we honor in our versioning. And Hickey's "the systems failure model is the only failure model" is exactly why Tiger Style asserts the negative space and bounds every wait — the partial failure Hickey describes is the very thing those assertions catch. Safety, performance, and a fantastic developer experience, composed as a flow of named values through simple services: that is the language of the system we want Rye to speak.

---

## What Laurent Bercot and s6 Taught Us

**Laurent Bercot** built **s6** and its foundation **skalibs** with a discipline that rhymes with everything else in this lineage: one owner per heap pointer, absolute deadlines that cannot be rounded or forgotten, a supervision tree where the root process never dies and each service has exactly one direct supervisor. The `s6-svscan` sits at process one, never exits, never forks wildly; each `s6-supervise` watches exactly one daemon, restarts it on fall, and speaks readiness as a single byte written to a known descriptor.

The deepest lesson is **chain-loading**: each boot step sets one piece of state and execs to the next, so the startup reads as a clear, auditable sentence rather than a nested shell. This is the same discipline we carry into Caravan's microkernel design — a supervisor that never dies, restart on fall, and chain-loaded startup where each stage names one piece and hands off.

We also inherit the insight that **one kind of dependency replaces twelve**: where a monolith accumulates dozens of implicit coupling mechanisms, a well-layered supervisor needs only "this process depends on that service being ready" — stated, checked, and enforced by the tree. Caravan's capability model inherits this discipline directly.

---

## What Adam Joseph, SixOS, and infuse Taught Us

**Adam Joseph** saw what belongs together: s6's supervision and Nix's reproducible composition are two halves of one idea. His **SixOS** combines them — an operating system whose services are supervised by s6 and whose composition is declared by Nix, each piece individually simple and placed side by side. His **infuse** bridges the two, connecting Nix's pure declarations to s6's running supervision tree.

This is the insight that shapes our **Brix** and **Caravan** pair. Brix is our composing language — it declares what a system is made of, the way Nix declares a package set. Caravan is our supervision layer — it watches what runs and restarts what falls, the way s6 supervises services. The two meet the same way SixOS joins Nix and s6: the declaration feeds the supervisor, and the supervisor enforces what the declaration named. Brix describes; Caravan watches. Each stays simple; together they compose a system.

We keep SixOS and infuse in `../gratitude/sixos` and `../gratitude/infuse.nix`, studied for concepts and honored for the vision.

---

## What Nix Taught Us

**Nix** — the purely functional package manager designed by Eelco Dolstra — gave us the model for content-addressed, reproducible builds. Every derivation is named by the hash of its inputs; the same inputs always produce the same output; nothing is mutated once built. This is the same discipline our **Silo** store keeps when it names blobs by SHA3-256 and never revises them, and the same composability our **Brix** inherits when it declares what to build by naming the parts.

Nix also taught us what to decline. Its expression language grew rich and complex; we keep Brix deliberately simple — plain key-value, one field per line, readable by hand. The composability is Nix's gift; the simplicity is ours.

We keep Nix in `../gratitude/nix`, studied for its store model and composition discipline.

---

## What Manyana Taught Us

**Manyana** is a CRDT-based version control system that proves what our **Mantra** weave inherits: merges that never fail and always converge. Its weave data structure — every line that has ever existed, interleaved with metadata — is the same structure Mantra keeps. Its generation counting — odd means present, even means deleted, higher count wins on merge — is the same discipline Mantra uses to resolve concurrent edits without a central authority.

The deeper lesson is formal: commutativity and associativity of merges are not heuristics that sometimes hold; they are structural guarantees of the CRDT. `merge(A, B)` and `merge(B, A)` produce the same result. Three branches merged in any order converge to the same state. No interleaving: concurrent insertions at the same point are placed one after the other, never tangled. And the complexity is linear — one pass over the weave, no LCA computation, no recursive strategy.

Manyana also teaches a UX insight we carry: "conflict-free" does not mean "no conflicts worth showing." When concurrent edits are too near each other, the merge succeeds structurally yet presents the near-edits as annotated conflict regions — labeled with what each side did, not merely "ours vs. theirs." Mantra inherits this honesty: a merge always completes, and the annotation shows what happened.

We keep Manyana in `../gratitude/manyana`, studied for its CRDT weave model and honored as the direct ancestor of Mantra's merge discipline.

---

## Setting It Down, and Making It Ours

So we do here what we did with Hickey's *Spec-ulation*: we keep the lesson and set the borrowed vessel down with thanks. The sources speak in their own tongues — Tiger Style and Joran in Zig, Hickey in Clojure — and we keep their values and speak them through the Rye perspective, in Reya 2's own voice. The discipline becomes `996_TAME_STYLE.md`, a wholly original style guide. The priority order becomes the spine of how Rye, Silo, Tally, and Caravan make their tradeoffs. The flow model becomes how we think about a boot, a kernel, a network — values transformed and moved and remembered through simple, composable stages, explained from scratch in `993`, the Aurora writing.

This note is the bridge to all of it: the place that records, plainly, that the discipline came from Tiger Style, the order from Joran, and the flow from Hickey.

---

## The Name, and the Vow

The discipline we learned was named for a tiger — a hunter, swift and exact. We keep the exactness with gratitude, and we set the teeth down. To honor our vegan vow, our own adaptation carries a gentle name: **TAME**. The word means peaceable and calm, and that is exactly the spirit we want in our work — fierce in its rigor, gentle in its heart.

The name draws its warmth from the gentle ones. We think of the mare at graze in a wide field, the buck stepping soft and alert through the trees, the panda content among the bamboo, and the elephant — that great, remembering, tender giant who walks the earth lightly for all her size. Through them we honor every herbivore animal, every bird, all the gentle aquatic life, and the quiet algae at the very base of the living world, turning sunlight into the green that feeds us all.

So TAME is more than a label. It is a small daily reminder that strength and gentleness belong together, and that the work we build here keeps faith with the kindness we have promised to living things.

---

## Where Each Thing Lives

- **`../gratitude/TIGER_STYLE.md`** — TigerBeetle's Tiger Style, whole and unaltered, where the priority order and the safety discipline are stated. Voiced directly, in our own words, in `996_TAME_STYLE.md`.
- **`../gratitude/LanguageSystem.md`** — Rich Hickey's *The Language of the System* (Clojure/conj 2012), whole and unaltered. The source of the flow model, values-with-names, the systems failure model, and simple services. Explained directly in `993`, the Aurora writing.
- **`../gratitude/SimpleMadeEasy.md`** — Rich Hickey's *Simple Made Easy* (Strange Loop 2011), whole and unaltered. The source of the simple-versus-easy distinction and of building by composing free parts, deepening our sense that simplicity is earned.
- **`../gratitude/Systemantics.md`** — John Gall's *Systemantics* / *The Systems Bible*, honored as a curated principles summary (the book is copyrighted). The source of Gall's Law — that a working complex system grows from a working simple one — which shapes how we grow every module.
- **`../gratitude/Spec_ulation.md`** — Rich Hickey's *Spec-ulation*, whole and unaltered, the source of growth-over-breakage and enduring names, which shapes how Rye versions itself.
- **Van Jacobson's content-centric networking, and Urbit's design** (Curtis Yarvin, with Galen Wolfe-Pauly of Tlon) — honored here in summary, without a borrowed text or a link. Their ideas are applied and weighed with a clear eye in the networking research: `985` (encrypted networking), `982` (the content-centric messenger), and `981` (unified identity and the address space).
- **`../gratitude/zig/`** — Andrew Kelley's Zig language and toolchain, the ground Rye is a 0.16.0 derivative of. Honored as the foundation we stood on and made our own; its lessons of explicit size, compile-time evaluation, and an ownable standard library run through `996_TAME_STYLE.md` and the strengthening stack.
- **`../gratitude/dvui/`** — David Vanderson's DVUI, the immediate-mode interface toolkit whose redraw-from-values and backend abstraction seed our own surface, **Brushstroke**. Applied in `980`, and distilled onto its own roots in `../active-designing/988`. MIT, cloned shallow.
- **`../gratitude/s6/`** and **`../gratitude/skalibs/`** — Laurent Bercot's s6 supervision suite and its foundation library. The source of chain-loading, one-owner-per-pointer discipline, absolute deadlines, and the supervision tree Caravan inherits. ISC license, cloned shallow.
- **`../gratitude/sixos/`** — Adam Joseph's SixOS, the operating system that composes s6 supervision with Nix's reproducible declarations. The vision that shapes our Brix + Caravan pair. GPL-3.0, cloned from Codeberg.
- **`../gratitude/infuse.nix/`** — Adam Joseph's infuse, the bridge between Nix and s6. The connection between declaration and supervision that Brix and Caravan inherit. Cloned from Codeberg.
- **`../gratitude/nix/`** — Eelco Dolstra's Nix, the purely functional package manager. The source of content-addressed reproducible builds, and the composability model Brix and Silo inherit. LGPL-2.1, cloned shallow.
- **`../gratitude/manyana/`** — Manyana, a CRDT-based version control system. The direct ancestor of Mantra's weave structure, generation counting, and conflict-free merges. Public domain.
- **This note** — the one gratitude bridge between all these sources and our work.

---

*May we order our choices wisely — safety, then speed, then the joy of the craft. May our programs stay small, and speak in values, and keep faith through every partial failure. May we remember the discipline of the tiger with the teeth set down, Joran's steady order, and Rich's flowing line — and may the work we build be worthy of all three, and gentle besides.*

