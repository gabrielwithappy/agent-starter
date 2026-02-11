---
name: plugin-manager
description: Install, manage, and remove Claude skills from GitHub repositories. Use when adding new skills from Git or managing installed skills.
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
# Plugin Manager v2.0.0

Install, update, and remove Claude skills from GitHub repositories. Uses Git-based cloning to store repositories in `repos/` and copies required skills to `.claude/skills/`.

## Requirements

- **Git**: Must be installed on your system (verify with `git --version`)
- **Python 3.6+**
- Internet connection (for public GitHub repository access)

## Commands

### Install

Install a skill from a GitHub repository:

```bash
python .claude/skills/plugin-manager/scripts/manage.py install --git-url "https://github.com/owner/repo"
```

Optional parameters:
- `--plugin-name`: Custom plugin name (default: repository name)

Behavior:
1. Shallow clone (`--depth 1`) to `repos/owner-repo/`
2. Auto-detect skill directory (`.claude/skills/` > `.agent/skills/` > `skills/`)
3. Copy only skills with SKILL.md to `.claude/skills/`
4. Record installation info and commit hash in registry.json

### Update

Update installed plugins to the latest version:

```bash
# Update all plugins
python .claude/skills/plugin-manager/scripts/manage.py update

# Update specific plugin
python .claude/skills/plugin-manager/scripts/manage.py update --plugin-name "skills"
```

Behavior:
1. Fetch latest code with `git pull`
2. Recopy skill files
3. Update commit hash

### Uninstall

Remove all skills associated with a plugin:

```bash
python .claude/skills/plugin-manager/scripts/manage.py uninstall --plugin-name "skills"
```

Behavior:
1. Delete plugin's skill directories from `.claude/skills/`
2. Delete cloned directory from `repos/`
3. Remove entry from registry

### List

Display installed plugins and skills:

```bash
python .claude/skills/plugin-manager/scripts/manage.py list
```

Output: Plugin name, repository URL, commit hash, installation/update time, list of included skills

## Examples

### Install Official Anthropic Skills

```bash
python .claude/skills/plugin-manager/scripts/manage.py install --git-url "https://github.com/anthropics/skills"
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
python .claude/skills/plugin-manager/scripts/manage.py install --git-url "https://github.com/kepano/obsidian-skills"
```

### Update All Plugins

```bash
python .claude/skills/plugin-manager/scripts/manage.py update
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
plugin-manager/
├── SKILL.md              # This file
├── README.md             # Quick start guide
├── repos/                # Git cloned repositories
│   ├── .gitignore
│   ├── anthropics-skills/
│   └── kepano-obsidian-skills/
├── scripts/
│   ├── manage.py         # Main CLI script
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
