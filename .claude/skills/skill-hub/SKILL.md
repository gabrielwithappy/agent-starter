---
name: skill-hub
description: Git 저장소에서 스킬을 설치하고 로컬 스킬을 통합 관리하는 중앙 허브. Use when: (1) Git 저장소에서 스킬 설치, (2) 로컬 제작 스킬 등록, (3) 전체 스킬 목록 조회 (Git + 로컬), (4) 스킬 업데이트/삭제, (5) SKILLS-INVENTORY.md 자동 생성
license: MIT
metadata:
  author: agent-starter
  version: 3.0.0
  keywords:
  - git
  - github
  - skill
  - installation
  - management
  - hub
  - registry
allowed-tools: Bash(python:*) Bash(git:*) Read Write Edit
tags: 30_Resources
---
# Skill Hub v3.0.0

Git 저장소에서 스킬을 설치하고 로컬에서 직접 만든 스킬을 통합 관리하는 중앙 허브입니다. Git 기반 클로닝으로 저장소를 `repos/`에 저장하고, 필요한 스킬을 `.claude/skills/`에 복사합니다.

## Requirements

- **Git**: Must be installed on your system (verify with `git --version`)
- **Python 3.6+**
- Internet connection (for public GitHub repository access)

## Commands

### Install

Install skills from a GitHub repository:

```bash
# Install all skills from repository
python .claude/skills/skill-hub/scripts/hub.py install --git-url "https://github.com/owner/repo"

# Install specific skills only
python .claude/skills/skill-hub/scripts/hub.py install --git-url "https://github.com/owner/repo" --skills "docx,pdf,xlsx"
```

Optional parameters:
- `--plugin-name`: Custom plugin name (default: repository name)
- `--skills`: Comma-separated list of specific skills to install (if omitted, all skills are installed)

Behavior:
1. Shallow clone (`--depth 1`) to `repos/owner-repo/`
2. Auto-detect skill directory (`.claude/skills/` > `.agent/skills/` > `skills/`)
3. Discover all available skills in repository
4. Install selected skills (or all if `--skills` not specified)
5. Copy only skills with SKILL.md to `.claude/skills/`
6. Record installation info and commit hash in registry.json
7. **Automatically update SKILLS-INVENTORY.md** with installed skills

### Update

Update installed plugins to the latest version:

```bash
# Update all plugins
python .claude/skills/skill-hub/scripts/hub.py update

# Update specific plugin
python .claude/skills/skill-hub/scripts/hub.py update --plugin-name "skills"
```

Behavior:
1. Fetch latest code with `git pull`
2. Recopy skill files
3. Update commit hash

### Uninstall

Remove all skills associated with a plugin:

```bash
python .claude/skills/skill-hub/scripts/hub.py uninstall --plugin-name "skills"
```

Behavior:
1. Delete plugin's skill directories from `.claude/skills/`
2. Delete cloned directory from `repos/`
3. Remove entry from registry

### List

Display installed plugins and skills:

```bash
python .claude/skills/skill-hub/scripts/hub.py list
```

Output: Plugin name, repository URL, commit hash, installation/update time, list of included skills

## Examples

### Install Official Anthropic Skills

```bash
python .claude/skills/skill-hub/scripts/hub.py install --git-url "https://github.com/anthropics/skills"
```

Output:
```
Cloning 'https://github.com/anthropics/skills' ...
Found 16 skills: algorithmic-art, brand-guidelines, ...
Copied 16 skills to .claude/skills
[OK] Plugin 'skills' installed successfully (1ed29a03dc85)
```

### Install Obsidian Skills

```bash
# Install all Obsidian skills
python .claude/skills/skill-hub/scripts/hub.py install --git-url "https://github.com/kepano/obsidian-skills"

# Or install only specific skills
python .claude/skills/skill-hub/scripts/hub.py install --git-url "https://github.com/kepano/obsidian-skills" --skills "obsidian-markdown,obsidian-note-crud"
```

### Install Google Workspace Skills (Selective)

```bash
# Install only Google Calendar and Gmail skills
python .claude/skills/skill-hub/scripts/hub.py install --git-url "https://github.com/sanjay3290/ai-skills" --skills "google-calendar,gmail"
```

### Update All Plugins

```bash
python .claude/skills/skill-hub/scripts/hub.py update
```

## Registry (registry.json)

Installed skills are tracked in `assets/registry.json`:

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

v1.0.0 registry automatically migrates to v2.0.0 on first run.

## Error Handling

| Error | Resolution |
|-------|-----------|
| `git is not installed` | Install git and add to PATH |
| `Invalid Git URL` | Verify format: `https://github.com/owner/repo` |
| `No skill directory found` | Check if repository has skills/, .claude/skills/, etc. |
| `Plugin already installed` | Use `update` command |

## File Structure

```
skill-hub/
├── SKILL.md              # This file
├── README.md             # Quick start guide
├── repos/                # Git cloned repositories
│   ├── .gitignore
│   ├── anthropics-skills/
│   └── kepano-obsidian-skills/
├── scripts/
│   ├── hub.py            # Main CLI script
│   ├── example.py        # Usage examples
│   └── validate.py       # Validation script
├── assets/
│   └── registry.json     # Installation registry
└── commands/             # Command implementations
    ├── install.py
    ├── uninstall.py
    ├── update.py
    └── list.py
```
