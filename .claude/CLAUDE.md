# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**중요: 모든 응답은 반드시 한국어로 작성하십시오.**

---

## 프로젝트 개요

이 워크스페이스는 **Obsidian KMS (Knowledge Management System) 자동화**를 위한 Claude Code 에이전트 환경입니다.

### 핵심 구성 요소
- **Obsidian Vault**: `obsidianKMS/` 서브모듈 (실제 노트 저장소)
- **Claude Skills**: 24개 이상의 특화된 스킬 (문서, 개발, 디자인, 콘텐츠)
- **MCP 서버**: Markitdown, Supabase, Next.js devtools, Desktop Commander
- **Python 환경**: `uv`로 통합 의존성 관리

### 주요 작업 유형
1. Obsidian 노트 생성/편집/검색
2. Frontmatter 메타데이터 관리
3. 문서 자동화 (Word, PDF, PowerPoint)
4. 웹 UI/아티팩트 생성
5. 다이어그램 및 시각화

---

## 공통 개발 명령어

### 초기 설정
```bash
# 저장소 클론 (서브모듈 포함)
git clone --recurse-submodules <repository-url>

# Python 의존성 설치
uv sync
```

### 일상적인 작업
```bash
# 스킬 스크립트 실행
uv run python .claude/skills/<skill>/scripts/<script>.py

# 또는 가상환경 활성화 후
.venv\Scripts\activate  # Windows
python .claude/skills/<skill>/scripts/<script>.py

# Git 서브모듈 업데이트
git submodule update --remote obsidianKMS

# 의존성 추가
uv add <package-name>
```

### Windows 환경 주의사항
- **인코딩 이슈**: Windows 기본 콘솔 인코딩은 cp949 (한글 환경)
  - Python 스크립트 시작 부분에 추가:
    ```python
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    ```
  - Unicode 이모지/기호 (⚠✓✗─⊘) 대신 ASCII 사용: `[OK]`, `[ERROR]`, `[WARNING]`

---

## 프로젝트 구조

```
obsidianKMS-agent/
├── obsidianKMS/                    # Git 서브모듈: 실제 Obsidian 볼트
│   ├── 0.Inbox/                   # 새 노트 기본 생성 위치
│   ├── 01.Projects/
│   ├── 02.Areas/
│   └── 03.Resource/
├── .claude/
│   ├── CLAUDE.md                  # 이 파일
│   ├── SKILLS-INVENTORY.md        # 전체 스킬 카탈로그
│   ├── config.json                # Claude Code CLI MCP 설정
│   ├── rules/
│   │   └── obsidian.md           # Obsidian 작업 규칙
│   ├── skills/                    # 24개 스킬
│   │   ├── obsidian-markdown/
│   │   ├── obsidian-note-crud/
│   │   ├── obsidian-frontmatter/
│   │   ├── docx/
│   │   ├── pdf/
│   │   └── ...
│   └── templates/
│       └── (Context) AI Context Template.md
├── .vscode/
│   └── mcp.json                   # VS Code 확장 MCP 설정
├── pyproject.toml                 # Python 의존성 (uv 관리)
└── README.md
```

### 핵심 디렉토리 역할
- **`obsidianKMS/`**: 실제 노트가 저장된 Git 서브모듈. PARA 방식 구조 (Projects, Areas, Resources, Archives)
- **`.claude/skills/`**: 도메인별 특화 스킬. 각 스킬은 `SKILL.md` + `scripts/` 포함
- **`.claude/rules/`**: 작업 도메인별 규칙 (현재 Obsidian)
- **`.claude/templates/`**: 재사용 가능한 템플릿 (AI Context 등)

---

## 스킬 시스템

### 빠른 참조: SKILLS-INVENTORY.md
**먼저 이 문서부터 확인하세요**: [.claude/SKILLS-INVENTORY.md](./.claude/SKILLS-INVENTORY.md)
- 24개 이상의 스킬을 4가지 카테고리로 분류
- 각 스킬의 목적과 핵심 기능 요약
- 빠른 참조 표와 스킬 선택 가이드 제공

### 스킬 우선순위 규칙
**특화된 스킬을 일반 파일 도구보다 우선 사용:**
- Obsidian 작업 → `obsidian-markdown` + `obsidian-note-crud` 조합 **필수**
- Word 문서 → `docx` 스킬 **필수**
- PDF 작업 → `pdf` 스킬 **필수**
- 웹 UI 빌드 → `frontend-design` 또는 `web-artifacts-builder` **필수**

### 새 스킬 추가

#### 외부 스킬 설치 (GitHub)
```bash
python .claude/skills/plugin-manager/scripts/manage.py install --git-url "https://github.com/owner/repo"
```
- `plugin-manager`가 자동으로 `SKILLS-INVENTORY.md` 업데이트

#### 로컬 스킬 생성
1. `.claude/skills/[skill-name]/` 폴더 생성
2. 필수 파일 작성:
   - `SKILL.md`: frontmatter + 스킬 설명
   - `scripts/`: Python 스크립트
3. **수동으로** `SKILLS-INVENTORY.md`의 "Local Custom Skills" 섹션에 추가
4. Git 커밋 & 푸시

### 스킬 작업 공간 (Workspace)

모든 스킬은 **표준화된 작업 공간**을 사용하여 임시 파일과 산출물을 관리해야 합니다.

#### 디렉토리 구조
```
.claude/skills/workspace/
├── [skill-name]/
│   ├── temp/      # 임시 파일 (자동 정리, Git 무시)
│   └── output/    # 산출물 (사용자 확인용, Git 무시)
```

#### 스킬 스크립트에서 사용하기

**Python 예시:**
```python
from pathlib import Path

# 작업 공간 경로 설정
SKILL_NAME = "pptx"  # 현재 스킬 이름
WORKSPACE = Path(__file__).parent.parent / "workspace" / SKILL_NAME
TEMP_DIR = WORKSPACE / "temp"
OUTPUT_DIR = WORKSPACE / "output"

# 디렉토리 자동 생성
TEMP_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 사용 예시
temp_file = TEMP_DIR / "processing.tmp"
final_output = OUTPUT_DIR / "result.docx"
```

**JavaScript 예시:**
```javascript
const path = require('path');
const fs = require('fs');

const SKILL_NAME = "pptx";
const WORKSPACE = path.join(__dirname, '..', '..', 'workspace', SKILL_NAME);
const TEMP_DIR = path.join(WORKSPACE, 'temp');
const OUTPUT_DIR = path.join(WORKSPACE, 'output');

// 디렉토리 자동 생성
fs.mkdirSync(TEMP_DIR, { recursive: true });
fs.mkdirSync(OUTPUT_DIR, { recursive: true });

// 사용 예시
const tempFile = path.join(TEMP_DIR, 'processing.tmp');
const finalOutput = path.join(OUTPUT_DIR, 'result.pptx');
```

#### 주의사항
- `workspace/*/temp/` 및 `workspace/*/output/`은 `.gitignore`에 포함되어 Git에서 추적되지 않음
- 임시 파일은 작업 완료 후 자동 정리 권장
- 최종 산출물은 사용자가 지정한 위치로 복사/이동

---

## Obsidian 작업 워크플로우

### 필수 규칙 (`.claude/rules/obsidian.md` 참조)

1. **기본 노트 생성 위치**: `obsidianKMS/0.Inbox/`
   - 사용자가 명시적으로 다른 경로를 지정하지 않는 한 **항상** Inbox에 생성

2. **Frontmatter 필수**:
   ```yaml
   ---
   created: YYYY-MM-DD
   tags:
     - tag1
     - tag2
   ---
   ```

3. **두 스킬 조합 사용**:

   **1단계: `obsidian-markdown` 스킬 로드**
   - Obsidian Flavored Markdown 문법 참조
   - Wikilinks: `[[노트명]]`
   - Callouts: `> [!note]`
   - Embeds: `![[파일명]]`
   - Properties (frontmatter)
   - **중요**: 리스트 들여쓰기는 **TAB 문자** 사용 (공백 아님)

   **2단계: 콘텐츠 작성**
   - 위 문법을 준수하여 마크다운 작성

   **3단계: `obsidian-note-crud` 스크립트로 저장**
   - `create_note.py`: 새 노트 생성
   - `update_note.py`: 기존 노트에 콘텐츠 추가
   - `search_notes.py`: 노트 검색
   - `delete_note.py`: 노트 삭제

4. **도구 선택 우선순위**:
   - ✅ **사용**: `obsidian-note-crud/scripts/*.py`
   - ❌ **피하기**: 일반 파일 IO 도구 (Write, Edit 등)

### AI Context 문서 관리

**명명 규칙**: `(Context) [주제명].md`
- 예: `(Context) 영신식품.md`, `(Context) React 개발.md`
- Obsidian에서 `(Context)` 검색으로 모든 Context 문서 찾기

**생성 방법**:
1. `.claude/templates/(Context) AI Context Template.md` 템플릿 사용
2. Obsidian vault 내 적절한 위치에 배치 (예: `03.Resource/`)
3. Frontmatter 작성 (`created`, `tags`, `status`)
4. 업무 중 발견한 정보를 점진적으로 추가

**유지보수**:
- 정보 생애주기: 발견 → 검증 → 핵심 개념으로 승격
- 크기 관리: "발견 및 학습 내용"은 최근 10-20개 항목만 유지
- 정기 검토: frontmatter의 `review-cycle`에 따라 업데이트

---

## 의존성 관리

### uv 기반 통합 관리
- **설정 파일**: `pyproject.toml`
- **가상환경**: `.venv/`
- **스킬별 requirements.txt는 사용하지 않음**

### 일반 작업
```bash
# 모든 의존성 설치
uv sync

# 새 패키지 추가
uv add <package-name>

# 스크립트 실행 (자동으로 .venv 사용)
uv run python <script>.py
```

---

## MCP 설정 (Model Context Protocol)

### 두 가지 설정 파일
Claude Code CLI와 VS Code 확장은 **각각 다른 MCP 설정 파일**을 사용합니다:

| 도구 | 설정 파일 | 키 경로 |
|------|----------|---------|
| **Claude Code CLI** | `.claude/config.json` | `mcpServers` |
| **VS Code 확장** | `.vscode/mcp.json` | `servers` |

### 현재 설치된 MCP 서버
1. **Markitdown**: 문서 변환 (Word, PDF, Excel → Markdown)
2. **Supabase**: 데이터베이스 작업
3. **Next.js devtools**: Next.js 프로젝트 관리
4. **Desktop Commander**: 데스크톱 자동화

### MCP 서버 추가/수정
- **Claude Code 사용 중**: `.claude/config.json` 편집
- **VS Code 확장 사용 중**: `.vscode/mcp.json` 편집
- **두 도구 동시 사용**: 각 파일을 별도로 관리

---

## 템플릿

### AI Context 템플릿
- **파일**: `.claude/templates/(Context) AI Context Template.md`
- **용도**: AI가 참고하는 배경 지식 문서 작성
- **적용 범위**: 개발, 문서, 자산 관리 등 모든 도메인
- **특징**: 정보 생애주기 관리 및 Context 크기 최적화

### 사용법
1. 템플릿을 Obsidian vault 내 적절한 위치로 복사
2. `[주제명]` 및 frontmatter 수정
3. 업무 중 발견한 정보를 점진적으로 추가

---

## 작업 워크플로우

1. **요청 분석**: 사용자 의도 파악
2. **스킬 매칭**: [SKILLS-INVENTORY.md](./SKILLS-INVENTORY.md)에서 적절한 스킬 찾기
3. **규칙 확인**: `.claude/rules/` 디렉토리의 도메인별 규칙 참조
4. **실행**: 스킬의 스크립트 또는 가이드에 따라 작업 수행
5. **검증**: 출력 결과 확인 및 사용자에게 보고

---

## 주요 참조 문서

- [SKILLS-INVENTORY.md](./.claude/SKILLS-INVENTORY.md): 전체 스킬 카탈로그
- [rules/obsidian.md](./.claude/rules/obsidian.md): Obsidian 작업 규칙
- [templates/(Context) AI Context Template.md](./.claude/templates/(Context)%20AI%20Context%20Template.md): AI Context 문서 템플릿
- [README.md](../README.md): 프로젝트 개요 및 MCP 설정