#!/usr/bin/env python3
"""
Extract fix entries from errors.md that are NOT already in fixes-needed.json.
Uses the same normalize/normalize_loose logic as merge_new_errors.py so
slight wording or formatting differences still count as "already present".

Run from project root:
  python3 fix/scripts/extract_new_from_errors_md.py
  python3 fix/scripts/extract_new_from_errors_md.py --md path/to/errors.md
  python3 fix/scripts/extract_new_from_errors_md.py --output new_fixes.txt
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path


def normalize(text: str) -> str:
    """Normalize for comparison: strip, collapse whitespace, normalize quotes."""
    if not text or not isinstance(text, str):
        return ""
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_loose(text: str) -> str:
    """Normalize for fuzzy comparison: drop punctuation and case."""
    if not text or not isinstance(text, str):
        return ""
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


def unescape_md(text: str) -> str:
    """Remove markdown backslash escapes so text is comparable to JSON."""
    return re.sub(r"\\(.)", r"\1", text)


def collect_existing( fixes_path: Path) -> tuple[set[str], set[str]]:
    """Build sets of normalized and loose-normalized text from fixes-needed.json."""
    data = json.loads(fixes_path.read_text(encoding="utf-8"))
    seen_norm: set[str] = set()
    seen_loose: set[str] = set()
    for section_items in data.values():
        if not isinstance(section_items, list):
            continue
        for item in section_items:
            if isinstance(item, dict) and "text" in item:
                text = str(item["text"])
                n = normalize(text)
                if n:
                    seen_norm.add(n)
                l = normalize_loose(text)
                if l:
                    seen_loose.add(l)
    return seen_norm, seen_loose


# Section headers that appear as a single **X** line (no colon) in errors.md
STANDALONE_HEADERS = {
    "neck", "necks", "head", "heads", "hands", "arms", "waist", "feet", "rings",
    "wondrous items", "tattoos", "companions", "alternative rewards",
    "items", "weapons", "implements", "armor", "armors", "consumables and alchemical items",
    "item sets", "races, classes, paragon paths, and features",
    "backgrounds and themes", "rituals", "glossary", "other",
}


def parse_errors_md(md_path: Path) -> list[tuple[str | None, str]]:
    """
    Parse errors.md into (section, entry_text) pairs.
    Section can be None for lines before any section.
    """
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    section: str | None = None
    out: list[tuple[str | None, str]] = []

    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        # Section: # **Powers** or ***Powers with augments*** or **Neck**
        if line.startswith("# "):
            # "# **Powers**" -> Powers
            section = line.lstrip("# ").strip().strip("*").strip()
            continue
        if line.startswith("***") and line.endswith("***"):
            # Subsection: keep parent (e.g. Powers)
            continue
        if line.startswith("**") and line.endswith("**") and ":" not in line:
            inner = line.strip("*").strip()
            if inner.lower() in STANDALONE_HEADERS:
                section = inner
                continue
        # Entry line: **Name (Source):** description or **Name (Source)**
        if line.startswith("**") and len(line) > 4:
            cleaned = line.strip()
            if cleaned.startswith("**"):
                cleaned = cleaned[2:]
            if cleaned.endswith("**"):
                cleaned = cleaned[:-2].strip()
            elif cleaned.endswith("**:"):
                cleaned = cleaned[:-3].strip()
            elif ":**" in cleaned:
                cleaned = cleaned  # keep full line
            cleaned = unescape_md(cleaned)
            if len(cleaned) < 4:
                continue
            out.append((section, cleaned))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find entries in errors.md that are not in fixes-needed.json"
    )
    parser.add_argument(
        "--md",
        default="errors.md",
        help="Path to errors.md",
    )
    parser.add_argument(
        "--json",
        default="fix/fixes-needed.json",
        help="Path to fixes-needed.json",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Write new entries to this file (default: print only)",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    md_path = root / args.md
    json_path = root / args.json

    if not md_path.exists():
        raise SystemExit(f"MD file not found: {md_path}")
    if not json_path.exists():
        raise SystemExit(f"JSON not found: {json_path}")

    seen_norm, seen_loose = collect_existing(json_path)
    entries = parse_errors_md(md_path)

    new_entries: list[tuple[str | None, str]] = []
    for section, entry in entries:
        n = normalize(entry)
        l = normalize_loose(entry)
        if n in seen_norm or l in seen_loose:
            continue
        # Also skip if any existing fix text is a substring (handles "X (Source):" in JSON vs "X (Source): desc" in MD)
        if not n and not l:
            continue
        is_covered = False
        for existing_loose in seen_loose:
            if len(existing_loose) < 20:
                continue
            # If 80% of words in entry appear in an existing fix, treat as same
            words = set(l.split())
            existing_words = set(existing_loose.split())
            overlap = len(words & existing_words) / max(len(words), 1)
            if overlap >= 0.75:
                is_covered = True
                break
        if is_covered:
            continue
        new_entries.append((section, entry))

    if not new_entries:
        print("No new entries found. Every errors.md line matches something in fixes-needed.json.")
        return

    lines_out = []
    lines_out.append(f"# Entries in errors.md not found in fixes-needed.json ({len(new_entries)})\n")
    cur_section: str | None = None
    for section, entry in new_entries:
        if section != cur_section:
            cur_section = section
            lines_out.append(f"\n## {section or 'Uncategorized'}\n")
        lines_out.append(f"- {entry}\n")

    result = "".join(lines_out)
    if args.output:
        out_path = root / args.output
        out_path.write_text(result, encoding="utf-8")
        print(f"Wrote {len(new_entries)} new entries to {out_path}")
    else:
        print(result)


if __name__ == "__main__":
    main()
