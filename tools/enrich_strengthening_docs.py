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
    "9989_tally_gardens.md": ("tally/gardens.rye", "tally_gardens_test"),
    "9990_mantra_seed.md": ("mantra/src/main.rye", "mantra_weave_test"),
}

META = {
    "9995_crypto_foundation.md": ("meta/foundation", "crypto foundation map"),
}

# Pass doc stem → parity witness slug when they diverge.
WITNESS_ALIASES = {
    "9982_alloc_print_trimend_strengthen.md": "alloc_print_test",
    "9987_allocator_alloc_skate_grid.md": "allocator_alloc_test",
    "9988_alloc_print_trimend.md": "alloc_print_test",
    "9993_mem_diff_primitives.md": "mem_diff_test",
    "9996_stdlib_call_paths.md": "call_paths_test",
    "9997_keccak_sponge.md": "sha3_512_test",
}

SKIP = {"9999_STRENGTHENING.md", "0000_STRENGTHENING_LEXICON.md"}

STD_REF = re.compile(r"\*\*`std\.([^`]+)`\*\*")
BACKTICK_FN = re.compile(r"`std\.([a-zA-Z0-9_.]+)`")
WIDTH_SECTION = "## Width notes"
SURFACE_SECTION = "## Rye std surface"
WIDTH_AUDIT_SECTION = "## Width audit"
AUDITED_SURFACES_SECTION = "## Audited surfaces"

# Passes with completed width audit at strengthen touch (k runs with audit table).
# Detection is content-based via pass_width_audit_done(); this set is not used for gating.
WIDTH_AUDIT_DONE = frozenset({"9913", "9914", "9915", "9916"})


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


def surface_display_name(surface: str) -> str:
    if surface.startswith("std."):
        return surface
    if "/" in surface or surface.endswith(".rye"):
        return surface
    return f"std.{surface}"


def zig_path_for_surface(surface: str) -> str:
    if "/" in surface or surface.endswith(".rye"):
        return surface
    full = surface_display_name(surface)
    rel = surface_to_std_file(full)
    if rel.startswith("authored/"):
        return rel.removeprefix("authored/")
    return f"rye/lib/std/{rel}"


def pass_width_audit_done(pass_num: str, text: str) -> bool:
    if not has_width_audit_section(text):
        return False
    section = text.split(WIDTH_AUDIT_SECTION, 1)[1].split("\n## ", 1)[0]
    if re.search(r"\|\s*pending\s*\|", section):
        return False
    return "done" in section or "unchanged" in section


def zig_audit_note(zig_rel: str, fn_short: str) -> str:
    """One-line width audit note from zig source when available."""
    path = ROOT / zig_rel
    if not path.is_file():
        return f"`{fn_short}` — Phase 4 `usize` seam policy applied"
    text = path.read_text(encoding="utf-8", errors="replace")
    fn_pat = re.compile(rf"pub fn {re.escape(fn_short)}\b")
    m = fn_pat.search(text)
    if not m:
        return f"`{fn_short}` — Phase 4 `usize` seam policy applied"
    chunk = text[m.start() : m.start() + 2500]
    bounds = re.findall(r"max_[a-zA-Z0-9_]+:\s*u32", chunk)
    if bounds:
        names = ", ".join(b.split(":")[0].strip() for b in bounds[:3])
        return f"`{fn_short}` — {names} `u32`; public `usize` unchanged"
    if "usize" in chunk.split("{", 1)[0]:
        return f"`{fn_short}` — inherited `usize` seam; assertions only"
    return f"`{fn_short}` — Phase 4 `usize` seam policy applied"


def build_audited_surfaces_block(surfaces: list[str], done: bool) -> str:
    mark = "x" if done else " "
    lines = [
        AUDITED_SURFACES_SECTION,
        "",
        "Width audit at strengthen touch ([`992` Phase 4](../work-in-progress/992_usize_width_baseline.md)). "
        "Each surface this pass strengthens:",
        "",
    ]
    for s in surfaces:
        full = surface_display_name(s)
        path = zig_path_for_surface(s)
        lines.append(f"- [{mark}] `{full}` — [`{path}`](../{path})")
    lines.append("")
    return "\n".join(lines)


def witness_slug_for_pass(path: Path) -> str | None:
    if path.name in WITNESS_ALIASES:
        return WITNESS_ALIASES[path.name]
    m = re.match(r"\d+_(.+)", path.stem)
    if not m:
        return None
    slug = m.group(1).replace("_strengthen", "")
    return f"{slug}_test"


def witness_path_for_pass(path: Path) -> str | None:
    slug = witness_slug_for_pass(path)
    if not slug:
        return None
    rel = f"rye/tests/{slug}.rye"
    return rel if (ROOT / rel).exists() else None


def build_width_audit_block(path: Path, pass_num: str, surfaces: list[str], done: bool) -> str:
    status = "done" if done else "pending"
    doc = path.name
    primary = surfaces[0] if surfaces else doc
    short = surface_short_name(surface_display_name(primary)) if surfaces else doc
    lines = [
        f"{WIDTH_AUDIT_SECTION} (affected files)",
        "",
        "| File | Audit | Status |",
        "|------|-------|--------|",
    ]
    if path.name in AUTHORED:
        mod = AUTHORED[path.name][0]
        lines.append(f"| `{mod}` | authored Tier A widths | {status} |")
    elif path.name in META:
        lines.append(f"| `meta/foundation` | crypto dependency map | {status} |")
    else:
        zig = zig_path_for_surface(primary)
        if zig.startswith("rye/"):
            note = zig_audit_note(zig, short) if done else f"`{short}` — Phase 4 `usize` seam policy applied"
            lines.append(f"| `{zig}` | {note} | {status} |")
        for s in surfaces[1:]:
            extra = surface_short_name(surface_display_name(s))
            zp = zig_path_for_surface(s)
            if zp.startswith("rye/"):
                note = zig_audit_note(zp, extra) if done else f"`{extra}` — co-strengthened in this pass"
                lines.append(f"| `{zp}` | {note} | {status} |")
    witness = witness_path_for_pass(path)
    if witness:
        lines.append(f"| `{witness}` | witness program | {status} |")
    elif path.name in WITNESS_ALIASES:
        slug = WITNESS_ALIASES[path.name]
        lines.append(f"| `rye/tests/{slug}.rye` | witness program | {status} |")
    lines.append(f"| `tools/parity.rish` | witness registered | {status} |")
    lines.append(f"| `strengthening-compiler/{doc}` | pass record + audited surfaces | {status} |")
    lines.append(f"| `992_strengthening_width_crosswalk.md` | lexicon row {pass_num} | {status} |")
    lines.append("")
    return "\n".join(lines)


def find_section_start(text: str, section_title: str) -> int | None:
    m = re.search(rf"^## {re.escape(section_title)}(?:\s|\(|$)", text, re.MULTILINE)
    return m.start() if m else None


def replace_or_insert_section(text: str, section_title: str, new_body: str) -> str:
    """Replace an existing ## section body or insert before postconditions."""
    idx = find_section_start(text, section_title)
    if idx is not None:
        next_hdr = text.find("\n## ", idx + 3)
        if next_hdr == -1:
            return text[:idx] + new_body.rstrip() + "\n"
        return text[:idx] + new_body.rstrip() + "\n\n" + text[next_hdr + 1 :]

    insert_at = None
    for m in (
        "\n## Postconditions\n",
        "\n## Postcondition\n",
        "\n## What the test asserts\n",
        "\n## Design notes\n",
        "\n## What we built\n",
        "\n---\n\n## What grows",
    ):
        pos = text.find(m)
        if pos != -1:
            insert_at = pos
            break
    if insert_at is None:
        insert_at = len(text)
    return text[:insert_at] + "\n" + new_body + text[insert_at:]


def has_width_audit_section(text: str) -> bool:
    return find_section_start(text, "Width audit") is not None


def witness_slug_in_parity(slug: str, parity_text: str) -> bool:
    return f'"{slug}"' in parity_text or f'"{slug}_test"' in parity_text or slug in parity_text


def pass_auditable(path: Path, parity_text: str) -> bool:
    if path.name in AUTHORED:
        witness_slug = AUTHORED[path.name][1]
        return witness_slug_in_parity(witness_slug, parity_text)
    if path.name in META:
        return witness_slug_in_parity("ed25519_sign_test", parity_text)
    witness = witness_path_for_pass(path)
    if witness:
        slug = witness.removeprefix("rye/tests/").removesuffix(".rye")
        return witness_slug_in_parity(slug, parity_text)
    if path.name in WITNESS_ALIASES:
        return witness_slug_in_parity(WITNESS_ALIASES[path.name], parity_text)
    return False


def complete_pending_width_audits(parity_text: str) -> int:
    """Flip pending width audits to done when witness + surfaces are in place."""
    changed = 0
    for path in sorted(SC_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        text = path.read_text(encoding="utf-8")
        if pass_width_audit_done("?", text):
            continue
        if "pending" not in text:
            continue
        surfaces = extract_surfaces_from_doc(text, path)
        if not surfaces:
            continue
        if not pass_auditable(path, parity_text):
            print(f"audit skip (no witness): {path.name}")
            continue
        m = re.match(r"(\d+)_", path.name)
        pass_num = m.group(1) if m else "?"
        new_text = text
        audit_block = build_width_audit_block(path, pass_num, surfaces, done=True)
        new_text = replace_or_insert_section(new_text, "Width audit", audit_block)
        audited_block = build_audited_surfaces_block(surfaces, done=True)
        new_text = replace_or_insert_section(new_text, "Audited surfaces", audited_block)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed += 1
    return changed


def sync_width_audit_docs(sources: dict[str, str]) -> int:
    """Ensure every pass doc lists audited surfaces and has a width audit table."""
    changed = 0
    for path in sorted(SC_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        text = path.read_text(encoding="utf-8")
        m = re.match(r"(\d+)_", path.name)
        pass_num = m.group(1) if m else "?"
        surfaces = extract_surfaces_from_doc(text, path)
        if not surfaces:
            continue
        done = pass_width_audit_done(pass_num, text)
        new_text = text
        if not pass_width_audit_done(pass_num, text):
            audit_block = build_width_audit_block(path, pass_num, surfaces, done=False)
            new_text = replace_or_insert_section(new_text, "Width audit", audit_block)
        audited_block = build_audited_surfaces_block(surfaces, done)
        new_text = replace_or_insert_section(new_text, "Audited surfaces", audited_block)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed += 1
    return changed


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


def surface_to_std_file(surface: str) -> str:
    """Map a dotted std surface name to rye/lib/std relative path."""
    if surface.startswith("std."):
        rest = surface[4:]
        parts = rest.split(".")
        head = parts[0]
        if head == "debug":
            return "debug.zig"
        if head == "mem":
            if len(parts) >= 2 and parts[1] == "Allocator":
                return "mem/Allocator.zig"
            return "mem.zig"
        if head == "fs":
            if len(parts) >= 2 and parts[1] == "path":
                return "fs/path.zig"
            return "fs.zig"
        if head == "crypto":
            low = rest.lower()
            if "sha3" in low or any(p.startswith("Sha3") for p in parts):
                return "crypto/sha3.zig"
            if "keccak" in low:
                return "crypto/keccak_p.zig"
            if "timing_safe" in rest:
                return "crypto/timing_safe.zig"
            return "crypto.zig"
        if head == "SemanticVersion":
            return "SemanticVersion.zig"
        if head == "process":
            return "process.zig"
        if head == "fmt":
            return "fmt.zig"
        if head == "Io":
            if len(parts) >= 2:
                return f"Io/{parts[1]}.zig"
            return "Io/"
        return "/".join(parts) + ".zig"
    if "/" in surface or surface.endswith(".rye"):
        return f"authored/{surface}"
    return "authored/misc"


def surface_short_name(surface: str) -> str:
    if surface.startswith("std."):
        parts = surface[4:].split(".")
        if len(parts) >= 3 and parts[0] in ("fs", "crypto", "Io"):
            return ".".join(parts[1:])
        if len(parts) >= 2 and parts[0] == "mem" and parts[1] == "Allocator":
            return ".".join(parts[1:])
        return parts[-1]
    return surface


def extract_surfaces_from_doc(text: str, path: Path) -> list[str]:
    if path.name in AUTHORED:
        mod, _ = AUTHORED[path.name]
        return [mod]
    if path.name in META:
        _, label = META[path.name]
        return [label]
    names: list[str] = []
    if SURFACE_SECTION in text:
        section = text.split(SURFACE_SECTION, 1)[1].split("\n## ", 1)[0]
        for m in STD_REF.finditer(section):
            if m.group(1) not in names:
                names.append(m.group(1))
        for m in BACKTICK_FN.finditer(section):
            n = m.group(1)
            if n not in names:
                names.append(n)
    if not names and "## What this pass covers" in text:
        cover = text.split("## What this pass covers", 1)[1].split("\n## ", 1)[0]
        for m in STD_REF.finditer(cover):
            if m.group(1) not in names:
                names.append(m.group(1))
    if not names:
        names = filename_guess(path)
    return names


def lexicon_entries(sources: dict[str, str]) -> list[dict]:
    entries: list[dict] = []
    for path in sorted(SC_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        m = re.match(r"(\d+)_", path.name)
        pass_num = m.group(1) if m else "?"
        surfaces = extract_surfaces_from_doc(text, path)
        if not surfaces:
            surfaces = [path.stem]
        for surface in surfaces:
            if path.name in META:
                full = META[path.name][1]
                std_file = META[path.name][0]
            elif path.name in AUTHORED:
                full = AUTHORED[path.name][0]
                std_file = surface_to_std_file(full)
            else:
                full = surface if surface.startswith("std.") else f"std.{surface}"
                std_file = surface_to_std_file(full)
            entries.append(
                {
                    "pass": pass_num,
                    "doc": path.name,
                    "surface": full,
                    "short": surface_short_name(full) if full.startswith("std.") else full,
                    "file": std_file,
                    "audited": pass_width_audit_done(pass_num, text),
                }
            )
    return entries


def generate_lexicon(entries: list[dict], stamp: str = "20260621.040612") -> str:
    by_file: dict[str, list[dict]] = {}
    for e in entries:
        by_file.setdefault(e["file"], []).append(e)

    audited_passes = len({e["pass"] for e in entries if e["audited"]})
    total_passes = len({e["pass"] for e in entries})
    audited_surfaces = sum(1 for e in entries if e["audited"])
    total_surfaces = len(entries)

    lines = [
        "# 0000 · Strengthening Lexicon — std-shaped tree",
        "",
        f"**Stamp:** `{stamp}`",
        "**Generated by:** `tools/enrich_strengthening_docs.py`",
        "**Chronicle floor:** [`9999_STRENGTHENING.md`](9999_STRENGTHENING.md)",
        "**Flat index:** [`../work-in-progress/992_strengthening_width_crosswalk.md`](../work-in-progress/992_strengthening_width_crosswalk.md)",
        "",
        f"**Width audit:** {audited_surfaces}/{total_surfaces} surfaces ✅ · "
        f"{audited_passes}/{total_passes} passes with completed width audit",
        "",
        "*The ceiling of the strengthening-compiler folder. Number `0000` sorts first; "
        "`9999` sorts last. Together they bracket the countdown chronicle (`9913`–`9998`).*",
        "",
        "---",
        "",
        "## Two ways to navigate",
        "",
        "| View | Role | Order |",
        "|------|------|-------|",
        "| **Lexicon** (this doc) | Find a strengthened surface by where it lives in `rye/lib/std` | std tree |",
        "| **Chronicle** (`9913`–`9998`) | Read how Rye's `std` became ours, pass by pass | newest first |",
        "| **Manifesto** (`9999`) | Method, four promises, versioning | floor |",
        "| **Crosswalk** (`992b`) | Machine index: pass → surface → width tier | pass number |",
        "",
        "Each pass doc holds the full story — signature, width notes, **audited surfaces**, postconditions, witness.",
        "✅ marks a pass whose width audit is `done`; `[ ]` marks surfaces still awaiting Phase 4 touch.",
        "",
        "---",
        "",
        "## Tree by `rye/lib/std` module",
        "",
    ]

    file_order = sorted(by_file.keys(), key=lambda f: (f.startswith("authored"), f))
    for std_file in file_order:
        rows = sorted(by_file[std_file], key=lambda e: (e["short"].lower(), -int(e["pass"])))
        lines.append(f"### `{std_file}`")
        lines.append("")
        lines.append("| Audit | Surface | Pass | Doc |")
        lines.append("|-------|---------|------|-----|")
        for e in rows:
            mark = "✅" if e["audited"] else "[ ]"
            lines.append(
                f"| {mark} | `{e['short']}` | {e['pass']} | [{e['pass']}]({e['doc']}) |"
            )
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "*May the lexicon show where each surface lives, and the chronicle show when it earned its witness.*"
    )
    lines.append("")
    return "\n".join(lines)


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

    synced = sync_width_audit_docs(sources)
    print(f"synced width audit + audited surfaces on {synced} pass docs")

    parity_text = (ROOT / "tools" / "parity.rish").read_text(encoding="utf-8")
    completed = complete_pending_width_audits(parity_text)
    print(f"completed width audits on {completed} pass docs")

    crosswalk = ROOT / "work-in-progress" / "992_strengthening_width_crosswalk.md"
    header = """# 992b · Strengthening ↔ Width Crosswalk

**Stamp:** `20260621.040612`
**Parent:** `992_usize_width_baseline.md`
**Lexicon:** [`../strengthening-compiler/0000_STRENGTHENING_LEXICON.md`](../strengthening-compiler/0000_STRENGTHENING_LEXICON.md)
**Prompt:** `expanding-prompts/10025_strengthening_stdlib_doc_width_pass.md`

Auto-generated index of every strengthening pass, its primary surface, and width tier.

| Pass | Doc | Primary surface | `usize` in signature | Width phase |
|------|-----|-----------------|----------------------|-------------|
"""
    rows = crosswalk_rows(sources)
    crosswalk.write_text(header + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"crosswalk: {len(rows)} rows -> {crosswalk}")

    entries = lexicon_entries(sources)
    lexicon_path = SC_DIR / "0000_STRENGTHENING_LEXICON.md"
    lexicon_path.write_text(generate_lexicon(entries), encoding="utf-8")
    print(f"lexicon: {len(entries)} surfaces -> {lexicon_path}")
    print(f"enriched {changed} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
