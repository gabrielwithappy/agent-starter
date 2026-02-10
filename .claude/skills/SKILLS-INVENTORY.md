# 스킬 인벤토리 (Skills Inventory)

이 문서는 프로젝트에 설치된 모든 Claude 스킬을 한눈에 보여줍니다. 각 스킬의 **핵심 목적**과 **사용 사례**를 설명합니다.

상세한 사용 방법은 각 스킬의 `SKILL.md` 파일을 참조하세요.

---

## 📋 스킬 분류 및 목록

### 🎨 **디자인 & 시각화 (Design & Visualization)**

| 스킬 | 목적 | 핵심 기능 |
|------|------|---------|
| **[algorithmic-art](./algorithmic-art)** | p5.js를 사용한 생성 미술 | 알고리즘 철학 정의 → 대화형 HTML 아트 생성 |
| **[canvas-design](./canvas-design)** | 고급 비주얼 디자인 (포스터, 아트) | 디자인 철학 → PNG/PDF 출력 |
| **[brand-guidelines](./brand-guidelines)** | Anthropic 브랜드 스타일 적용 | 공식 색상/타이포그래피 가이드 |
| **[theme-factory](./theme-factory)** | 아티팩트 테마 적용 | 10개 사전 정의 테마 + 커스텀 테마 생성 |

### 📄 **문서 작성 & 편집 (Documents)**

| 스킬 | 목적 | 핵심 기능 |
|------|------|---------|
| **[obsidian-markdown](./obsidian-markdown)** | Obsidian Flavored Markdown | Wikilinks, embeds, callouts, properties 문법 참조 |
| **[obsidian-note-crud](./obsidian-note-crud)** | Obsidian 노트 생성/수정/삭제 | Python 스크립트로 볼트 자동화 |
| **[obsidian-frontmatter](./obsidian-frontmatter)** | Obsidian 메타데이터 관리 | 프론트매터 검색/생성/업데이트 |
| **[obsidian-bases](./obsidian-bases)** | Obsidian 데이터베이스 뷰 | .base 파일 생성 (테이블/카드 뷰) |
| **[docx](./docx)** | Word 문서 작성/편집 | .docx 파일 조작 (TOC, 서식, 병합) |
| **[pdf](./pdf)** | PDF 처리 | 텍스트 추출, 병합, 분할, OCR, 폼 작성 |
| **[doc-coauthoring](./doc-coauthoring)** | 문서 협력 작성 가이드 | 구조화된 문서 작성 워크플로우 |
| **[pptx](./pptx)** | PowerPoint 생성/편집 | 슬라이드 덱 생성 및 편집 |

### 🛠️ **개발 & 기술 (Development)**

| 스킬 | 목적 | 핵심 기능 |
|------|------|---------|
| **[mcp-builder](./mcp-builder)** | MCP 서버 개발 | LLM ↔ 외부 서비스 통합 가이드 |
| **[frontend-design](./frontend-design)** | 고급 웹 UI 빌드 | React, HTML/CSS, 프로덕션 품질 컴포넌트 |
| **[web-artifacts-builder](./web-artifacts-builder)** | 복잡한 웹 아티팩트 | React, Tailwind, shadcn/ui 통합 |
| **[webapp-testing](./webapp-testing)** | 웹앱 테스트 자동화 | Playwright로 기능 테스트 |
| **[json-canvas](./json-canvas)** | JSON Canvas 파일 생성 | Obsidian canvas, 마인드맵, 플로우차트 |
| **[plantuml-ascii](./plantuml-ascii)** | ASCII 다이어그램 생성 | 시퀀스/클래스/플로우 다이어그램 |
| **[xlsx](./xlsx)** | 스프레드시트 자동화 | Excel 파일 생성/편집/데이터 정리 |
| **[plugin-manager](./plugin-manager)** | 스킬 설치 & 관리 | GitHub 저장소에서 스킬 추가/제거 |

### 📝 **콘텐츠 작성 (Content)**

| 스킬 | 목적 | 핵심 기능 |
|------|------|---------|
| **[internal-comms](./internal-comms)** | 내부 커뮤니케이션 | 상태 보고, 뉴스레터, FAQ 등 |
| **[prd](./prd)** | PRD 문서 생성 | 요구사항 정의서, 유저 스토리 |
| **[slack-gif-creator](./slack-gif-creator)** | Slack 최적화 GIF | 애니메이션 GIF 생성 |
| **[skill-creator](./skill-creator)** | 새 스킬 만들기 가이드 | 커스텀 스킬 개발 |

---

## 🚀 빠른 참조

### Obsidian 작업할 때
```
1. obsidian-markdown 로드 → 마크다운 문법 확인
2. obsidian-note-crud 로드 → 노트 생성/수정 스크립트 실행
3. obsidian-frontmatter로 메타데이터 관리
```

### 웹 UI 만들 때
```
간단한 페이지 → frontend-design
복잡한 상호작용 → web-artifacts-builder
```

### 문서 작업할 때
```
Word → docx
PDF → pdf
PowerPoint → pptx
기술 문서 → doc-coauthoring
```

### 다이어그램/시각화
```
플로우차트, 시퀀스 → plantuml-ascii
마인드맵, 캔버스 → json-canvas
생성 미술 → algorithmic-art
```

---

## 📌 스킬 추가 시 업데이트 방법

새로운 스킬을 설치할 때마다:

1. 스킬의 `SKILL.md` 첫 번째 라인에서 설명 확인
2. 이 문서의 적절한 분류 섹션에 추가
3. 필요시 CLAUDE.md의 "스킬 발견 및 사용" 섹션 업데이트

각 스킬은 다음 정보를 포함해야 합니다:
- **이름**: 스킬 폴더명
- **목적**: 한 줄 설명
- **핵심 기능**: 주요 기능 3-4개

---

## 💡 스킬 선택 가이드

| 하고 싶은 일 | 추천 스킬 |
|-----------|---------|
| Obsidian 자동화 | obsidian-note-crud + obsidian-markdown |
| 웹사이트/앱 만들기 | frontend-design 또는 web-artifacts-builder |
| 문서 작성 | docx, pdf, pptx, doc-coauthoring |
| 데이터 정리 | xlsx |
| 다이어그램 | plantuml-ascii, json-canvas |
| 시각 디자인 | canvas-design, algorithmic-art |
| API 연동 | mcp-builder |

---

**마지막 업데이트**: 2025-02-11
