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
