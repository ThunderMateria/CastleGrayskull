#!/usr/bin/env python3
"""
Extract full <div id="detail"> HTML from Portable Compendium Glossary SQL by line regex.

Use this when portable_sql_extract.py returns null DetailHtml (e.g. long or
malformed strings with unescaped apostrophes like "item's"). This script does
NOT parse the full VALUES clause; it finds the INSERT line for the given ID and
extracts the detail div with a regex, so it is robust to unescaped quotes inside
the HTML.

Caveat: Content is taken up to the first </div>. If a glossary entry ever
contains a nested <div>...</div> inside the detail block, we would truncate
there. For standard glossary entries this does not occur.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def _sql_unescape(value: str) -> str:
    return (
        value.replace("\\r", "\r")
        .replace("\\n", "\n")
        .replace("\\t", "\t")
        .replace("\\'", "'")
        .replace('\\"', '"')
        .replace("\\\\", "\\")
    )


def extract_glossary_detail_by_id(sql_path: Path, glossary_id: str) -> str | None:
    """
    Find the INSERT line for this glossary ID and extract the content of
    <div id="detail">...</div> from the raw line using regex (no full VALUES parse).
    """
    prefix = f"INSERT INTO `Glossary` VALUES ('{glossary_id}',"
    # In the SQL file, double-quotes in the HTML may be stored as \"
    # Match either id="detail"> or id=\"detail\">
    detail_start = re.compile(r'id=\\"detail\\">', re.IGNORECASE)
    # Capture from there until the first </div> (non-greedy, DOTALL for newlines)
    detail_pattern = re.compile(r'id=\\"detail\\">(.*?)</div>', re.DOTALL | re.IGNORECASE)

    with sql_path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if not line.startswith(prefix):
                continue
            match = detail_pattern.search(line)
            if not match:
                return None
            raw = match.group(1)
            return _sql_unescape(raw).strip()
    return None


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract full glossary detail HTML from raw SQL by ID (regex-based)."
    )
    parser.add_argument(
        "--sql-dir",
        default="Portable Compendium New/sql",
        help="Directory containing ddiGlossary.sql",
    )
    parser.add_argument(
        "--ids",
        required=True,
        nargs="+",
        help="Glossary IDs to extract (e.g. 170 366 370 424 472 680)",
    )
    parser.add_argument(
        "--output",
        default="glossary_full_extract.json",
        help="Output JSON file with id -> detailHtml",
    )
    args = parser.parse_args()

    sql_path = Path(args.sql_dir) / "ddiGlossary.sql"
    if not sql_path.exists():
        raise SystemExit(f"SQL file not found: {sql_path}")

    result: dict[str, str | None] = {}
    for gid in args.ids:
        html = extract_glossary_detail_by_id(sql_path, gid)
        result[gid] = html
        status = "ok" if html else "missing"
        print(f"glossary {gid}: {status} (len={len(html) if html else 0})")

    Path(args.output).write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
