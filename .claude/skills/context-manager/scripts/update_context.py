#!/usr/bin/env python3
"""
Update an existing AI Context document by appending to a specific section.
"""
import sys
import io
import argparse
from pathlib import Path
from datetime import datetime
import re

# Windows UTF-8 encoding fix
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def find_section(content, section_name):
    """
    Find the line range of a section in markdown content.

    Returns:
        Tuple of (start_line, end_line) or None if not found
    """
    lines = content.split('\n')

    # Find section header
    section_pattern = re.compile(r'^##\s+.*' + re.escape(section_name), re.IGNORECASE)
    start_line = None

    for i, line in enumerate(lines):
        if section_pattern.search(line):
            start_line = i
            break

    if start_line is None:
        return None

    # Find end of section (next ## header or end of file)
    end_line = len(lines)
    for i in range(start_line + 1, len(lines)):
        if lines[i].startswith('## '):
            end_line = i
            break

    return (start_line, end_line)

def update_context_document(file_path, section_name, new_content):
    """
    Append content to a specific section in a Context document.

    Args:
        file_path: Path to Context document
        section_name: Name of section to update (e.g., "발견 및 학습 내용")
        new_content: Content to append

    Returns:
        Updated file path
    """
    file_path = Path(file_path).resolve()

    if not file_path.exists():
        print(f"[ERROR] File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    # Read existing content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find section
    section_range = find_section(content, section_name)
    if section_range is None:
        print(f"[ERROR] Section '{section_name}' not found in document", file=sys.stderr)
        print("[INFO] Available sections:", file=sys.stderr)
        for line in content.split('\n'):
            if line.startswith('## '):
                print(f"       - {line[3:]}", file=sys.stderr)
        sys.exit(1)

    start_line, end_line = section_range
    lines = content.split('\n')

    # Prepare new entry with date
    today = datetime.now().strftime('%Y-%m-%d')
    new_entry = f"\n### {today}: [제목]\n{new_content}\n"

    # Insert new entry at end of section (before next section or callout warnings)
    insert_pos = end_line
    for i in range(end_line - 1, start_line, -1):
        line = lines[i].strip()
        if line and not line.startswith('>') and not line.startswith('###'):
            insert_pos = i + 1
            break

    # Insert new content
    lines.insert(insert_pos, new_entry)

    # Update frontmatter 'updated' field
    updated_content = '\n'.join(lines)
    if updated_content.startswith('---'):
        try:
            end_index = updated_content.index('---', 3)
            frontmatter = updated_content[3:end_index]
            if 'updated:' in frontmatter:
                frontmatter = re.sub(r'updated:.*', f'updated: {today}', frontmatter)
            else:
                frontmatter += f'\nupdated: {today}'
            updated_content = '---' + frontmatter + updated_content[end_index:]
        except ValueError:
            pass  # No proper frontmatter, skip update

    # Write updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    return file_path

def main():
    parser = argparse.ArgumentParser(description='Update AI Context document')
    parser.add_argument('--file', required=True, help='Path to Context document')
    parser.add_argument('--section', required=True, help='Section to update (e.g., "발견 및 학습 내용")')
    parser.add_argument('--content', required=True, help='Content to append')

    args = parser.parse_args()

    file_path = update_context_document(args.file, args.section, args.content)

    print(f"[OK] Updated Context document:")
    print(f"     {file_path}")
    print(f"     Section: {args.section}")

if __name__ == '__main__':
    main()
