# Windows 환경 설정 가이드

## 인코딩 이슈

Windows 기본 콘솔 인코딩은 cp949 (한글 환경)이므로 UTF-8 설정이 필요합니다.

### Python 스크립트 시작 부분에 추가

```python
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
```

### 출력 문자 권장사항

Unicode 이모지/기호 (⚠✓✗─⊘) 대신 ASCII 사용:
- `[OK]` - 성공
- `[ERROR]` - 오류
- `[WARNING]` - 경고
- `[INFO]` - 정보

## 경로 처리

### 백슬래시 이스케이프

```python
# 좋은 예
path = Path("d:/00_MyData/obsidianKMS-agent")
path = Path(r"d:\00_MyData\obsidianKMS-agent")

# 피할 예
path = "d:\00_MyData\obsidianKMS-agent"  # 이스케이프 문제
```

### 경로 구분자

```python
# 좋은 예 - 크로스 플랫폼
from pathlib import Path
path = Path("folder") / "subfolder" / "file.txt"

# 피할 예 - Windows 종속
path = "folder\\subfolder\\file.txt"
```

## 가상환경 활성화

```bash
# Windows
.venv\Scripts\activate

# PowerShell
.venv\Scripts\Activate.ps1

# Git Bash
source .venv/Scripts/activate
```

## 일반적인 문제 해결

### 1. 권한 문제
- 관리자 권한으로 터미널 실행
- 또는 사용자 디렉토리에서 작업

### 2. 긴 경로 문제
- Windows 10 이상: 긴 경로 지원 활성화
- 레지스트리: `HKLM\SYSTEM\CurrentControlSet\Control\FileSystem\LongPathsEnabled` = 1

### 3. 스크립트 실행 정책 (PowerShell)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```