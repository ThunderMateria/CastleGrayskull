#!/usr/bin/env python3
"""
Run validation and exit with error if any issues found.
Use this as a pre-deploy check.

Usage:
    python3 fix/scripts/check_validation.py

Exit codes:
    0 - All clean
    1 - Validation found issues (DO NOT DEPLOY)
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATION_SCRIPT = ROOT / "fix" / "scripts" / "validate_compendium.py"
VALIDATION_OUTPUT = ROOT / "fix" / "compendium-validation.json"


def main() -> int:
    # Run validation
    print("Running compendium validation...")
    result = subprocess.run(
        [sys.executable, str(VALIDATION_SCRIPT), "--output", str(VALIDATION_OUTPUT)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Validation script failed: {result.stderr}")
        return 1

    # Check results
    report = json.loads(VALIDATION_OUTPUT.read_text())
    
    issues = []
    for cat in report.get("categories", []):
        name = cat["category"]
        if cat["missing_data"]:
            issues.append(f"  {name}: {len(cat['missing_data'])} entries in listing but missing from data files")
        if cat["missing_index"]:
            issues.append(f"  {name}: {len(cat['missing_index'])} entries missing from _index.js")
        if cat["misrouted_data"]:
            issues.append(f"  {name}: {len(cat['misrouted_data'])} entries in wrong dataN.js file")
        # extra_index is informational, not blocking

    if report.get("global_name_index_missing"):
        issues.append(f"  global index: {len(report['global_name_index_missing'])} names point to missing IDs")

    if issues:
        print("\n❌ VALIDATION FAILED - DO NOT DEPLOY\n")
        print("Issues found:")
        for issue in issues:
            print(issue)
        print(f"\nSee {VALIDATION_OUTPUT} for details.")
        return 1

    print("\n✅ Validation passed - all clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
