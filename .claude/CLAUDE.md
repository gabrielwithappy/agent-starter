# CLAUDE.md

**중요: 모든 응답은 반드시 한국어로 작성하십시오.**

---

## 프로젝트 개요 (WHAT)

이 워크스페이스는 **Obsidian KMS (Knowledge Management System) 자동화**를 위한 Claude Code 에이전트 환경입니다.

### 기술 스택
- **Obsidian Vault**: `obsidianKMS/` Git 서브모듈
- **Claude Skills**: 24개 특화 스킬 (문서, 개발, 디자인)
- **MCP 서버**: Markitdown, Supabase, Next.js devtools, Desktop Commander
- **Python 환경**: `uv` 통합 의존성 관리

### 핵심 디렉토리
- `obsidianKMS/`: PARA 구조 노트 저장소 (Projects, Areas, Resources, Archives)
- `.claude/skills/`: 도메인별 특화 스킬

---

## 스킬 시스템

이 프로젝트는 24개의 특화 스킬을 제공합니다 (문서, 개발, 디자인).

**전체 스킬 카탈로그**: [SKILLS-INVENTORY.md](./SKILLS-INVENTORY.md)

---

## Obsidian 작업 워크플로우

### 필수 3단계
1. **`obsidian-markdown` 스킬 로드** → 문법 참조
2. **콘텐츠 작성** → Obsidian Flavored Markdown
3. **`obsidian-note-crud` 스크립트 실행** → 저장

### 핵심 규칙
- **기본 생성 위치**: `obsidianKMS/0.Inbox/`
- **Frontmatter 필수**: `created`, `tags`
- **도구 우선순위**: `obsidian-note-crud` 스크립트 > 일반 파일 IO

### AI Context 관리
Context 문서 생성/검색/업데이트는 **`context-manager` 스킬** 사용

---

## 환경 설정

### Windows 환경
- **인코딩**: cp949 (한글) → UTF-8 변환 필요
- **출력**: Unicode 이모지 대신 ASCII 사용 (`[OK]`, `[ERROR]`, `[WARNING]`)

### MCP 설정
- **Claude Code CLI**: `.claude/config.json`
- **VS Code 확장**: `.vscode/mcp.json`

