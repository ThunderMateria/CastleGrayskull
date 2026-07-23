# Fix Pipeline — How to Apply Compendium Fixes Again

This folder documents how to run the **fix pipeline** for the D&D 4e compendium. Use it when a user reports a correction or addition and you need to update `4e_database_files/` safely and consistently.

All **fix-related files** (queue, HTML, scripts) live in **`fix/`**; compendium data (`4e_database_files/`) stays at the **project root**. Run all commands from the **project root**. This README is the single place that explains the workflow.

---

## 1. Where Things Live

| What | Location |
|------|----------|
| Fix queue (source of truth) | **`fix/fixes-needed.json`** |
| Fix status HTML (record) | **`fix/index.htm`** |
| Source HTML (optional) | **`fix/fixes-needed.html`** |
| Compendium data | **`4e_database_files/`** (project root) |
| Scripts | **`fix/scripts/`** |
| Change log | **`fix/CHANGELOG.md`** |

---

## 2. Fix Queue Format

`fix/fixes-needed.json` is a JSON object. Each key is a category (e.g. `"Powers"`, `"Feats"`). Each value is an array of entries:

```json
{
  "Category Name": [
    { "text": "Entry name (Source): description of fix", "status": "needs_fix" },
    { "text": "Another entry (Source): fix description", "status": "corrected" }
  ]
}
```

- **`status: "needs_fix"`** — still to do.
- **`status: "corrected"`** — already applied.

When adding a **new** fix reported by a user, append an entry with `"status": "needs_fix"` to the appropriate category (or create the category).

---

## 3. Per-Entry Workflow

For each fix you apply:

### 3.1 Find the entry

- Identify **category** (power, feat, item, paragonpath, etc.) and **name/source** from the fix text.
- Get the **entry ID** (e.g. `power6872`, `feat2269`):
  - Search **`4e_database_files/<category>/_listing.js`** for the name, or
  - Use **`4e_database_files/index.js`** (lowercased name → ID).
- **Data file:** `dataN.js` where **N = (numeric suffix of ID) % 20**.  
  Example: `power6872` → suffix 6872 → 6872 % 20 = 12 → **`power/data12.js`**.

### 3.2 Update all related files

**Every** edit must keep these in sync:

1. **`4e_database_files/<category>/dataN.js`** — main HTML/content for the entry.
2. **`4e_database_files/<category>/_index.js`** — plain-text version (for search); update the same content there.
3. **`4e_database_files/<category>/_listing.js`** — only if the fix changes listing row (e.g. name, level).
4. **`4e_database_files/index.js`** — global name → ID map (lowercased). Update if name changes or entry is new.
5. **`4e_database_files/catalog.js`** — only if you **add** or **remove** an entry (update counts).

Never edit only one of these; always update every file that contains that entry.

### 3.3 Optional: Portable Compendium as source

If you have **Portable Compendium** SQL dumps (`Portable Compendium New/sql/*.sql`), you can pull canonical HTML:

```bash
python3 fix/scripts/portable_sql_extract.py \
  --table power \
  --name "Twin Strike" \
  --limit 1 \
  --extract-detail \
  --output portable_compendium_extract.json
```

Use the extracted content to guide or paste the correct HTML into `dataN.js` and the matching text into `_index.js`.

---

## 4. After Applying a Fix

1. **Mark corrected**  
   Either edit `fix/fixes-needed.json` and set that entry’s `"status"` to `"corrected"`, or:
   ```bash
   python3 fix/scripts/mark_fix_corrected.py --text "Exact fix text or unique substring"
   ```
   (Script defaults use `fix/fixes-needed.json`.)

2. **Regenerate fix-status HTML**  
   ```bash
   python3 fix/scripts/render_fixes_html.py --input fix/fixes-needed.json --output fix/index.htm
   ```
   Or run with no args (defaults point to `fix/`). This keeps **`fix/index.htm`** up-to-date.

3. **⚠️ MANDATORY: Validate compendium (must pass before deploy)**  
   ```bash
   python3 fix/scripts/check_validation.py
   ```
   This runs validation and **exits with error code 1 if issues are found**. DO NOT DEPLOY if this fails.
   
   The script checks:
   - `missing_data`: IDs in listing but missing from dataN.js
   - `missing_index`: IDs in listing but missing from _index.js  
   - `misrouted_data`: IDs in wrong dataN.js file (wrong bucket)
   - `global_name_index_missing`: Names in index.js pointing to non-existent IDs
   
   Full report is written to `fix/compendium-validation.json`.

4. **Update fix/CHANGELOG.md**  
   Add a short entry: date, what was fixed (entry name/source), and that validation passed.

5. **Quick smoke test**  
   Open **`index.html`** in a browser: confirm the changed entry appears correctly in listing, detail, name search, and full search.

---

## 5. Guardrails

- Work in **small batches** (e.g. 5–20 entries).
- After each batch: run the validator and a quick manual check.
- If a fix would **delete** an entry from the compendium, do not do it in this pipeline; treat it as manual review.
- Prefer Portable Compendium SQL as source-of-truth when available.

---

## 6. Script Reference

| Script | Purpose |
|--------|--------|
| `fix/scripts/check_validation.py` | **Run this before deploy.** Runs validation and exits with error if issues found. |
| `fix/scripts/mark_fix_corrected.py` | Set status to `corrected` in `fix/fixes-needed.json` by matching fix text. |
| `fix/scripts/render_fixes_html.py` | Regenerate `fix/index.htm` from `fix/fixes-needed.json`. |
| `fix/scripts/validate_compendium.py` | Check data/index/listing/catalog consistency; write report to `fix/compendium-validation.json`. |
| `fix/scripts/portable_sql_extract.py` | Pull entry HTML from Portable Compendium SQL (optional). |

Other scripts in `fix/scripts/` (e.g. batch fix, extract, prioritize) were used for the initial bulk run; for **new one-off fixes**, the workflow above is enough.

---

You’re done when: the fix is in `4e_database_files/`, the entry is `corrected` in `fix/fixes-needed.json`, `fix/index.htm` is regenerated, **check_validation.py passes**, and `fix/CHANGELOG.md` is updated.
