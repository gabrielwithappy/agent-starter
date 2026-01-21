#!/usr/bin/env python3
"""
Refactors Obsidian notes by updating Frontmatter metadata.
Can add, update, or remove YAML keys and tags across multiple files.
"""

import sys
import argparse
import re
from pathlib import Path
from datetime import datetime

# Setup output file path
SCRATCH_DIR = Path(__file__).resolve().parent.parent / "scratch"
OUTPUT_FILE = SCRATCH_DIR / "refactor_result.txt"

def log(message, file_obj=None):
    """Prints to stdout and optionally writes to a file."""
    print(message)
    if file_obj:
        print(message, file=file_obj)

def update_frontmatter(content, changes):
    """
    Parses and updates frontmatter.
    `changes` is a dict: { 'key': 'value' } to add/update, or { 'key': None } to remove.
    """
    has_frontmatter = content.startswith("---\n")
    
    if has_frontmatter:
        # Split existing frontmatter
        parts = re.split(r'^---$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            frontmatter_raw = parts[1]
            body = parts[2]
            
            # Simple line-based parser/updater to preserve comments/ordering as much as possible
            lines = frontmatter_raw.splitlines()
            new_lines = []
            seen_keys = set()
            
            # Process existing lines
            for line in lines:
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    new_lines.append(line)
                    continue
                
                if ":" in stripped:
                    key = stripped.split(":", 1)[0].strip()
                    if key in changes:
                        # If value is None, skip (delete)
                        if changes[key] is None:
                            seen_keys.add(key)
                            continue
                        # Update value
                        new_lines.append(f"{key}: {changes[key]}")
                        seen_keys.add(key)
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            
            # Add new keys
            for key, value in changes.items():
                if key not in seen_keys and value is not None:
                    new_lines.append(f"{key}: {value}")
            
            # Reconstruct
            new_frontmatter = "\n".join(new_lines)
            if not new_frontmatter.endswith("\n"):
                new_frontmatter += "\n"
                
            return f"---\n{new_frontmatter}---{body}"
            
    else:
        # Create new frontmatter
        lines = ["---"]
        for key, value in changes.items():
            if value is not None:
                lines.append(f"{key}: {value}")
        lines.append("---\n")
        return "\n".join(lines) + content

def process_vault(vault_path, target_key, target_value=None, action="update", auto_date=False, dry_run=True):
    vault = Path(vault_path)
    if not vault.exists():
        print(f"Error: Vault path '{vault_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Ensure scratch dir exists
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)
    
    # Define changes
    changes = {}
    if action == "update":
        changes[target_key] = target_value
    elif action == "remove":
        changes[target_key] = None
        
    if auto_date:
        changes["updated"] = datetime.now().strftime("%Y-%m-%d")

    mode_str = "[DRY RUN]" if dry_run else "[LIVE]"
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        log(f"=== Metadata Refactor {mode_str} ===", f)
        log(f"Action: {action} key '{target_key}' -> '{target_value}'", f)
        if auto_date:
            log("Option: Adding 'updated' timestamp", f)
        log("", f)
        
        modified_count = 0
        
        # Scan all .md files
        for md_file in vault.rglob("*.md"):
            try:
                original_content = md_file.read_text(encoding="utf-8", errors="ignore")
                new_content = update_frontmatter(original_content, changes)
                
                if new_content != original_content:
                    rel_path = md_file.relative_to(vault)
                    log(f"Modify: {rel_path}", f)
                    
                    if not dry_run:
                        md_file.write_text(new_content, encoding="utf-8")
                        
                    modified_count += 1
            except Exception as e:
                log(f"Error processing {md_file.name}: {e}", f)
                continue
                
        log(f"\nTotal files processed: {modified_count}", f)
        if dry_run:
            log("\nNOTE: This was a dry run. No files were changed.", f)
            log("Use --no-dry-run to apply changes.", f)

    print(f"\n[INFO] Log saved to: {OUTPUT_FILE}")

def main():
    parser = argparse.ArgumentParser(description="Refactor Obsidian Metadata")
    parser.add_argument("vault_path", help="Path to the Obsidian Vault root")
    parser.add_argument("--key", required=True, help="Metadata key to modify")
    parser.add_argument("--value", help="Value to set (required for update)")
    parser.add_argument("--remove", action="store_true", help="Remove the key instead of updating")
    parser.add_argument("--auto-date", action="store_true", help="Automatically add/update 'updated: YYYY-MM-DD'")
    parser.add_argument("--no-dry-run", action="store_true", help="Execute actual changes (Default is Dry Run)")
    
    args = parser.parse_args()
    
    action = "remove" if args.remove else "update"
    if action == "update" and not args.value:
        parser.error("--value is required unless --remove is set")
        
    try:
        process_vault(
            args.vault_path, 
            args.key, 
            args.value, 
            action, 
            args.auto_date, 
            dry_run=not args.no_dry_run
        )
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
