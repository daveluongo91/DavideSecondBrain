#!/usr/bin/env python3
"""Rigenera wiki/index.md leggendo il frontmatter delle pagine Markdown."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
INDEX = WIKI / "index.md"
SKIP = {INDEX, WIKI / "log.md"}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            data[key] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    groups: dict[str, list[tuple[str, str, str, str]]] = defaultdict(list)
    for path in sorted(WIKI.rglob("*.md")):
        if path in SKIP:
            continue
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        rel = path.relative_to(WIKI)
        title = fm.get("title") or path.stem.replace("-", " ").title()
        summary = fm.get("summary") or "Nessun riassunto disponibile."
        status = fm.get("status") or "unknown"
        group = rel.parts[0] if len(rel.parts) > 1 else "root"
        groups[group].append((title, rel.as_posix(), summary, status))

    labels = {
        "dashboards": "Dashboard",
        "profile": "Profilo",
        "areas": "Aree",
        "projects": "Progetti",
        "gear": "Attrezzatura",
        "knowledge": "Conoscenza",
        "workflows": "Workflow",
        "people": "Persone",
        "organizations": "Organizzazioni",
        "decisions": "Decisioni",
        "questions": "Domande",
        "templates": "Template",
        "root": "Altro",
    }

    lines = [
        "# Indice",
        "",
        "Catalogo generato automaticamente da `python scripts/rebuild_index.py`.",
        "",
        "- [Home](home.md)",
        "- [Log](log.md)",
        "",
    ]
    order = list(labels)
    for group in order:
        entries = groups.get(group)
        if not entries:
            continue
        lines.append(f"## {labels[group]}")
        lines.append("")
        for title, rel, summary, status in sorted(entries, key=lambda x: x[0].lower()):
            lines.append(f"- [{title}]({rel}) — {summary} _({status})_")
        lines.append("")

    INDEX.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Indice aggiornato: {INDEX.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
