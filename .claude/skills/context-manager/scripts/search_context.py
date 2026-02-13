#!/usr/bin/env python3
"""
Search for AI Context documents in the Obsidian vault.
"""
import sys
import io
import argparse
import os
from pathlib import Path
import re

# Windows UTF-8 encoding fix
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def parse_frontmatter(content):
    """Extract frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}

    try:
        end_index = content.index('---', 3)
        frontmatter_text = content[3:end_index].strip()

        # Simple YAML parsing for tags
        tags = []
        for line in frontmatter_text.split('\n'):
            if line.strip().startswith('- '):
                tags.append(line.strip()[2:])

        return {'tags': tags}
    except ValueError:
        return {}

def search_context_files(vault_path, query, search_mode='all'):
    """
    Search for Context documents.

    Args:
        vault_path: Path to Obsidian vault
        query: Search query string
        search_mode: 'title', 'tags', 'content', or 'all'

    Returns:
        List of matching file paths with relevance info
    """
    vault_path = Path(vault_path).resolve()
    results = []
    query_lower = query.lower()

    # Find all Context files
    for md_file in vault_path.rglob('(Context)*.md'):
        match_info = {
            'path': str(md_file.relative_to(vault_path)),
            'absolute_path': str(md_file),
            'matches': []
        }

        # Search in filename
        if search_mode in ['title', 'all']:
            if query_lower in md_file.name.lower():
                match_info['matches'].append('title')

        # Read file for content/tags search
        if search_mode in ['tags', 'content', 'all']:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Search in tags
                if search_mode in ['tags', 'all']:
                    fm = parse_frontmatter(content)
                    if any(query_lower in tag.lower() for tag in fm.get('tags', [])):
                        match_info['matches'].append('tags')

                # Search in content
                if search_mode in ['content', 'all']:
                    if query_lower in content.lower():
                        match_info['matches'].append('content')

            except Exception as e:
                print(f"[WARNING] Could not read {md_file}: {e}", file=sys.stderr)

        if match_info['matches']:
            results.append(match_info)

    return results

def main():
    parser = argparse.ArgumentParser(description='Search for AI Context documents')
    parser.add_argument('--vault-path', required=True, help='Path to Obsidian vault')
    parser.add_argument('--query', required=True, help='Search query')
    parser.add_argument('--search-mode',
                       choices=['title', 'tags', 'content', 'all'],
                       default='all',
                       help='Where to search')

    args = parser.parse_args()

    results = search_context_files(args.vault_path, args.query, args.search_mode)

    if not results:
        print(f"[INFO] No Context documents found matching '{args.query}'")
        return

    print(f"[OK] Found {len(results)} Context document(s):\n")

    for i, result in enumerate(results, 1):
        print(f"{i}. {result['path']}")
        print(f"   Matches: {', '.join(result['matches'])}")
        print(f"   Full path: {result['absolute_path']}")
        print()

if __name__ == '__main__':
    main()
