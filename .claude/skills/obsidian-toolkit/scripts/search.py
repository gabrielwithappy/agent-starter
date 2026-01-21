#!/usr/bin/env python3
"""
Searches for keywords in an Obsidian Vault.
"""

import os
import sys
import argparse
from pathlib import Path

# Setup output file path
SCRATCH_DIR = Path(__file__).resolve().parent.parent / "scratch"
OUTPUT_FILE = SCRATCH_DIR / "search_result.txt"

def log(message, file_obj=None):
    """Prints to stdout and optionally writes to a file."""
    print(message)
    if file_obj:
        print(message, file=file_obj)

def search_vault(vault_path, query, context_lines=2):
    vault = Path(vault_path)
    if not vault.exists():
        print(f"Error: Vault path '{vault_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Ensure scratch dir exists
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        log(f"Searching for '{query}' in {vault_path}...", f)
        
        query_lower = query.lower()
        matches = 0
        
        for md_file in vault.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8", errors="ignore")
                lines = content.splitlines()
                
                # Check filename match
                if query_lower in md_file.name.lower():
                    log(f"\n[FILE MATCH] {md_file.relative_to(vault)}", f)
                    matches += 1
                    
                # Check content match
                for i, line in enumerate(lines):
                    if query_lower in line.lower():
                        log(f"\n[CONTENT MATCH] {md_file.relative_to(vault)}:{i+1}", f)
                        matches += 1
                        
                        # Print context
                        start = max(0, i - context_lines)
                        end = min(len(lines), i + context_lines + 1)
                        
                        for j in range(start, end):
                            prefix = ">" if j == i else " "
                            log(f"{prefix} {j+1}: {lines[j]}", f)
                            
            except Exception as e:
                # Skip unreadable files silently or verbose?
                continue
                
        if matches == 0:
            log("No matches found.", f)
        else:
            log(f"\nFound {matches} matches.", f)

        print(f"\n[INFO] Result saved to: {OUTPUT_FILE}")

def main():
    parser = argparse.ArgumentParser(description="Search Obsidian Vault")
    parser.add_argument("vault_path", help="Path to the Obsidian Vault root")
    parser.add_argument("query", help="Text to search for")
    
    args = parser.parse_args()
    
    try:
        search_vault(args.vault_path, args.query)
    except KeyboardInterrupt:
        print("\nSearch cancelled.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
