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
- `.claude/rules/`: 작업 도메인별 규칙
- `.claude/docs/`: 상세 가이드 문서
- `.claude/templates/`: 재사용 템플릿

---

## 핵심 작업 유형 (WHY)

1. **Obsidian 노트 관리**: 생성/편집/검색/메타데이터 관리
2. **문서 자동화**: Word, PDF, PowerPoint 생성/변환
3. **웹 UI 개발**: React, HTML/CSS 컴포넌트
4. **다이어그램**: PlantUML, JSON Canvas
5. **AI Context 관리**: 프로젝트별 배경 지식 문서화

---

## 빠른 시작 (HOW)

### 초기 설정
```bash
git clone --recurse-submodules <repository-url>
uv sync
```

### 일상 작업
```bash
# 스킬 스크립트 실행
uv run python .claude/skills/<skill>/scripts/<script>.py

# Git 서브모듈 업데이트
git submodule update --remote obsidianKMS

# 의존성 추가
uv add <package-name>
```

---

## 스킬 시스템

### 빠른 참조
**[SKILLS-INVENTORY.md](./SKILLS-INVENTORY.md)**: 24개 스킬 카탈로그 및 선택 가이드

### 필수 규칙
- **Obsidian** → `obsidian-markdown` + `obsidian-note-crud` 조합
- **Word** → `docx` 스킬
- **PDF** → `pdf` 스킬
- **웹 UI** → `frontend-design` 또는 `web-artifacts-builder`

### 작업 공간
모든 스킬은 `.claude/skills/workspace/[skill-name]/` 사용 (temp/, output/)

**상세 가이드**: [docs/workspace.md](./docs/workspace.md)

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

**상세 규칙**: [rules/obsidian.md](./rules/obsidian.md)

---

## 작업 워크플로우

1. **요청 분석** → 사용자 의도 파악
2. **스킬 매칭** → [SKILLS-INVENTORY.md](./SKILLS-INVENTORY.md) 참조
3. **규칙 확인** → `.claude/rules/` 확인
4. **실행** → 스킬 스크립트 실행
5. **검증** → 결과 확인 및 보고

---

## 상세 가이드

### 환경 설정
- **Windows 환경**: [docs/windows-setup.md](./docs/windows-setup.md)
- **MCP 설정**: [docs/mcp-setup.md](./docs/mcp-setup.md)

### 도메인별 가이드
- **스킬 작업 공간**: [docs/workspace.md](./docs/workspace.md)
- **AI Context 관리**: [docs/ai-context.md](./docs/ai-context.md)
- **Obsidian 규칙**: [rules/obsidian.md](./rules/obsidian.md)

### 참조 문서
- **스킬 카탈로그**: [SKILLS-INVENTORY.md](./SKILLS-INVENTORY.md)
- **AI Context 템플릿**: [templates/(Context) AI Context Template.md](./templates/(Context)%20AI%20Context%20Template.md)
- **프로젝트 README**: [../README.md](../README.md)