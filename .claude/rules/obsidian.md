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
4.  **Markdown Syntax**: **CRITICAL**: When writing or editing Obsidian note **content**, you **MUST** first load the `obsidian-markdown` skill to reference Obsidian Flavored Markdown syntax (wikilinks, callouts, embeds, properties, etc.). This ensures all generated content is fully compatible with Obsidian.
5.  **Tool Usage**: **CRITICAL**: When creating, reading, updating, or deleting Obsidian notes, **ALWAYS** prefer using the scripts provided in the `obsidian-note-crud` skill (e.g., `.claude/skills/obsidian-note-crud/scripts/create_note.py`) over standard file tools like `write_to_file`, to ensure proper handling of Obsidian-specific features.
6.  **Obsidian 작업 워크플로우**: Obsidian 노트를 작성할 때 반드시 아래 순서를 따릅니다:
    1. `obsidian-markdown` 스킬 로드 → 마크다운 문법 참조
    2. 콘텐츠 작성 (Obsidian Flavored Markdown 준수)
    3. `obsidian-note-crud` 스킬의 스크립트로 노트 생성/수정
7.  **AI Context 문서 관리**: AI Context 문서 생성/검색/업데이트는 **`context-manager` 스킬**을 사용합니다.
