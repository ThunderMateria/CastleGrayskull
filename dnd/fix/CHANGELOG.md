# Change Log (Fix Batches)

Use one entry per batch. Keep it short and factual.

## YYYY-MM-DD — Batch Title

- **Scope**: power/feat/item/monster/etc.
- **Entries**: list IDs or names
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `_listing.js`, `dataN.js`, `_index.js`, `index.js`, `catalog.js` (if applicable), `fixes-needed.json`, `index.htm`
- **Validation**: `compendium-validation.json` (pass/fail)
- **Smoke test**: listing/detail/search/lookup (pass/fail)

---
## 2026-01-29 — Batch: Ammunition labels + Gauntlet Axe (mixed fix)

- **Scope**: weapon
- **Entries**: Ammunition—relabeled 13 AV2/EPG/DR373 magical ammo from specific type to "Arrow or bolt": Onslaught Arrow (1931), Firestorm Arrow (1292), Freezing Arrow (1357), Lightning Arrow (1735), Arrow of Revelation (551), Dual Arrow (1136), Phasing Arrow (2040); Spider Bolt (2576), Bolt of Clumsiness (732), Bolt of Transit (733), Dispelling Bolt (1097), Space-Shifting Bolt (2570), Forbiddance Bolt (1341). Gauntlet Axe (weapon3718): no change—"light shield" sentence not present.
- **Source**: fixes-needed.json (mixed), docs/INVESTIGATION-mixed-ammo-gauntlet-axe.md
- **Files touched**: 4e_database_files/weapon/data0.js, data1.js, data10.js, data11.js, data12.js, data13.js, data15.js, data16.js, data17.js, _index.js, fixes-needed.json
- **Validation**: pending
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Immurement of the Strident Statuary (item1610)

- **Scope**: item
- **Entries**: Immurement of the Strident Statuary (item1610)—added 10th Immurement consumable, Level 28 Rare, 85,000 gp; close blast 8; platform +1 square height, healing +4d6 in blast, statue opportunity attacks (+35 vs. AC; 2d8+8; moving target ends movement); Special: counts as magic item daily use.
- **Source**: user-provided text (AV2-style)
- **Files touched**: 4e_database_files/item/data10.js, _index.js, _listing.js, 4e_database_files/index.js, catalog.js
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Awaken God Fragment full content (feat2269)

- **Scope**: feat
- **Entries**: Awaken God Fragment (feat2269)—added all 11 god fragment options (Avandra, Bahamut, Corellon, Erathis, Ioun, Kord, Melora, Moradin, Pelor, Raven Queen, Sehanine) with Constant Benefits, Divine Manifestation, Quirks; fragment name as main red heading, Divine Manifestation as h3 subheading.
- **Source**: fixes-needed.json (DR382:57), user-provided markdown
- **Files touched**: 4e_database_files/feat/data9.js, 4e_database_files/feat/_index.js, fixes-needed.json, index.htm
- **Validation**: pass (no new entries; existing feat2269 updated)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Glossary full-content entries from PC extract (6 entries)

- **Scope**: glossary
- **Entries**: Filled in full HTML for glossary entries that had listing rows but were missing or truncated in data: (1) Paragon Multiclassing and Psionic Augmentation (glossary681), (2) Tattoos (glossary682), (3) Warforged Components (glossary683), (4) Wands (glossary684). Also marked as corrected: Background Rules (glossary680 already present), Healing Surge usage (glossary679 already present). Content from `glossary_extract_full.py` (Portable Compendium ddiGlossary.sql).
- **Source**: fixes-needed.json + Portable Compendium SQL (glossary_full_extract.json)
- **Files touched**: 4e_database_files/glossary/data1.js, data2.js, data3.js, data4.js, _index.js, 4e_database_files/index.js, fixes-needed.json, index.htm
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Glossary additions/updates from Portable Compendium (4 entries)

- **Scope**: glossary
- **Entries**: (1) Battle Standards: Added new glossary entry (glossary677) from PC—battle standard mechanics (AV:179). (2) Languages (glossary623): Added Supernal/Immortal rules paragraph from PC (RC:69). (3) Paragon Multiclassing: Added new glossary entry (glossary678) from PC (PHB:209). (4) Staff (implement) (glossary668): Added wielding sentence from PC (one hand as implement, two hands as weapon).
- **Source**: fixes-needed.json + Portable Compendium SQL (glossary extracts)
- **Files touched**: 4e_database_files/glossary/_listing.js, data3.js, data8.js, data17.js, data18.js, _index.js, 4e_database_files/index.js, catalog.js, fixes-needed.json, index.htm
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Class features and paragon path fixes (7 entries)

- **Scope**: class, paragonpath
- **Entries**: (1) Assassin (Executioner) (class811): Added Master of Shrouds optional class feature after Attack Finesse. (2) Paladin (Cavalier) (class784): Added Benefit line to Summoned Steed feature. (3) Hybrid Vampire (class893): Updated healing surges text to clarify "a character gains a total of two healing surges regardless of the class combined with vampire to create it or the character's Constitution modifier." (4) Hybrids' Bonus Skills: Header marked as corrected (all individual entries already corrected). (5) Druid (Sentinel) animal companion errors: Header marked as corrected (all individual entries already corrected). (6) Luckbringer of Tymora (paragonpath153): Added "must worship Tymora" to prerequisite; moved Divine Fortune to 11th level, Probability Control to 16th level. (7) Paladin (class4): Added ALTERNATIVE PALADIN FEATURES section with Ardent Vow and Virtue's Touch powers that can replace Lay on Hands.
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/class/data11.js`, `data4.js`, `data13.js`, `4e_database_files/class/_index.js`, `4e_database_files/paragonpath/data13.js`, `4e_database_files/paragonpath/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Power notes + Hybrids header (3 entries)

- **Scope**: power, fixes-needed (header)
- **Entries**: (1) Sigil of Admixture (power14404): Added note that power was retracted and does not appear in published Dragon Magazine 403. (2) Item Resurgence (power7577): Added note that the rule it references (daily item power restrictions) no longer exists. (3) Hybrids' Bonus Skills: Header marked as corrected (all individual hybrid bonus-skill entries were already corrected).
- **Source**: fixes-needed.json
- **Files touched**: `4e_database_files/power/data4.js`, `data17.js`, `4e_database_files/power/_index.js`, `fixes-needed.json`, HTML outputs
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Deep Goblin Wretch + Cavalier Benefit (2 entries)

- **Scope**: monster, class
- **Entries**: (1) Deep Goblin Wretch (monster3561): Corrected defenses and attack bonuses from Portable Compendium—AC 32→18, Fort 27→15, Ref 29→17, Will 26→14; Stone Dagger and Shortbow +13→+8 vs AC. (2) Cavalier Summoned Steed Benefit line: Marked corrected (Benefit line already present in Paladin (Cavalier) SUMMONED STEED section).
- **Source**: fixes-needed.json + Portable Compendium SQL (monster extract)
- **Files touched**: `4e_database_files/monster/data1.js`, `4e_database_files/monster/_index.js`, `fixes-needed.json`, HTML outputs
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Item Sets (5 entries)

- **Scope**: item (Item Sets)
- **Entries**: (1) Armory of the Unvanquished (item430), (2) Caelynnvala's Boons (item431), (3) Heirlooms of Mazgorax (item433), (4) Implements of Argent (item435), (5) The Returning Beast (item438). Reviewed all five; Armory, Caelynnvala's Boons, Heirlooms, Implements of Argent had correct formatting (Lvl/Enhancement/Price tables and separate Implement/Weapon lines). The Returning Beast: Totem of the Dancing Leaf was missing the Enhancement Bonus line—added “Enhancement Bonus: attack rolls and damage rolls” in data18.js and _index.js.
- **Source**: fixes-needed.json (Item Sets: AV2:130, AV2:132, AV2:134, RotG:15, DR396:40)
- **Files touched**: `4e_database_files/item/data18.js`, `4e_database_files/item/_index.js`, `fixes-needed.json`, HTML outputs
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Grim Blackguard duplicate powers (1 paragon path)

- **Scope**: paragon path
- **Entries**: Grim Blackguard (paragonpath814): Removed duplicated power block—all path powers (Proof of Domination, Slave to Fury, Altar of Domination, Altar of Fury, Mortal Dread, Uncontrolled Fury) were repeated after the level 20 daily entries; duplicate block and duplicate index text removed.
- **Source**: fixes-needed.json (Grim Blackguard HoS:41 entry)
- **Files touched**: `4e_database_files/paragonpath/data14.js`, `4e_database_files/paragonpath/_index.js`, `fixes-needed.json`, HTML outputs
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Time Wizard's Tools Staff of Time formatting (1 item)

- **Scope**: item
- **Entries**: Time Wizard's Tools (item428): Staff of Time entry in the item set was missing enhancement bonus in display and had cost on the same line as Implement. Added Lvl 30 / +6 / 3,125,000 gp table; moved cost off Implement line; kept Implement: Staff and Enhancement Bonus on separate lines.
- **Source**: fixes-needed.json (Time Wizard's Tools AV2:128 entry)
- **Files touched**: `4e_database_files/item/data8.js`, `4e_database_files/item/_index.js`, `fixes-needed.json`, HTML outputs
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Rings of the Akarot Voice of the Akarot (1 item)

- **Scope**: item
- **Entries**: Rings of the Akarot (item434): Voice of the Akarot power was already present; fixed typo in Target line ("Each enemyin burst" → "Each enemy in burst") in data and _index.
- **Source**: fixes-needed.json (Rings of the Akarot / Voice of the Akarot entry)
- **Files touched**: `4e_database_files/item/data14.js`, `4e_database_files/item/_index.js`, `fixes-needed.json`, HTML outputs
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Battle Cleric's Lore optional class feature (2 entries)

- **Scope**: class
- **Entries**: Cleric (Templar) (class2), Hybrid Cleric (class352): Added optional class feature—Clerics and Hybrid Clerics can choose Battle Cleric's Lore in place of Healer's Lore; added BATTLE CLERIC'S LORE with Benefit (+2 shield bonus to AC, proficiency with scale armor, +2 attack bonus to target when using cleric healing power to allow spending a healing surge). Source: Dragon Magazine 400.
- **Source**: fixes-needed.json (Battle Cleric's Lore + Benefit text entries)
- **Files touched**: `4e_database_files/class/data2.js`, `4e_database_files/class/data12.js`, `4e_database_files/class/_index.js`, `fixes-needed.json`, `index.htm`, `fixes-needed-view.html`
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Summoned Steed (Cavalier) optional class feature (1 item)

- **Scope**: class
- **Entries**: Paladin (Cavalier) (class784): Added optional class feature text and Summoned Steed option at Level 4—Cavaliers can choose Summoned Steed in place of Pace of the Virtuous Charger; added full Summon Celestial Steed power and Celestial Warhorse stat block (source: Dragon Magazine 393).
- **Source**: fixes-needed.json + D&D 4e wiki / Dragon 393
- **Files touched**: `4e_database_files/class/data4.js`, `4e_database_files/class/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Lizard Companion duplicate Opportunity Attack (1 item)

- **Scope**: companion
- **Entries**: Lizard (companion4): Removed duplicate "Opportunity Attack: A lizard gains a +2 bonus to the attack roll when making an opportunity attack" (was listed after Trained Skills).
- **Source**: fixes-needed.json (Familiar's Baldric / Lizard Companion entry; Lizard part fixed)
- **Files touched**: `4e_database_files/companion/data4.js`, `4e_database_files/companion/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-28 — Batch: Channel Divinity powers (4 items)

- **Scope**: class
- **Entries**: 
  - Avenger (class129): Verified already mentions "Each avenger has the power oath of enmity and the Channel Divinity powers abjure undead and divine guidance"
  - Invoker (class127): Added "You gain two CD powers: Rebuke Undead and a power determined by your Divine Covenant" to Channel Divinity section
  - Paladin (class4): Added "You gain two CD powers: Divine Mettle and Divine Strength" to Channel Divinity section
  - Channel Divinity general entry: Documented that classes with Channel Divinity each begin with two CD powers
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/class/data7.js`, `4e_database_files/class/data4.js`, `4e_database_files/class/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-28 — Batch: Wyrm Form power + Unicorn Destrier verification (2 items)

- **Scope**: power, companion
- **Entries**: 
  - Wyrm Form (power5882): Added missing Wyrm Form Breath Weapon Attack (Encounter, Arcane, Implement, Close blast 5) and Wyrm Form Reactive Attack (At-Will, Arcane, Immediate Reaction, triggered when enemy flanks)
  - Unicorn Destrier (associate63): Verified action types are already correct (Kick: Standard, Fey Step: Move, Horn Touch: Minor)
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/power/data2.js`, `4e_database_files/power/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---

- **Scope**: power
- **Entries**: 
  - Wyrm Form (power5882): Added missing Wyrm Form Breath Weapon Attack (Encounter, Arcane, Implement, Close blast 5) and Wyrm Form Reactive Attack (At-Will, Arcane, Immediate Reaction, triggered when enemy flanks)
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/power/data2.js`, `4e_database_files/power/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-28 — Batch: Powers, items, companions (10 items)

- **Scope**: power, item, companion
- **Entries**: 
  - Ardent Surge (power10273): Added Mantle of Impulsiveness rider (+2 speed until end of next turn)
  - Brilliant Corona (power13453): Clarified Effect as "one melee basic attack against a single enemy"
  - Solitaire (all 7 items): Added Special line "You cannot use more than one solitaire in an encounter" to Quartz Lens, Cinnabar, Citrine, Aquamarine, Cerulean, Violet, Zaarani's Solitaire
  - Wolf Animal Companion (associate1): Moved "(add your level to each defense)" from Perception to defense line
  - Bear Animal Companion (associate5): Added "(add your level to each defense)" to defense line
  - Living Zephyr Animal Companion (associate64): Added "(add your level to each defense)" to defense line
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/power/data13.js`, `4e_database_files/power/_index.js`, `4e_database_files/item/data6.js`, `data7.js`, `data8.js`, `data9.js`, `data10.js`, `data11.js`, `4e_database_files/item/_index.js`, `4e_database_files/companion/data1.js`, `data4.js`, `data5.js`, `4e_database_files/companion/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-28 — Batch: Simple fixes (4 items)

- **Scope**: power, ritual, glossary
- **Entries**: 
  - Song of Storms (power2394): Moved Effect line from Hit line to separate Effect line, removed revision note
  - Beast Stalker's Target (power1686): Changed level from 16 to 20 in listing
  - Thief's Lament (ritual279): Fixed table structure - moved "Burst" values to correct Warded Area column
  - Mount (glossary604): Removed duplicate entry, kept glossary56 with multiple source references
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/power/data14.js`, `4e_database_files/power/_listing.js`, `4e_database_files/ritual/data19.js`, `4e_database_files/glossary/_listing.js`, `4e_database_files/glossary/data4.js`, `4e_database_files/glossary/_index.js`, `4e_database_files/index.js`, `4e_database_files/catalog.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json` - all categories clean)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: Remaining simple fixes (4 items)

- **Scope**: power, glossary
- **Entries**: 
  - Psychic Anomaly: Verified Augmentable keyword is on primary power (not secondary) - already correct
  - Darkspiral Aura: Changed "that enemy" to "the triggering enemy" in Effect line
  - Treasure by Party Level: Changed first row from <th> tags to <td> tags (removed table header formatting)
  - Hybrid Essentials classes: Verified all show DR400 (already correct)
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/power/data11.js`, `4e_database_files/power/_index.js`, `4e_database_files/glossary/data16.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: Simple text fixes (6 items)

- **Scope**: item, ritual, power, class, implement
- **Entries**: 
  - Desert Rose: Fixed "a arcane" → "an arcane"
  - Thief's Lament: Moved "Burst" from Skill Check Result column to Warded Area column
  - Beast Stalker's Target: Changed level from 16 to 20
  - Bonus to Defense (Hybrid Warden): Added space before colon
  - Familiar's Baldric: Changed "defense" to "defenses" in level scaling
  - Symbol of Vengeance: Updated damage scaling from 2d8/3d8 to 4d8/6d8 for higher levels
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/item/data11.js`, `data7.js`, `4e_database_files/item/_index.js`, `4e_database_files/ritual/data19.js`, `4e_database_files/ritual/_index.js`, `4e_database_files/power/data6.js`, `4e_database_files/power/_index.js`, `4e_database_files/class/data6.js`, `4e_database_files/class/_index.js`, `4e_database_files/implement/data3.js`, `4e_database_files/implement/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: Goring Weapon fix

- **Scope**: weapon
- **Entries**: 
  - Goring Weapon: Changed power action from "Immediate Reaction" to "Free Action", added note "The published name of this item is Impaling Weapon"
- **Source**: fixes-needed.json + user specification
- **Files touched**: `4e_database_files/weapon/data0.js`, `4e_database_files/weapon/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: Easy medium fixes (7 items)

- **Scope**: item, weapon, implement, power
- **Entries**: 
  - Tattoo of Vengeance: Added "rolls" after "damage" in higher-level versions
  - Crimson Determination: Added "rolls" after "damage" in higher-level versions
  - Wrathful Spirit: Added "rolls" after "damage" in higher-level versions
  - Symbol of Fire and Fury: Added level scaling for dice increase while bloodied (2d6/2d10 at 19/24, 3d6/3d10 at 29)
  - Shoulderbow: Added (embedded component) trait and requirement line
  - Symbol of Revivification: Added enhancement, level, and cost table
  - In Death, Life: Added Channel Divinity line
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/item/data9.js`, `data12.js`, `data17.js`, `4e_database_files/item/_index.js`, `4e_database_files/weapon/data18.js`, `4e_database_files/weapon/_index.js`, `4e_database_files/implement/data14.js`, `4e_database_files/implement/_index.js`, `4e_database_files/power/data3.js`, `4e_database_files/power/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: Lightweight medium fixes (7 items)

- **Scope**: weapon, item, implement
- **Entries**: 
  - Hestavar Dueling Blade: Removed period before "the", fixed level 24→23 and cost 525k→425k
  - Tempest Fan: Added Lightning/Teleportation keywords, fixed "close 3 burst" → "close burst 3"
  - Ring of Fury: Added Special line about Belt of Fiends synergy
  - Sandals of the Temporal Step: Added Special line about Mark of Passage synergy
  - Flaming Weapon: Added scaling ongoing damage (10 at 15/20, 15 at 25/30)
  - Tuning Songblade: Added leveled ongoing damage (10 at 14/19, 15 at 24/29)
  - Rod of Scouring Justice: Added leveled ongoing damage (10 at 23/28)
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/weapon/data14.js`, `4e_database_files/weapon/data6.js`, `4e_database_files/weapon/_index.js`, `4e_database_files/item/data2.js`, `4e_database_files/item/data3.js`, `4e_database_files/item/data8.js`, `4e_database_files/item/_index.js`, `4e_database_files/implement/data5.js`, `4e_database_files/implement/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: All remaining simple fixes (15+ items)

- **Scope**: item, class, item sets, typo fixes
- **Entries**: 
  - Item fixes: Kord's Mighty Strength, Potion of Spirit, Sliver of Salvation, Warding Mind (removed extra text from higher-level versions)
  - Verified correct: Lockburst Chalk, Sigil of Companionship, Battle-Scarred Champion, Beloved Performer, Imperial Oration, Sanctuary's Poise, Torog's Lamentation, Alchemist's Frost
  - Item Sets: Changed "Pieces" to "Wielders" in all item set benefit tables (20 data files)
  - Class: Hybrid Warden (Bonus to Defense: "+1 Fortitude, +1 Will" → "+1 Fortitude or +1 Will")
  - Typo fixes: Fixed common patterns across 124 files ("damage ." → "damage.", ".." → ".", ",." → ".", "turn,any" → "turn, any", ". </p>" → ".</p>")
  - Verified: Determining Cover for Melee Attacks (already correct), Wizard (Mage) duplicates (already removed)
- **Source**: fixes-needed.json + fixes-priority.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/item/data*.js` (24 files), `4e_database_files/item/_index.js`, `4e_database_files/class/data6.js`, `4e_database_files/class/_index.js`, `4e_database_files/*/data*.js` (124 files for typo fixes), `4e_database_files/*/_index.js` (multiple categories), `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---

## 2026-01-27 — Batch: Remaining simple fixes (11 items)

- **Scope**: class, theme, monster
- **Entries**: Rogue (Scoundrel) - Sharpshooter Talent text, Vigilante theme - Level 5/Starting feature swap, Runescribed Dracolich - Blackfire attack, Monk - Unarmed Combatant text, Warlock (Binder) - removed hexblade-only lines, Warlock (Hexblade) - removed binder-only lines, Warlock - Vestige Pact Boons to Free Actions
- **Source**: fixes-needed.json + fixes-priority.json
- **Files touched**: `4e_database_files/class/data*.js`, `4e_database_files/class/_index.js`, `4e_database_files/theme/data19.js`, `4e_database_files/monster/data16.js`, `4e_database_files/monster/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: All remaining Waist items (7 items)

- **Scope**: item
- **Entries**: Baldric of Dividing Ranks, Belt of Fiends, Belt of Sacrifice, Belt of Sonnlinor Righteousness, Belt of Vigor, Dynamic Belt, Swimtide Harness
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/item/data1.js`, `data6.js`, `data11.js`, `data12.js`, `data14.js`, `4e_database_files/item/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: All remaining Hands items (8 items)

- **Scope**: item
- **Entries**: Cat Paws, Caustic Gauntlets, Flaying Gloves, Gauntlets of Blood, Gloves of the Healer, Gorilla Gloves, Rampaging Slayer's Gloves, Storm Gauntlets
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/item/data2.js`, `data3.js`, `data11.js`, `data13.js`, `data14.js`, `data19.js`, `4e_database_files/item/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: All remaining Heads items (4 items)

- **Scope**: item
- **Entries**: Helm of Opportunity, Laurel Circlet, Philosopher's Crown, Stag Helm
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/item/data2.js`, `data3.js`, `data9.js`, `data16.js`, `4e_database_files/item/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: All remaining Arms items (7 items)

- **Scope**: item, armor
- **Entries**: Angelsteel Shield, Bloodsoaked Bracers, Bracers of Mighty Striking, Bracers of the Perfect Shot, Trauma Bracers, Shield of the Barrier Sentinels, Shield of the Guardian
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/item/data12.js`, `data13.js`, `data19.js`, `4e_database_files/item/_index.js`, `4e_database_files/armor/data3.js`, `data4.js`, `data14.js`, `data16.js`, `4e_database_files/armor/_listing.js`, `4e_database_files/armor/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-27 — Batch: 4 Arms items (remove text from higher-level versions)

- **Scope**: item
- **Entries**: Bracers of Archery, Breach Bracers, Cold Iron Bracers, Iron Armbands of Power
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/item/data3.js`, `data4.js`, `data8.js`, `data14.js`, `4e_database_files/item/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-26 — Arcane Defiling power (missing entry)

- **Scope**: power
- **Entries**: power16699 (Arcane Defiling)
- **Source**: Portable Compendium SQL (Dark Sun Campaign Setting, page 80)
- **Files touched**: , , , , , , 
- **Validation**: pass ()
- **Smoke test**: pending

## 2026-01-26 — Batch: 23 powers with secondary attacks (encounter not daily)

- **Scope**: power
- **Entries**: Form of the Primeval Ape, Form of the Primeval Bear, Form of the Primeval Boar, Form of the Primeval Lizard, Form of the Primeval Spider, Form of the Primeval Wolf, Form of the Primeval Cat, Form of the Primeval Raptor, Form of the Primeval Serpent, Form of the Night Owl, Form of the Walking Conflagration Attack, Form of the Vengeful Storm Attack, Form of the Magma Brute Attack, Form of the Seething Sandstorm Attack, Form of the Imperious Phoenix Attack, Form of the Erupting Volcano Attack, Diabolic Transformation, Storm of Debris, Of Wood and Stone, Stone-Shatter Strike, Form of the Living Breach Attack, Form of the Forge Spirit, Form of the All-Spirit
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/power/data1.js`, `data2.js`, `data4.js`, `data5.js`, `data7.js`, `data11.js`, `data12.js`, `data14.js`, `data16.js`, `data17.js`, `data18.js`, `4e_database_files/power/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

## 2026-01-26 — Jousting Charge feat (missing entry)

- **Scope**: feat
- **Entries**: feat3799 (Jousting Charge)
- **Source**: Portable Compendium SQL (Dragon Magazine 401)
- **Files touched**: `4e_database_files/feat/_listing.js`, `4e_database_files/feat/data19.js`, `4e_database_files/feat/_index.js`, `4e_database_files/index.js`, `4e_database_files/catalog.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

## 2026-01-26 — Batch: 15 Paragon Multiclassing feats

- **Scope**: feat
- **Entries**: Agile Brawler, Arcane Aegis, Battle Acumen, Battle Instructor, Channel of Faith, Channel of Invocation, Channel of Valor, Channel of Vengeance, Courageous Shooter, First In, Healing Song, Implement Master, Sorcerous Power, Walker in Gloom, Wild Savant
- **Source**: fixes-needed.json
- **Files touched**: `4e_database_files/feat/data1.js`, `data2.js`, `data3.js`, `data4.js`, `data5.js`, `data6.js`, `data10.js`, `data13.js`, `data14.js`, `data17.js`, `data19.js`, `4e_database_files/feat/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

## 2026-01-26 — Batch: 2 Epic tier feats

- **Scope**: feat
- **Entries**: Improved Steed (Silver Dragon), Fey Shift
- **Source**: fixes-needed.json
- **Files touched**: `4e_database_files/feat/data4.js`, `4e_database_files/feat/data15.js`, `4e_database_files/feat/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---

## 2026-01-26 — Batch: 17 Paragon tier feats

- **Scope**: feat
- **Entries**: Alert Familiar, Secrets of Belial, Elusive Hexer, Aspect of the Elements, Improved Steed (Celestial Behemoth), Improved Steed (Celestial Pegasus), Flitting Harrier, Guardian of the Weeping Willow, Burning Vapors, Fiery Blood, Icy Heart, Lightning Soul, Thunder's Rumble, Thri-Kreen Scuttling Master, Vigorous Familiar, Free-Ranging Familiar, Infernal Captain's Fury
- **Source**: fixes-needed.json
- **Files touched**: `4e_database_files/feat/data0.js`, `data2.js`, `data3.js`, `data5.js`, `data8.js`, `data9.js`, `data10.js`, `data11.js`, `data12.js`, `data15.js`, `data17.js`, `4e_database_files/feat/_index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-26 — Batch: 4 simple fixes (powers and items)

- **Scope**: power, item
- **Entries**: `power12570` (Shadow Knives), `item1218` (Eremann, Speaker of the Dead), `item1655` (Ironheart Tattoo), `item2050` (Pierced Heart Tattoo)
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/power/data10.js`, `4e_database_files/power/_index.js`, `4e_database_files/item/data18.js`, `4e_database_files/item/data15.js`, `4e_database_files/item/data10.js`, `4e_database_files/item/_index.js`, `fixes-needed.json`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-26 — Glossary: Ammunition rules

- **Scope**: glossary
- **Entries**: `glossary425` (Ammunition)
- **Source**: fixes-needed.json
- **Files touched**: `4e_database_files/glossary/data5.js`, `4e_database_files/glossary/_listing.js`, `4e_database_files/glossary/_index.js`, `4e_database_files/index.js`, `fixes-needed.json`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-26 — Batch: 5 simple item fixes

- **Scope**: armor, item
- **Entries**: Shockweave Armor, Headband of Intellect, Helm of Heroes, Gloves of Venom, Twice-Clawed Gauntlets
- **Source**: fixes-needed.json
- **Files touched**: `4e_database_files/armor/data17.js`, `4e_database_files/armor/_index.js`, `4e_database_files/item/data0.js`, `4e_database_files/item/data1.js`, `4e_database_files/item/data7.js`, `4e_database_files/item/data19.js`, `4e_database_files/item/_index.js`, `fixes-needed.json`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-26 — Batch: 5 simple power fixes

- **Scope**: power
- **Entries**: `power3287` (Body Shield), `power5831` (Sabotage Trap), `power1605` (Weaponsoul Dance), `power9484` (Grasp of the Obsidian Tomb), `power8097` (Ardent Vow), `power7240` (Virtue's Touch)
- **Source**: fixes-needed.json
- **Files touched**: `4e_database_files/power/_listing.js`, `4e_database_files/power/data7.js`, `4e_database_files/power/data11.js`, `4e_database_files/power/data5.js`, `4e_database_files/power/data4.js`, `4e_database_files/power/data17.js`, `4e_database_files/power/data0.js`, `4e_database_files/power/_index.js`, `fixes-needed.json`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-26 — Dance of Flame typo

- **Scope**: power
- **Entries**: `power7001` (Dance of Flame)
- **Source**: fixes-needed.json
- **Files touched**: `4e_database_files/power/data1.js`, `4e_database_files/power/_index.js`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-26 — Batch: feats, implements, shields

- **Scope**: feat, implement, armor
- **Entries**: Body Shield (Garrote Expert), Sniper’s Aim, Prophetic Preparation, The Fearcatcher, Light/Heavy/Barbed Shield
- **Source**: fixes-needed.json
- **Files touched**: `4e_database_files/feat/data10.js`, `4e_database_files/feat/data2.js`, `4e_database_files/feat/data7.js`, `4e_database_files/feat/_index.js`, `4e_database_files/implement/data3.js`, `4e_database_files/implement/_index.js`, `4e_database_files/armor/data7.js`, `4e_database_files/armor/data8.js`, `4e_database_files/armor/data19.js`, `4e_database_files/armor/_index.js`, `fixes-needed.json`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Hybrid Classes fixes (8 items)

- **Scope**: class, glossary
- **Entries**: 
  - Hybrid Ardent (class588): Added missing Mantle of Impulsiveness (Hybrid) power and rider for Ardent Surge
  - Hybrid Monk (class609): Added missing Desert Wind (Hybrid), Eternal Tide (Hybrid), and Iron Soul (Hybrid) monastic traditions with their Flurry of Blows powers
  - Hybrid Battlemind (class590): Added missing Wild Focus and Persistent Harrier (Hybrid) powers
  - Hybrid Psion (class610): Added missing Shaper Focus (Hybrid) option with Minor Creation power
  - Hybrid Vampire (class893): Fixed healing surges text and bonus to defense (changed from "+1 Fortitude, +1 Will" to "+1 Fortitude or +1 Will")
  - Glossary: Added "Creating a Hybrid Character" (glossary362)
  - Glossary: Added "Psionic Augmentation and Hybrid Characters" (glossary364)
- **Source**: fixes-needed.json + Portable Compendium SQL
- **Files touched**: `4e_database_files/class/data8.js`, `4e_database_files/class/data9.js`, `4e_database_files/class/data10.js`, `4e_database_files/class/data13.js`, `4e_database_files/class/_index.js`, `4e_database_files/glossary/data2.js`, `4e_database_files/glossary/data4.js`, `4e_database_files/glossary/_listing.js`, `4e_database_files/glossary/_index.js`, `4e_database_files/index.js`, `fixes-needed.json`, `index.htm`
- **Validation**: pass (`compendium-validation.json`)
- **Smoke test**: pending

---
