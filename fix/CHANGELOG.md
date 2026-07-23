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
## 2026-07-12 — Batch: Missing book data (4 new entries + 2 fixes)

- **Scope**: monster, glossary
- **New entries**: Tiamat (monster115941, Level 35 Solo Brute, Draconomicon: Chromatic Dragons p.245); Rot Slinger Decayer (monster115942, Level 20 Artillery, E1 Adventure Book Two p.13); Fledgling Black Dragon (monster115943, Level 2 Solo Lurker, 2010 Starter Set DM Book p.47 — note the compendium Fledgling White Dragon is the Monster Vault p.64 variant, which differs from the Starter Set tuning; this entry is faithful to the Starter Set printing the errata doc cites); Dragonshard Augments (glossary682, EPG p.111 rules text).
- **Fixes**: Blackstar Idol (monster2665) — added the missing Blackstar Pulse (Healing) aura 3 per E1 Book Two p.63. Kalarel (monster822) — repaired mangled type line to "Medium natural humanoid (human)"; otherwise verified to match H1 p.78 as printed (the book itself carries a vestigial "see also shadow form below" reference to a mechanic that appears nowhere in the adventure — checked pp.78-80).
- **Observed but NOT changed** (for maintainer adjudication): Blackstar Idol has Blackstar Nova at +26 vs. Will and Languages "-", where the p.63 "Blackstar Idol of Timesus" printing reads +24 vs. Will and Languages Primordial; the compendium pages cited (19, 48) may reflect a different instance. Glossary catalog count (536) vs listing rows (545) were already offset by 9 before this batch; both were incremented by 1 consistently.
- **Source**: verbatim transcriptions from page scans, read visually (screenshots retained by contributor). Recharge dice transcribed as glyphs (⚄⚅ etc.) matching existing entry conventions.
- **Files touched**: monster/{data1,data2,data3,data5,_index,_listing}.js, glossary/{data2,_index,_listing}.js, catalog.js (monster 5326→5329, glossary 535→536), index.js, fix/fixes-needed.json (6 items → corrected)
- **Validation**: all touched jsonp files parse; monster listing rows == catalog count (5329); name lookups resolve (tiamat now [deity141, deity43, monster115941])
## 2026-07-12 — Batch: Cairn item corrections (2 entries fixed)

- **Scope**: implement, item
- **Entries**: Ice Scepter (implement3739), Crown of Winter (item3754) — corrections to our own earlier batch, found by verifying the entries against the Cairn of the Winter King page scans (p.8 / p.29).
- **Fixes**: Ice Scepter — Critical is "+1d8 cold damage per plus" (was wrongly "+2d8 cold damage"); implement label "Rod, Wand, Staff" per the book; encounter power wording "...for the attack rolls and the damage roll"; flavor text added. Crown of Winter — **added the missing Power (Encounter ✦ Cold, Psychic)** (Immediate Reaction: triggering enemy takes 5 cold and psychic damage and is immobilized until the end of its next turn); daily effect reads "You reroll the attack roll and use the new result"; flavor text added.
- **Source**: verified against page scans of Monster Vault: Cairn of the Winter King (screenshots retained by contributor).
- **Files touched**: implement/{data19,_index,_listing}.js, item/{data14,_index}.js
## 2026-07-12 — Batch: Bound Soul companion (1 new entry)

- **Scope**: companion
- **Entries**: Bound Soul (associate115, Summoned Creature, Soul Binder paragon path, Dragon 427) — was the open fixes-needed item [Other] "creature from Soul Binder paragon path (D427) is entirely absent."
- **Source**: heroic4e.com compendium (ID_DRAG427_SOUL), formatted per the Air Archon Grunt summoned-creature template, then **verified line-by-line against Dragon 427 p.14**. Corrections from verification: base Hit line keeps "modifier" (as printed); Level 21 line omits it (as printed); Minor Action is At-Will (1/round); standard action carries (necrotic, radiant) keywords; publishedIn page 14 added.
- **Files touched**: companion/{data15,_index,_listing}.js, catalog.js (companion 193→194), index.js, fix/fixes-needed.json
- **Validation**: pending
- **Smoke test**: pending

---
## 2026-07-12 — Batch: Cairn of the Winter King items (2 new entries)

- **Scope**: implement, item
- **Entries**: Ice Scepter (implement3739, Level 6 Rare, Cairn of the Winter King p.8), Crown of Winter (item3754, Level 8 Rare, Cairn of the Winter King p.29) — both were "missing from the compendium" in fixes-needed.json.
- **Source**: heroic4e.com compendium (manually entered from the adventure); stat text cross-contributed. These items never appeared in the online compendium so no official ids exist — implement3739/item3754 are next-sequential; maintainers should feel free to renumber.
- **Files touched**: `implement/data19.js`, `implement/_index.js`, `implement/_listing.js`, `item/data14.js`, `item/_index.js`, `item/_listing.js`, `catalog.js` (implement 647→648, item 1964→1965), `index.js`, `fix/fixes-needed.json`
- **Validation**: pending
- **Smoke test**: pending

---
## 2026-07-07 — Batch: ID alignment (remaps + new entries)

- **Scope**: glossary, item, power, background
- **Source**: Audit against 2 prior compendium dumps (mostly in pursuit of making sure ids were in alignment for cbloader)
- **Id remaps (14)** — align iws ids with compendium dumps:
  - glossary: 680→366 (Backgrounds), 678→365 (Paragon Multiclassing), 681→370 (Paragon Multiclassing and Psionic Augmentation), 679→170 (Healing Surge), 682→424 (Tattoos), 683→472 (Warforged Components), 677→681 (Battle Standards), 684→680 (Wands). Applied as a collision-free chain (677→681 lands after 681→370 vacates it; 684→680 after 680→366).
  - item: 1610→3753 (Immurement of the Strident Statuary).
  - power: 12682→16704 (Shielding Blade), 12683→16703 (Bludgeoning Counterstrike), 5184→16700 (Armor of Wrath), 5185→16701 (Preserver's Rebuke), 16333→16702 (Elemental Transformation).
  - power: Ardent Alacrity had a power id overlapping with an existing power, corrected it to what it should've been and deleted the nonexistent/broken pointer (Arcane Armor) that was there 
- **New entries (86)** — IWS lacked: 9 backgrounds (background283–291: Blood of the Darkwalker, Fastpaw, Greenbeard, Knight of Synnoria, Lashrael Crusader, Northman Reaver, Skinwalker, Totem-Mystic, Wrath of the Ancients) + 77 glossary keyword/rules entries.
- **Files touched**: `glossary/{_listing,_index,dataN}.js`, `item/{_listing,_index,dataN}.js`, `power/{_listing,_index,dataN}.js`, `background/{_listing,_index,dataN}.js`, `index.js`, `catalog.js` (48 files, 436 insertions / 137 deletions).
- **Validation**: pass (check_validation.py exit 0)
- **Smoke test**: pending

---
## 2026-02-01 — Batch: Sorcerer-King Pact feats (D390) — benefit text (enhance not augment)

- **Scope**: feat (Sorcerer-King Pact, Dragon Magazine 390)
- **Entries**: 9 fix entries applied across 12 feats—Golden Lion of Urik, Tyrian Ascendant (Greater Pact); Balican Praetor, Balican High Praetor, Favored of Raam, Nibenese Bride, Spirit Talker of Lalali-Puy, Tyrian Bureaucrat, Yellow Cloak of Urik (Lesser Pact); Nibenese Favored Wife, Champion of Raam, Draji Devotee (Greater Pact). Benefit text: augment → enhance, augmented → enhanced; Golden Lion: added Once per encounter limits and closing sentence; Tyrian Ascendant: added against you; Lesser Pact feats: Once per encounter when you enhance hand of blight, the enhance would deal.
- **Source**: fix/fixes-needed.json (Feats: D390 Sorcerer-King Pact entries). SQL did not have corrected text; changes applied from fix spec.
- **Files touched**: 4e_database_files/feat/data0.js, data2.js, data3.js, data4.js, data5.js, data6.js, data7.js, data8.js, data9.js, data16.js, data17.js, data19.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Alchemical Items (Multiple Sources) — ritual rarity

- **Scope**: ritual (alchemical item rituals)
- **Entries**: 22 rituals—embedded alchemical item descriptions listed as Uncommon; changed to Common per fix. Rituals: acidic fire (237), alchemist's spark (238), antivenom (138), blinding bomb (141), clarity salts (348), clear-path mist (239), clockwork bomb (240), giggle gas (349), herbal poultice (148), inferno oil (243), kinetic oil (350), lodret leaf (245), noxious grenade (246), panther tears (247), resonance crystal (248), spotted toadstool venom (249), suppression crystal (250), tension wheel (251), tethercord (252), tracking dust (157), universal solvent (158), walking death (351).
- **Source**: fix/fixes-needed.json (Rituals: "Alchemical Items (Multiple Sources)...")
- **Files touched**: 4e_database_files/ritual/_index.js, data0.js–data19.js (44 lines); fix/scripts/fix_alchemical_ritual_rarity.py (new); fix/fixes-needed.json, fix/index.htm
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Ammunition label (Quarrel of Biting typo) — 1 entry

- **Scope**: weapon (ammunition)
- **Entries**: Quarrel of Biting (weapon3471)—data11.js had typo "Arrow or bolt or bolt"; corrected to "Arrow or bolt". All other AV2/EPG/DR373 magical ammo were already relabeled in a prior batch (13 items).
- **Source**: fix/fixes-needed.json (Items: "Ammunition: All AV2 magical ammo...")
- **Files touched**: 4e_database_files/weapon/data11.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Salve of Slipperiness (Alchemical Ritual) — 1 entry

- **Scope**: ritual
- **Entries**: Salve of Slipperiness (Alchemical Ritual) (AV:29)—ritual lacked higher level versions; added Level 13: +16 bonus, Level 18: +19 bonus, Level 23: +21 bonus, Level 28: +24 bonus to ritual151 in ritual/data11.js and ritual/_index.js (matching item scaling).
- **Source**: fix/fixes-needed.json (AV:29)
- **Files touched**: 4e_database_files/ritual/data11.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Bludgeoning Counterstrike and Shielding Blade (Stalwart Knight Utility 12) — 2 entries

- **Scope**: power
- **Entries**: (1) Bludgeoning Counterstrike (Stalwart Knight Utility 12) (HotFL:141)—was missing from Power listing; added power12683 to power/data3.js, _index.js, _listing.js (Encounter ✦ Martial, Immediate Reaction, Personal; Trigger: enemy misses you with melee attack while wielding hammer or mace; Effect: +2 power bonus to attack rolls with hammer/mace vs. triggering enemy). (2) Shielding Blade (Stalwart Knight Utility 12) (HotFL:140)—was missing; added power12682 to power/data2.js, _index.js, _listing.js (Encounter ✦ Martial, Immediate Reaction, Personal; Trigger: enemy misses you with melee attack while wielding heavy blade; Effect: +2 power bonus to all defenses vs. triggering enemy). Source: Portable Compendium ddiPower.sql.
- **Source**: fix/fixes-needed.json, Portable Compendium New/sql/ddiPower.sql
- **Files touched**: 4e_database_files/power/data2.js, data3.js, _index.js, _listing.js; 4e_database_files/catalog.js (power count 9413→9415), index.js ("bludgeoning counterstrike"→power12683, "shielding blade"→["weapon2486","power12682"]); fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Elemental Transformation (Legendary Hexblade Attack 20) — 1 entry

- **Scope**: power
- **Entries**: Elemental Transformation (Legendary Hexblade Attack 20) (HotEC:135)—was missing from Power listing; added power16333 to power/data13.js, power/_index.js, power/_listing.js (Daily ✦ Arcane, Elemental, Polymorph; Minor Action Personal; resist 5 acid/cold/fire/lightning/thunder, +2 AC and Fort, secondary power once per round; Elemental Transformation Secondary Power At-Will Close burst 1). Source: Portable Compendium ddiPower.sql.
- **Source**: fix/fixes-needed.json, Portable Compendium New/sql/ddiPower.sql
- **Files touched**: 4e_database_files/power/data13.js, _index.js, _listing.js; 4e_database_files/catalog.js (power count 9412→9413), index.js ("elemental transformation"→power16333); fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Preserver's Rebuke (Invoker Feature) — 1 entry

- **Scope**: power
- **Entries**: Preserver's Rebuke (Invoker Feature) (PHB2:102)—was missing from Power listing; added power5185 to power/data5.js, power/_index.js, power/_listing.js (Encounter, Immediate Reaction, Personal; Channel Divinity; Trigger: enemy within 10 hits your ally; Effect: bonus to next attack roll vs. triggering enemy = Int mod). Source: Portable Compendium ddiPower.sql.
- **Source**: fix/fixes-needed.json, Portable Compendium New/sql/ddiPower.sql
- **Files touched**: 4e_database_files/power/data5.js, _index.js, _listing.js; 4e_database_files/catalog.js (power count 9411→9412), index.js ("preserver's rebuke"→power5185); fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Armor of Wrath (Invoker Feature) — 1 entry

- **Scope**: power
- **Entries**: Armor of Wrath (Invoker Feature) (PHB2:102)—was missing from Power listing; added power5184 to power/data6.js, power/_index.js, and power/_listing.js (Encounter, Immediate Reaction, Close burst 5; Channel Divinity; Trigger: enemy within 5 hits you; Effect: radiant damage = Con mod, push 2; Level 11/21 scaling). Source: Portable Compendium ddiPower.sql.
- **Source**: fix/fixes-needed.json, Portable Compendium New/sql/ddiPower.sql
- **Files touched**: 4e_database_files/power/data6.js, _index.js, _listing.js; 4e_database_files/catalog.js (power count 9410→9411), index.js ("armor of wrath"→power5184); fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Consumables and Alchemical Items — 3 entries

- **Scope**: weapon (ammunition), item (alchemical)
- **Entries**: (1) Alchemist's Spark Ammunition (EPG:99)—added missing power details (Power (Lightning) ✦ Consumable, Area burst 1 within 10, +6 vs. Reflex; 1d6 lightning damage and -1 penalty to attack rolls; Level 9/14/19/24/29 scaling) to weapon/data14.js and weapon/_index.js (from Portable Compendium ddiItem.sql). (2–3) Salve of Slipperiness (Alchemical Item) (AV:29)—added higher-level bonus lines (Level 13: +16; Level 18: +19; Level 23: +21; Level 28: +24) to item/data2.js and item/_index.js (from ddiItem.sql); both duplicate fix entries marked corrected.
- **Source**: fix/fixes-needed.json, Portable Compendium New/sql/ddiItem.sql
- **Files touched**: 4e_database_files/weapon/data14.js, _index.js; 4e_database_files/item/data2.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Races, Classes, Paragon Paths, and Features — 4 entries

- **Scope**: companion (animal companions), class (hybrid)
- **Entries**: (1) Wolf Animal Companion (HotFK:91)—added low-light vision to data1.js and _index.js; "(add your level to each defense)" already present. (2) Living Zephyr (HotEC:62)—"(add your level to each defense)" already present in data4.js and _index.js; marked corrected (no data change). (3) Hybrid Assassin (Executioner)—added Way of the Ninja (Hybrid) guild option with Ninja-to Rush, Poisonous Shuriken, Whirling Kusari-gama to class/data11.js. (4) Hybrid Fighter (DSCS)—added Arena fighting (Hybrid) to Hybrid Talent Options in class/data13.js and class/_index.js.
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/companion/data1.js, _index.js; 4e_database_files/class/data11.js, data13.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Simple fixes (class) — 5 entries

- **Scope**: class
- **Entries**: (1) Cleric (Templar) (PHB1:61)—added free ritual book sentence (Gentle Repose + one 1st-level ritual) to RITUAL CASTING in class/data2.js and _index.js. (2) Wizard (All) Cantrips—added cantrip list (Ghost Sound, Light, Mage Hand, Prestidigitation, Suggestion, Disrupt Undead, Spook) to Wizard (Arcanist) CANTRIPS in class/data9.js and _index.js. (3) Wizard (Sha'ir) Familiars—added Sha'ir-specific familiars list (Daolanin, Djinnling, Efreetking, Maridan) to GEN SERVANT in class/data18.js and _index.js. (4) One-handed Weapon Talent (Hybrid)—Hybrid Fighter: "attack rolls" → "weapon attack rolls" in class/data13.js and _index.js. (5) Hybrid Vampire (DR400:6)—healing surges sentence already present; marked corrected (no data change).
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/class/data2.js, data9.js, data13.js, data18.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Simple fixes (items, glossary, class) — 10 entries

- **Scope**: item, glossary, class
- **Entries**: (1) Chaos Cloak (item858)—removed duplicated die-roll labels ("1-2: 1-2:" → "1-2:", etc.) in Power Effect. (2) Amulet of Psychic Interference (item499)—Daily Power effect tiers: Level 5 or 10: 10 damage; Level 15 or 20: 15; Level 25 or 30: 20 (was 10/15, 20/30). (3) Initiative (glossary637)—added initiative modifier components: one-half level + Dexterity + other bonuses (RC:192). (4) Retraining (glossary625)—added Theme Retraining paragraph (HotFW:104). (5) Primordial Channeler—already "11th level"; marked corrected. (6) Druid (Sentinel) / Hybrid Druid (Sentinel)—"Primal Guardian (Sentinel)" → "Primal Guardian" in class779, class894, _index. (7) Magic Items listing—note; marked corrected. Marked corrected (no data change): Die rolls duplicated, Amulet tiers, Initiative, Retraining, Primordial Channeler, Druid Primal Guardian, Magic Items listing.
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/item/data18.js, data19.js, _index.js; 4e_database_files/glossary/data5.js, data17.js, _index.js; 4e_database_files/class/data14.js, data19.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Blade of Vengeance, Spying Mirrors, Courageous Strike (3 fixes)

- **Scope**: weapon, item, power
- **Entries**: (1) Blade of Vengeance (weapon678)—added Special line "This weapon is part of the Radiant Temple Treasures item set"; fixed typo mmistat → mistat. (2) Spying Mirrors (pair) (item2593)—added Special paragraph: "The two mirrors must be used together; the power does not function if the mirrors are separated or if one is lost." (3) Courageous Strike (power10287)—removed erroneous "one ally adjacent to the target can make a melee basic attack against it as an opportunity action" from Augment 2 Hit line (PHB3:28 errata; duplicated Mindlink Strike).
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/weapon/data18.js, _index.js; 4e_database_files/item/data13.js, _index.js; 4e_database_files/power/data7.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Remaining Companions and Implements fixes

- **Scope**: implement, glossary, companion
- **Entries**: (Implements) Accurate Implements [All] (MME:41)—updated Accurate property in glossary and all accurate implement entries (dagger, ki focus, orb, rod, staff, symbol, totem, wand) to "You gain a +1 bonus to implement attack rolls when you make an implement attack with an accurate implement" so the bonus is clearly limited to implement attacks made with the accurate implement. Master's Wand of Magic Missile—already Level 4+ in data; marked corrected. (Companions) Vadalis-bred Griffon (EPG:79)—Melee Basic Attack: added "+ 3" and "AC" so it reads "Claw; level + 3 vs. AC; 2d6 + Strength modifier damage" in companion/data14.js and companion/_index.js. Cooperative Charge listed 3 times—removed two duplicate Cooperative Charge paragraphs from Vadalis-bred Griffon in data14.js and _index.js (kept one).
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/implement/_index.js, data2.js, data3.js, data6.js, data7.js, data11.js, data18.js, data19.js; 4e_database_files/glossary/_index.js (no net change); 4e_database_files/companion/data14.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Vestige of Kulnoghrim miscoloring; 4 feats Epic Tier label

- **Scope**: power, feat
- **Entries**: (1) Vestige of Kulnoghrim—power/data11.js: changed &lt;h1 class=encounterpower&gt; to class=dailypower so the Daily power displays with correct (daily) coloring. (2) Earthwalker, Haunted, Seastrider, Windfoot—added Epic Tier label in feat data (data0.js, data3.js, data14.js, data17.js) and feat/_index.js so all four show "Epic Tier" like other 21st-level feats.
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/power/data11.js; 4e_database_files/feat/data0.js, data3.js, data14.js, data17.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Tier 3 simple fixes (implement, item, monster)

- **Scope**: implement, item, monster
- **Entries**: (12) Rod of the Churning Inferno—added Level 17 or 22: ongoing 10 fire damage; Level 27: ongoing 15 fire damage in implement/data17.js and implement/_index.js. (13) Sandals of Precise Stepping—removed "Gain a " from property in item/data7.js and item/_index.js. (14) Black Slaad (Void Slaad)—Zone of Oblivion: changed from (zone) At-Will to (when reduced to 0 hit points) ✦ Zone in monster/data13.js and monster/_index.js.
- **Source**: fix/fixes-needed.json, fix/batch-simple-fixes.md
- **Files touched**: 4e_database_files/implement/data17.js, _index.js; 4e_database_files/item/data7.js, _index.js; 4e_database_files/monster/data13.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Tier 2 simple fixes (armor, weapon, companion)

- **Scope**: armor, weapon, companion
- **Entries**: (7) Ironclad Armor—augment already "The damage equals 1d10 per plus"; marked corrected. (8) Gauntlet Axe—no "light shield" line in data; marked corrected. (9) Lizard/Serpent Companion—removed duplicate Opportunity Attack sentence from Serpent in companion/data6.js and companion/_index.js; Lizard entry marked corrected. (10) Wrab Familiar—added blindsight range 5 in companion/data0.js and companion/_index.js. (11) Simian companion—added Manipulate Items to Trained Skills in companion/data11.js and companion/_index.js.
- **Source**: fix/fixes-needed.json, fix/batch-simple-fixes.md
- **Files touched**: 4e_database_files/companion/data0.js, data6.js, data11.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-30 — Batch: Tier 1 simple fixes (armor, item, monster, class)

- **Scope**: armor, item (Familiar slot), monster, class
- **Entries**: (1) Predator's Hide—higher-level already "defenses"; marked corrected. (2) Familiar's Baldric—higher-level already "defenses"; marked corrected. (3) Angel of Tiamat—defenses already 35/35/31/30; marked corrected. (4) Eclavdra Eilservs—On Your Knees attack: "3" → "Melee 3" in data4.js and monster _index.js. (5) Warlock (PHB:131)—removed Prime Shot line "You do not gain this feature if you choose the Beast Mastery fighting style." from class/data7.js and class/_index.js. (6) Classes that start with A (Ardent, Artificer, Assassin, Avenger)—"Creating A..." → "Creating AN..." in class data5.js, data6.js, data9.js and class/_index.js.
- **Source**: fix/fixes-needed.json, fix/batch-simple-fixes.md
- **Files touched**: 4e_database_files/monster/data4.js, _index.js; 4e_database_files/class/data5.js, data6.js, data7.js, data9.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: 10 simple text corrections (feats, weapons, implements, glossary)

- **Scope**: feat, weapon, implement, glossary
- **Entries**: (1) Dragon Magazine 400 Feats—17 feats Published in 402 → 400. (2) Hidden Weapon—removed redundant Special line. (3) Scorpion Tail Blade—critical ongoing poison damage tiered by level. (4) Orb of Impenetrable Escape—added Critical: +1d6 per plus. (5) Master's Wand of Magic Missile—level 4+. (6) Earthfall Totem—Level 17, 22, or 27: 2d6 extra damage. (7) Accurate (glossary)—bonus when making implement attack with accurate implement. (8) Ki Focuses (six)—Published in D398, not HoS. (9) Swift Blade Style—already correct. (10) Dread of Sakkors—already correct.
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/feat (Dragon 400), weapon (Hidden Weapon, Scorpion Tail Blade), implement (Orb, Master's Wand, Earthfall Totem, Ki Focuses), glossary (accurate); fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Aggressive Familiar, Powerful Lure (Paragon tier label)

- **Scope**: feat
- **Entries**: (1) Aggressive Familiar [Familiar]—added Paragon Tier label to data and _index (was missing; listing already Paragon). (2) Powerful Lure—same.
- **Source**: fix/fixes-needed.json (Feats that should be labeled as Paragon)
- **Files touched**: 4e_database_files/feat/data14.js, data7.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Bloodhound/Cruel Cut Style, Your Doom Awaits, Winged Revival, Vigorous Familiar, Mark of Making (6 fixes)

- **Scope**: power, feat
- **Entries**: (1) Bloodhound Style—"Predator's Strike" → "Predator Strike" (ranger power name, MP:43). (2) Cruel Cut Style—same. (3) Your Doom Awaits (power10871)—Target line moved before Attack, formatting fixed (Redeemer of the Damned 11, PHR:T:21). (4) Winged Revival—prerequisite already 21st level; marked corrected. (5) Vigorous Familiar—removed erroneous "Heroic Tier" from _index (DR377:35). (6) Mark of Making—already listed Heroic; marked corrected.
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/feat/data17.js, data19.js, _index.js; 4e_database_files/power/data11.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: 20 simple fixes (powers, feat, items, notes)

- **Scope**: power, feat, item
- **Entries**: Decelerating Slash (indentation); Slashing Claws (Beast Form KW, Melee touch); Prescient Knowledge, Echoing Dirge (no level), Force Orb, Acid Arrow (Published in); Seeker's Due, Seeker's Peeress Shot (Spiritbond removed); Rippling Strike (Psychic only); Spirit's Sacrifice (Close Burst Spirit 5); Life and Death Struggle, Pain to Pleasure (Miss line), Summon Succubus (Intrinsic Nature), Void Shard (errata text); Knack for Success (Racial Utility); Cliffwalk Shifting (typo); Blastpatch (Cold, Fire, or Lightning); Raven Tens (no extra br); two Powers-section notes marked corrected.
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/power/data7.js; 4e_database_files/item/_index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Implacable Enmity, Dervish's Challenge, Brand the Heretic, Memories of Wind and Rain, Rescue Familiar (5 fixes)

- **Scope**: power
- **Entries**: (1) Implacable Enmity (power14242)—Utility 20 → Attack 20; listing Daily Utility → Daily Attack (NCS:56). (2) Dervish's Challenge (power10496)—Range Personal → Melee weapon (Fighter Daily 5, CErr). (3) Brand the Heretic (power11294)—Range "Melee or Ranged 5" → "Melee 1 or Ranged 5" (Invoker Daily 9, D383:34). (4) Memories of Wind and Rain (power12874)—typo "WInd" → "Wind" (Shaman encounter 7). (5) Rescue Familiar (power9293)—Target line → Trigger (Familiar Bloodsmith Util 12, DR377:37).
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/power/data2.js, data16.js, data14.js, data13.js, _listing.js, _index.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Agile Recovery, Shadow Sight, Favor of Tymora (3 simple fixes)

- **Scope**: power, feat
- **Entries**: (1) Agile Recovery (power9295)—added Personal keyword (Acrobatics Util 2, PHB3:164). (2) Shadow Sight (power16627)—"Miss" → "Effect" (Misshapen Util 2, DR416). (3) Favor of Tymora (feat723 embedded power)—"Minor Action" → "Immediate Reaction" in feat data (Channel Divinity, DR365:24).
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/power/data15.js, data7.js, _index.js; 4e_database_files/feat/data3.js; fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Winter's Kiss missing Target line (power11556)

- **Scope**: power
- **Entries**: Winter's Kiss (power11556)—added missing "Target: One creature" line (Bralani Wintersoul E11, DR384). Placement verified from Portable Compendium SQL (ddiPower.sql).
- **Source**: fix/fixes-needed.json + Portable Compendium New/sql/ddiPower.sql (portable_sql_extract.py)
- **Files touched**: 4e_database_files/power/data16.js, _index.js, fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

---
## 2026-01-29 — Batch: Shadowy Figurine typo (power14401)

- **Scope**: power
- **Entries**: Shadowy Figurine (power14401)—typo "within ange" → "within range." (Artificer Utility 2, DR403)
- **Source**: fix/fixes-needed.json
- **Files touched**: 4e_database_files/power/data1.js, _index.js, fix/fixes-needed.json, fix/index.htm
- **Validation**: pass (fix/compendium-validation.json)
- **Smoke test**: pending

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
