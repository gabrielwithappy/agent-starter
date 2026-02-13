# MCP 설정 가이드 (Model Context Protocol)

## 두 가지 설정 파일

Claude Code CLI와 VS Code 확장은 **각각 다른 MCP 설정 파일**을 사용합니다:

| 도구 | 설정 파일 | 키 경로 |
|------|----------|---------|
| **Claude Code CLI** | `.claude/config.json` | `mcpServers` |
| **VS Code 확장** | `.vscode/mcp.json` | `servers` |

## 현재 설치된 MCP 서버

### 1. Markitdown
- **목적**: 문서 변환
- **기능**: Word, PDF, Excel → Markdown
- **사용 예시**: 문서 분석, 텍스트 추출

### 2. Supabase
- **목적**: 데이터베이스 작업
- **기능**: PostgreSQL 데이터베이스 CRUD
- **사용 예시**: 데이터 저장, 조회, 업데이트

### 3. Next.js devtools
- **목적**: Next.js 프로젝트 관리
- **기능**: 빌드, 개발 서버, 라우팅 분석
- **사용 예시**: Next.js 앱 개발 지원

### 4. Desktop Commander
- **목적**: 데스크톱 자동화
- **기능**: 파일 시스템, 프로세스 관리
- **사용 예시**: 시스템 작업 자동화

## MCP 서버 추가/수정

### Claude Code CLI 사용 시

`.claude/config.json` 편집:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "command",
      "args": ["arg1", "arg2"]
    }
  }
}
```

### VS Code 확장 사용 시

`.vscode/mcp.json` 편집:

```json
{
  "servers": {
    "server-name": {
      "command": "command",
      "args": ["arg1", "arg2"]
    }
  }
}
```

## 주의사항

- **두 도구 동시 사용**: 각 파일을 별도로 관리
- **서버 추가 후**: Claude Code 재시작 필요
- **경로 설정**: 절대 경로 사용 권장