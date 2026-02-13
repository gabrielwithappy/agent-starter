# Obsidian Agent Rules

## 핵심 워크플로우 (필수)

**CRITICAL**: Obsidian 노트 작업 시 반드시 아래 순서를 따릅니다:

1. **`obsidian-markdown` 스킬 로드** → Obsidian Flavored Markdown 문법 참조
2. **콘텐츠 작성** → 위키링크, callout, embed 등 Obsidian 문법 준수
3. **`obsidian-note-crud` 스크립트 실행** → 노트 생성/수정/삭제

---

## 세부 규칙

### 1. 기본 생성 위치
- **CRITICAL**: 새 노트는 항상 `obsidianKMS/0.Inbox/`에 생성
- 사용자가 명시적으로 다른 경로를 지정하지 않는 한 다른 폴더(예: `03.Resource/`) 사용 금지

### 2. Frontmatter (필수)
모든 노트는 YAML frontmatter 필수:
```yaml
---
created: YYYY-MM-DD
tags:
  - tag1
  - tag2
---
```

### 3. 파일명 규칙
- 명확하고 설명적인 파일명 사용
- 날짜가 관련 있는 경우 `YYYY-MM-DD` 형식으로 앞에 추가

### 4. AI Context 문서
AI Context 문서 생성/검색/업데이트는 **`context-manager` 스킬** 사용
