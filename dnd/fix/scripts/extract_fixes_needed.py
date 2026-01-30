#!/usr/bin/env python3
"""
Extract structured fixes from fixes-needed.html.

Outputs JSON with sections and items, preserving "corrected" (strikethrough) status.
This script does not modify any compendium data.
"""
from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional


def _parse_strike_classes(html_text: str) -> set[str]:
    """Return CSS class names that include line-through decoration."""
    strike_classes: set[str] = set()
    style_match = re.search(r"<style[^>]*>(.*?)</style>", html_text, re.S | re.I)
    if not style_match:
        return strike_classes
    css = style_match.group(1)
    for class_block in re.finditer(r"\.([a-zA-Z0-9_-]+)\s*\{([^}]*)\}", css):
        class_name = class_block.group(1)
        props = class_block.group(2)
        if "line-through" in props:
            strike_classes.add(class_name)
    return strike_classes


class FixesParser(HTMLParser):
    def __init__(self, strike_classes: set[str]) -> None:
        super().__init__()
        self.strike_classes = strike_classes
        self.blocks: List[Dict[str, object]] = []
        self._current_block: Optional[Dict[str, object]] = None
        self._block_tags = {"p", "h1", "h2", "h3", "li"}
        self._strike_stack: List[bool] = []
        self._in_block = False

    def handle_starttag(self, tag: str, attrs: List[tuple[str, Optional[str]]]) -> None:
        attrs_dict = {k: v for k, v in attrs}
        if tag in self._block_tags:
            self._in_block = True
            self._current_block = {
                "tag": tag,
                "text_parts": [],
                "strike_parts": [],
            }
        if tag == "span":
            class_attr = attrs_dict.get("class") or ""
            classes = set(class_attr.split())
            is_strike = bool(classes & self.strike_classes)
            self._strike_stack.append(is_strike)

    def handle_endtag(self, tag: str) -> None:
        if tag == "span" and self._strike_stack:
            self._strike_stack.pop()
        if tag in self._block_tags and self._current_block:
            text = " ".join(self._current_block["text_parts"]).strip()
            if text:
                strike_parts = self._current_block["strike_parts"]
                has_strike = any(strike_parts)
                has_plain = any(not s for s in strike_parts) if strike_parts else False
                status = "mixed" if has_strike and has_plain else ("corrected" if has_strike else "needs_fix")
                self.blocks.append(
                    {
                        "tag": self._current_block["tag"],
                        "text": text,
                        "status": status,
                    }
                )
            self._current_block = None
            self._in_block = False

    def handle_data(self, data: str) -> None:
        if not self._in_block or not self._current_block:
            return
        cleaned = re.sub(r"\s+", " ", data)
        if not cleaned.strip():
            return
        self._current_block["text_parts"].append(cleaned.strip())
        is_strike = self._strike_stack[-1] if self._strike_stack else False
        self._current_block["strike_parts"].append(is_strike)


KNOWN_HEADINGS = {
    "Powers",
    "Powers with augments that should have the Augmentable keyword",
    "Powers with secondary attacks that should be encounter, not daily",
    "Powers with secondary powers labeled as encounter/daily that should be at-will",
    "Powers that are miscolored (should be daily grey)",
    "Feats",
    "Feats that should be labeled as Paragon",
    "Paragon Multiclassing feats (should be Paragon)",
    "Feats that should be labeled as Epic",
    "Items",
    "Weapons",
    "Implements",
    "Armor",
    "Necks",
    "Heads",
    "Hands",
    "Rings",
    "Arms",
    "Waist",
    "Feet",
    "Wondrous Items",
    "Tattoos",
    "Companions",
    "Alternative Rewards",
    "Consumables and Alchemical Items",
    "Item Sets",
    "Races, Classes, Paragon Paths, and Features",
    "Backgrounds and Themes",
    "Rituals",
    "Glossary",
    "Other",
}


def _is_heading(text: str, tag: str) -> bool:
    if tag in {"h1", "h2", "h3"}:
        return True
    if text in KNOWN_HEADINGS:
        return True
    if len(text) <= 40 and text.isalpha():
        return True
    return False


def extract_fixes(html_path: Path) -> Dict[str, List[Dict[str, str]]]:
    html_text = html_path.read_text(encoding="utf-8")
    strike_classes = _parse_strike_classes(html_text)
    parser = FixesParser(strike_classes)
    parser.feed(html_text)

    sections: Dict[str, List[Dict[str, str]]] = {}
    current_section = "Uncategorized"
    sections[current_section] = []

    for block in parser.blocks:
        text = block["text"]
        tag = block["tag"]
        status = block["status"]
        if _is_heading(text, tag):
            current_section = text
            sections.setdefault(current_section, [])
            continue
        sections[current_section].append({"text": text, "status": status})

    return sections


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract fixes-needed.html into structured JSON.")
    parser.add_argument(
        "--input",
        default="fix/fixes-needed.html",
        help="Path to fixes-needed.html",
    )
    parser.add_argument(
        "--output",
        default="fix/fixes-needed.json",
        help="Output JSON path",
    )
    parser.add_argument(
        "--section",
        default=None,
        help="Optional section filter (case-insensitive substring match).",
    )
    args = parser.parse_args()

    sections = extract_fixes(Path(args.input))
    if args.section:
        needle = args.section.lower()
        sections = {k: v for k, v in sections.items() if needle in k.lower()}

    output_path = Path(args.output)
    output_path.write_text(json.dumps(sections, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
