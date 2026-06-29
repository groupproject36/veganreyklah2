#!/usr/bin/env python3
"""Align session-logs/ to one-clock discipline: Stamp, Editor, Model; rebuild README index."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SESSION_DIR = ROOT / "session-logs"
README = SESSION_DIR / "README.md"

FNAME_RE = re.compile(r"^(\d{8})-(\d{6})(?:_(.+))?\.md$")


def dot_stamp(ymd: str, hms: str) -> str:
    return f"{ymd}.{hms}"


def hyphen_stamp(ymd: str, hms: str) -> str:
    return f"{ymd}-{hms}"


def infer_editor_model(text: str, ymd: str) -> tuple[str, str]:
    if "**Editor:**" in text:
        return ("", "")  # caller skips insert

    agent = re.search(r"^\*\*Agent:\*\*\s*(.+)$", text, re.MULTILINE)
    if agent:
        a = agent.group(1).strip()
        if "Zed" in a:
            return ("Claude Code (Zed)", "Claude Opus")
        if "Cursor" in a:
            return ("Cursor", "Composer")

    head = text[:1200]
    if re.search(r"Claude Code|launch-zed|Zed", head) and "Cursor" not in head[:400]:
        return ("Claude Code (Zed)", "Claude Opus")
    if "Composer" in head:
        return ("Cursor", "Composer")
    if re.search(r"\bOpus\b", head):
        return ("Claude Code (Zed)", "Claude Opus")

    if ymd >= "20260628":
        return ("Cursor", "Composer")
    return ("(historical)", "(historical)")


def repair_weak_h1(h1: str, slug: str | None, ymd: str, hms: str, content: str) -> str:
    if not re.match(r"^# Session log — session\s*$", h1):
        return h1
    if "## The Request" in content and ymd == "20260619" and hms == "072600":
        return "# Session log — first log (one-clock practice begins)"
    m = re.search(r"## Thinking trace\s*\n+(.+?)(?:\n|$)", content, re.DOTALL)
    if m:
        first = m.group(1).strip().split("\n")[0].strip()
        first = re.sub(
            r"^(User|Kaeden) (asked|said|requested|noted|handed|delivered)[^.]*\.\s*",
            "",
            first,
            flags=re.I,
        )
        if len(first) > 60:
            cut = first[:60].rsplit(" ", 1)[0]
            first = cut + "…" if cut else first[:57] + "…"
        if first:
            return f"# Session log — {first}"
    if slug:
        return f"# Session log — {slug.replace('-', ' ')}"
    return f"# Session log — {ymd}-{hms}"


def fix_h1(line: str, slug: str | None, dot: str, content: str, ymd: str, hms: str) -> str:
    if not line.startswith("#"):
        return f"# Session log — {slug.replace('-', ' ') if slug else dot}"

    # Retire countdown in H1; keep strengthening `k` pass titles.
    if re.search(r"Session [Ll]og · \d{5}", line) or "99999" in line:
        if slug:
            return f"# Session log — {slug.replace('-', ' ')}"
        parts = [p.strip() for p in re.sub(r"^#\s*", "", line).split("·")]
        if len(parts) >= 3 and parts[2]:
            return f"# Session log — {parts[2]}"
        if len(parts) >= 2 and parts[1]:
            return f"# Session log — {parts[1]}"
        return line

    if line.startswith("# Session Log ·"):
        rest = line.split("·", 1)[-1].strip()
        return f"# Session log — {rest}"

    return repair_weak_h1(line, slug, ymd, hms, content)


def align_file(path: Path) -> tuple[str, dict] | None:
    m = FNAME_RE.match(path.name)
    if not m:
        return None

    ymd, hms, slug = m.group(1), m.group(2), m.group(3)
    dot = dot_stamp(ymd, hms)
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()

    header_end = len(lines)
    for j, line in enumerate(lines):
        if line.startswith("## "):
            header_end = j
            break

    h1 = fix_h1(lines[0] if lines else "", slug, dot, original, ymd, hms)
    new_header: list[str] = [h1, ""]

    had_stamp = False
    had_editor = False
    trailing_meta: list[str] = []

    for line in lines[1:header_end]:
        if re.match(r"^\*\*Countdown:\*\*", line):
            continue
        if re.match(r"^\*\*Clock:\*\*", line):
            continue
        if re.match(r"^\*\*Date:\*\*", line):
            continue
        if re.match(r"^\*\*Agent:\*\*", line):
            continue
        if re.match(r"^\*\*Stamp:\*\*", line):
            new_header.append(f"**Stamp:** `{dot}`")
            had_stamp = True
            continue
        if re.match(r"^\*\*Editor:\*\*", line):
            new_header.append(line.rstrip())
            had_editor = True
            continue
        if line.strip() == "":
            continue
        trailing_meta.append(line.rstrip())

    if not had_stamp:
        new_header.append(f"**Stamp:** `{dot}`")

    if not had_editor:
        ed, mod = infer_editor_model(original, ymd)
        if ed:
            new_header.append(f"**Editor:** {ed} · **Model:** {mod}")

    for meta in trailing_meta:
        new_header.append(meta)

    new_header.append("")
    body = lines[header_end:]
    new_text = "\n".join(new_header + body).rstrip() + "\n"

    meta = {
        "hyphen": hyphen_stamp(ymd, hms),
        "fname": path.name,
        "h1": h1,
        "meaning": extract_meaning(new_text, h1),
    }
    return new_text, meta


def extract_meaning(content: str, h1: str) -> str:
    m = re.search(r"## Thinking trace\s*\n+(.+?)(?:\n\n|\n##|\Z)", content, re.DOTALL)
    if m:
        line = m.group(1).strip().split("\n")[0].strip()
        line = re.sub(r"^(Kaeden|User) (asked|said|requested|noted|delivered)[^.]*\.\s*", "", line, flags=re.I)
        if line:
            return (line[:140] + "…") if len(line) > 140 else line

    m2 = re.search(r"^## (.+)$", content, re.MULTILINE)
    if m2 and m2.group(1) != "Thinking trace":
        return m2.group(1)[:100]

    title = re.sub(r"^#\s*Session log[—·\-]\s*", "", h1, flags=re.I).strip()
    return title[:100] if title else "Session log"


def link_title(h1: str, fname: str) -> str:
    title = re.sub(r"^#\s*", "", h1).strip()
    title = re.sub(r"^Session log\s*[—–\-·]\s*", "", title, flags=re.I).strip()
    if not title or title == fname:
        slug = FNAME_RE.match(fname)
        if slug and slug.group(3):
            return slug.group(3).replace("-", " ")
        return fname.replace(".md", "")
    return title


def rebuild_readme(entries: list[dict]) -> str:
    entries.sort(key=lambda e: e["hyphen"], reverse=True)

    rows = []
    for e in entries:
        title = link_title(e["h1"], e["fname"])
        meaning = e["meaning"].replace("|", "\\|")
        rows.append(
            f"| `{e['hyphen']}` | [{title}]({e['fname']}) | {meaning} |"
        )

    header = """# Session logs

Living index for the append-only session stream. Files sort ascending by stamp; this table reads **newest first**.

Naming follows [`context/specs/20260627-102012_one-clock-naming-law.md`](../context/specs/20260627-102012_one-clock-naming-law.md).

**Filename:** `YYYYMMDD-HHMMSS_short-slug.md` — no countdown prefix. **Body:** `**Stamp:**` in dot form (`YYYYMMDD.HHMMSS`); **Editor** and **Model** at the top per `.claude/rules/session-logs.md`.

**Commit discipline:** ship the log in the **same commit** as the work it records whenever possible. A follow-up commit only for the log is a last resort.

| Stamp | Log | Meaning |
|-------|-----|---------|
"""
    return header + "\n".join(rows) + "\n"


def main() -> None:
    entries: list[dict] = []
    changed = 0

    for path in sorted(SESSION_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        result = align_file(path)
        if result is None:
            continue
        new_text, meta = result
        entries.append(meta)
        old = path.read_text(encoding="utf-8")
        if old != new_text:
            path.write_text(new_text, encoding="utf-8")
            changed += 1

    readme_text = rebuild_readme(entries)
    README.write_text(readme_text, encoding="utf-8")

    print(f"Aligned {len(entries)} logs; {changed} files updated.")
    print(f"README index: {len(entries)} rows.")


if __name__ == "__main__":
    main()
