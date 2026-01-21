---
name: obsidian-toolkit
description: A comprehensive toolkit for interacting with an Obsidian Vault. Allows searching, reading, querying metadata, and managing vault structure.
license: MIT
metadata:
  author: agent-starter
  version: "1.1"
allowed-tools: Bash(python3:*) Read
---

# Obsidian Toolkit

This skill provides a suite of tools for interacting with `Obsidian.md` vaults. It goes beyond simple file reading by offering semantic search, metadata querying, and structural analysis/management.

## Purpose

Use this skill when you need to answer questions based on the user's personal notes, find specific documents in their Obsidian vault, or list notes based on tags/metadata.

## Usage

This skill operates on a "Vault Path". Since the agent runs in a Linux environment but the user is on Windows, you must ensure the Vault path is accessible.
- If using WSL, a Windows path `C:\Users\Name\Vault` maps to `/mnt/c/Users/Name/Vault`.
- Ask the user for the **Vault Path** if it's not provided.

## Instructions

### 1. Search for Content
Use `search.py` to find notes containing specific keywords.

```bash
# Syntax: python3 scripts/search.py <vault_path> <query>
python3 scripts/search.py "/mnt/c/Users/MyVault" "project alpha"
```

### 2. Read a Note
Use `read_note.py` to read the full content of a note. You can provide a filename (with or without `.md`) or a partial path.

```bash
# Syntax: python3 scripts/read_note.py <vault_path> <note_name>
python3 scripts/read_note.py "/mnt/c/Users/MyVault" "Meeting Notes/2023-10-10"
```

### 3. Query Metadata (The "DB")
Use `query_db.py` to find notes based on Frontmatter (YAML) properties, effectively treating the vault as a database.

```bash
# Syntax: python3 scripts/query_db.py <vault_path> --key <key> [--value <value>]

# Find all notes with a 'status' property
python3 scripts/query_db.py "/mnt/c/Users/MyVault" --key "status"

# Find notes where 'type' is 'book'
python3 scripts/query_db.py "/mnt/c/Users/MyVault" --key "type" --value "book"
```

### 4. Analyze Vault Structure & Metadata
Use `analyze_vault.py` to get a high-level overview of the vault, including directory structure, installed plugins, defined properties, and content statistics.

```bash
# Syntax: python3 scripts/analyze_vault.py <vault_path>
python3 scripts/analyze_vault.py "/mnt/c/Users/MyVault"
```

### 5. Batch Update Metadata (Refactor)
Use `batch_metadata.py` to add, update, or remove Frontmatter keys across the entire vault. Perfect for adding timestamps or standardizing properties. Defaults to Dry Run.

```bash
# Syntax: python3 scripts/batch_metadata.py <vault_path> --key <key> --value <val> [--no-dry-run]

# Add 'author: Gabriel' to all notes (Dry Run)
python3 scripts/batch_metadata.py "/mnt/c/Users/MyVault" --key "author" --value "Gabriel"

# Apply changes and include 'updated' date
python3 scripts/batch_metadata.py "/mnt/c/Users/MyVault" --key "status" --value "reviewed" --auto-date --no-dry-run
```

## Examples

**User:** "What plugins am I using in my Obsidian?"
**Action:**
```bash
python3 scripts/analyze_vault.py "/path/to/vault"
```

**User:** "Find my notes about the 'Apollo' project."
**Action:**
```bash
python3 scripts/search.py "/path/to/vault" "Apollo"
```

**User:** "Show me all books I've read (notes with type: book)."
**Action:**
```bash
python3 scripts/query_db.py "/path/to/vault" --key "type" --value "book"
```

## References

- [Obsidian YAML Frontmatter](https://help.obsidian.md/Editing+and+formatting/Metadata)
