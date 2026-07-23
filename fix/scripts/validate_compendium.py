#!/usr/bin/env python3
"""
Validate integrity of 4e_database_files.

Checks:
- IDs in _listing.js have matching entries in dataN.js and _index.js
- dataN.js routing matches id suffix % 20
- _index.js does not contain IDs missing from listing (optional)
- global name index entries resolve to existing IDs
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple


# Project root (parent of fix/)
ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = ROOT / "4e_database_files"


def _extract_ids_from_listing(text: str) -> Set[str]:
    return set(re.findall(r'\\["\']([a-z]+\\d+)\\["\']', text))


def _extract_ids_from_index(text: str) -> Set[str]:
    return set(re.findall(r'\\["\']([a-z]+\\d+)\\["\']\\s*:', text))


def _extract_ids_from_data(text: str) -> Set[str]:
    return set(re.findall(r'\\["\']([a-z]+\\d+)\\["\']\\s*:', text))


def _id_to_bucket(entry_id: str) -> int:
    match = re.search(r"(\\d{1,2})$", entry_id)
    if not match:
        return -1
    return int(match.group(1)) % 20


def _load_js(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def validate_category(category_dir: Path) -> Dict[str, object]:
    name = category_dir.name
    listing_path = category_dir / "_listing.js"
    index_path = category_dir / "_index.js"

    results = {
        "category": name,
        "missing_data": [],
        "missing_index": [],
        "misrouted_data": [],
        "extra_index": [],
    }

    if not listing_path.exists():
        return results

    listing_ids = _extract_ids_from_listing(_load_js(listing_path))
    index_ids = _extract_ids_from_index(_load_js(index_path)) if index_path.exists() else set()

    # Build data file ID map
    data_ids_by_file: Dict[str, Set[str]] = {}
    for n in range(20):
        data_path = category_dir / f"data{n}.js"
        if not data_path.exists():
            continue
        data_ids_by_file[data_path.name] = _extract_ids_from_data(_load_js(data_path))

    # Validate listing IDs -> data + index
    for entry_id in sorted(listing_ids):
        bucket = _id_to_bucket(entry_id)
        if bucket < 0:
            continue
        data_file = f"data{bucket}.js"
        data_ids = data_ids_by_file.get(data_file, set())
        if entry_id not in data_ids:
            results["missing_data"].append({"id": entry_id, "expected_file": data_file})
        if index_path.exists() and entry_id not in index_ids:
            results["missing_index"].append(entry_id)

    # Validate index IDs not in listing (optional)
    extra_index = sorted(list(index_ids - listing_ids))
    results["extra_index"] = extra_index

    # Validate data routing (id in wrong file)
    for file_name, ids in data_ids_by_file.items():
        for entry_id in ids:
            bucket = _id_to_bucket(entry_id)
            if bucket < 0:
                continue
            expected = f"data{bucket}.js"
            if expected != file_name:
                results["misrouted_data"].append({"id": entry_id, "actual_file": file_name, "expected_file": expected})

    return results


def validate_global_name_index() -> List[str]:
    index_path = DATA_ROOT / "index.js"
    if not index_path.exists():
        return []
    text = _load_js(index_path)
    name_to_ids = re.findall(r'\\["\']([^"\']+)\\["\']\\s*:\\s*\\["\']([^"\']+)\\["\']', text)
    # Build a global set of valid IDs
    valid_ids: Set[str] = set()
    for category_dir in DATA_ROOT.iterdir():
        if not category_dir.is_dir() or category_dir.name == "res":
            continue
        listing = category_dir / "_listing.js"
        if listing.exists():
            valid_ids |= _extract_ids_from_listing(_load_js(listing))

    missing = []
    for _, entry_id in name_to_ids:
        if entry_id not in valid_ids:
            missing.append(entry_id)
    return missing


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate 4e_database_files integrity.")
    default_output = ROOT / "fix" / "compendium-validation.json"
    parser.add_argument("--output", default=str(default_output), help="Output JSON report path")
    args = parser.parse_args()

    report = {"categories": [], "global_name_index_missing": []}

    for category_dir in sorted(DATA_ROOT.iterdir()):
        if not category_dir.is_dir() or category_dir.name == "res":
            continue
        report["categories"].append(validate_category(category_dir))

    report["global_name_index_missing"] = validate_global_name_index()

    Path(args.output).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
