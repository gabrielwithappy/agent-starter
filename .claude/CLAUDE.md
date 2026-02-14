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

이 프로젝트는 40개 이상의 특화 스킬을 제공합니다 (문서, 개발, 디자인, Google Workspace 연동).

### 스킬 참고 자료
- **전체 카탈로그**: [SKILLS-INVENTORY.md](./skills/skill-hub/assets/SKILLS-INVENTORY.md)
- **각 스킬 문서**: `.claude/skills/[skill-name]/SKILL.md` (사용법, 예시)
- **스킬 관리**: `skill-hub` 스킬 사용

### Skill 임시 파일 및 산출물 관리

#### 디렉토리 구조
```
.claude/skills/workspace/
├── [skill-name]/
│   ├── temp/          # 임시 파일 (자동 생성/정리)
│   └── output/        # 산출물 (최종 저장)
```

#### 임시 파일 (`.claude/skills/workspace/[skill-name]/temp/`)
- **용도**: Skill 실행 중 필요한 중간 파일
- **생명주기**: Skill 실행 시 자동 생성, 완료 후 자동 정리
- **Git 무시**: `.gitignore`의 `.claude/skills/workspace/*/temp/` 규칙으로 관리

#### 산출물 (`.claude/skills/workspace/[skill-name]/output/`)
- **용도**: Skill이 생성한 최종 결과물
- **보관**: 필요에 따라 프로젝트 폴더로 이동 또는 Obsidian Vault에 저장
- **Git 무시**: `.gitignore`의 `.claude/skills/workspace/*/output/` 규칙으로 관리

#### 규칙 요약
1. **임시 파일**: `.claude/skills/workspace/[skill-name]/temp/`에 자동 생성/정리
2. **산출물**: `.claude/skills/workspace/[skill-name]/output/`에 저장
3. **최종 위치**: 필요시 프로젝트의 적절한 폴더로 수동 이동 또는 스킬에서 직접 저장
4. **GitHub 커밋**: 산출물은 자동 커밋하지 않음 (사용자 명시 요청 필요)

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

