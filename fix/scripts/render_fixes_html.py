#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


STATUS_LABELS = {
    "needs_fix": "Needs Fix",
    "corrected": "Corrected",
    "mixed": "Mixed",
}

STATUS_CLASSES = {
    "needs_fix": "status-needs",
    "corrected": "status-corrected",
    "mixed": "status-mixed",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def count_status(items: list[dict]) -> dict[str, int]:
    counts = {"needs_fix": 0, "corrected": 0, "mixed": 0, "other": 0}
    for item in items:
        status = item.get("status", "other")
        if status not in counts:
            counts["other"] += 1
        else:
            counts[status] += 1
    return counts


def render_counts(counts: dict[str, int]) -> str:
    return (
        f'<span class="count needs">Needs Fix: {counts["needs_fix"]}</span>'
        f'<span class="count corrected">Corrected: {counts["corrected"]}</span>'
        f'<span class="count mixed">Mixed: {counts["mixed"]}</span>'
        f'<span class="count other">Other: {counts["other"]}</span>'
    )


def render_item(text: str, status: str) -> str:
    status_label = STATUS_LABELS.get(status, status)
    css_class = STATUS_CLASSES.get(status, "status-other")
    safe_text = html.escape(text, quote=True)
    return (
        f'<li class="item {css_class}">'
        f'<span class="badge {css_class}">{status_label}</span>'
        f"<span class=\"text\">{safe_text}</span>"
        f"</li>"
    )


def render_section(name: str, items: list[dict]) -> str:
    counts = count_status(items)
    safe_name = html.escape(name, quote=True)
    out = [f'<section class="section">']
    out.append(
        f'<h2 class="section-title">{safe_name}'
        f'<span class="section-counts">{render_counts(counts)}</span>'
        f"</h2>"
    )
    out.append('<ul class="items">')
    for item in items:
        text = str(item.get("text", "")).strip()
        status = str(item.get("status", "other")).strip() or "other"
        if not text:
            continue
        out.append(render_item(text, status))
    out.append("</ul>")
    out.append("</section>")
    return "\n".join(out)


def render_page(data: dict) -> str:
    sections_html = []
    for section, items in data.items():
        if not isinstance(items, list):
            continue
        sections_html.append(render_section(section, items))

    total_counts = count_status(
        [item for items in data.values() if isinstance(items, list) for item in items]
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Fixes Needed</title>
  <style>
    :root {{
      color-scheme: light dark;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      margin: 0;
      background: #0f1115;
      color: #e6e8ee;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 24px 20px 64px;
    }}
    h1 {{
      font-size: 28px;
      margin: 0 0 8px;
    }}
    .summary {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin: 12px 0 24px;
    }}
    .count {{
      font-size: 12px;
      padding: 4px 8px;
      border-radius: 999px;
      background: #1b1f2a;
      border: 1px solid #2a3140;
    }}
    .needs {{ border-color: #7a2a2a; color: #ffb4b4; }}
    .corrected {{ border-color: #2a6a3a; color: #baf5c5; }}
    .mixed {{ border-color: #6a5a2a; color: #ffe2a1; }}
    .other {{ border-color: #3a3a3a; color: #c0c0c0; }}
    .section {{
      margin: 18px 0 28px;
      border: 1px solid #1f2432;
      border-radius: 12px;
      background: #131824;
      overflow: hidden;
    }}
    .section-title {{
      margin: 0;
      padding: 12px 16px;
      background: #151b2a;
      border-bottom: 1px solid #1f2432;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      font-size: 18px;
    }}
    .section-counts {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .items {{
      list-style: none;
      margin: 0;
      padding: 0;
    }}
    .item {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 10px 16px;
      border-bottom: 1px solid #1f2432;
    }}
    .item:last-child {{
      border-bottom: none;
    }}
    .badge {{
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 999px;
      border: 1px solid;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      white-space: nowrap;
    }}
    .status-needs {{
      border-color: #7a2a2a;
      color: #ffb4b4;
      background: #2a1515;
    }}
    .status-corrected {{
      border-color: #2a6a3a;
      color: #baf5c5;
      background: #13251a;
    }}
    .status-mixed {{
      border-color: #6a5a2a;
      color: #ffe2a1;
      background: #2a2415;
    }}
    .status-other {{
      border-color: #3a3a3a;
      color: #c0c0c0;
      background: #1a1a1a;
    }}
    .text {{
      line-height: 1.4;
    }}
    @media (prefers-color-scheme: light) {{
      body {{
        background: #f5f6fa;
        color: #182030;
      }}
      .section {{
        background: #ffffff;
        border-color: #d6dbe8;
      }}
      .section-title {{
        background: #f0f3fa;
        border-color: #d6dbe8;
      }}
      .item {{
        border-color: #e4e8f2;
      }}
      .count {{
        background: #ffffff;
        border-color: #d6dbe8;
      }}
      .status-needs {{ background: #ffecec; color: #8a1c1c; }}
      .status-corrected {{ background: #e9f9ee; color: #1d6a2a; }}
      .status-mixed {{ background: #fff4da; color: #6a4b00; }}
      .status-other {{ background: #f1f1f1; color: #555555; }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>Fixes Needed</h1>
    <div class="summary">
      {render_counts(total_counts)}
    </div>
    {''.join(sections_html)}
  </div>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render fixes-needed.json as a color-coded HTML page."
    )
    parser.add_argument(
        "--input",
        default="fix/fixes-needed.json",
        help="Path to fixes-needed.json (default: fix/fixes-needed.json)",
    )
    parser.add_argument(
        "--output",
        default="fix/index.htm",
        help="Output HTML file path (default: fix/index.htm)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    data = load_json(input_path)
    html_text = render_page(data)
    output_path.write_text(html_text, encoding="utf-8")


if __name__ == "__main__":
    main()
