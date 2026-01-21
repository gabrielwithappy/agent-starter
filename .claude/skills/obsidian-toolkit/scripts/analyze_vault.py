#!/usr/bin/env python3
"""
Analyzes Obsidian Vault configuration and content to provide deep insights.
Unlike simple search, this looks at .obsidian config, plugins, and structure.
"""

import sys
import argparse
import json
import os
import re
from pathlib import Path

def analyze_vault(vault_path):
    vault = Path(vault_path)
    if not vault.exists():
        print(f"Error: Vault path '{vault_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Setup output file path
    SCRATCH_DIR = Path(__file__).resolve().parent.parent / "scratch"
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE = SCRATCH_DIR / "analyze_result.txt"

    def log(message, file_obj=None):
        """Prints to stdout and optionally writes to a file."""
        print(message)
        if file_obj:
            print(message, file=file_obj)
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        log(f"=== Vault Analysis: {vault_path} ===", f)
        log("", f)

        # 1. Structure Analysis (Top Level)
        log("1. Directory Structure (Top Level):", f)
        try:
            items = list(vault.iterdir())
            dirs = [d.name for d in items if d.is_dir() and not d.name.startswith('.')]
            files = [f.name for f in items if f.is_file() and f.suffix == '.md']
            
            log(f"   Directories ({len(dirs)}): {', '.join(sorted(dirs))}", f)
            log(f"   Root Notes ({len(files)}): {', '.join(sorted(files)[:10])} {'...' if len(files)>10 else ''}", f)
        except Exception as e:
            log(f"   Error reading structure: {e}", f)

        # 2. Configuration Analysis (.obsidian)
        log("\n2. Configuration (.obsidian):", f)
        config_dir = vault / ".obsidian"
        if not config_dir.exists():
            log("   No .obsidian directory found.", f)
        else:
            # Core Plugins
            core_plugins_path = config_dir / "core-plugins.json"
            if core_plugins_path.exists():
                try:
                    with open(core_plugins_path, 'r') as cf:
                        core = json.load(cf)
                        enabled_core = [k for k, v in core.items() if v]
                        log(f"   Enabled Core Plugins: {len(enabled_core)}", f)
                except:
                    log("   Error reading core-plugins.json", f)

            # Community Plugins
            comm_plugins_path = config_dir / "community-plugins.json"
            if comm_plugins_path.exists():
                try:
                    with open(comm_plugins_path, 'r') as cf:
                        comm = json.load(cf)
                        log(f"   Community Plugins ({len(comm)}):", f)
                        log(f"     {', '.join(comm)}", f)
                except:
                    log("   Error reading community-plugins.json", f)
                    
            # Property Types
            types_path = config_dir / "types.json"
            if types_path.exists():
                try:
                    with open(types_path, 'r') as cf:
                        types_data = json.load(cf)
                        log(f"   Defined Properties ({len(types_data.get('types', {}))}):", f)
                        for prop, type_name in types_data.get('types', {}).items():
                            log(f"     - {prop}: {type_name}", f)
                except:
                    pass

        # 3. Content Stats
        log("\n3. Content Statistics:", f)
        md_count = len(list(vault.rglob("*.md")))
        log(f"   Total Markdown Files: {md_count}", f)
        
        # 4. Tag Analysis
        log("\n4. Tag Analysis:", f)
        # We will scan files to find tags in Frontmatter and inline
        # Regex for inline tags: #tagname
        # Use non-capturing group for the whitespace/start boundary
        tag_pattern = re.compile(r'(?:^|[\s])#([a-zA-Z0-9_\-\/]+)')
        
        unique_tags = set()
        scanned_count = 0
        max_scan = 2000 # Increase limit for better coverage
        
        log(f"   Scanning up to {max_scan} files for tags...", f)
        
        for md_file in vault.rglob("*.md"):
            if scanned_count >= max_scan:
                break
            
            try:
                content = md_file.read_text(encoding="utf-8", errors="ignore")
                scanned_count += 1
                
                # A. Frontmatter Tags
                parts = re.split(r'^---$', content, maxsplit=2, flags=re.MULTILINE)
                if len(parts) >= 3:
                    yaml_text = parts[1]
                    in_tags_block = False
                    
                    for line in yaml_text.splitlines():
                        stripped = line.strip()
                        if not stripped: continue
                        
                        # Check for "tags:" key
                        if stripped.startswith("tags:"):
                            in_tags_block = True
                            val = stripped.split(":", 1)[1].strip()
                            if val:
                                # Inline list [a, b] or inline values
                                if val.startswith("[") and val.endswith("]"):
                                    tags_list = [t.strip().strip("'").strip('"') for t in val[1:-1].split(",")]
                                    unique_tags.update(tags_list)
                                else:
                                    cleaned = [t.strip() for t in val.split() if t.strip()]
                                    unique_tags.update(cleaned)
                            continue
                        
                        # Check if we are starting a new key (line contains : and doesn't start with -)
                        if ":" in stripped and not stripped.startswith("-"):
                            in_tags_block = False
                            
                        # Capture list items if we are in tags block
                        if in_tags_block and stripped.startswith("- "):
                            tag_val = stripped[2:].strip() # remove "- "
                            # Remove quotes if present
                            if (tag_val.startswith('"') and tag_val.endswith('"')) or (tag_val.startswith("'") and tag_val.endswith("'")):
                                tag_val = tag_val[1:-1]
                            unique_tags.add(tag_val)

                # B. Inline Tags
                body = parts[2] if len(parts) >= 3 else content
                found = tag_pattern.findall(body)
                unique_tags.update(found)
                
            except Exception:
                continue

        # Cleanup tags
        clean_tags = sorted([t for t in unique_tags if t and not t.isdigit()])
        
        if clean_tags:
            log(f"   Found {len(clean_tags)} unique tags:", f)
            if len(clean_tags) > 50:
                 for i in range(0, len(clean_tags), 10):
                    log(f"     {', '.join(clean_tags[i:i+10])}", f)
            else:
                for t in clean_tags:
                    log(f"     - {t}", f)
        else:
            log("   No tags found.", f)
    
    print(f"\n[INFO] Analysis saved to: {OUTPUT_FILE}")

def main():
    parser = argparse.ArgumentParser(description="Analyze Obsidian Vault")
    parser.add_argument("vault_path", help="Path to the Obsidian Vault root")
    
    args = parser.parse_args()
    
    try:
        analyze_vault(args.vault_path)
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
