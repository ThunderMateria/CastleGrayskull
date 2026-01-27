# Execution Plan: Fix 98 Secondary Powers

## Overview
Fix 98 powers where secondary powers are incorrectly labeled as "Encounter" or "Daily" when they should be "At-Will".

## What Needs to Change

### Pattern to Find:
```html
<h1 class=dailypower>Secondary Power Name</h1>
...
<p class=powerstat><b>Daily</b> ✦ ...
```

OR

```html
<h1 class=encounterpower>Secondary Power Name</h1>
...
<p class=powerstat><b>Encounter</b> ✦ ...
```

### Pattern to Replace:
```html
<h1 class=atwillpower>Secondary Power Name</h1>
...
<p class=powerstat><b>At-Will</b> ✦ ...
```

## Files to Update Per Power

1. **`4e_database_files/power/dataN.js`** (where N = power ID suffix % 20)
   - Replace secondary power HTML section

2. **`4e_database_files/power/_index.js`**
   - Replace "Daily" or "Encounter" with "At-Will" in secondary power text

3. **`fixes-needed.json`**
   - Change status to "corrected"

## Batch Processing Strategy

### Recommended: Process 10-15 powers per batch

**Batch 1: Test Run (3-5 powers)**
- Verify the process works correctly
- Test validation
- Refine approach if needed

**Batches 2-8: Main Processing (10-15 powers each)**
- Process systematically
- Validate after each batch
- Mark as corrected

**Final Batch: Remaining powers + cleanup**
- Finish remaining powers
- Final validation
- Regenerate HTML
- Update CHANGELOG

## Step-by-Step Process for Each Power

1. **Extract from SQL**
   ```bash
   python3 scripts/portable_sql_extract.py \
     --table power \
     --name "Power Name" \
     --limit 1 \
     --extract-detail \
     --output /tmp/power_extract.json
   ```

2. **Find Power ID**
   - Search `power/_listing.js` for power name
   - Extract ID (format: `power####`)
   - Calculate data file: `N = (numeric suffix) % 20`

3. **Update dataN.js**
   - Find power entry by ID
   - Locate secondary power section (second `<h1>` tag)
   - Replace with correct version from SQL extract
   - Key changes:
     - `class=dailypower` → `class=atwillpower`
     - `class=encounterpower` → `class=atwillpower`
     - `<b>Daily</b>` → `<b>At-Will</b>`
     - `<b>Encounter</b>` → `<b>At-Will</b>`

4. **Update _index.js**
   - Find power entry by ID
   - Locate secondary power text (usually after primary power text)
   - Replace "Daily" or "Encounter" with "At-Will" in that section

5. **Mark as Corrected**
   ```bash
   python3 scripts/mark_fix_corrected.py \
     --text "Power Name (Class Type Level) (Source)"
   ```

## Validation Checklist (After Each Batch)

- [ ] Run: `python3 scripts/validate_compendium.py`
- [ ] Check validation report for errors
- [ ] Manually verify 2-3 powers in browser (`index.html`)
- [ ] Verify secondary power shows as "At-Will"
- [ ] Verify primary power unchanged

## Special Cases

1. **Flameburst Armor** - Has additional fix needed (armor name change)
2. **Powers with multiple secondary powers** - Check each one
3. **Powers where secondary power name is unclear** - Use SQL source as reference

## Progress Tracking

Track completed powers in a simple list:
- [ ] Power 1
- [ ] Power 2
- etc.

Or use a script to count remaining:
```python
import json
data = json.load(open('fixes-needed.json'))
items = [i for i in data.get('Powers with secondary powers labeled as encounter/daily that should be at-will', []) if i.get('status') == 'needs_fix']
print(f'Remaining: {len(items)}')
```

## Final Steps

1. Process all 98 powers
2. Final validation: `python3 scripts/validate_compendium.py`
3. Regenerate HTML: `python3 scripts/render_fixes_html.py --output index.htm`
4. Update CHANGELOG.md with batch summary
5. Manual spot-check 5-10 random powers in browser

## Estimated Time

- Per power: ~2-3 minutes (with helper script)
- Per batch (10 powers): ~20-30 minutes + validation
- Total: ~4-5 hours for all 98 powers

With automation/helper script: Could reduce to ~2-3 hours total.
