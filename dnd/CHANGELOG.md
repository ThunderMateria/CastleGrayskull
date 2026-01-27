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
