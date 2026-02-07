import argparse
import io
import os
import sys

def update_note(vault_path, note_name, content, mode='append'):
    # Ensure .md extension
    if not note_name.endswith('.md'):
        note_name += '.md'
    
    full_path = os.path.join(vault_path, note_name)
    
    if not os.path.exists(full_path):
        print(f"Error: Note '{note_name}' not found. Use create_note to create.")
        sys.exit(1)
        
    try:
        file_mode = 'a' if mode == 'append' else 'w'
        # Add a newline before appending if not empty and adhering to markdown style
        prefix = ""
        if mode == 'append':
             # check if file ends with newline
             with open(full_path, 'r', encoding='utf-8') as check_f:
                 existing = check_f.read()
                 if existing and not existing.endswith('\n'):
                     prefix = "\n"

        with open(full_path, file_mode, encoding='utf-8') as f:
            f.write(prefix + content)
            
        print(f"Successfully updated note: {full_path} (mode: {mode})")
    except Exception as e:
        print(f"Error updating note: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Force UTF-8 encoding for stdout/stderr on Windows
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

    parser = argparse.ArgumentParser(description="Update a note in Obsidian vault")
    parser.add_argument("--vault", required=True, help="Path to the Obsidian vault root")
    parser.add_argument("--name", required=True, help="Name of the note (relative path)")
    parser.add_argument("--content", required=True, help="Content to append or replace")
    parser.add_argument("--mode", choices=['append', 'replace'], default='append', help="Update mode: append to end or replace entire content")

    args = parser.parse_args()
    # Interpret escape sequences in content (e.g., \n -> newline, \t -> tab)
    content = args.content.replace('\\n', '\n').replace('\\t', '\t')
    update_note(args.vault, args.name, content, args.mode)
