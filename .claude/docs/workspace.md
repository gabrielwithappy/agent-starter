# 스킬 작업 공간 (Workspace) 가이드

모든 스킬은 **표준화된 작업 공간**을 사용하여 임시 파일과 산출물을 관리합니다.

## 디렉토리 구조

```
.claude/skills/workspace/
├── [skill-name]/
│   ├── temp/      # 임시 파일 (자동 정리, Git 무시)
│   └── output/    # 산출물 (사용자 확인용, Git 무시)
```

## 스킬 스크립트에서 사용하기

### Python 예시

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

### JavaScript 예시

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

## 주의사항

- `workspace/*/temp/` 및 `workspace/*/output/`은 `.gitignore`에 포함되어 Git에서 추적되지 않음
- 임시 파일은 작업 완료 후 자동 정리 권장
- 최종 산출물은 사용자가 지정한 위치로 복사/이동