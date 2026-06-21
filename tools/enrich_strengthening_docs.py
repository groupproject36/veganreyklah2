#!/usr/bin/env python3
"""Add Rye std surface + width notes to strengthening-compiler pass docs."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SC_DIR = ROOT / "strengthening-compiler"
STD_ROOT = ROOT / "rye" / "lib" / "std"

# Passes that are authored .rye modules, not std surfaces.
AUTHORED = {
    "9989_tally_gardens.md": ("tally/gardens.rye", None),
    "9990_mantra_seed.md": ("mantra/src/main.rye", None),
}

SKIP = {"9999_STRENGTHENING.md"}

STD_REF = re.compile(r"\*\*`std\.([^`]+)`\*\*")
BACKTICK_FN = re.compile(r"`std\.([a-zA-Z0-9_.]+)`")
WIDTH_SECTION = "## Width notes"
SURFACE_SECTION = "## Rye std surface"


def zig_files() -> dict[str, str]:
    out: dict[str, str] = {}
    for p in STD_ROOT.rglob("*.zig"):
        try:
            out[str(p.relative_to(STD_ROOT))] = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            pass
    return out


def find_signature(name: str, sources: dict[str, str]) -> str | None:
    """Find pub fn signature for a dotted name like mem.replace or fs.path.join."""
    parts = name.split(".")
    fn = parts[-1]
    module_hints = []
    if len(parts) >= 2:
        if parts[0] == "mem":
            module_hints.append("mem.zig")
        elif parts[0] == "crypto":
            module_hints.append("crypto")
        elif parts[0] == "fs" and len(parts) >= 3:
            module_hints.append(f"fs/{parts[1]}.zig")
        elif parts[0] == "process":
            module_hints.append("process.zig")
        elif parts[0] == "SemanticVersion":
            module_hints.append("SemanticVersion.zig")
        elif parts[0] == "Io":
            module_hints.append("Io")

    pat = re.compile(
        rf"pub fn {re.escape(fn)}\b[^{{]*",
        re.MULTILINE,
    )

    candidates: list[tuple[int, str]] = []
    for rel, text in sources.items():
        score = 0
        for h in module_hints:
            if h in rel:
                score += 10
        for m in pat.finditer(text):
            sig = m.group(0).strip()
            if sig.endswith("{"):
                sig = sig[:-1].strip()
            candidates.append((score, sig))

    if not candidates:
        return None
    candidates.sort(key=lambda x: (-x[0], len(x[1])))
    return candidates[0][1]


def extract_std_names(text: str) -> list[str]:
    names: list[str] = []
    for m in STD_REF.finditer(text):
        names.append(m.group(1))
    for m in BACKTICK_FN.finditer(text):
        n = m.group(1)
        if n not in names:
            names.append(n)
    # filename fallback: mem_replace -> mem.replace
    return names


def filename_guess(path: Path) -> list[str]:
    stem = path.stem
    m = re.match(r"\d+_(.+)", stem)
    if not m:
        return []
    slug = m.group(1)
    if slug in ("tally_gardens", "mantra_seed"):
        return []
    slug = slug.replace("_strengthen", "")
    parts = slug.split("_")
    if parts[0] == "mem":
        return ["mem." + "_".join(parts[1:])] if len(parts) > 1 else []
    if parts[0] == "sha3":
        return ["crypto.sha3"]
    if parts[0] == "keccak":
        return ["crypto.keccak"]
    if parts[0] == "path":
        return ["fs.path." + parts[1]] if len(parts) > 1 else []
    if parts[0] == "semantic":
        return ["SemanticVersion." + parts[2]] if len(parts) > 2 else []
    if parts[0] == "allocator":
        return ["mem.Allocator.alloc"]
    if parts[0] == "alloc":
        return ["fmt.allocPrint"]
    if parts[0] == "process":
        return ["process.run"]
    if parts[0] == "dir":
        return ["Io.Dir.iterate"]
    if parts[0] == "fs":
        return ["fs"]
    if parts[0] == "window":
        return ["mem.window"]
    if parts[0] == "iterator":
        return ["mem.Iterator.reset"]
    if parts[0] == "tokenize":
        return ["mem.tokenize"]
    if parts[0] == "split":
        return ["mem.split"]
    return []


def width_note_for(name: str, sig: str | None) -> str:
    if sig and "usize" in sig:
        seam = (
            "Public signature inherits Zig `usize` for slice lengths and indices — "
            "keep at the inherited seam per `992` Phase 4. Narrow to `u32`/`u64` "
            "only for named bounds inside the body (`max_*_check`, loop counters) "
            "with `assert` before `@intCast`."
        )
    elif sig:
        seam = (
            "No `usize` in the public signature; internal slice walks still use "
            "`usize` at the seam where Zig slices require it."
        )
    else:
        seam = (
            "Authored module or iterator family — width migration lives in Tier A "
            "(`992`); std iterator indices remain `usize` until wrapped at our API."
        )
    return (
        f"**`std.{name}`** — {seam}\n\n"
        f"| Surface | Width policy |\n"
        f"|---------|-------------|\n"
        f"| Inherited params (`[]T`, `len`, indices) | `usize` — Zig seam |\n"
        f"| Named snapshot/check bounds | prefer `u32` + `assert(len <= max)` |\n"
        f"| Wire-persistent counts | `u64` when on the wire (`992` Phase 2) |\n"
    )


def build_surface_block(names: list[str], sources: dict[str, str]) -> str:
    if not names:
        return ""
    lines = [SURFACE_SECTION, ""]
    for name in names:
        sig = find_signature(name, sources)
        if sig:
            lines.append(f"**`std.{name}`**")
            lines.append("")
            lines.append("```zig")
            lines.append(sig)
            lines.append("```")
            lines.append("")
        else:
            lines.append(f"**`std.{name}`** — see `rye/lib/std` (signature not auto-located).")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_width_block(names: list[str], sources: dict[str, str]) -> str:
    if not names:
        return ""
    lines = [WIDTH_SECTION, ""]
    for name in names:
        sig = find_signature(name, sources)
        lines.append(width_note_for(name, sig))
    return "\n".join(lines).rstrip() + "\n"


def enrich_file(path: Path, sources: dict[str, str]) -> bool:
    text = path.read_text(encoding="utf-8")
    if SURFACE_SECTION in text and WIDTH_SECTION in text:
        return False

    if path.name in AUTHORED:
        mod, _ = AUTHORED[path.name]
        surface = (
            f"{SURFACE_SECTION}\n\n"
            f"**Authored:** `{mod}` — not an inherited `std` function. "
            f"Width migration is Tier A in `992`.\n"
        )
        width = (
            f"{WIDTH_SECTION}\n\n"
            f"Migrate struct fields and counters to `u32`/`u64` per `10024`; "
            f"keep `usize` only at `buf[0..n]` slice seams with `bufLenU32` helpers.\n"
        )
        names: list[str] = []
    else:
        names = extract_std_names(text)
        if not names:
            names = filename_guess(path)
        surface = build_surface_block(names, sources)
        width = build_width_block(names, sources)

    # Insert after "## What this pass covers" section (before ## Postcondition(s))
    insert_at = None
    for marker in (
        "\n## Postconditions\n",
        "\n## Postcondition\n",
        "\n## What the test asserts\n",
        "\n## Design notes\n",
        "\n## What we built\n",
        "\n---\n\n## What grows",
    ):
        idx = text.find(marker)
        if idx != -1:
            insert_at = idx
            break
    if insert_at is None:
        insert_at = len(text)

    block = "\n" + surface + "\n" + width
    new_text = text[:insert_at] + block + text[insert_at:]
    path.write_text(new_text, encoding="utf-8")
    return True


def crosswalk_rows(sources: dict[str, str]) -> list[str]:
    rows = []
    for path in sorted(SC_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        m = re.match(r"(\d+)_", path.name)
        num = m.group(1) if m else "?"
        if path.name in AUTHORED:
            mod, _ = AUTHORED[path.name]
            rows.append(f"| {num} | `{path.name}` | `{mod}` | authored | Tier A |")
            continue
        names = extract_std_names(text) or filename_guess(path)
        primary = names[0] if names else path.stem
        sig = find_signature(primary, sources) if names else None
        usize = "yes" if sig and "usize" in sig else ("authored" if not names else "internal")
        rows.append(
            f"| {num} | `{path.name}` | `std.{primary}` | {usize} seam | Phase 4 |"
        )
    return rows


def main() -> int:
    sources = zig_files()
    changed = 0
    for path in sorted(SC_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        if enrich_file(path, sources):
            changed += 1
            print(f"enriched {path.name}")

    crosswalk = ROOT / "work-in-progress" / "992_strengthening_width_crosswalk.md"
    header = """# 992b · Strengthening ↔ Width Crosswalk

**Stamp:** `20260621.031812`
**Parent:** `992_usize_width_baseline.md`
**Prompt:** `expanding-prompts/10025_strengthening_stdlib_doc_width_pass.md`

Auto-generated index of every strengthening pass, its primary surface, and width tier.

| Pass | Doc | Primary surface | `usize` in signature | Width phase |
|------|-----|-----------------|----------------------|-------------|
"""
    rows = crosswalk_rows(sources)
    crosswalk.write_text(header + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"crosswalk: {len(rows)} rows -> {crosswalk}")
    print(f"enriched {changed} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
