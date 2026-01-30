#!/usr/bin/env python3
"""Fix Fey Beast Tamer Background and Theme with missing content from SQL."""
import json
import re
from pathlib import Path

# Project root (parent of fix/)
ROOT = Path(__file__).resolve().parents[2]


def normalize_html(html: str) -> str:
    """Normalize HTML from SQL format to database format."""
    # Basic entity replacements
    html = html.replace('&nbsp;', ' ')
    html = html.replace('<br/>', '<br>')
    html = html.replace('&quot;', '"')
    html = html.replace('&amp;', '&')
    
    # Fix quoted attributes to unquoted
    html = re.sub(r'class="([^"]+)"', r'class=\1', html)
    html = re.sub(r'src="([^"]+)"', r'src=\1', html)
    html = re.sub(r'alt="([^"]+)"', r'alt=\1', html)
    html = re.sub(r'target="([^"]+)"', r'target=\1', html)
    html = re.sub(r'href="([^"]+)"', r'href=\1', html)
    
    # Remove <p> tags around power headers
    html = re.sub(r'<p><h1', '<h1', html)
    html = re.sub(r'</h1></p>', '</h1>', html)
    
    # Remove <a> tags from publishedIn, keep just text
    html = re.sub(r'<a[^>]*>([^<]+)</a>', r'\1', html)
    
    # Remove <img> tags (they're not in the database format)
    html = re.sub(r'<img[^>]*>', '', html)
    
    # Fix extra spaces
    html = re.sub(r'  +', ' ', html)
    
    return html


def extract_text_for_index(html: str) -> str:
    """Extract text content from HTML for index file."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', html)
    # Replace entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&quot;', '"')
    text = text.replace('&amp;', '&')
    # Normalize whitespace
    text = re.sub(r'  +', ' ', text).strip()
    return text


def main():
    # Extract theme from SQL
    print("Extracting theme from SQL...")
    import subprocess
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name
    
    try:
        result = subprocess.run(
            [
                "python3",
                str(ROOT / "fix" / "scripts" / "portable_sql_extract.py"),
                "--table", "theme",
                "--id", "915",
                "--limit", "1",
                "--extract-detail",
                "--output", temp_path,
            ],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        
        if result.returncode != 0 or not Path(temp_path).exists():
            print(f"ERROR: Could not extract theme from SQL: {result.stderr}")
            return
        
        with open(temp_path, 'r', encoding='utf-8') as f:
            theme_data = json.load(f)
        
        if not theme_data.get("records"):
            print("ERROR: No theme records found")
            return
        
        theme_html_sql = theme_data["records"][0]["DetailHtml"]
        theme_html_normalized = normalize_html(theme_html_sql)
        theme_text = extract_text_for_index(theme_html_sql)
        
    finally:
        Path(temp_path).unlink(missing_ok=True)
    
    # Extract background from SQL
    print("Extracting background from SQL...")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name
    
    try:
        result = subprocess.run(
            [
                "python3",
                str(ROOT / "fix" / "scripts" / "portable_sql_extract.py"),
                "--table", "background",
                "--id", "804",
                "--limit", "1",
                "--extract-detail",
                "--output", temp_path,
            ],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        
        if result.returncode != 0 or not Path(temp_path).exists():
            print(f"ERROR: Could not extract background from SQL: {result.stderr}")
            return
        
        with open(temp_path, 'r', encoding='utf-8') as f:
            bg_data = json.load(f)
        
        if not bg_data.get("records"):
            print("ERROR: No background records found")
            return
        
        bg_html_sql = bg_data["records"][0]["DetailHtml"]
        bg_html_normalized = normalize_html(bg_html_sql)
        bg_text = extract_text_for_index(bg_html_sql)
        
    finally:
        Path(temp_path).unlink(missing_ok=True)
    
    # Update theme data file
    print("Updating theme data file...")
    theme_file = ROOT / "4e_database_files" / "theme" / "data15.js"
    with theme_file.open('r', encoding='utf-8') as f:
        theme_content = f.read()
    
    # Replace theme915 entry - find the exact match and replace
    # Escape the HTML for JSON (escape backslashes and quotes)
    escaped_html = theme_html_normalized.replace('\\', '\\\\').replace('"', '\\"')
    pattern = r'"theme915"\s*:\s*"[^"]*"'
    replacement = f'"theme915": "{escaped_html}"'
    theme_content = re.sub(pattern, replacement, theme_content)
    
    with theme_file.open('w', encoding='utf-8') as f:
        f.write(theme_content)
    
    print("✓ Updated theme data file")
    
    # Update theme index file
    print("Updating theme index file...")
    theme_index_file = ROOT / "4e_database_files" / "theme" / "_index.js"
    with theme_index_file.open('r', encoding='utf-8') as f:
        theme_index_content = f.read()
    
    pattern = r'"theme915"\s*:\s*"[^"]*"'
    escaped_text = theme_text.replace('\\', '\\\\').replace('"', '\\"')
    replacement = f'"theme915": "{escaped_text}"'
    theme_index_content = re.sub(pattern, replacement, theme_index_content)
    
    with theme_index_file.open('w', encoding='utf-8') as f:
        f.write(theme_index_content)
    
    print("✓ Updated theme index file")
    
    # Update background data file
    print("Updating background data file...")
    bg_file = ROOT / "4e_database_files" / "background" / "data4.js"
    with bg_file.open('r', encoding='utf-8') as f:
        bg_content = f.read()
    
    pattern = r'"background804"\s*:\s*"[^"]*"'
    escaped_bg = bg_html_normalized.replace('\\', '\\\\').replace('"', '\\"')
    replacement = f'"background804": "{escaped_bg}"'
    bg_content = re.sub(pattern, replacement, bg_content)
    
    with bg_file.open('w', encoding='utf-8') as f:
        f.write(bg_content)
    
    print("✓ Updated background data file")
    
    # Update background index file
    print("Updating background index file...")
    bg_index_file = ROOT / "4e_database_files" / "background" / "_index.js"
    with bg_index_file.open('r', encoding='utf-8') as f:
        bg_index_content = f.read()
    
    pattern = r'"background804"\s*:\s*"[^"]*"'
    escaped_bg_text = bg_text.replace('\\', '\\\\').replace('"', '\\"')
    replacement = f'"background804": "{escaped_bg_text}"'
    bg_index_content = re.sub(pattern, replacement, bg_index_content)
    
    with bg_index_file.open('w', encoding='utf-8') as f:
        f.write(bg_index_content)
    
    print("✓ Updated background index file")
    print("\n✅ All files updated successfully!")


if __name__ == "__main__":
    main()
