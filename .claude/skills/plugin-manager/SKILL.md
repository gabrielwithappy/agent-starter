---
name: plugin-manager
description: GitHub 저장소에서 Claude 스킬을 설치, 관리, 제거합니다. Git에서 새 스킬을 추가하거나 설치된 스킬을 관리해야 할 때 사용하세요.
license: MIT
metadata:
  author: agent-starter
  version: 2.0.0
  keywords:
  - git
  - github
  - skill
  - installation
  - management
  - plugin
allowed-tools: Bash(python:*) Bash(git:*) Read Write
tags: 30_Resources
---
# Git Skill Manager v2.0.0

GitHub 저장소에서 Claude 스킬을 설치, 업데이트, 제거하는 스킬입니다.
Git clone 기반으로 저장소를 `repos/`에 clone하고 필요한 skill을 `.claude/skills/`로 복사합니다.

## 필수 요구사항

- **Git**: 시스템에 git이 설치되어 있어야 합니다 (`git --version`으로 확인)
- **Python 3.6+**
- 인터넷 연결 (공개 GitHub 저장소 접근)

## 명령어

### 설치 (install)

GitHub 저장소에서 스킬을 설치합니다:

```bash
python .claude/skills/plugin-manager/scripts/manage.py install --git-url "https://github.com/owner/repo"
```

선택적 매개변수:
- `--plugin-name`: 커스텀 플러그인 이름 (기본값: 저장소 이름)

동작:
1. `repos/owner-repo/`에 shallow clone (`--depth 1`)
2. 저장소 내 skill 디렉토리 자동 탐지 (`.claude/skills/` > `.agent/skills/` > `skills/`)
3. SKILL.md가 있는 skill만 `.claude/skills/`로 복사
4. registry.json에 설치 정보 및 commit hash 기록

### 업데이트 (update)

설치된 플러그인을 최신 버전으로 업데이트합니다:

```bash
# 전체 업데이트
python .claude/skills/plugin-manager/scripts/manage.py update

# 특정 플러그인만
python .claude/skills/plugin-manager/scripts/manage.py update --plugin-name "skills"
```

동작:
1. `git pull`로 최신 코드 가져오기
2. skill 파일 재복사
3. commit hash 업데이트

### 제거 (uninstall)

플러그인과 관련된 모든 스킬을 제거합니다:

```bash
python .claude/skills/plugin-manager/scripts/manage.py uninstall --plugin-name "skills"
```

동작:
1. `.claude/skills/`에서 해당 플러그인의 skill 디렉토리 삭제
2. `repos/`에서 clone 디렉토리 삭제
3. registry에서 항목 제거

### 목록 (list)

설치된 플러그인과 스킬 목록을 표시합니다:

```bash
python .claude/skills/plugin-manager/scripts/manage.py list
```

표시 정보: 플러그인 이름, 저장소 URL, commit hash, 설치/업데이트 시각, 포함된 skill 목록

## 예시

### Anthropic 공식 스킬 설치

```bash
python .claude/skills/plugin-manager/scripts/manage.py install --git-url "https://github.com/anthropics/skills"
```

출력:
```
Cloning 'https://github.com/anthropics/skills' ...
Found 16 skills: algorithmic-art, brand-guidelines, ...
Copied 16 skills to .claude/skills
[OK] Plugin 'skills' installed successfully (1ed29a03dc85)
```

### Obsidian 스킬 설치

```bash
python .claude/skills/plugin-manager/scripts/manage.py install --git-url "https://github.com/kepano/obsidian-skills"
```

### 전체 업데이트

```bash
python .claude/skills/plugin-manager/scripts/manage.py update
```

## 레지스트리 (registry.json)

설치된 스킬은 `assets/registry.json`에서 추적됩니다:

```json
{
  "version": "2.0.0",
  "plugins": [{
    "name": "skills",
    "git_url": "https://github.com/anthropics/skills",
    "owner": "anthropics",
    "repo": "skills",
    "repo_path": "anthropics-skills",
    "skill_prefix": "skills/",
    "commit_hash": "1ed29a03dc85...",
    "installed_at": "...",
    "updated_at": "...",
    "skills": ["docx", "pdf", "..."],
    "status": "installed"
  }]
}
```

v1.0.0 레지스트리는 첫 실행 시 자동으로 v2.0.0으로 마이그레이션됩니다.

## 오류 처리

| 오류 | 해결 |
|------|------|
| `git is not installed` | git 설치 후 PATH에 추가 |
| `Invalid Git URL` | `https://github.com/owner/repo` 형식 확인 |
| `No skill directory found` | 저장소에 skills/, .claude/skills/ 등이 있는지 확인 |
| `Plugin already installed` | `update` 명령 사용 |

## 파일 구조

```
plugin-manager/
├── SKILL.md              # 이 파일
├── repos/                # Git clone 저장소 (gitignored)
│   ├── .gitignore
│   ├── anthropics-skills/
│   └── kepano-obsidian-skills/
├── scripts/
│   └── manage.py         # CLI 스크립트
├── assets/
│   └── registry.json     # 설치 레지스트리
└── commands/             # 명령 문서
    ├── install.md
    ├── uninstall.md
    ├── update.md
    └── list.md
```
