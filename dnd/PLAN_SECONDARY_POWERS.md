# Plan: Fix 98 Powers with Secondary Powers Labeled as Encounter/Daily → At-Will

## Problem Summary
98 powers have secondary attacks/powers that are incorrectly labeled as "Encounter" or "Daily" when they should be "At-Will". The primary power remains unchanged (stays Daily/Encounter).

## Files That Need Changes

For each power fix, we need to update:

1. **`4e_database_files/power/dataN.js`** (N = ID suffix % 20)
   - Change secondary power `<h1 class=dailypower>` or `<h1 class=encounterpower>` → `<h1 class=atwillpower>`
   - Change secondary power `<b>Daily</b>` or `<b>Encounter</b>` → `<b>At-Will</b>` in powerstat line
   - Primary power stays unchanged

2. **`4e_database_files/power/_index.js`**
   - Update text index: change "Daily" or "Encounter" to "At-Will" for the secondary power text
   - Primary power text stays unchanged

3. **`fixes-needed.json`**
   - Mark each fix as `"status": "corrected"` after completion

## Files That DON'T Need Changes

- `4e_database_files/power/_listing.js` - Only tracks primary power, not secondary
- `4e_database_files/index.js` - Only tracks primary power name
- `4e_database_files/catalog.js` - Counts don't change

## Systematic Fix Process

### Step 1: Extract All 98 Power Names
- Parse `fixes-needed.json` to get all powers with `status: "needs_fix"` in the category
- Extract power name from each entry (format: "Power Name (Class Type Level)")

### Step 2: For Each Power (Batch Processing)
1. **Extract correct version from Portable Compendium SQL**
   ```bash
   python3 scripts/portable_sql_extract.py \
     --table power \
     --name "Power Name" \
     --limit 1 \
     --extract-detail \
     --output /tmp/power_extract.json
   ```

2. **Identify the power ID and data file**
   - Find power in `power/_listing.js` to get ID
   - Calculate `dataN.js` where N = (ID numeric suffix) % 20

3. **Update dataN.js**
   - Find the secondary power section (usually starts with `<h1 class=dailypower>` or `<h1 class=encounterpower>` after the primary power)
   - Replace with correct version from Portable Compendium (which has `<h1 class=atwillpower>` and `<b>At-Will</b>`)

4. **Update _index.js**
   - Find the power's index entry
   - Replace "Daily" or "Encounter" with "At-Will" in the secondary power text portion

5. **Mark as corrected**
   - Update `fixes-needed.json` entry to `"status": "corrected"`

### Step 3: Validation
After each batch (10-20 powers):
1. Run validator: `python3 scripts/validate_compendium.py`
2. Check for errors
3. Manual spot-check 2-3 powers in browser

### Step 4: Final Steps
1. Regenerate HTML: `python3 scripts/render_fixes_html.py`
2. Final validation
3. Update CHANGELOG.md

## Batch Strategy

**Recommended: Process in batches of 10-15 powers**

Reasons:
- Allows validation after each batch
- Easier to track progress
- Can catch patterns/errors early
- Manageable file sizes

**Batch Organization Options:**
1. **By class** (e.g., all Barbarian powers, then all Battlemind, etc.)
2. **By data file** (group by which dataN.js they're in)
3. **Alphabetically** (simple, predictable order)

**Recommendation: By data file** - This minimizes file I/O and makes it easier to batch-edit files.

## Pattern Recognition

The fix pattern is consistent:
- Find: `<h1 class=dailypower>Secondary Power Name</h1>` or `<h1 class=encounterpower>Secondary Power Name</h1>`
- Replace: `<h1 class=atwillpower>Secondary Power Name</h1>`
- Find: `<b>Daily</b>` or `<b>Encounter</b>` in secondary power's powerstat
- Replace: `<b>At-Will</b>`

## Special Cases to Watch For

1. **Flameburst Armor** - Also needs "Fireburst" armor changed to "flameburst" (separate fix)
2. **Shadow Knives** - Also needs aftereffect listed as primary power (already corrected)
3. Some powers might have multiple secondary powers - need to check each one

## Automation Opportunity

Since the pattern is very consistent, we could:
1. Create a helper script that:
   - Takes a power name
   - Extracts from SQL
   - Finds the power in data files
   - Makes the replacements
   - Updates index
   - Marks as corrected

But manual review is still recommended for accuracy.

## Quality Checks

For each power, verify:
- [ ] Secondary power header changed to `atwillpower`
- [ ] Secondary power usage changed to "At-Will"
- [ ] Primary power unchanged
- [ ] Index updated correctly
- [ ] No other unintended changes
- [ ] Power displays correctly in browser
