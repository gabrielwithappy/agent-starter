# Claude AI 에이전트 가이드

이 문서는 이 워크스페이스 내에서 작동하는 Claude AI 에이전트를 위한 상위 수준의 지침을 제공합니다.

**중요: 모든 응답은 반드시 한국어로 작성하십시오.**

## 1. 스킬 발견 및 사용

### 스킬 인벤토리 참조 (Quick Start)
**먼저 이 문서부터 확인하세요**: [.claude/skills/SKILLS-INVENTORY.md](./.claude/skills/SKILLS-INVENTORY.md)
- **목적**: 설치된 모든 스킬의 목적과 기능을 분류별로 정리
- **구조**: 디자인, 문서, 개발, 콘텐츠 4가지 카테고리로 구분
- **활용**: 빠른 참조 표와 스킬 선택 가이드 제공

### 상세 정보 확인
- **SKILL.md 참조**: 각 스킬 폴더의 `SKILL.md` 파일에서 상세 사용법 확인
- **스킬 우선순위**: 일반 파일 도구(`write_to_file`, `replace_file_content`)보다 특화된 스킬 우선 사용
  - Obsidian 작업 → `obsidian-markdown` + `obsidian-note-crud` 조합 필수
  - Word 문서 → `docx` 스킬 필수
  - 웹 UI 빌드 → `frontend-design` 또는 `web-artifacts-builder` 필수

### 새 스킬 추가 (설치 후 필수)
새로운 스킬을 설치할 때마다:
1. 스킬 설치 (GitHub 저장소에서)
2. `SKILLS-INVENTORY.md`의 적절한 분류 섹션에 추가
3. 필수 정보: 이름, 목적, 핵심 기능 3-4개
4. 변경사항 커밋 & 푸시

## 2. Obsidian 작업 (Obsidian Operations)

Obsidian 작업에는 두 가지 스킬을 **함께** 사용합니다:

- **콘텐츠 작성**: `obsidian-markdown` 스킬
  - **위치**: `.claude/skills/obsidian-markdown`
  - **역할**: Obsidian Flavored Markdown 문법 참조 (wikilinks, callouts, embeds, properties 등)
  - **규칙**: 노트 콘텐츠를 작성하거나 편집할 때 **반드시** 이 스킬을 먼저 로드하여 문법을 참조합니다.

- **파일 CRUD**: `obsidian-note-crud` 스킬
  - **위치**: `.claude/skills/obsidian-note-crud`
  - **역할**: 노트 생성, 읽기, 수정, 삭제, 검색
  - **규칙**: 가능한 한 일반적인 파일 IO 도구를 직접 사용하지 마십시오. 대신 `obsidian-note-crud/scripts/`에 제공된 Python 스크립트를 **사용**하십시오.
  - 예시: 노트를 생성할 때는 `create_note.py`, 텍스트를 추가할 때는 `update_note.py`를 사용합니다.

- **워크플로우**: `obsidian-markdown` 로드 → 콘텐츠 작성 → `obsidian-note-crud`으로 저장

## 3. 의존성 관리 (Dependency Management)

모든 스킬의 Python 의존성은 프로젝트 루트의 `pyproject.toml`에서 `uv`로 통합 관리합니다.

- **새 시스템 설정**: `git clone` 후 `uv sync` 한 번이면 모든 의존성이 설치됩니다.
- **스크립트 실행**: `uv run python .claude/skills/<skill>/scripts/<script>.py` 또는 `.venv` 활성화 후 `python` 직접 실행
- **의존성 추가**: 새 스킬에 외부 패키지가 필요하면 `uv add <package>`로 추가합니다. 스킬별 `requirements.txt`는 사용하지 않습니다.

## 4. MCP 설정 (Model Context Protocol)

Claude Code와 VS Code 확장은 **각각 다른 MCP 설정 파일**을 사용합니다:

- **Claude Code CLI**: `.claude/config.json` 사용 (mcpServers 섹션)
- **VS Code 확장**: `.vscode/mcp.json` 사용

**중요**: MCP 서버를 추가하거나 변경할 때 유의사항:
- **Claude Code 사용 시**: `.claude/config.json`의 `mcpServers` 섹션을 수정합니다
- **VS Code 확장 사용 시**: `.vscode/mcp.json`의 `servers` 섹션을 수정합니다
- 두 도구를 동시에 사용하는 경우, **각 설정 파일을 별도로 관리**해야 합니다

### Google Workspace MCP 설정

Google Workspace MCP를 사용하려면 Google Cloud 프로젝트 설정이 필수입니다:

**⚠️ 중요: uvx는 .env.local을 읽지 않습니다**

`uvx workspace-mcp`로 실행되므로 **시스템 환경변수**를 사용해야 합니다:

**Windows PowerShell (관리자 권한)**:
```powershell
[Environment]::SetEnvironmentVariable("GOOGLE_OAUTH_CLIENT_ID", "YOUR_CLIENT_ID", "User")
[Environment]::SetEnvironmentVariable("GOOGLE_OAUTH_CLIENT_SECRET", "YOUR_CLIENT_SECRET", "User")
[Environment]::SetEnvironmentVariable("OAUTHLIB_INSECURE_TRANSPORT", "1", "User")
```

**또는 GUI**:
1. Windows 검색에서 "환경 변수" 검색
2. "사용자 환경 변수 편집" 클릭
3. "새로 만들기" 버튼으로 각 변수 추가

**Google Cloud 설정 단계**:
1. [Google Cloud Console](https://console.cloud.google.com/) 접속
2. 새 프로젝트 생성
3. OAuth 2.0 자격증명 생성 (Desktop Application 타입)
4. Gmail, Drive, Calendar, Docs, Sheets 등 필요한 API 활성화
5. 클라이언트 ID와 시크릿을 환경변수에 설정

**MCP 설정**:
```json
{
  "command": "uvx",
  "args": ["workspace-mcp", "--tool-tier", "core"]
}
```

**사용 가능한 도구**:
- Gmail, Drive, Calendar, Docs, Sheets, Slides, Forms, Tasks, Contacts, Chat
- `--tool-tier` 옵션: `core`, `extended`, `complete`

## 5. 워크플로우 (Workflow)
1.  **요청 분석**: 사용자의 의도를 파악합니다.
2.  **스킬 매칭**: 도메인(예: "Obsidian", "Git", "Python")에 맞는 스킬을 찾습니다.
3.  **실행**: 스킬에 정의된 방법을 사용하여 작업을 수행합니다.
