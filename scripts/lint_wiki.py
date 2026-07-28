#!/usr/bin/env python3
"""Controlla frontmatter, link interni e pagine orfane della wiki."""

from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
REQUIRED = {"title", "type", "status", "updated", "summary", "tags"}
FRONTMATTER_EXEMPT = {WIKI / "index.md", WIKI / "log.md"}
ORPHAN_EXEMPT = FRONTMATTER_EXEMPT | {WIKI / "home.md"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):", re.MULTILINE)


def frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    md_files = sorted(WIKI.rglob("*.md"))
    inbound = {path.resolve(): 0 for path in md_files}

    for path in md_files:
        text = path.read_text(encoding="utf-8")
        if path not in FRONTMATTER_EXEMPT:
            fm = frontmatter(text)
            if fm is None:
                errors.append(f"{path.relative_to(ROOT)}: frontmatter mancante o non chiuso")
            else:
                keys = set(KEY_RE.findall(fm))
                missing = REQUIRED - keys
                if missing:
                    errors.append(
                        f"{path.relative_to(ROOT)}: campi frontmatter mancanti: {', '.join(sorted(missing))}"
                    )

        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / target).resolve()
            if resolved.is_dir():
                resolved = resolved / "README.md"
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: link rotto -> {raw_target}")
            elif resolved.suffix.lower() == ".md" and resolved in inbound:
                inbound[resolved] += 1

    for path, count in inbound.items():
        if count == 0 and path not in {p.resolve() for p in ORPHAN_EXEMPT}:
            if "templates" not in path.parts:
                warnings.append(f"{path.relative_to(ROOT)}: possibile pagina orfana")

    print(f"File controllati: {len(md_files)}")
    if warnings:
        print("\nAvvisi:")
        for warning in warnings:
            print(f"- {warning}")
    if errors:
        print("\nErrori:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\nLint completato senza errori.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
