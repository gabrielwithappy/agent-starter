---
tags: 30_Resources
---
# Claude Plugin Installer 사용 예시

## 1. 기본 사용법

### VS Code에서 Claude Code로 사용

```
@skills install_git_plugin
나는 이 플러그인을 설치하고 싶어:
https://github.com/gabrielwithappy/obsidian-skills
```

또는 더 간단하게:

```
이 저장소를 .claude 폴더에 plugin으로 설치해줘:
https://github.com/gabrielwithappy/obsidian-skills
```

## 2. 터미널에서 직접 실행

### Python 사용 (권장)
```bash
cd d:\00_PRJ\agent-starter

# obsidian-skills 설치
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'

# 커스텀 이름으로 설치
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills", "plugin_name": "my-obsidian"}'
```

### Node.js 사용
```bash
node .claude/skills/install_git_plugin/index.js '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'
```

## 3. 설치된 플러그인 확인

```bash
# 설치된 모든 플러그인 목록 조회
python3 .claude/skills/list_plugins.py './.claude'
```

## 4. 플러그인 제거

```bash
# 플러그인 제거
python3 .claude/skills/remove_plugin.py '{"plugin_name": "obsidian-skills"}'
```

## 5. 여러 저장소 설치 예시

```bash
# obsidian-skills 설치
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'

# 다른 플러그인 설치
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/user/another-plugin"}'

# 설치된 목록 확인
python3 .claude/skills/list_plugins.py './.claude'
```

## 6. VS Code 통합 워크플로우

### 단계별 가이드

1. **프로젝트 루트 확인**
   ```bash
   # .claude 폴더가 d:\00_PRJ\agent-starter에 위치
   ls -la .claude/
   ```

2. **VS Code에서 Claude Code 확장 설치**
   - Extensions에서 "Claude Code" 또는 "Claude" 검색 및 설치

3. **VS Code 재시작**
   - 이제 Claude Code가 `.claude/skills` 폴더의 skills를 자동으로 인식

4. **Claude와 상호작용**
   ```
   이 GitHub 저장소를 설치해줘: https://github.com/gabrielwithappy/obsidian-skills
   ```

5. **설치 확인**
   - `.claude/plugins/obsidian-skills/` 폴더가 생성되면 성공

## 7. 스킬 매개변수 옵션

### install_git_plugin 스킬

```json
{
  "git_url": "https://github.com/gabrielwithappy/obsidian-skills",  // 필수
  "plugin_name": "obsidian-skills",                                   // 선택사항 (기본값: repo 이름)
  "target_path": "./.claude"                                          // 선택사항 (기본값: .claude)
}
```

## 8. 응답 메시지 예시

### 성공
```json
{
  "status": "success",
  "message": "플러그인 'obsidian-skills'이(가) 성공적으로 설치되었습니다.",
  "plugin_path": "./.claude/plugins/obsidian-skills",
  "plugin_info": {
    "name": "obsidian-skills",
    "repository": "https://github.com/gabrielwithappy/obsidian-skills",
    "owner": "gabrielwithappy",
    "installed_at": "2026-01-23T20:31:00.000000",
    "status": "active"
  }
}
```

### 실패
```json
{
  "status": "error",
  "message": "플러그인 설치 실패: 오류 메시지",
  "plugin_path": null,
  "plugin_info": null
}
```

## 9. 지원되는 플러그인 형식

이 skill은 다음과 같은 Claude plugin 형식을 지원합니다:

- **Standard Claude Plugin**
  - manifest.json (플러그인 메타데이터)
  - plugin.json (설정)
  - index.js / install_plugin.py (실행 파일)

- **Obsidian Skills Plugin**
  - .claude-plugin (설정 파일)
  - skills/ (스킬 모음)
  - README.md (문서)

## 10. 트러블슈팅

### Q: "모듈을 찾을 수 없음" 오류

**A:** Python이 설치되어 있는지 확인하세요.
```bash
python3 --version
```

### Q: "repository를 찾을 수 없음" 오류

**A:** Git URL이 올바른지 확인하세요.
```bash
# 올바른 형식
https://github.com/owner/repo
https://github.com/owner/repo.git
```

### Q: VS Code에서 skill이 보이지 않음

**A:** 다음을 확인하세요:
1. `.claude` 폴더가 프로젝트 루트에 있는지
2. `plugin.json` 파일이 `.claude` 폴더에 있는지
3. VS Code를 다시 시작했는지

### Q: 권한 거부 오류

**A:** Python 스크립트에 실행 권한을 부여하세요.
```bash
chmod +x .claude/skills/install_git_plugin/install_plugin.py
```

## 11. 고급 사용법

### 환경 변수로 설정

```bash
# Windows PowerShell
$env:CLAUDE_PLUGINS_PATH = ".\.claude"

# Linux/macOS
export CLAUDE_PLUGINS_PATH="./.claude"
```

### 스크립트로 자동 설치

```bash
# install_plugins.sh (Linux/macOS)
#!/bin/bash
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/user/another-plugin"}'
```

```powershell
# install_plugins.ps1 (Windows)
$plugins = @(
    "https://github.com/gabrielwithappy/obsidian-skills",
    "https://github.com/user/another-plugin"
)

foreach ($url in $plugins) {
    python3 .claude/skills/install_git_plugin/install_plugin.py "{`"git_url`": `"$url`"}"
}
```
