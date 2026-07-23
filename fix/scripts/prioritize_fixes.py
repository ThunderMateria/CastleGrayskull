#!/usr/bin/env python3
"""
Prioritize fixes-needed.json by heuristic complexity.

This script reads fixes-needed.json and outputs fixes-priority.json with
simple/medium/complex labels and a brief reason.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple


SIMPLE_HINTS = [
    "misspelled",
    "typo",
    "extra space",
    "spacing",
    "should be",
    "should say",
    "should read",
    "listed as",
    "remove",
    "replace",
    "keyword",
    "color",
    "miscolored",
    "add \"rolls\"",
    "add \"the\"",
    "missing the word",
]

MEDIUM_HINTS = [
    "missing line",
    "missing target line",
    "missing effect line",
    "missing requirement",
    "missing prerequisite",
    "missing power",
    "missing powers",
    "add the following",
    "change to",
    "incorrect",
    "should not have",
    "should have",
]

COMPLEX_HINTS = [
    "missing entirely",
    "missing rules",
    "missing mechanics",
    "missing options",
    "missing class features",
    "missing feature",
    "missing entries",
    "duplicated",
    "incorrect defenses",
    "incorrect attack",
    "missing from compendium",
    "not exist",
    "not appear",
]


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).lower()


def classify(text: str) -> Tuple[str, str]:
    t = _normalize(text)
    for hint in COMPLEX_HINTS:
        if hint in t:
            return "complex", f"matched '{hint}'"
    for hint in MEDIUM_HINTS:
        if hint in t:
            return "medium", f"matched '{hint}'"
    for hint in SIMPLE_HINTS:
        if hint in t:
            return "simple", f"matched '{hint}'"
    # Default to medium when unsure.
    return "medium", "default heuristic"


def prioritize(input_path: Path) -> Dict[str, object]:
    data = json.loads(input_path.read_text(encoding="utf-8"))
    result: Dict[str, object] = {"sections": {}, "summary": {"simple": 0, "medium": 0, "complex": 0}}

    for section, items in data.items():
        out_items: List[Dict[str, str]] = []
        for item in items:
            if item.get("status") != "needs_fix":
                continue
            text = item.get("text", "")
            complexity, reason = classify(text)
            result["summary"][complexity] += 1
            out_items.append(
                {
                    "text": text,
                    "complexity": complexity,
                    "reason": reason,
                }
            )
        # Order: simple -> medium -> complex
        out_items.sort(key=lambda x: {"simple": 0, "medium": 1, "complex": 2}[x["complexity"]])
        result["sections"][section] = out_items

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Prioritize fixes by heuristic complexity.")
    parser.add_argument("--input", default="fix/fixes-needed.json", help="Input JSON from extract_fixes_needed.py")
    parser.add_argument("--output", default="fix/fixes-priority.json", help="Output JSON path")
    args = parser.parse_args()

    result = prioritize(Path(args.input))
    Path(args.output).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
