# Antigravity IDE와 Notion MCP를 활용한 문서 업데이트 가이드

이 문서는 Antigravity IDE 환경에서 Notion MCP(Model Context Protocol) 서버를 활용하여 Notion 페이지를 검색, 생성 및 업데이트하는 방법을 설명합니다.

## 1. 개요
Antigravity IDE는 MCP를 통해 외부 도구와 연동할 수 있습니다. `notion-mcp-server`를 사용하면 IDE를 벗어나지 않고도 Notion의 데이터베이스와 페이지에 접근하여 정보를 읽거나 새로운 문서를 작성할 수 있습니다.

## 2. 전제 조건
*   **Antigravity IDE**: 최신 버전의 Antigravity IDE가 설치되어 있어야 합니다.
*   **Notion MCP Server**: 프로젝트 설정(`config.json` 등)에 `notion-mcp-server`가 올바르게 구성되어 있어야 합니다.
*   **Notion Integration**: Notion API 토큰이 발급되어 있고, 작업하려는 페이지나 데이터베이스에 해당 Integration이 초대되어 있어야 권한을 가집니다.

## 3. 주요 기능 및 사용법

### 3.1 페이지 검색 (`API-post-search`)
Notion 내의 특정 페이지나 데이터베이스를 찾기 위해 사용합니다. 예를 들어, 글을 작성할 상위 페이지(Parent Page)를 찾을 때 유용합니다.

**사용 예시:**
> "Notion에서 '프로젝트 회의록' 페이지를 찾아줘."

에이전트는 내부적으로 다음과 같이 호출합니다:
```json
{
  "query": "프로젝트 회의록",
  "filter": {
    "value": "page",
    "property": "object"
  }
}
```

### 3.2 페이지 생성 (`API-post-page`)
새로운 페이지를 생성할 때 사용합니다. 상위 페이지(Parent)의 ID와 페이지 속성(제목 등), 본문 내용(Blocks)을 지정해야 합니다.

**사용 예시:**
> "회의록 페이지 하위에 '2월 7일 주간 회의'라는 문서를 만들어줘."

에이전트는 찾은 `parent_page_id`를 사용하여 페이지를 생성합니다.

### 3.3 페이지 업데이트 (`API-patch-page`, `API-patch-block-children`)
*   **API-patch-page**: 페이지의 제목, 아이콘, 속성(Properties) 등을 수정할 때 사용합니다.
*   **API-patch-block-children**: 페이지 본문에 새로운 블록을 추가(Append)할 때 사용합니다.

## 4. 워크플로우 예시

1.  **목표 설정**: 사용자가 "Antigravity 사용법을 정리해서 Notion에 올려줘"라고 요청.
2.  **위치 확인**: 에이전트가 `API-post-search`를 사용하여 저장할 적절한 상위 페이지(예: '기술 문서', 'Wiki')를 검색.
3.  **내용 작성**: 에이전트가 `write_to_file` 등으로 초안을 작성하거나 메모리에 구성.
4.  **페이지 생성**: `API-post-page`를 호출하여 Notion에 실제 페이지 생성 및 내용 입력.
5.  **확인**: 생성된 페이지의 URL을 사용자에게 제공.

## 5. 트러블슈팅
*   **검색 결과가 없을 때**: Notion 페이지 우측 상단의 `...` 메뉴 > `Connections` > `Connect to`에서 해당 Integration이 추가되어 있는지 확인하세요. Integration이 초대되지 않은 페이지는 API로 접근할 수 없습니다.
