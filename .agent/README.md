# Claude Plugin Installer Skills

VS Code에서 사용 가능한 Claude Plugin 설치 도구 모음입니다.

## 개요

이 skill 모음은 Git repository에서 Claude plugin을 다운로드하여 `.claude` 폴더에 자동으로 설치할 수 있게 합니다. VS Code에서 Claude Code나 Claude Chat 확장과 함께 사용할 수 있습니다.

## 설치 위치

```
.claude/
├── plugins/           # 설치된 플러그인들
├── skills/           # Skill 정의들
│   └── install_git_plugin/
│       ├── manifest.json
│       ├── index.js
│       └── install_plugin.py
├── plugin.json       # 플러그인 설정
└── .claude-plugin    # Claude 플러그인 설정
```

## 사용 방법

### 1. VS Code에서 Claude Code 사용

`.claude` 폴더가 프로젝트 루트에 있으면 Claude Code에서 자동으로 인식됩니다.

### 2. Skill 실행

#### Python 버전
```bash
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'
```

#### Node.js 버전
```bash
node .claude/skills/install_git_plugin/index.js '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'
```

### 3. Claude에게 지시하기

Claude Code 또는 Claude Chat에서 다음과 같이 명령할 수 있습니다:

```
이 저장소를 설치해줘: https://github.com/gabrielwithappy/obsidian-skills
```

Claude는 `install_git_plugin` skill을 사용하여 해당 플러그인을 설치할 것입니다.

## Skill 입력 파라미터

### install_git_plugin

| 파라미터 | 타입 | 필수 | 설명 |
|---------|------|------|------|
| git_url | string | ✓ | Claude plugin이 저장된 Git repository URL |
| plugin_name | string | | 설치할 플러그인의 이름 (기본값: repository 이름) |
| target_path | string | | 설치 대상 경로 (기본값: .claude) |

### 사용 예시

```json
{
  "git_url": "https://github.com/gabrielwithappy/obsidian-skills",
  "plugin_name": "obsidian-skills",
  "target_path": "./.claude"
}
```

## 출력 형식

성공 응답:
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

실패 응답:
```json
{
  "status": "error",
  "message": "플러그인 설치 실패: [오류 메시지]",
  "plugin_path": null,
  "plugin_info": null
}
```

## 지원되는 Plugin 형식

이 skill은 다음 형식의 Claude plugin을 자동으로 인식합니다:

- `manifest.json` - 플러그인 메타데이터
- `plugin.json` - 플러그인 설정
- `.claude-plugin` - Claude 플러그인 설정 파일
- `README.md` - 플러그인 문서
- `index.js` / `install_plugin.py` - 플러그인 실행 파일

## VS Code 통합

### 설정 방법

1. 프로젝트 루트에 `.claude` 폴더가 있는지 확인
2. Claude Code 확장 설치
3. VS Code를 재시작하면 자동으로 `.claude` 폴더의 skills을 인식합니다

### Claude와 상호작용

```
@skills install_git_plugin
설치할 Git 주소: https://github.com/gabrielwithappy/obsidian-skills
```

또는 더 간단히:

```
이 GitHub repository를 plugin으로 설치해줘: https://github.com/gabrielwithappy/obsidian-skills
```

## 권한 설정

이 skill이 필요로 하는 권한:

- `filesystem` - read/write: 플러그인 파일 저장
- `network` - read: GitHub에서 파일 다운로드

## 트러블슈팅

### 플러그인이 설치되지 않는 경우

1. Git URL이 올바른지 확인
2. Repository가 public인지 확인
3. 필수 파일(manifest.json, plugin.json 등)이 repository에 있는지 확인

### VS Code에서 skill을 인식하지 못하는 경우

1. `.claude` 폴더 경로 확인
2. `plugin.json` 파일이 `.claude` 폴더에 있는지 확인
3. VS Code 재시작

## 라이선스

MIT License

## 참고

- [Claude Skills Documentation](https://platform.claude.com/docs/agents-and-tools/agent-skills)
- [Agent Skills Specification](https://agentskills.io/specification)
