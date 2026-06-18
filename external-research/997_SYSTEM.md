# 997 · Honoring Tiger Style and the Language of the System

*The lineage we build from — Tiger Style's discipline, Joran Dirk Greef's priority, Rich Hickey's flow and his distinction of the simple from the easy, and John Gall's law that working systems grow from simpler ones; and, as the work reached the network, Van Jacobson's content-centric vision and the clean-slate coherence of Urbit — set down with thanks, together with the gentle name and the vow we carry forward.*

**Language:** EN
**Version:** `20260618.223812` (Rye chronological stamp)
**Last updated:** 2026-06-18
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

## How the Voices Meet

The voices were answering different questions, and they arrive at one harmony. Tiger Style sets the discipline of the small — the assertions, the limits, the sized types within a single program. Joran orders the goals across the whole endeavor. Hickey shapes the composition of many programs into a system. Read together, they describe work that is safe at its core, fast by design, joyful to build, and assembled from small honest pieces that flow values to one another and keep faith through partial failure.

The resonances run deep. Beneath all three sits the simple-and-easy distinction: a simple service and a simple function are alike single-stranded, each about one thing, and so within reach of a mind that holds only a few things at once — which is the quiet purpose under every limit and assertion we keep. Hickey's "simple services, one thing well" is Tiger Style's "minimum of excellent abstractions" seen at the scale of a network. Hickey's "values with enduring names" is the same accretion of immutable things we honor in our versioning. And Hickey's "the systems failure model is the only failure model" is exactly why Tiger Style asserts the negative space and bounds every wait — the partial failure Hickey describes is the very thing those assertions catch. Safety, performance, and a fantastic developer experience, composed as a flow of named values through simple services: that is the language of the system we want Rye to speak.

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
- **This note** — the one gratitude bridge between all these sources and our work.

---

*May we order our choices wisely — safety, then speed, then the joy of the craft. May our programs stay small, and speak in values, and keep faith through every partial failure. May we remember the discipline of the tiger with the teeth set down, Joran's steady order, and Rich's flowing line — and may the work we build be worthy of all three, and gentle besides.*

