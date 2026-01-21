#!/usr/bin/env python3
"""
Scans Obsidian Vault for notes with specific metadata (frontmatter).
Acts like a database query for your vault.
"""

import sys
import argparse
import re
from pathlib import Path

def parse_frontmatter(content):
    """
    Parser for YAML frontmatter. Supports inline values and multi-line lists.
    """
    if not content.startswith("---"):
        return {}
        
    try:
        # split by ---
        parts = re.split(r'^---$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) < 3:
            return {}
            
        yaml_content = parts[1]
        metadata = {}
        current_list_key = None
        
        for line in yaml_content.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            
            # Check for list item "- value"
            if stripped.startswith("- "):
                if current_list_key:
                    val = stripped[2:].strip()
                    # Remove quotes
                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    
                    if current_list_key not in metadata or not isinstance(metadata[current_list_key], list):
                        metadata[current_list_key] = []
                    metadata[current_list_key].append(val)
                continue
            
            # Check for key: value
            if ":" in stripped:
                key, value = stripped.split(":", 1)
                key = key.strip()
                value = value.strip()
                
                # If value is empty, it might be start of a list
                if not value:
                    metadata[key] = []
                    current_list_key = key
                    continue
                
                # Reset list tracking for new simple key
                current_list_key = None
                
                # Remove quotes
                if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]
                    
                # Handle lists (inline [a, b])
                if value.startswith("[") and value.endswith("]"):
                     value = [v.strip().strip("'").strip('"') for v in value[1:-1].split(",")]
                
                metadata[key] = value
                
        return metadata
    except Exception:
        return {}

# Setup output file path
SCRATCH_DIR = Path(__file__).resolve().parent.parent / "scratch"
OUTPUT_FILE = SCRATCH_DIR / "query_result.txt"

def log(message, file_obj=None):
    """Prints to stdout and optionally writes to a file."""
    print(message)
    if file_obj:
        print(message, file=file_obj)

def query_vault(vault_path, key_filter=None, value_filter=None):
    vault = Path(vault_path)
    if not vault.exists():
        print(f"Error: Vault path '{vault_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Ensure scratch dir exists
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        log(f"Scanning vault for metadata... Key='{key_filter}', Value='{value_filter}'", f)
        
        matches = []
        
        for md_file in vault.rglob("*.md"):
            try:
                #Read first 2KB for frontmatter to save time
                with open(md_file, 'r', encoding="utf-8", errors="ignore") as rf:
                    head = rf.read(2048)
                    
                metadata = parse_frontmatter(head)
                if not metadata:
                    continue
                    
                match = True
                if key_filter:
                    if key_filter not in metadata:
                        match = False
                    elif value_filter:
                       # Simple string comparison
                       val = metadata[key_filter]
                       if isinstance(val, list):
                           if value_filter not in val:
                               match = False
                       elif str(val) != value_filter:
                           match = False
                
                if match:
                    matches.append((md_file, metadata))
                    
            except Exception:
                continue
                
        # Output results
        if not matches:
            log("No matches found.", f)
            print(f"\n[INFO] Result saved to: {OUTPUT_FILE}")
            return

        log(f"Found {len(matches)} notes:\n", f)
        for file_path, meta in matches:
            rel_path = file_path.relative_to(vault)
            log(f"File: {rel_path}", f)
            log(f"  Meta: {meta}", f)
            log("-" * 20, f)
            
        print(f"\n[INFO] Result saved to: {OUTPUT_FILE}")

def main():
    parser = argparse.ArgumentParser(description="Query Obsidian Vault Metadata")
    parser.add_argument("vault_path", help="Path to the Obsidian Vault root")
    parser.add_argument("--key", help="Metadata key to filter by (e.g. 'status', 'tags')")
    parser.add_argument("--value", help="Value to match for the key")
    
    args = parser.parse_args()
    
    try:
        query_vault(args.vault_path, args.key, args.value)
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
