#!/usr/bin/env python3
"""
Helper script to fix secondary powers labeled as encounter/daily → at-will.

This script:
1. Extracts correct version from Portable Compendium SQL
2. Identifies the power in the data files
3. Makes the necessary replacements
4. Updates the index
5. Provides a diff for review

Usage:
    python3 fix/scripts/fix_secondary_power.py --name "Thunder Hawk Rage"
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Optional, Tuple

# Project root (parent of fix/)
ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = ROOT / "4e_database_files" / "power"
SQL_DIR = ROOT / "Portable Compendium New" / "sql"


def extract_power_from_sql(power_name: str, power_id: Optional[str] = None) -> Optional[dict]:
    """Extract power from Portable Compendium SQL."""
    import subprocess
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name
    
    try:
        # If we have an ID, use that (more reliable, especially for names with apostrophes)
        if power_id:
            cmd = [
                "python3",
                str(ROOT / "fix" / "scripts" / "portable_sql_extract.py"),
                "--table", "power",
                "--id", power_id,
                "--limit", "1",
                "--extract-detail",
                "--output", temp_path,
            ]
        else:
            cmd = [
                "python3",
                str(ROOT / "fix" / "scripts" / "portable_sql_extract.py"),
                "--table", "power",
                "--name", power_name,
                "--limit", "1",
                "--extract-detail",
                "--output", temp_path,
            ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        
        # Always try to read the file, even if returncode is non-zero
        # (sometimes the script succeeds but writes warnings to stderr)
        if not Path(temp_path).exists():
            # File wasn't created - this is an error
            return None
        
        try:
            with open(temp_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if data.get("records") and len(data["records"]) > 0:
                return data["records"][0]
        except Exception as e:
            # If returncode is 0 but we can't read, that's a real error
            return None
        
        # No records found
        return None
    finally:
        Path(temp_path).unlink(missing_ok=True)


def find_power_id(power_name: str) -> Optional[Tuple[str, int]]:
    """Find power ID and calculate data file number."""
    listing_path = DATA_ROOT / "_listing.js"
    if not listing_path.exists():
        return None
    
    text = listing_path.read_text(encoding='utf-8')
    
    # Find power name in listing (format: ["powerID", "Power Name", ...])
    # Power name is in the second column (index 1)
    # Pattern: ["powerID", "Power Name", ...] - handle newlines and whitespace
    # The listing can have the array elements on separate lines
    pattern = rf'\[\s*"([a-z]+\d+)"\s*,\s*"[^"]*{re.escape(power_name)}[^"]*"'
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    
    if not match:
        return None
    
    power_id = match.group(1)
    # Extract numeric suffix
    num_match = re.search(r'(\d+)$', power_id)
    if not num_match:
        return None
    
    num = int(num_match.group(1))
    return (power_id, num % 20)


def fix_secondary_power_in_data(data_file: Path, power_id: str, correct_html: str) -> Tuple[bool, str, str, str]:
    """
    Fix secondary power in data file.
    Returns: (success, old_text, new_text)
    """
    text = data_file.read_text(encoding='utf-8')
    
    # Find the power entry - it's on a single line in JSON format
    pattern = rf'"{re.escape(power_id)}"\s*:\s*"([^"]+)"'
    match = re.search(pattern, text)
    
    if not match:
        return (False, "", "", "Power ID not found in data file")
    
    old_html = match.group(1)
    
    # Normalize correct_html (remove HTML entities, normalize tags)
    correct_html = correct_html.replace('&nbsp;', ' ')
    correct_html = correct_html.replace('<br/>', '<br>')
    correct_html = correct_html.replace('&quot;', '"')
    
    # Find secondary power header in old HTML (second h1 tag)
    # Pattern: <h1 class=dailypower>Name</h1> or <h1 class=encounterpower>Name</h1>
    # Use a simpler approach: find all h1 opening tags, then match to their closing tags
    h1_matches = []
    pos = 0
    while True:
        # Find next h1 opening tag
        h1_start = old_html.find('<h1 class=', pos)
        if h1_start == -1:
            break
        
        # Find the class name (handle both quoted and unquoted)
        class_match = re.search(r'class=["\']?(dailypower|encounterpower|atwillpower)["\']?', old_html[h1_start:h1_start+50])
        if not class_match:
            pos = h1_start + 1
            continue
        
        class_name = class_match.group(1)
        
        # Find the closing > of the opening tag
        tag_end = old_html.find('>', h1_start)
        if tag_end == -1:
            pos = h1_start + 1
            continue
        
        # Find the closing </h1>
        h1_end = old_html.find('</h1>', tag_end)
        if h1_end == -1:
            pos = h1_start + 1
            continue
        
        h1_end += 5  # Include </h1>
        
        # Extract content and power name
        content = old_html[tag_end+1:h1_end-5]  # Content between > and </h1>
        # Get text before first < tag for name
        name_match = re.search(r'^([^<]+)', content)
        power_name_text = name_match.group(1).strip() if name_match else content.strip()
        
        h1_matches.append((h1_start, h1_end, class_name, power_name_text, old_html[h1_start:h1_end]))
        pos = h1_end
    
    if len(h1_matches) < 2:
        # Some powers might not have secondary powers - check if this is expected
        if len(h1_matches) == 1:
            return (False, old_html, old_html, f"Power has only one h1 tag - no secondary power to fix (this power may not belong in this category)")
        return (False, old_html, old_html, f"Could not find secondary power (found {len(h1_matches)} h1 tags)")
    
    # The second h1 is the secondary power
    secondary_h1_info = h1_matches[1]
    secondary_power_name = secondary_h1_info[3]  # The name text
    secondary_h1_start = secondary_h1_info[0]
    secondary_h1_end = secondary_h1_info[1]
    secondary_h1_full = secondary_h1_info[4]  # The full match
    
    # Find the same secondary power in correct HTML using same approach
    correct_h1_matches = []
    pos = 0
    while True:
        h1_start = correct_html.find('<h1 class=', pos)
        if h1_start == -1:
            break
        class_match = re.search(r'class=["\']?(dailypower|encounterpower|atwillpower)["\']?', correct_html[h1_start:h1_start+50])
        if not class_match:
            pos = h1_start + 1
            continue
        class_name = class_match.group(1)
        tag_end = correct_html.find('>', h1_start)
        if tag_end == -1:
            pos = h1_start + 1
            continue
        h1_end = correct_html.find('</h1>', tag_end)
        if h1_end == -1:
            pos = h1_start + 1
            continue
        h1_end += 5
        content = correct_html[tag_end+1:h1_end-5]
        # Extract text content, removing HTML tags
        text_content = re.sub(r'<[^>]+>', '', content).strip()
        # Get the actual power name (all text, cleaned up)
        power_name_text = ' '.join(text_content.split()) if text_content else content.strip()
        correct_h1_matches.append((class_name, power_name_text, content))
        pos = h1_end
    
    if len(correct_h1_matches) < 2:
        return (False, old_html, old_html, "Could not find secondary power in correct HTML")
    
    correct_secondary_h1 = correct_h1_matches[1]
    # Compare names (handle case where correct has span tags)
    correct_name_clean = correct_secondary_h1[1]  # Already cleaned in extraction
    
    # Normalize names for comparison (handle spaces around apostrophes, etc.)
    def normalize_name(name):
        # Remove extra spaces, normalize apostrophes
        name = ' '.join(name.split())  # Normalize whitespace
        name = name.replace(" '", "'").replace("' ", "'")  # Fix apostrophe spacing
        return name.strip()
    
    if normalize_name(correct_name_clean) != normalize_name(secondary_power_name):
        return (False, old_html, old_html, f"Secondary power name mismatch: '{secondary_power_name}' vs '{correct_name_clean}'")
    
    # Check that correct version has atwillpower
    if correct_secondary_h1[0] != 'atwillpower':
        return (False, old_html, old_html, f"Correct version doesn't have atwillpower class (has {correct_secondary_h1[0]})")
    
    # Replace the secondary power header - keep the original content but change class
    # Extract the content part (everything between > and </h1>)
    content_match = re.search(r'>([^<]*(?:<[^>]+>[^<]*)*)</h1>', secondary_h1_full)
    content = content_match.group(1) if content_match else secondary_power_name
    new_h1 = f'<h1 class=atwillpower>{content}</h1>'
    new_html = old_html[:secondary_h1_start] + new_h1 + old_html[secondary_h1_end:]
    
    # Find and replace the usage label in secondary power section
    # Find the powerstat line that comes after the secondary power header
    # Look for <b>Daily</b> or <b>Encounter</b> that appears after the secondary h1
    secondary_start = new_html.find(new_h1)
    if secondary_start == -1:
        return (False, old_html, new_html, "Could not find secondary power header in new HTML")
    
    secondary_section = new_html[secondary_start:]
    
    # Replace Daily or Encounter with At-Will in the secondary power's powerstat
    # Pattern: <b>Daily</b> or <b>Encounter</b> in powerstat after secondary h1
    daily_pattern = r'(<p class=powerstat><b>)Daily(</b>)'
    encounter_pattern = r'(<p class=powerstat><b>)Encounter(</b>)'
    
    # Only replace if it's in the secondary section (after the secondary h1)
    daily_match = re.search(daily_pattern, secondary_section)
    encounter_match = re.search(encounter_pattern, secondary_section)
    
    if daily_match:
        # Replace Daily with At-Will
        replacement_start = secondary_start + daily_match.start()
        replacement_end = secondary_start + daily_match.end()
        new_html = new_html[:replacement_start] + daily_match.group(1) + 'At-Will' + daily_match.group(2) + new_html[replacement_end:]
    elif encounter_match:
        # Replace Encounter with At-Will
        replacement_start = secondary_start + encounter_match.start()
        replacement_end = secondary_start + encounter_match.end()
        new_html = new_html[:replacement_start] + encounter_match.group(1) + 'At-Will' + encounter_match.group(2) + new_html[replacement_end:]
    else:
        return (False, old_html, new_html, "Could not find Daily or Encounter label in secondary power section")
    
    return (True, old_html, new_html, secondary_power_name)


def fix_index(power_id: str, secondary_power_name: str, old_index: str) -> Tuple[bool, str, str]:
    """Fix power in _index.js by finding secondary power text and replacing Daily/Encounter with At-Will."""
    # Find the secondary power text in the index (it comes after the primary power text)
    # Look for the secondary power name followed by "Daily" or "Encounter"
    # Pattern: "Secondary Power Name Daily" or "Secondary Power Name Encounter"
    # Try with ✦ first
    secondary_pattern = rf'({re.escape(secondary_power_name)})\s+(Daily|Encounter)(\s+✦)'
    match = re.search(secondary_pattern, old_index)
    
    # If that fails, try without the ✦ requirement (some might not have it)
    if not match:
        secondary_pattern = rf'({re.escape(secondary_power_name)})\s+(Daily|Encounter)(\s|$)'
        match = re.search(secondary_pattern, old_index)
    
    if not match:
        return (False, "", f"Could not find secondary power '{secondary_power_name}' with Daily/Encounter in index")
    
    # Replace Daily or Encounter with At-Will
    new_index = old_index[:match.start(2)] + 'At-Will' + old_index[match.end(2):]
    
    return (True, old_index, new_index)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fix secondary power labeled as encounter/daily → at-will"
    )
    parser.add_argument("--name", required=True, help="Power name (e.g., 'Thunder Hawk Rage')")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without applying")
    parser.add_argument("--apply", action="store_true", help="Actually apply the changes")
    args = parser.parse_args()
    
    if not args.dry_run and not args.apply:
        print("Error: Must specify --dry-run or --apply")
        return
    
    power_name = args.name
    
    print(f"Processing: {power_name}")
    print("-" * 60)
    
    # Step 1: Find power ID first (needed for SQL extraction with apostrophes)
    print("1. Finding power ID...")
    result = find_power_id(power_name)
    if not result:
        print("   ERROR: Could not find power ID")
        return
    
    power_id, data_file_num = result
    data_file = DATA_ROOT / f"data{data_file_num}.js"
    
    print(f"   ✓ Found: {power_id} in {data_file.name}")
    
    # Step 2: Extract from SQL (use ID for reliability)
    # Extract just the numeric part of the ID
    import re
    num_match = re.search(r'(\d+)$', power_id)
    numeric_id = num_match.group(1) if num_match else power_id
    
    print("2. Extracting from Portable Compendium SQL...")
    sql_record = extract_power_from_sql(power_name, numeric_id)
    if not sql_record:
        print("   ERROR: Could not extract from SQL")
        return
    
    correct_html = sql_record.get("DetailHtml", "")
    if not correct_html:
        print("   ERROR: No DetailHtml in SQL record")
        return
    
    print("   ✓ Extracted successfully")
    
    # Step 3: Fix data file
    print("3. Analyzing data file...")
    success, old_html, new_html, secondary_power_name = fix_secondary_power_in_data(data_file, power_id, correct_html)
    
    if not success:
        print(f"   ERROR: {new_html}")
        return
    
    print("   ✓ Changes identified")
    
    # Step 4: Fix index
    print("4. Analyzing index file...")
    index_path = DATA_ROOT / "_index.js"
    if not index_path.exists():
        print("   ERROR: Index file not found")
        return
    
    index_text = index_path.read_text(encoding='utf-8')
    index_pattern = rf'"{re.escape(power_id)}"\s*:\s*"([^"]+)"'
    index_match = re.search(index_pattern, index_text)
    
    if not index_match:
        print("   ERROR: Power ID not found in index")
        return
    
    old_index = index_match.group(1)
    index_success, old_index_check, new_index = fix_index(power_id, secondary_power_name, old_index)
    
    if not index_success:
        print(f"   ERROR: {new_index}")
        return
    
    print("   ✓ Index changes identified")
    
    # Step 5: Show diff
    print("\n" + "=" * 60)
    print("CHANGES TO APPLY:")
    print("=" * 60)
    
    # Find the secondary power section in both
    secondary_old_match = re.search(
        r'(<h1 class=(?:dailypower|encounterpower)>[^<]+</h1>.*?)(?=<br><p class=publishedIn|$)',
        old_html,
        re.DOTALL
    )
    secondary_new_match = re.search(
        r'(<h1 class=atwillpower>[^<]+</h1>.*?)(?=<br><p class=publishedIn|$)',
        new_html,
        re.DOTALL
    )
    
    if secondary_old_match and secondary_new_match:
        print("\nDATA FILE - Secondary Power Change:")
        print("-" * 60)
        old_snippet = secondary_old_match.group(1)
        new_snippet = secondary_new_match.group(1)
        print("OLD (first 300 chars):")
        print(old_snippet[:300] + "..." if len(old_snippet) > 300 else old_snippet)
        print("\nNEW (first 300 chars):")
        print(new_snippet[:300] + "..." if len(new_snippet) > 300 else new_snippet)
    
    # Show index changes
    if old_index != new_index:
        print("\nINDEX FILE - Secondary Power Text Change:")
        print("-" * 60)
        # Extract secondary power name from HTML for display
        h1_matches = list(re.finditer(r'<h1 class=(?:dailypower|encounterpower|atwillpower)>([^<]+)</h1>', old_html))
        if len(h1_matches) >= 2:
            sec_name = h1_matches[1].group(1).strip()
            # Find the changed portion
            old_portion = re.search(rf'([^"]*{re.escape(sec_name)}[^"]*Daily[^"]*|{re.escape(sec_name)}[^"]*Encounter[^"]*)', old_index)
            new_portion = re.search(rf'([^"]*{re.escape(sec_name)}[^"]*At-Will[^"]*)', new_index)
            if old_portion and new_portion:
                print("OLD:")
                print(old_portion.group(1)[:200] + "..." if len(old_portion.group(1)) > 200 else old_portion.group(1))
                print("\nNEW:")
                print(new_portion.group(1)[:200] + "..." if len(new_portion.group(1)) > 200 else new_portion.group(1))
    
    if args.apply:
        print("\n" + "=" * 60)
        print("APPLYING CHANGES...")
        print("=" * 60)
        
        # Update data file
        text = data_file.read_text(encoding='utf-8')
        pattern = rf'"{re.escape(power_id)}"\s*:\s*"([^"]+)"'
        new_text = re.sub(pattern, f'"{power_id}": "{new_html}"', text)
        
        if new_text == text:
            print(f"   ERROR: Failed to update {data_file.name}")
            return
        
        data_file.write_text(new_text, encoding='utf-8')
        print(f"   ✓ Updated {data_file.name}")
        
        # Update index file
        index_text = (DATA_ROOT / "_index.js").read_text(encoding='utf-8')
        index_pattern = rf'"{re.escape(power_id)}"\s*:\s*"([^"]+)"'
        new_index_text = re.sub(index_pattern, f'"{power_id}": "{new_index}"', index_text)
        
        if new_index_text == index_text:
            print(f"   ERROR: Failed to update _index.js")
            return
        
        (DATA_ROOT / "_index.js").write_text(new_index_text, encoding='utf-8')
        print(f"   ✓ Updated _index.js")
        
        print("\n   ✓ All changes applied successfully!")
        print("   Next steps:")
        print("   1. Mark as corrected in fix/fixes-needed.json (use fix/scripts/mark_fix_corrected.py)")
        print("   2. Validate with: python3 fix/scripts/validate_compendium.py")
    else:
        print("\n" + "=" * 60)
        print("DRY RUN - No changes applied")
        print("Use --apply to actually make changes")


if __name__ == "__main__":
    main()
