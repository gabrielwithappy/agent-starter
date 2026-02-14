---
description: Install a skill plugin from a Git repository
---
# Install Plugin Command

Install skills from a GitHub repository via git clone.

## Usage

```powershell
python .claude/skills/skill-hub/scripts/hub.py install --git-url "$ARGUMENTS"
```

Optional: `--plugin-name "custom-name"` to override the default repo name.

## Examples

```
/skill-hub:install https://github.com/anthropics/skills
/skill-hub:install https://github.com/kepano/obsidian-skills
```

The command clones the repo, detects skill directories, and copies them to `.claude/skills/`.
