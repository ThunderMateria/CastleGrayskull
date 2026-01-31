#!/usr/bin/env python3
"""
In ritual _index.js and ritual/dataN.js, change ' Uncommon' to ' Common' only in
the 22 alchemical-item rituals listed in the fix (rituals that list their
corresponding alchemical item as Uncommon rather than Common).
"""
from __future__ import annotations

from pathlib import Path

RITUAL_IDS = (
    "138", "141", "148", "157", "158",
    "237", "238", "239", "240", "243",
    "245", "246", "247", "248", "249",
    "250", "251", "252",
    "348", "349", "350", "351",
)

def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    changed = 0
    for i, line in enumerate(lines):
        for rid in RITUAL_IDS:
            # Match line that defines this ritual: "ritual138": "..." or "ritual138":
            if f'"ritual{rid}":' in line or f'"ritual{rid}" :' in line:
                if " Uncommon" in line:
                    new_line = line.replace(" Uncommon", " Common")
                    if new_line != line:
                        lines[i] = new_line
                        changed += 1
                break
    if changed:
        path.write_text("\n".join(lines), encoding="utf-8")
    return changed


def main() -> None:
    base = Path(__file__).resolve().parent.parent.parent / "4e_database_files" / "ritual"
    total = 0
    total += process_file(base / "_index.js")
    for n in range(20):
        total += process_file(base / f"data{n}.js")
    print(f"Updated {total} ritual entries (Uncommon -> Common).")


if __name__ == "__main__":
    main()
