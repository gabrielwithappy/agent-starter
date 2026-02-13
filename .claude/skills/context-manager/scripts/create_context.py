#!/usr/bin/env python3
"""
Create a new AI Context document from template.
"""
import sys
import io
import argparse
import os
from pathlib import Path
from datetime import datetime

# Windows UTF-8 encoding fix
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def get_template_content():
    """Get the AI Context template content."""
    script_dir = Path(__file__).parent
    template_path = script_dir.parent / 'references' / 'template.md'

    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERROR] Template not found at {template_path}", file=sys.stderr)
        sys.exit(1)

def create_context_document(vault_path, topic, location=''):
    """
    Create a new Context document from template.

    Args:
        vault_path: Path to Obsidian vault
        topic: Topic name for the Context document
        location: Optional subdirectory within vault (e.g., '03.Resource/개발')

    Returns:
        Path to created document
    """
    vault_path = Path(vault_path).resolve()
    today = datetime.now().strftime('%Y-%m-%d')

    # Determine target directory
    if location:
        target_dir = vault_path / location
    else:
        target_dir = vault_path / '0.Inbox'

    target_dir.mkdir(parents=True, exist_ok=True)

    # Create filename
    filename = f"(Context) {topic}.md"
    file_path = target_dir / filename

    if file_path.exists():
        print(f"[WARNING] File already exists: {file_path}")
        response = input("Overwrite? (y/N): ").strip().lower()
        if response != 'y':
            print("[INFO] Aborted.")
            sys.exit(0)

    # Get template and substitute placeholders
    content = get_template_content()
    content = content.replace('YYYY-MM-DD', today)
    content = content.replace('[주제명]', topic)
    content = content.replace('[주제]', topic)

    # Write file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return file_path

def main():
    parser = argparse.ArgumentParser(description='Create a new AI Context document')
    parser.add_argument('--topic', required=True, help='Topic name for the Context document')
    parser.add_argument('--vault-path', required=True, help='Path to Obsidian vault')
    parser.add_argument('--location', default='', help='Target subdirectory (e.g., 03.Resource/개발)')

    args = parser.parse_args()

    file_path = create_context_document(args.vault_path, args.topic, args.location)

    print(f"[OK] Created Context document:")
    print(f"     {file_path}")
    print()
    print("[INFO] Next steps:")
    print("       1. Open the document in Obsidian")
    print("       2. Fill in the basic information section")
    print("       3. Add content as you discover new information")

if __name__ == '__main__':
    main()
