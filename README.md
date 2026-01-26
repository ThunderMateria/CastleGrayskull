# D&D 4e Offline Compendium (Static JSONP)

This repository is a **fully offline**, **static** D&D 4e compendium. There is no server, database, or runtime backend. All data is precompiled into JavaScript files that are loaded by the browser as JSONP.

This README is a complete onboarding guide for future developers. It explains:
- How the application is structured
- How data is organized and loaded
- How search and indexing work
- Exactly where and how to make edits
- A surgical edit checklist for fixes/additions

---

## 1) Application Entry Points

- `index.html`
  - Defines the global `od` namespace
  - Sets `od.data_path` to `4e_database_files`
  - Loads the compiled runtime: `4e_database_files/res/script.js`

- `4e_database_files/res/script.js`
  - Contains the application logic (data model, search, loader)
  - Defines URL patterns for all data files
  - Implements JSONP read/load workflow

---

## 2) Repository Layout

```
/index.html
/4e_database_files/
  /catalog.js
  /index.js                     # global name index
  /<category>/
    /_listing.js                # table listing
    /_index.js                  # category full-text index
    /data0.js ... data19.js     # full HTML entry bodies
  /res/
    /script.js                  # compiled app logic
    /style.css                  # UI and content styling
    /icon.png, viewer_category_icon.png, manifest.json
```

Categories present in this build:
`armor`, `background`, `class`, `companion`, `deity`, `disease`, `epicdestiny`,
`feat`, `glossary`, `implement`, `item`, `monster`, `paragonpath`, `poison`,
`power`, `race`, `ritual`, `theme`, `trap`, `weapon`.

---

## 3) Data Formats (JSONP, not JSONL)

All data is JSONP delivered via `<script>` injection. The loader functions live in `res/script.js`.

### 3.1 Catalog
`4e_database_files/catalog.js`
```
od.reader.jsonp_catalog(timestamp, {
  "power": 9409,
  "monster": 5326,
  ...
})
```
This drives category counts and the main browse UI.

### 3.2 Listing (Table Data)
`4e_database_files/<category>/_listing.js`
```
od.reader.jsonp_data_listing(timestamp, "category", ["ID", "Name", ...], [
  ["id", "name", "type", "level", ...],
  ...
])
```
This is the primary source for table sorting, filtering, and Name Search.

### 3.3 Entry Bodies (HTML Content)
`4e_database_files/<category>/data0.js ... data19.js`
```
od.reader.jsonp_batch_data(timestamp, "category", {
  "id": "<h1>...</h1><p>...</p>",
  ...
})
```
This HTML string is what the detail view renders.

### 3.4 Category Full-Text Index
`4e_database_files/<category>/_index.js`
```
od.reader.jsonp_data_index(timestamp, "category", {
  "id": "Text-only index string",
  ...
})
```
Used for Full Search.

### 3.5 Global Name Index (Quick Lookup)
`4e_database_files/index.js`
```
od.reader.jsonp_name_index(timestamp, {
  "lowercased name": "category123",
  ...
})
```
Used when clicking text in an entry to do a quick lookup.

---

## 4) Data Loading & Routing

URL patterns are defined in `od.config.url` in `res/script.js`:

- `catalog` -> `${data_path}/catalog.js`
- `listing` -> `${data_path}/${category}/_listing.js`
- `index` -> `${data_path}/${category}/_index.js` or `${data_path}/index.js`
- `data` -> `${data_path}/${category}/data${id % 20}.js`

**Important**: The entry file is selected by ID suffix modulo 20:
```
dataN.js where N = (numeric suffix of ID) % 20
```
Example:
- `power6872` -> `6872 % 20 = 12` -> `data12.js`

---

## 5) Search & Indexing Behavior

There are two search modes:

1) **Name Search**
   - Searches the `Name` column in listing data.

2) **Full Search**
   - Uses the category `_index.js` text index.
   - Supports AND, OR, quoted phrases, minus to exclude, plus for whole-word, and wildcard `*`.

Search is entirely client-side, using regex over the index strings.

---

## 6) Quick Lookup Behavior

Clicking text in an entry triggers a lookup using the **global name index** in `4e_database_files/index.js`.

This index maps lowercased names to one or more IDs, so new entries must be added here if you want quick lookup to work.

---

## 7) Compression Support

Some data may be stored as a string prefixed with `T>t<;`, which indicates a Base85 + LZMA-compressed JSON payload. The loader auto-decompresses in `od.reader._inflate()`.

If you see a `T>t<;` prefix, do not edit the raw compressed string manually unless you re-encode it correctly.

---

## 8) Visual Styling & Colors

All styling lives in `4e_database_files/res/style.css`:

- Color-coded headers for power types:
  - `.atwillpower`, `.encounterpower`, `.dailypower`
- Category icon sprites
- Layout and typography for detail view

If you need color changes or presentation tweaks, this is the file to edit.

---

## 9) Edit Touchpoints (What Must Stay in Sync)

For any change to an entry, you typically need to update **multiple files**:

1) **Listing row**:  
   `4e_database_files/<category>/_listing.js`

2) **Full entry HTML**:  
   `4e_database_files/<category>/dataN.js`

3) **Full-text index**:  
   `4e_database_files/<category>/_index.js`

4) **Global name index** (for quick lookup):  
   `4e_database_files/index.js`

5) **Catalog counts** (if adding/removing entries):  
   `4e_database_files/catalog.js`

6) **UI styles** (if color/presentation changes):  
   `4e_database_files/res/style.css`

---

## 10) Surgical Edit Checklist

Use this checklist for **every** correction or new entry.

### A) Identify the Target
- Determine `category` (power, feat, monster, etc.)
- Determine entry ID (e.g., `power6872`)
- Confirm numeric suffix for file routing:
  - `fileIndex = suffix % 20`

### B) Update Listing Data
- Edit `4e_database_files/<category>/_listing.js`
- Ensure columns match category schema
- Update or add row:
  - `["id", "Name", ...]`

### C) Update Full Entry HTML
- Edit `4e_database_files/<category>/data<fileIndex>.js`
- Update or add the HTML string for the ID
- Keep existing HTML conventions:
  - `<h1 class=...>`, `<p class=...>`, `<b>`, `<br>`

### D) Update Full-Text Index
- Edit `4e_database_files/<category>/_index.js`
- Ensure index string is a **text-only version** of the entry
- Keep it in sync with the HTML content so Full Search matches

### E) Update Global Name Index
- Edit `4e_database_files/index.js`
- Add lowercased names that should map to the entry ID
- Include common variants if needed

### F) Update Catalog Counts (if needed)
- If an entry is added or removed, update the category count in:
  - `4e_database_files/catalog.js`

### G) Validate File Routing
- Confirm the entry ID ends up in the correct `dataN.js` file
- `N = numeric suffix % 20`

### H) Optional Visual Edits
- If you changed any visual class/color conventions, update:
  - `4e_database_files/res/style.css`

---

## 11) Common Pitfalls

- **Forgetting `_index.js`** causes Full Search to miss entries.
- **Forgetting `index.js`** breaks quick lookup from clicked text.
- **Wrong `dataN.js` file** means the entry never loads.
- **Incorrect ID casing** can break lookups (IDs are case-sensitive).
- **Compressed payload edits** without re-encoding will corrupt data.

---

## 12) Quick Reference: Where to Edit

| Goal | File(s) |
|------|---------|
| Change listing columns/row | `4e_database_files/<category>/_listing.js` |
| Change entry content | `4e_database_files/<category>/dataN.js` |
| Fix full-text search | `4e_database_files/<category>/_index.js` |
| Fix quick lookup | `4e_database_files/index.js` |
| Update counts | `4e_database_files/catalog.js` |
| Change colors/styles | `4e_database_files/res/style.css` |

---

## 13) No Build Pipeline in This Repo

This repo appears to be a **compiled output**. There are no build scripts or generators included here. Edits must be done directly in the JS files.

If you need to regenerate compressed payloads or rebuild indexes programmatically, that tooling is not present in this repository.

---

## 14) Suggested Workflow for Clean Edits

1) Locate entry by ID in `_listing.js` and `dataN.js`.
2) Edit entry HTML.
3) Update `_index.js` to reflect the new text.
4) Update `index.js` if new/renamed name strings should be searchable.
5) Update `catalog.js` if count changes.
6) Load `index.html` in a browser and verify:
   - Listing row shows correctly
   - Detail view renders correctly
   - Name Search finds it
   - Full Search finds it
   - Quick lookup works

---

## 15) Entry-Type Templates (Listing Columns + HTML Conventions)

Use this section to create entries consistently. The authoritative source of columns
is always the first line of each `4e_database_files/<category>/_listing.js`.

### 15.1 Listing Columns by Category (from this repo)

- `power`: `["ID", "Name", "ClassName", "Level", "Type", "Action", "Keywords", "SourceBook"]`
- `feat`: `["ID", "Name", "Tier", "Prerequisite", "SourceBook"]`
- `monster`: `["ID", "Name", "Level", "CombatRole", "GroupRole", "Size", "CreatureType", "SourceBook"]`
- `item`: `["ID", "Name", "Category", "Type", "Level", "Cost", "Rarity", "SourceBook"]`
- `ritual`: `["ID", "Name", "Level", "ComponentCost", "Price", "KeySkillDescription", "SourceBook"]`
- `class`: `["ID", "Name", "RoleName", "PowerSourceText", "KeyAbilities", "SourceBook"]`
- `race`: `["ID", "Name", "Origin", "DescriptionAttribute", "Size", "SourceBook"]`
- `paragonpath`: `["ID", "Name", "Prerequisite", "SourceBook"]`
- `epicdestiny`: `["ID", "Name", "Prerequisite", "SourceBook"]`
- `theme`: `["ID", "Name", "Prerequisite", "SourceBook"]`

If you touch other categories (armor, weapon, implement, background, etc.),
open that category's `_listing.js` and follow its column order exactly.

### 15.2 Listing Cell Conventions

Listing cells can be:
- **Simple strings** (most common).
- **Range/multi-value arrays** for filtering:
  - Format: `["display text", min, max, ...]`
  - Example from `item` listing: `["360+ gp", 360, 225000, 9000]`
  - Used by range filters in numeric fields (`Level`, `Cost`, `Price`).

### 15.3 Detail HTML Conventions

Entry bodies are HTML strings in `dataN.js`. Keep the existing conventions so the
CSS renders correctly:

Common structure patterns:
- `<h1 class=player>` for player-facing entries (classes, races).
- `<h1 class=atwillpower>`, `<h1 class=encounterpower>`, `<h1 class=dailypower>` for powers.
- `<p class=flavor>` for italic flavor text.
- `<p class=powerstat>` for key stats lines.
- `<p class=publishedIn>` for source citation.

Other known classes used by styles:
- `monster`, `trap`, `poison`, `magicitem`, `mihead`, `miset`, `miflavor`, `bodytable`.

When editing, preserve:
- Header hierarchy (`h1`, `h2`, `h3`)
- Existing `<b>` and `<br>` layout patterns
- Class names that control styling

### 15.4 Suggested Template Steps by Entry Type

**Power**
1) Add row in `power/_listing.js`.
2) Add HTML in `power/dataN.js` using `atwillpower` / `encounterpower` / `dailypower`.
3) Add text-only index in `power/_index.js`.
4) Add name mapping in global `index.js`.

**Feat**
1) Add row in `feat/_listing.js`.
2) Add HTML in `feat/dataN.js` (typically `h1` + flavor + rules text).
3) Add index string in `feat/_index.js`.
4) Add name mapping in global `index.js`.

**Monster**
1) Add row in `monster/_listing.js`.
2) Add HTML in `monster/dataN.js` (stat block structure).
3) Add index string in `monster/_index.js`.
4) Add name mapping in global `index.js`.

**Item / Ritual**
1) Add row in `item/_listing.js` or `ritual/_listing.js`.
2) Add HTML in `dataN.js`.
3) Add index string in `_index.js`.
4) Add name mapping in global `index.js`.

**Class / Race / Theme / Paragon Path / Epic Destiny**
1) Add row in category `_listing.js`.
2) Add HTML in `dataN.js` (class/race feature structure).
3) Add index string in `_index.js`.
4) Add name mapping in global `index.js`.

---

## 16) HTML Skeleton Snippets (Copy-Adjust)

These are minimal skeletons that match the existing styling conventions.
Always keep the class names and overall structure consistent with nearby entries.

### 16.1 Power (At-Will / Encounter / Daily)

```
<h1 class=atwillpower>Power Name<span class=level>Class Attack 1</span></h1>
<p class=flavor><i>Short flavor text.</i></p>
<p class=powerstat><b>At-Will</b> ✦ <b>Keywords</b><br><b>Standard Action</b> <b>Melee</b> weapon</p>
<p class=powerstat><b>Target</b>: One creature</p>
<p class=powerstat><b>Attack</b>: Ability vs. Defense</p>
<p class=flavor><b>Hit</b>: X[W] + ability modifier damage.</p>
<p class=powerstat><b>Effect</b>: Optional effect text.</p>
<p class=publishedIn>Published in Source Book, page(s) N.</p>
```

For encounter/daily, replace `atwillpower` with `encounterpower` or `dailypower`
and update the usage line accordingly.

### 16.2 Feat

```
<h1>Feat Name</h1>
<p><b>Tier</b>: Heroic</p>
<p><b>Prerequisite</b>: Condition or class</p>
<p><b>Benefit</b>: Rules text.</p>
<p class=publishedIn>Published in Source Book, page(s) N.</p>
```

### 16.3 Monster

```
<h1 class=monster>Monster Name<span class=level>Level X Role</span></h1>
<p class=flavor><i>Short flavor.</i></p>
<p class=powerstat><b>XP</b> N</p>
<p><b>Initiative</b> +N; <b>Senses</b> ...</p>
<p><b>HP</b> N; <b>Bloodied</b> N</p>
<p><b>AC</b> N; <b>Fortitude</b> N; <b>Reflex</b> N; <b>Will</b> N</p>
<p><b>Speed</b> N</p>
<p><b>Traits</b> ...</p>
<h2>Standard Actions</h2>
<p><b>Attack Name</b> (standard; at-will) ✦ Keywords</p>
<p>Attack text.</p>
<p class=publishedIn>Published in Source Book, page(s) N.</p>
```

### 16.4 Item

```
<h1 class=magicitem>Item Name</h1>
<p><b>Level</b> N</p>
<p><b>Price</b> N gp</p>
<p><b>Item Slot</b>: Slot (if applicable)</p>
<p><b>Property</b>: Rules text.</p>
<p><b>Power</b> (Daily ✦ ...): Rules text.</p>
<p class=publishedIn>Published in Source Book, page(s) N.</p>
```

### 16.5 Ritual

```
<h1>Ritual Name<span class=level>Level N</span></h1>
<p><b>Category</b>: Category</p>
<p><b>Time</b>: X minutes</p>
<p><b>Duration</b>: Duration text</p>
<p><b>Component Cost</b>: N gp</p>
<p><b>Market Price</b>: N gp</p>
<p><b>Key Skill</b>: Skill</p>
<p><b>Effect</b>: Rules text.</p>
<p class=publishedIn>Published in Source Book, page(s) N.</p>
```

### 16.6 Class / Race / Theme / Paragon Path / Epic Destiny

```
<h1 class=player>Entry Name</h1>
<p class=flavor><b>CLASS TRAITS</b></p>
<blockquote>
  <b>Role</b>: ...
  <br><b>Power Source</b>: ...
  <br><b>Key Abilities</b>: ...
</blockquote>
<p>Descriptive text...</p>
<p class=publishedIn>Published in Source Book, page(s) N.</p>
```

---

## 17) Text-Only Index String Examples (Full Search)

These examples are for `_index.js` entries. They **do not change site structure**;
they only describe the text-only strings that power Full Search. Keep them in sync
with the HTML entry content, using plain text (no HTML tags).

### 17.1 Power (example)

```
"power1234": "Power Name Class Attack 1 At-Will Martial Weapon Standard Action Melee weapon Target: One creature Attack: Strength vs. AC Hit: 1[W] + Strength modifier damage Effect: Optional effect text. Published in Player's Handbook page 123."
```

### 17.2 Feat (example)

```
"feat1234": "Feat Name Tier: Heroic Prerequisite: Condition or class Benefit: Rules text. Published in Source Book page 123."
```

### 17.3 Monster (example)

```
"monster1234": "Monster Name Level 5 Skirmisher Medium humanoid natural XP 200 Initiative +6 Senses ... HP 62 Bloodied 31 AC 19 Fortitude 17 Reflex 18 Will 16 Speed 6 ... Attack Name (standard; at-will) +10 vs AC Hit: 1d8+5 damage ... Published in Monster Manual page 123."
```

### 17.4 Item (example)

```
"item1234": "Item Name Level 5 Price 1000 gp Item Slot: Hands Property: Rules text. Power (Daily): Rules text. Published in Adventurer's Vault page 123."
```

### 17.5 Ritual (example)

```
"ritual1234": "Ritual Name Level 5 Category: Travel Time: 10 minutes Duration: 8 hours Component Cost: 250 gp Market Price: 1000 gp Key Skill: Arcana Effect: Rules text. Published in Player's Handbook page 123."
```

### 17.6 Class / Race / Theme / Paragon Path / Epic Destiny (example)

```
"class123": "Class Name Class Traits Role: Defender Power Source: Martial Key Abilities: Strength, Constitution ... Armor Proficiencies: ... Weapon Proficiencies: ... Class Features: ... Published in Player's Handbook page 123."
```

### 17.7 Index String Extraction Tips

These tips help keep Full Search accurate **without changing any site structure**.

- Strip HTML tags and keep the visible text in reading order.
- Preserve headings and labels (e.g., "Role:", "Prerequisite:", "Hit:") because users search for them.
- Keep punctuation minimal; use spaces to separate fields.
- Keep key numbers (level, damage, page, XP, price).
- Include source book citations so users can search by book.
- For multiline HTML sections, concatenate with spaces (avoid newlines).
