#!/usr/bin/env python3
"""
Compare fix/CompendiumErrors.html (full updated list) to fix/fixes-needed.json,
find entries that are in the HTML but not yet in the JSON, and append them
with status "needs_fix".

Run from project root:
  python3 fix/scripts/merge_new_errors.py
  python3 fix/scripts/merge_new_errors.py --dry-run   # print new entries only, do not write
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
import sys
from html.parser import HTMLParser
from pathlib import Path

# Allow importing from same directory when run from project root
_script_dir = Path(__file__).resolve().parent
if str(_script_dir) not in sys.path:
    sys.path.insert(0, str(_script_dir))
from extract_fixes_needed import extract_fixes, KNOWN_HEADINGS

# Section names in HTML sometimes differ from fixes-needed.json keys
SECTION_ALIAS = {
    "Neck": "Necks",
    "Head": "Heads",
    "Armors": "Armor",
    "Feet": "Feet",
    "Hands": "Hands",
    "Arms": "Arms",
    "Waist": "Waist",
    "Rings": "Rings",
    "Wondrous Items": "Wondrous Items",
    "Consumables and Alchemical Items": "Consumables and Alchemical Items",
    "Item Sets": "Item Sets",
    "Races, Classes, Paragon Paths, and Features": "Races, Classes, Paragon Paths, and Features",
    "Backgrounds and Themes": "Backgrounds and Themes",
    "Rituals": "Rituals",
    "Glossary": "Glossary",
    "Other": "Other",
}


def normalize(text: str) -> str:
    """Normalize for comparison: strip, collapse whitespace, normalize quotes/apostrophes."""
    if not text or not isinstance(text, str):
        return ""
    # Unicode normalize and replace common curly/smart quotes with ASCII
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


class CompendiumParser(HTMLParser):
    """
    Parse CompendiumErrors.html into blocks and split on <br> within a block.
    """

    def __init__(self) -> None:
        super().__init__()
        self.blocks: list[dict[str, object]] = []
        self._block_tags = {"p", "li", "h1", "h2", "h3"}
        self._in_block = False
        self._current_tag: str | None = None
        self._current_lines: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self._block_tags:
            self._in_block = True
            self._current_tag = tag
            self._current_lines = [""]
            return
        if tag == "br" and self._in_block:
            self._current_lines.append("")

    def handle_endtag(self, tag: str) -> None:
        if tag in self._block_tags and self._in_block and self._current_tag == tag:
            lines = [normalize(line) for line in self._current_lines if normalize(line)]
            if lines:
                self.blocks.append({"tag": tag, "lines": lines})
            self._in_block = False
            self._current_tag = None
            self._current_lines = []

    def handle_data(self, data: str) -> None:
        if not self._in_block or not self._current_lines:
            return
        cleaned = re.sub(r"\s+", " ", data)
        if not cleaned.strip():
            return
        self._current_lines[-1] = (self._current_lines[-1] + " " + cleaned.strip()).strip()


def collect_existing_texts(fixes_path: Path) -> tuple[set[str], set[str]]:
    """Build sets of normalized text and loose-normalized text."""
    data = json.loads(fixes_path.read_text(encoding="utf-8"))
    seen_texts: set[str] = set()
    seen_loose: set[str] = set()
    for section_items in data.values():
        if not isinstance(section_items, list):
            continue
        for item in section_items:
            if isinstance(item, dict) and "text" in item:
                text = str(item["text"])
                seen_texts.add(normalize(text))
                seen_loose.add(normalize_loose(text))
    return seen_texts, seen_loose


def extract_entries_from_html(html_path: Path) -> dict[str, list[str]]:
    """
    Parse HTML and return { section_name: [ entry_text, ... ] }.
    Splits multi-entry paragraphs into separate entries using <br>.
    """
    html_text = html_path.read_text(encoding="utf-8")
    parser = CompendiumParser()
    parser.feed(html_text)

    result: dict[str, list[str]] = {}
    current_section = "Uncategorized"
    result[current_section] = []

    def is_heading(text: str, tag: str) -> bool:
        if tag in {"h1", "h2", "h3"}:
            return True
        if text in KNOWN_HEADINGS:
            return True
        if text in SECTION_ALIAS:
            return True
        return False

    for block in parser.blocks:
        tag = str(block["tag"])
        lines = block["lines"] if isinstance(block["lines"], list) else []
        if not lines:
            continue
        if is_heading(lines[0], tag):
            current_section = lines[0]
            result.setdefault(current_section, [])
            continue
        for line in lines:
            if len(line) < 5:
                continue
            result.setdefault(current_section, []).append(line)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge new entries from CompendiumErrors.html into fixes-needed.json"
    )
    parser.add_argument(
        "--html",
        default="fix/CompendiumErrors.html",
        help="Path to full errors HTML",
    )
    parser.add_argument(
        "--json",
        default="fix/fixes-needed.json",
        help="Path to fixes-needed.json",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only print new entries, do not write JSON",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    html_path = root / args.html
    json_path = root / args.json

    if not html_path.exists():
        raise SystemExit(f"HTML not found: {html_path}")
    if not json_path.exists():
        raise SystemExit(f"JSON not found: {json_path}")

    existing_normalized, existing_loose = collect_existing_texts(json_path)
    section_to_entries = extract_entries_from_html(html_path)

    # Map section name to key used in fixes-needed.json
    def section_key(name: str) -> str:
        return SECTION_ALIAS.get(name, name)

    new_by_section: dict[str, list[str]] = {}
    for section, entries in section_to_entries.items():
        key = section_key(section)
        for entry in entries:
            normalized_entry = normalize(entry)
            if normalized_entry in existing_normalized:
                continue
            if normalize_loose(entry) in existing_loose:
                continue
            new_by_section.setdefault(key, []).append(entry)

    total_new = sum(len(v) for v in new_by_section.values())
    if total_new == 0:
        print("No new entries found. fixes-needed.json is already up to date with the HTML.")
        return

    print(f"Found {total_new} new entr{'y' if total_new == 1 else 'ies'} to add:\n")
    for section in sorted(new_by_section.keys()):
        items = new_by_section[section]
        print(f"  [{section}] ({len(items)} new)")
        for t in items[:5]:
            print(f"    - {t[:80]}{'...' if len(t) > 80 else ''}")
        if len(items) > 5:
            print(f"    ... and {len(items) - 5} more")
        print()

    if args.dry_run:
        print("(Dry run: no changes written.)")
        return

    data = json.loads(json_path.read_text(encoding="utf-8"))
    for section, new_entries in new_by_section.items():
        target = data.setdefault(section, [])
        for text in new_entries:
            target.append({"text": text, "status": "needs_fix"})
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Updated {json_path} with {total_new} new entries.")


if __name__ == "__main__":
    main()
