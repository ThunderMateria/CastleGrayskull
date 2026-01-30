#!/usr/bin/env python3
"""
Mark fixes-needed.json entries as corrected by exact text match.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Mark fixes-needed.json items as corrected.")
    parser.add_argument("--input", default="fix/fixes-needed.json", help="Input fixes-needed.json")
    parser.add_argument("--text", required=True, help="Exact fix text to mark corrected")
    parser.add_argument("--output", default=None, help="Output path (default: overwrite input)")
    args = parser.parse_args()

    input_path = Path(args.input)
    data = json.loads(input_path.read_text(encoding="utf-8"))
    target = args.text.strip()
    updated = 0

    for section, items in data.items():
        for item in items:
            if item.get("text") == target:
                item["status"] = "corrected"
                updated += 1

    if updated == 0:
        raise SystemExit("No matching entries found. Check exact text.")

    output_path = Path(args.output) if args.output else input_path
    output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Updated {updated} entr{'y' if updated==1 else 'ies'} to corrected.")


if __name__ == "__main__":
    main()
