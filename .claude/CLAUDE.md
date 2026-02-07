# Claude Agent Instructions

This document provides high-level instructions for the Claude AI agent operating within this workspace.

## 1. Skill Discovery and Usage
- **Check Available Skills**: At the beginning of a task, or when faced with a new type of operation, check the `.claude/skills` directory for specialized capabilities.
- **Read Instructions**: If a relevant skill folder is found, read its `SKILL.md` file to understand how to use it.
- **Prioritize Skills**: Always prefer using specialized skills (custom scripts, tools) over generic file editing tools (`write_to_file`, `replace_file_content`) when a skill is available for the task. This ensures consistency and handles edge cases (like Obsidian-specific syntax) correctly.

## 2. Obsidian Operations

Obsidian 작업에는 두 가지 스킬을 **함께** 사용합니다:

- **콘텐츠 작성**: `obsidian-markdown` 스킬
  - **Location**: `.claude/skills/obsidian-markdown`
  - **Role**: Obsidian Flavored Markdown 문법 참조 (wikilinks, callouts, embeds, properties 등)
  - **Rule**: 노트 콘텐츠를 작성하거나 편집할 때 **반드시** 이 스킬을 먼저 로드하여 문법을 참조합니다.

- **파일 CRUD**: `obsidian-note-crud` 스킬
  - **Location**: `.claude/skills/obsidian-note-crud`
  - **Role**: 노트 생성, 읽기, 수정, 삭제, 검색
  - **Rule**: **DO NOT** use generic file IO tools directly if possible. **USE** the python scripts provided in `obsidian-note-crud/scripts/`.
  - Example: Use `create_note.py` to create a note, `update_note.py` to append text.

- **워크플로우**: `obsidian-markdown` 로드 → 콘텐츠 작성 → `obsidian-note-crud`으로 저장

## 3. Dependency Management

모든 스킬의 Python 의존성은 프로젝트 루트의 `pyproject.toml`에서 `uv`로 통합 관리합니다.

- **새 시스템 설정**: `git clone` 후 `uv sync` 한 번이면 모든 의존성이 설치됩니다.
- **스크립트 실행**: `uv run python .claude/skills/<skill>/scripts/<script>.py` 또는 `.venv` 활성화 후 `python` 직접 실행
- **의존성 추가**: 새 스킬에 외부 패키지가 필요하면 `uv add <package>`로 추가합니다. 스킬별 `requirements.txt`는 사용하지 않습니다.

## 4. Workflow
1.  **Analyze Request**: Understand the user's intent.
2.  **Match Skill**: Look for a skill that matches the domain (e.g., "Obsidian", "Git", "Python").
3.  **Execute**: Use the skill's defined methods.
