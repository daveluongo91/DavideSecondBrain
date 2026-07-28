#!/usr/bin/env python3
"""Ricerca testuale semplice nella wiki, senza dipendenze esterne."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"


def main() -> int:
    if len(sys.argv) < 2:
        print('Uso: python scripts/search_wiki.py "testo da cercare"')
        return 2
    query = " ".join(sys.argv[1:]).strip()
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    hits = 0
    for path in sorted(WIKI.rglob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        matches = [(i, line.strip()) for i, line in enumerate(lines, 1) if pattern.search(line)]
        if matches:
            hits += len(matches)
            print(f"\n{path.relative_to(ROOT)}")
            for line_no, line in matches[:8]:
                print(f"  {line_no}: {line}")
            if len(matches) > 8:
                print(f"  … altri {len(matches) - 8} risultati")
    if not hits:
        print(f'Nessun risultato per: "{query}"')
        return 1
    print(f"\nTotale corrispondenze: {hits}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
