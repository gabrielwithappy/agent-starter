# Skills Inventory

이 문서는 프로젝트에 설치된 모든 Claude 스킬에 대한 포괄적인 개요를 제공합니다. 각 스킬의 **핵심 목적**과 **사용 사례**를 설명합니다.

자세한 사용 방법은 각 스킬의 `SKILL.md` 파일을 참조하세요: `skills/[skill-name]/SKILL.md`

---

## 📋 카테고리별 스킬

### 🎨 **디자인 & 시각화**

| 스킬 | 목적 | 핵심 기능 |
|------|------|---------|
| **algorithmic-art** | p5.js를 사용한 생성 미술 | 알고리즘 철학 → 인터랙티브 HTML 아트 |
| **canvas-design** | 고급 시각 디자인 (포스터, 미술) | 디자인 철학 → PNG/PDF 출력 |
| **brand-guidelines** | Anthropic 브랜드 스타일 적용 | 공식 색상/타이포그래피 가이드라인 |
| **theme-factory** | 아티팩트에 테마 적용 | 10개 사전정의 테마 + 커스텀 테마 생성 |

### 📄 **문서**

| 스킬 | 목적 | 핵심 기능 |
|------|------|---------|
| **obsidian-markdown** | Obsidian Flavored Markdown | 위키링크, 임베드, callout, properties 문법 |
| **obsidian-note-crud** | Obsidian 노트 CRUD 작업 | 볼트 자동화용 Python 스크립트 |
| **obsidian-frontmatter** | Obsidian 메타데이터 관리 | 속성별 노트 검색, frontmatter 생성/수정/삭제 |
| **obsidian-bases** | Obsidian 데이터베이스 뷰 | .base 파일 생성 (테이블/카드 뷰) |
| **docx** | Word 문서 생성/편집 | .docx 조작 (목차, 형식, 병합) |
| **pdf** | PDF 처리 | 텍스트 추출, 병합, 분할, OCR, 양식 작성 |
| **doc-coauthoring** | 문서 협력 저술 가이드 | 구조화된 문서 작성 워크플로우 |
| **pptx** | PowerPoint 생성/편집 | 슬라이드 덱 생성 및 편집 |

### 🛠️ **개발 & 기술**

| 스킬 | 목적 | 핵심 기능 |
|------|------|---------|
| **mcp-builder** | MCP 서버 개발 | LLM ↔ 외부 서비스 통합 가이드 |
| **frontend-design** | 고급 웹 UI 빌드 | React, HTML/CSS, 프로덕션 품질 컴포넌트 |
| **web-artifacts-builder** | 복잡한 웹 아티팩트 | React, Tailwind, shadcn/ui 통합 |
| **webapp-testing** | 웹 애플리케이션 테스트 | Playwright 자동화 테스트 |
| **json-canvas** | JSON Canvas 파일 생성 | Obsidian canvas, 마인드맵, 플로우차트 |
| **plantuml-ascii** | ASCII 다이어그램 생성 | 시퀀스/클래스/플로우 다이어그램 (ASCII) |
| **xlsx** | 스프레드시트 자동화 | Excel 파일 생성/편집/정리 |
| **plugin-manager** | 스킬 설치 & 관리 | GitHub에서 스킬 설치/제거 |

### 📝 **콘텐츠 작성**

| 스킬 | 목적 | 핵심 기능 |
|------|------|---------|
| **internal-comms** | 내부 커뮤니케이션 | 상태 보고서, 뉴스레터, FAQ |
| **prd** | PRD 문서 생성 | 요구사항 문서, 사용자 스토리 |
| **slack-gif-creator** | Slack용 GIF 생성 | 애니메이션 GIF 생성 |
| **skill-creator** | 새 스킬 생성 가이드 | 커스텀 스킬 개발 가이드 |

---

## 🏠 **로컬 커스텀 스킬**

이 스킬들은 프로젝트 내에서 로컬로 유지되며 plugin-manager로 관리되지 않습니다:

| 스킬 | 목적 | 핵심 기능 |
|------|------|---------|
| **context-manager** | AI Context 문서 관리 | Context 생성/검색/업데이트, 대화 간 지식 보존 |
| **obsidian-note-crud** | 노트 레벨 CRUD 작업 | Python 스크립트: 생성, 읽기, 수정, 삭제, 검색, 태그 관리 |
| **obsidian-frontmatter** | Frontmatter 메타데이터 검색 & 관리 | 속성으로 노트 찾기, frontmatter 생성/수정/삭제 |
| **plantuml-ascii** | ASCII 아트 다이어그램 생성 | PlantUML을 ASCII로 변환, 시퀀스/클래스/플로우 다이어그램 |
| **prd** | 제품 요구사항 문서 | 포괄적인 PRD 생성, 사용자 스토리 및 사양 포함 |
| **plugin-manager** | 스킬 생명주기 관리 | GitHub 저장소에서 스킬 설치/업데이트/제거 |

---

## 🚀 빠른 참조

### Obsidian 작업
```
1. obsidian-markdown 로드 → 마크다운 문법 참조
2. obsidian-note-crud → 노트 생성/수정 스크립트 실행
3. obsidian-frontmatter → 메타데이터 관리
4. context-manager → AI Context 문서 관리 (대화 간 지식 보존)
```

### 웹 UI 빌드
```
간단한 페이지 → frontend-design
복잡한 상호작용 → web-artifacts-builder
```

### 문서 작업
```
Word → docx
PDF → pdf
PowerPoint → pptx
기술 문서 → doc-coauthoring
```

### 다이어그램 & 시각화
```
플로우차트, 시퀀스 → plantuml-ascii
마인드맵, canvas → json-canvas
생성 미술 → algorithmic-art
```

---

## 🗂️ 스킬 작업 공간 (Workspace)

모든 스킬의 임시 파일과 산출물은 `.claude/skills/workspace/[skill-name]/`에 저장됩니다.

**자세한 사용법**: [CLAUDE.md - 스킬 작업 공간](./CLAUDE.md#스킬-작업-공간-workspace) 참조

---

## 📌 이 문서 업데이트하기

### 새 스킬 설치 시 (plugin-manager 사용)

`plugin-manager install` 명령어를 사용할 때 **자동으로 이 파일이 업데이트됩니다**:
```bash
python skills/plugin-manager/scripts/manage.py install --git-url "https://github.com/owner/repo"
# ↓ 자동으로 SKILLS-INVENTORY.md 업데이트
```

### 새 로컬 커스텀 스킬 생성 시

1. `skills/[skill-name]/` 폴더에 스킬 생성
2. `SKILL.md` 파일 추가 (frontmatter 포함)
3. **수동으로 이 문서의 "Local Custom Skills" 섹션 업데이트**

구조:
```
---
name: skill-name
description: 간단한 설명
---
```

---

## 💡 스킬 선택 가이드

| 작업 | 추천 스킬 |
|------|---------|
| Obsidian 자동화 | obsidian-note-crud + obsidian-markdown |
| 웹사이트/앱 빌드 | frontend-design 또는 web-artifacts-builder |
| 문서 작성 | docx, pdf, pptx, doc-coauthoring |
| 데이터 정리 | xlsx |
| 다이어그램 | plantuml-ascii, json-canvas |
| 시각 디자인 | canvas-design, algorithmic-art |
| API 통합 | mcp-builder |

---

## 📊 요약

- **관리형 스킬** (GitHub): 19개
- **로컬 스킬**: 5개
- **총 스킬**: 24개 이상

**마지막 업데이트**: 2026-02-11
**유지보수**: plugin-manager install/uninstall 자동 업데이트 + 로컬 스킬 수동 업데이트
