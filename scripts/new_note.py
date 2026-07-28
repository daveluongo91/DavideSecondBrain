#!/usr/bin/env python3
"""Crea una nuova nota da un template della wiki."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

TYPE_TO_FOLDER = {
    "project": "projects",
    "entity": "people",
    "decision": "decisions",
    "content": "projects",
}
TYPE_TO_TEMPLATE = {
    "project": "project.md",
    "entity": "entity.md",
    "decision": "decision.md",
    "content": "content-idea.md",
}


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9àèéìòù]+", "-", value)
    return value.strip("-")


def main() -> int:
    if len(sys.argv) < 3:
        print('Uso: python scripts/new_note.py project "Titolo"')
        return 2
    note_type = sys.argv[1].lower()
    title = " ".join(sys.argv[2:]).strip()
    if note_type not in TYPE_TO_TEMPLATE:
        print("Tipi supportati: " + ", ".join(sorted(TYPE_TO_TEMPLATE)))
        return 2

    template_path = WIKI / "templates" / TYPE_TO_TEMPLATE[note_type]
    text = template_path.read_text(encoding="utf-8")
    text = re.sub(r"^title:.*$", f"title: {title}", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^type: template$", f"type: {note_type}", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^status: reference$", "status: planned", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^updated:.*$", f"updated: {date.today().isoformat()}", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^summary:.*$", "summary: Da completare.", text, count=1, flags=re.MULTILINE)
    text = text.replace("# Titolo progetto", f"# {title}", 1)
    text = text.replace("# Nome entità", f"# {title}", 1)
    text = text.replace("# Titolo decisione", f"# {title}", 1)
    text = text.replace("# Idea contenuto", f"# {title}", 1)

    dest = WIKI / TYPE_TO_FOLDER[note_type] / f"{slugify(title)}.md"
    if dest.exists():
        print(f"Esiste già: {dest.relative_to(ROOT)}")
        return 1
    dest.write_text(text, encoding="utf-8")
    print(f"Creata: {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
