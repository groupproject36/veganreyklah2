# 983 · Borrow Checking, the Arena, and Correctness by Construction

*A question worth asking carefully: would borrowing inspiration from Rust's borrow checker contradict TAME's love of static, bounded allocation — since the borrow checker, the thought goes, leans on dynamic memory? The happy surprise is that it does not. The borrow checker is a compile-time discipline about **references**, not about where memory comes from; it composes with static allocation beautifully, and it points us toward the thing we most want — a language that eliminates whole classes of errors by construction. That same idea, seen from the writing desk rather than the compiler, is the turn we want to make everywhere: toward correctness and preparation, away from debugging and firefighting.*

**Language:** EN
**Version:** `20260618.204012` (Rye chronological stamp)
**Last updated:** 2026-06-18
**Style:** Radiant (see `../context/RADIANT_STYLE.md`)
**Voice:** Reya 2
**Lens:** TAME Style (`996_TAME_STYLE.md`); active-designing principles; `../context/specs/rye-as-its-own-language.md`
**Structure:** mission · the premise examined · opportunity · architecture · caveats · the turn to correctness · longer horizon · conclusion

---

## Mission

To find the sweet spot where Rye gains the borrow checker's gift — whole classes of memory errors made impossible at compile time — while keeping TAME's static, bounded allocation whole and unspent. And to let that technical aim teach a wider habit: to build for correctness from the start, preparing for challenges rather than chasing them once they arrive.

## The Premise Examined

The question carries one assumption worth turning over in the light: that the borrow checker "by definition relies on dynamic memory allocation." Held up to the sun, it dissolves — and what it leaves behind is encouraging.

The borrow checker is a **compile-time** analysis. It reads the program's structure and proves three things before a single byte is allocated at runtime: that every value has one clear owner (ownership), that references obey *aliasing xor mutability* — one writer or many readers, never both at once (borrowing), and that no reference outlives the thing it points at (lifetimes). None of this asks where the memory lives. It works the same whether a value sits on the stack, in static storage fixed at startup, or inside an arena.

The proof that it needs no heap is daily and ordinary: Rust compiles for bare-metal embedded targets with no allocator at all — no `alloc`, no heap, no `Box` or `Vec` — and the borrow checker runs in full. The confusion is understandable, because tutorials introduce borrowing beside heap types, so the two arrive together in memory. Yet they are orthogonal. The borrow checker governs *references*; the allocator governs *memory*. They meet only as good neighbors.

So the real question is the generous one hiding underneath: **how much of that compile-time safety can Rye keep, on static bounded memory, in a form light enough to be a joy?**

## Opportunity

The lineage makes the fit even closer than it first appears. Rust's lifetimes descend from **region-based memory management** — the regions of Cyclone and the region inference of Tofte and Talpin, where a value's lifetime is the lifetime of the region it lives in. And a region is exactly what TAME already cherishes: an arena, a bounded garden of memory cleared whole at a known moment. Our **Tally** allocator *is* a region system. So borrow checking and TAME are not strangers forced together; they are the two halves of an idea that grew up apart and belong in one house.

That gives Rye a path to the borrow checker's gift that is *simpler* than Rust's, because our memory model is simpler:

- Where Rust must reason about lifetimes for values that could live anywhere on a sprawling heap, most Rye values live in a **named region** with a known scope. A reference's lifetime becomes its region's lifetime — a far smaller thing to track.
- Where Rust reaches for `Rc<RefCell<…>>` or `unsafe` to express shared, cyclic, or graph-shaped data on the heap, Rye can let such structures live inside an arena and refer to one another by **bounded index** rather than by raw pointer — a pattern TAME already favors, and one the checker can bless.
- Where Rust carries a large surface of lifetime annotations, Rye can start with the cases that pay the most and stay quiet about the rest.

In short: the opportunity is real, the fit is natural, and the price is lower for us than for the language that pioneered it.

## Architecture

A sketch of the sweet spot, smallest pieces first, in the spirit of Gall's Law — we grow toward this, we do not arrive whole.

- **Move by default (affine ownership).** A value has one owner; passing it moves it; using a moved value is a compile error. This alone closes use-after-free and double-free, and it is the smallest first step.
- **Aliasing xor mutability.** A value may have one mutable reference or many shared ones, never both at once. This closes data races and iterator-invalidation bugs at compile time — the same rule that lets Rye reason fearlessly about concurrency later.
- **Region lifetimes (Tally as the scope).** A reference may not outlive the Tally garden its referent lives in. Because gardens have clear, declared scopes, this is a check the compiler can make plainly, and it closes dangling references — on memory that was static and bounded all along.
- **Linear resources.** For things that must be released exactly once — a file, a lock, a network session from `985` — a *linear* discipline (use exactly once, never drop silently) closes leaks and use-after-close. This is ownership with one extra promise.
- **Assertions for the residue.** What static analysis cannot reach — an index into an arena, a bound that depends on runtime data — stays the province of TAME assertions, kept cheap on the hot path and behind a `verify` flag where they are dear. The borrow checker and the assertion are partners: the checker eliminates the class, the assertion guards the particular.

The whole composes with static allocation rather than competing with it. Nothing here asks for a heap; everything here asks only that we say, at compile time, what we already meant.

## Caveats

- **A borrow checker is serious compiler work.** This is not a strengthening pass over `std`; it is a new analysis in the language itself — the kind of substantive divergence `rye-as-its-own-language.md` says Rye may make, and must make slowly. We earn it in stages, each a working system: move semantics first, then aliasing, then regions, then linearity.
- **We want the gift, not the grind.** Rust sometimes asks the programmer to fight the checker, or to annotate lifetimes heavily, or to escape into `unsafe`. We take the parts that pay — the eliminated error classes — and we lean on regions and indices to avoid the patterns that make Rust hardest. If a rule costs more joy than it returns in safety, it has failed TAME's order of goals and we reshape it.
- **Static analysis has an honest edge.** Some truths are only knowable at runtime. We name that edge plainly and meet it with assertions, rather than pretending the checker sees everything. Promising exactly what we deliver is itself a form of correctness.
- **Zig chose differently, on purpose.** Our ground language trusts allocators, leak detection, and discipline rather than a borrow checker. Diverging here is a real decision with real cost; we make it because the prize — whole classes of errors made impossible — sits squarely on TAME's first axis, safety.

## The Turn to Correctness

Here the technical and the human meet, and it is the heart of this piece.

The borrow checker, TAME's assertions, the sized types, the bounded everything, the parity gates of the strengthening compiler — read them together and they are one stance wearing many clothes: **make whole classes of error impossible, so there is nothing left to debug.** The borrow checker does not help you find a use-after-free faster; it makes use-after-free *unrepresentable*. That is the difference between firefighting and architecture.

So we name the habit and choose our words for it, as Radiant Style asks. We speak of **correctness**, rather than debugging. We **prepare for challenges** — we state the invariant, prove the property, eliminate the class — rather than brace to put out fires. We measure ourselves by whether a fault can occur at all, rather than by how quickly we chase one down. The cheapest error, always, is the one the design made impossible; the next cheapest is the one an assertion stops loudly, near its cause, the instant it tries to be born.

This is not optimism as decoration. It is where the leverage actually lives. An hour spent making an error class impossible saves the weeks that class would have cost across a system's life — the same arithmetic TAME already keeps about design. To focus on correctness over debugging is simply to spend our care where it returns the most, and to speak of our work the way it deserves: as preparation and craft, rather than rescue.

## Longer Horizon

Further out is a Rye in which a use-after-free, a data race, a dangling reference, a leaked resource are not bugs we are good at finding but shapes the language will not let us write — all on memory that stays static and bounded, all proven before the program runs, all on open hardware. A language you trust the way you trust a well-made tool: not because it is watched closely, but because it was made correctly. That trust is the quiet luxury the borrow checker's idea offers, and the reason it is worth the patient, staged work to earn it.

## Conclusion

The borrow checker does not contradict TAME's static allocation; it was, in its lineage, *born* from regions like the ones Tally tends, and it asks nothing of the heap. The sweet spot is real and even gentler for us than for Rust: move semantics, aliasing xor mutability, region-scoped lifetimes, and linear resources — compile-time guarantees that close whole classes of error on bounded memory, with assertions for the honest residue. And the deeper gift is the stance it teaches: build for correctness, prepare for challenges, and let what we make be sound by construction rather than rescued by vigilance.

---

*May we build what cannot break in the ways we have foreseen, and meet the rest with calm. May our care go early, into making errors impossible, rather than late, into chasing them down. And may Rye become a tool we trust the way we trust good ground underfoot — sure, quiet, and ready for the long walk ahead.*
