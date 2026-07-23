#!/usr/bin/env python3
"""
Batch process all remaining secondary power fixes.

This script:
1. Reads fixes-needed.json
2. Finds all powers with status "needs_fix" in the category
3. Processes each one using fix_secondary_power.py
4. Marks each as corrected
5. Validates and regenerates HTML
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

# Project root (parent of fix/)
ROOT = Path(__file__).resolve().parents[2]


def extract_power_name(fix_text: str) -> str:
    """Extract power name from fix text."""
    # Format: "Power Name (Class Type Level) (Source)"
    # Or: "Power Name (Class Type Level) (Source): Additional notes"
    parts = fix_text.split(" (")
    if parts:
        return parts[0].strip()
    return fix_text.split(":")[0].strip()


def main() -> None:
    # Load fixes-needed.json from fix/
    fixes_path = ROOT / "fix" / "fixes-needed.json"
    with fixes_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    
    category = "Powers with secondary powers labeled as encounter/daily that should be at-will"
    items = [i for i in data.get(category, []) if i.get("status") == "needs_fix"]
    
    if not items:
        print("No powers need fixing!")
        return
    
    print(f"Found {len(items)} powers to fix")
    print("=" * 60)
    
    success_count = 0
    failed = []
    
    for i, item in enumerate(items, 1):
        fix_text = item.get("text", "")
        power_name = extract_power_name(fix_text)
        
        print(f"\n[{i}/{len(items)}] Processing: {power_name}")
        print("-" * 60)
        
        # Run fix_secondary_power.py
        result = subprocess.run(
            [
                "python3",
                str(ROOT / "fix" / "scripts" / "fix_secondary_power.py"),
                "--name",
                power_name,
                "--apply",
            ],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        
        if result.returncode != 0:
            print(f"   ✗ FAILED: {result.stderr}")
            failed.append((power_name, fix_text, result.stderr))
            continue
        
        # Check if it says "All changes applied successfully"
        if "All changes applied successfully" in result.stdout:
            print(f"   ✓ Success")
            success_count += 1
            
            # Mark as corrected
            mark_result = subprocess.run(
                [
                    "python3",
                    str(ROOT / "fix" / "scripts" / "mark_fix_corrected.py"),
                    "--text",
                    fix_text,
                ],
                capture_output=True,
                text=True,
                cwd=str(ROOT),
            )
            
            if mark_result.returncode != 0:
                print(f"   ⚠ Warning: Could not mark as corrected: {mark_result.stderr}")
        else:
            print(f"   ✗ FAILED: Script did not report success")
            print(f"   Output: {result.stdout[-500:]}")
            failed.append((power_name, fix_text, "Script did not report success"))
    
    print("\n" + "=" * 60)
    print("BATCH PROCESSING COMPLETE")
    print("=" * 60)
    print(f"Successfully fixed: {success_count}/{len(items)}")
    
    if failed:
        print(f"\nFailed ({len(failed)}):")
        for power_name, fix_text, error in failed:
            print(f"  - {power_name}: {error[:100]}")
    
    # Final validation
    print("\nRunning validation...")
    validate_result = subprocess.run(
        [
            "python3",
            str(ROOT / "fix" / "scripts" / "validate_compendium.py"),
            "--output",
            str(ROOT / "fix" / "compendium-validation.json"),
        ],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    
    if validate_result.returncode == 0:
        print("✓ Validation completed")
    else:
        print(f"✗ Validation failed: {validate_result.stderr}")
    
    # Regenerate HTML
    print("\nRegenerating HTML...")
    html_result = subprocess.run(
        [
            "python3",
            str(ROOT / "fix" / "scripts" / "render_fixes_html.py"),
            "--input",
            "fix/fixes-needed.json",
            "--output",
            "fix/index.htm",
        ],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    
    if html_result.returncode == 0:
        print("✓ HTML regenerated")
    else:
        print(f"✗ HTML regeneration failed: {html_result.stderr}")
    
    print("\n" + "=" * 60)
    print("All done! Review failed items above if any.")
    print("=" * 60)


if __name__ == "__main__":
    main()
