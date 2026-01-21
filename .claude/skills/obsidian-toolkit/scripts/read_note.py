#!/usr/bin/env python3
"""
Reads a note from the Obsidian Vault. 
Attempts to find the note by name if a partial path is given.
"""

import sys
import argparse
from pathlib import Path

# Setup output file path
SCRATCH_DIR = Path(__file__).resolve().parent.parent / "scratch"
OUTPUT_FILE = SCRATCH_DIR / "read_note_result.txt"

def log(message, file_obj=None):
    """Prints to stdout and optionally writes to a file."""
    print(message)
    if file_obj:
        print(message, file=file_obj)

def find_and_read_note(vault_path, note_name):
    vault = Path(vault_path)
    if not vault.exists():
        print(f"Error: Vault path '{vault_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Clean up note name (remove brackets if present)
    target_name = note_name.replace("[[", "").replace("]]", "")
    if not target_name.endswith(".md"):
        target_name += ".md"
        
    # Ensure scratch dir exists
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # Try exact path first
        target_path = vault / target_name
        if target_path.exists():
            log(f"Reading: {target_path.relative_to(vault)}\n", f)
            log(target_path.read_text(encoding="utf-8", errors="replace"), f)
            print(f"\n[INFO] Note content saved to: {OUTPUT_FILE}")
            return

        # Try searching recursively
        found_files = list(vault.rglob(target_name))
        
        if not found_files:
            print(f"Error: Note '{note_name}' not found in {vault_path}", file=sys.stderr)
            sys.exit(1)
            
        if len(found_files) > 1:
            print(f"Error: Multiple notes found for '{note_name}':", file=sys.stderr)
            for f in found_files:
                print(f"- {f.relative_to(vault)}", file=sys.stderr)
            sys.exit(1)
            
        # Single match found
        target_file = found_files[0]
        log(f"Reading: {target_file.relative_to(vault)}\n", f)
        log(target_file.read_text(encoding="utf-8", errors="replace"), f)
        print(f"\n[INFO] Note content saved to: {OUTPUT_FILE}")

def main():
    parser = argparse.ArgumentParser(description="Read Obsidian Note")
    parser.add_argument("vault_path", help="Path to the Obsidian Vault root")
    parser.add_argument("note_name", help="Name of the note (e.g. 'Daily Note' or 'Folder/My Note')")
    
    args = parser.parse_args()
    
    try:
        find_and_read_note(args.vault_path, args.note_name)
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
