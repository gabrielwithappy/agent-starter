# Claude Scripts

이 디렉토리에는 Claude Code 작업에 사용되는 유틸리티 스크립트가 포함되어 있습니다.

## 환경 변수 설정

스크립트는 프로젝트 루트의 `.env` 파일에서 환경 변수를 읽습니다.

### 사용법

1. **프로젝트 루트에 `.env` 파일 생성**:
   ```bash
   # Notion API Configuration
   NOTION_API_TOKEN=your_token_here
   NOTION_PAGE_ID=your_page_id_here
   NOTION_API_VERSION=2022-06-28
   ```

2. **스크립트 실행 전 환경 변수 로드** (Linux/Mac):
   ```bash
   export $(cat .env | xargs)
   python3 .claude/scripts/notion_test.py
   ```

3. **PowerShell 사용 시** (Windows):
   ```powershell
   Get-Content .env | ForEach-Object {
       if ($_ -match '^([^=]+)=(.*)$') {
           [System.Environment]::SetEnvironmentVariable($matches[1], $matches[2])
       }
   }
   python .claude/scripts/notion_test.py
   ```

4. **또는 `uv` 사용**:
   ```bash
   uv run --env-file .env python .claude/scripts/notion_test.py
   ```

## 스크립트 목록

### `notion_test.py`
Notion API를 테스트하는 스크립트입니다.

**필수 환경 변수**:
- `NOTION_API_TOKEN`: Notion API 토큰
- `NOTION_PAGE_ID`: 대상 페이지 ID
- `NOTION_API_VERSION`: API 버전 (기본값: 2022-06-28)

**실행**:
```bash
export $(cat .env | xargs)
python3 .claude/scripts/notion_test.py
```

## 보안 주의사항

- **.env 파일은 절대 Git에 커밋하지 마세요**
- `.gitignore`에 `.env` 파일이 포함되어 있는지 확인하세요
- API 토큰이 노출되었다면 즉시 재발급하세요
