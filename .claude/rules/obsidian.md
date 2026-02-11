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

## AI Context 문서 관리

### 파일명 규칙
- **명명 형식**: `(Context) [주제명].md`
- **예시**: `(Context) 영신식품.md`, `(Context) React 개발.md`
- **검색**: Obsidian에서 `(Context)` 검색으로 모든 Context 문서 찾기 가능

### Context 문서 생성
1. `.claude/templates/(Context) AI Context Template.md` 템플릿 사용
2. Obsidian vault 내 적절한 위치에 배치 (예: `03.Resource/`)
3. Frontmatter의 `created`, `tags`, `status` 필드 작성
4. `[주제명]`을 실제 주제로 변경
5. 업무 중 발견한 정보를 점진적으로 추가

### Context 문서 유지보수
- **정보 생애주기**: 발견 → 검증 → 핵심 개념/반복 패턴으로 승격
- **크기 관리**: "발견 및 학습 내용"은 최근 10-20개 항목만 유지
- **정기 검토**: frontmatter의 `review-cycle`에 따라 정기적으로 업데이트
