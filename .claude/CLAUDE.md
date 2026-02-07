# Claude Agent Instructions

This document provides high-level instructions for the Claude AI agent operating within this workspace.

## 1. Skill Discovery and Usage
- **Check Available Skills**: At the beginning of a task, or when faced with a new type of operation, check the `.claude/skills` directory for specialized capabilities.
- **Read Instructions**: If a relevant skill folder is found, read its `SKILL.md` file to understand how to use it.
- **Prioritize Skills**: Always prefer using specialized skills (custom scripts, tools) over generic file editing tools (`write_to_file`, `replace_file_content`) when a skill is available for the task. This ensures consistency and handles edge cases (like Obsidian-specific syntax) correctly.

## 2. Obsidian Operations
- **Tool**: `obsidian-toolkit`
- **Location**: `.claude/skills/obsidian-toolkit`
- **Rule**: For creating, reading, updating, or deleting Markdown files intended for Obsidian:
    - **DO NOT** use generic file IO tools directly if possible.
    - **USE** the python scripts provided in `obsidian-toolkit/scripts/`.
    - Example: Use `create_note.py` to create a note, `update_note.py` to append text.

## 3. Workflow
1.  **Analyze Request**: Understand the user's intent.
2.  **Match Skill**: Look for a skill that matches the domain (e.g., "Obsidian", "Git", "Python").
3.  **Execute**: Use the skill's defined methods.
