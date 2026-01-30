#!/usr/bin/env python3
"""
Extract records from Portable Compendium SQL dumps.

This script reads the SQL files in Portable Compendium New/sql and can:
- list columns for a table
- extract rows by ID or name substring
- output JSON for downstream comparison
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, Iterator, List, Optional


TABLE_TO_FILE = {
    "power": "ddiPower.sql",
    "feat": "ddiFeat.sql",
    "item": "ddiItem.sql",
    "monster": "ddiMonster.sql",
    "race": "ddiRace.sql",
    "class": "ddiClass.sql",
    "paragonpath": "ddiParagonPath.sql",
    "epicdestiny": "ddiEpicDestiny.sql",
    "theme": "ddiTheme.sql",
    "ritual": "ddiRitual.sql",
    "background": "ddiBackground.sql",
    "companion": "ddiCompanion.sql",
    "associate": "ddiAssociate.sql",
    "glossary": "ddiGlossary.sql",
    "poison": "ddiPoison.sql",
    "disease": "ddiDisease.sql",
    "deity": "ddiDeity.sql",
    "trap": "ddiTrap.sql",
    "terrain": "ddiTerrain.sql",
    "skill": "ddiSkill.sql",
}

TABLE_TO_SQL_TABLE = {
    "power": "Power",
    "feat": "Feat",
    "item": "Item",
    "monster": "Monster",
    "race": "Race",
    "class": "Class",
    "paragonpath": "ParagonPath",
    "epicdestiny": "EpicDestiny",
    "theme": "Theme",
    "ritual": "Ritual",
    "background": "Background",
    "companion": "Companion",
    "associate": "Associate",
    "glossary": "Glossary",
    "poison": "Poison",
    "disease": "Disease",
    "deity": "Deity",
    "trap": "Trap",
    "terrain": "Terrain",
    "skill": "Skill",
}


def _sql_unescape(value: str) -> str:
    return (
        value.replace("\\r", "\r")
        .replace("\\n", "\n")
        .replace("\\t", "\t")
        .replace("\\'", "'")
        .replace('\\"', '"')
        .replace("\\\\", "\\")
    )


def _parse_columns(sql_text: str) -> List[str]:
    match = re.search(r"CREATE TABLE IF NOT EXISTS `[^`]+`\s*\((.*?)\)\s*ENGINE", sql_text, re.S)
    if not match:
        return []
    body = match.group(1)
    cols = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("`"):
            continue
        col = line.split("`", 2)[1]
        cols.append(col)
    return cols


def _iter_insert_lines(sql_path: Path, table_name: str) -> Iterator[str]:
    prefix = f"INSERT INTO `{table_name}` VALUES"
    with sql_path.open("r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            if line.startswith(prefix):
                yield line.strip()


def _parse_values_line(line: str) -> List[Optional[str]]:
    # Extract the part between VALUES ( ... );
    start = line.find("VALUES")
    if start == -1:
        return []
    open_idx = line.find("(", start)
    close_idx = line.rfind(")")
    if open_idx == -1 or close_idx == -1 or close_idx <= open_idx:
        return []
    segment = line[open_idx + 1 : close_idx]

    values: List[Optional[str]] = []
    buf = []
    in_quote = False
    i = 0
    while i < len(segment):
        ch = segment[i]
        if in_quote:
            if ch == "\\" and i + 1 < len(segment):
                buf.append(segment[i : i + 2])
                i += 2
                continue
            if ch == "'":
                in_quote = False
                i += 1
                continue
            buf.append(ch)
            i += 1
            continue
        if ch == "'":
            in_quote = True
            i += 1
            continue
        if ch == ",":
            raw = "".join(buf).strip()
            values.append(_sql_unescape(raw) if raw not in {"NULL", ""} else None)
            buf = []
            i += 1
            continue
        buf.append(ch)
        i += 1

    raw = "".join(buf).strip()
    values.append(_sql_unescape(raw) if raw not in {"NULL", ""} else None)
    return values


def _extract_detail_html(txt: str) -> Optional[str]:
    if not txt:
        return None
    match = re.search(r"<div id=\"detail\">(.*)</div>", txt, re.S | re.I)
    if not match:
        return None
    return match.group(1).strip()


def extract_records(
    sql_dir: Path,
    table: str,
    target_id: Optional[str],
    name_contains: Optional[str],
    limit: int,
    extract_detail: bool,
) -> Dict[str, object]:
    table_key = table.lower()
    file_name = TABLE_TO_FILE.get(table_key)
    if not file_name:
        raise ValueError(f"Unknown table: {table}")
    sql_table = TABLE_TO_SQL_TABLE.get(table_key)
    if not sql_table:
        raise ValueError(f"Unknown SQL table mapping: {table}")
    sql_path = sql_dir / file_name
    sql_text = sql_path.read_text(encoding="utf-8", errors="ignore")
    columns = _parse_columns(sql_text)
    records = []

    for line in _iter_insert_lines(sql_path, sql_table):
        values = _parse_values_line(line)
        if not values or not columns:
            continue
        record = {col: values[i] if i < len(values) else None for i, col in enumerate(columns)}
        if target_id and str(record.get("ID")) != str(target_id):
            continue
        if name_contains:
            name = str(record.get("Name") or "").lower()
            if name_contains.lower() not in name:
                continue
        if extract_detail and record.get("Txt"):
            record["DetailHtml"] = _extract_detail_html(str(record["Txt"]))
        records.append(record)
        if limit and len(records) >= limit:
            break

    return {"table": table_key, "columns": columns, "records": records}


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract Portable Compendium SQL records.")
    parser.add_argument("--sql-dir", default="Portable Compendium New/sql", help="SQL directory path")
    parser.add_argument("--table", required=True, help="Table name (power, feat, item, monster, race, etc.)")
    parser.add_argument("--id", dest="target_id", default=None, help="Record ID to extract")
    parser.add_argument("--name", dest="name_contains", default=None, help="Name substring match (case-insensitive)")
    parser.add_argument("--limit", type=int, default=10, help="Max records to return")
    parser.add_argument("--extract-detail", action="store_true", help="Extract only <div id=\"detail\"> HTML")
    parser.add_argument("--output", default="portable_compendium_extract.json", help="Output JSON file")
    args = parser.parse_args()

    result = extract_records(
        sql_dir=Path(args.sql_dir),
        table=args.table,
        target_id=args.target_id,
        name_contains=args.name_contains,
        limit=args.limit,
        extract_detail=args.extract_detail,
    )
    Path(args.output).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
