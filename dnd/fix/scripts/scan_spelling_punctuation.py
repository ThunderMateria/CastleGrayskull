#!/usr/bin/env python3
"""
Report-only scanner for spelling and punctuation issues in 4e_database_files.

Does NOT edit any files. Outputs candidates for human review. Use the blacklist
file to suppress false positives (entire pattern or specific match).
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = ROOT / "4e_database_files"
BLACKLIST_PATH = Path(__file__).resolve().parent / "spelling_scan_blacklist.txt"

# Pattern id -> (label, search). Search is str (literal) or compiled regex.
PATTERNS: list[tuple[str, str, Any]] = [
    # Known typos (from fix description + manual finds)
    ("typo_actino", "Likely typo: actino → action", "actino"),
    ("typo_leabes", "Likely typo: leabes → leaves", "leabes"),
    ("typo_attackwas", "Likely typo: attackwas → attack was", "attackwas"),
    # Wrong ordinals (21th → 21st, etc.)
    ("ordinal_21th", "Wrong ordinal: 21th → 21st", re.compile(r"\b21th\b")),
    ("ordinal_22th", "Wrong ordinal: 22th → 22nd", re.compile(r"\b22th\b")),
    ("ordinal_23th", "Wrong ordinal: 23th → 23rd", re.compile(r"\b23th\b")),
    ("ordinal_31th", "Wrong ordinal: 31th → 31st", re.compile(r"\b31th\b")),
    # Possibly wrong (Aura vs Area burst) – easy to blacklist if correct in context
    ("maybe_aura_burst_1", "Possibly wrong: Aura burst 1 → Area burst 1?", "Aura burst 1"),
    # Punctuation / spacing (conservative)
    ("comma_period", "Comma followed by period ,.", re.compile(r",\s*\.(?!\d)")),
    ("space_before_period", "Space before period (e.g. 'damage .')", re.compile(r"[a-z]\s+\.(?!\s*\.)(?=\s|$)")),
    ("space_before_closing_p", "Space before </p> (e.g. '. </p>')", " . </p>"),
    ("space_comma_no_space", "Space before comma then no space after (e.g. ' ,word')", re.compile(r"\s,\s*[a-z]")),
    # Double period (but not ellipsis)
    ("double_period", "Double period .. (not ...)", re.compile(r"(?<!\.)\.\.(?!\.)")),
]

SNIPPET_RADIUS = 50


def load_blacklist(blacklist_path: Path) -> tuple[set[str], set[str]]:
    """Load blacklist file. Returns (blacklisted_pattern_ids, blacklisted_match_fingerprints)."""
    blacklisted_patterns: set[str] = set()
    blacklisted_matches: set[str] = set()
    if not blacklist_path.exists():
        return blacklisted_patterns, blacklisted_matches
    for line in blacklist_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("pattern:"):
            blacklisted_patterns.add(line[8:].strip())
        else:
            # Assume "path:line:pattern_id" (match fingerprint)
            blacklisted_matches.add(line)
    return blacklisted_patterns, blacklisted_matches


def extract_entry_id(line: str) -> str | None:
    m = re.search(r'"([a-z]+\d+)":\s*"', line)
    return m.group(1) if m else None


def find_matches(
    content: str,
    path_from_data_root: str,
    pattern_id: str,
    label: str,
    pattern: str | re.Pattern,
) -> Iterable[tuple[int, int, str]]:
    """Yield (line_number, column, snippet) for each match. 1-based line numbers."""
    lines = content.splitlines()
    for i, line in enumerate(lines, start=1):
        if isinstance(pattern, str):
            start = 0
            while True:
                idx = line.find(pattern, start)
                if idx == -1:
                    break
                snippet_start = max(0, idx - SNIPPET_RADIUS)
                snippet_end = min(len(line), idx + len(pattern) + SNIPPET_RADIUS)
                snippet = line[snippet_start:snippet_end]
                if snippet_start > 0:
                    snippet = "…" + snippet
                if snippet_end < len(line):
                    snippet = snippet + "…"
                yield (i, idx + 1, snippet)
                start = idx + 1
        else:
            for m in pattern.finditer(line):
                idx = m.start()
                snippet_start = max(0, idx - SNIPPET_RADIUS)
                snippet_end = min(len(line), m.end() + SNIPPET_RADIUS)
                snippet = line[snippet_start:snippet_end]
                if snippet_start > 0:
                    snippet = "…" + snippet
                if snippet_end < len(line):
                    snippet = snippet + "…"
                yield (i, m.start() + 1, snippet)


def fingerprint(path_from_data_root: str, line_num: int, pattern_id: str) -> str:
    return f"{path_from_data_root}:{line_num}:{pattern_id}"


def scan(
    data_root: Path,
    blacklist_path: Path,
    categories: list[str] | None,
    verbose: bool,
) -> list[dict]:
    blacklisted_patterns, blacklisted_matches = load_blacklist(blacklist_path)
    results: list[dict] = []

    if categories:
        category_dirs = [data_root / c for c in categories]
    else:
        category_dirs = [d for d in data_root.iterdir() if d.is_dir() and not d.name.startswith(".")]
    # Skip res (assets only)
    category_dirs = [d for d in category_dirs if d.name != "res"]

    for cat_dir in sorted(category_dirs, key=lambda p: p.name):
        cat_name = cat_dir.name
        if not cat_dir.is_dir():
            continue
        # Scan _index.js and data*.js only
        for js_file in sorted(cat_dir.glob("_index.js")) + sorted(cat_dir.glob("data*.js")):
            rel_path = js_file.relative_to(data_root)
            path_str = str(rel_path).replace("\\", "/")
            try:
                content = js_file.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                if verbose:
                    results.append({"path": path_str, "error": str(e)})
                continue
            for pattern_id, label, pattern in PATTERNS:
                if pattern_id in blacklisted_patterns:
                    continue
                for line_num, _col, snippet in find_matches(content, path_str, pattern_id, label, pattern):
                    fp = fingerprint(path_str, line_num, pattern_id)
                    if fp in blacklisted_matches:
                        continue
                    lines = content.splitlines()
                    line_content = lines[line_num - 1] if line_num <= len(lines) else ""
                    entry_id = extract_entry_id(line_content)
                    results.append({
                        "path": path_str,
                        "line": line_num,
                        "entry_id": entry_id,
                        "pattern_id": pattern_id,
                        "label": label,
                        "snippet": snippet,
                        "blacklist_match": fp,
                    })
    return results


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Scan 4e_database_files for spelling/punctuation issues (report only, no edits)."
    )
    ap.add_argument(
        "--blacklist",
        type=Path,
        default=BLACKLIST_PATH,
        help="Blacklist file (default: spelling_scan_blacklist.txt in script dir)",
    )
    ap.add_argument(
        "--category",
        action="append",
        dest="categories",
        metavar="NAME",
        help="Limit to category dir(s), e.g. power, feat (repeatable). Use to speed up full scan.",
    )
    ap.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format",
    )
    ap.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Only print count, no details",
    )
    args = ap.parse_args()
    data_root = ROOT / "4e_database_files"
    if not data_root.exists():
        raise SystemExit("4e_database_files not found")
    results = scan(data_root, args.blacklist, args.categories, verbose=not args.quiet)
    if args.format == "json":
        import json
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        if not args.quiet:
            for r in results:
                print(f"File: {r['path']}")
                print(f"Line: {r['line']}")
                if r.get("entry_id"):
                    print(f"Entry: {r['entry_id']}")
                print(f"Pattern: [{r['pattern_id']}] {r['label']}")
                print(f"Snippet: {r['snippet']}")
                print(f"Blacklist this match: {r['blacklist_match']}")
                print("---")
        print(f"Total: {len(results)} match(es)")


if __name__ == "__main__":
    main()
