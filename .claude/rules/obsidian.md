# Obsidian Agent Rules

1.  **Default Document Location**: **CRITICAL**: When creating new documents in Obsidian, you **MUST** always place them in the `obsidianKMS/0.Inbox` folder. Do not create files in other folders like `03.Resource` even if the content seems relevant there, unless the user explicitly specifies a different path.
2.  **Naming Convention**: Use clear, descriptive filenames. if a date is relevant, prepend it in `YYYY-MM-DD` format.
3.  **Frontmatter**: **CRITICAL**: Ensure all new documents have valid YAML frontmatter at the very top of the file.
    - Required fields:
        - `created`: Current date in `YYYY-MM-DD` format.
        - `tags`: A list of relevant tags.
    - Example:
      ```yaml
      ---
      created: 2024-01-01
      tags:
        - tag1
        - tag2
      ---
      ```
4.  **Tool Usage**: **CRITICAL**: When creating, reading, updating, or deleting Obsidian notes, **ALWAYS** prefer using the scripts provided in the `obsidian-toolkit` skill (e.g., `.claude/skills/obsidian-toolkit/scripts/create_note.py`) over standard file tools like `write_to_file`, to ensure proper handling of Obsidian-specific features.
