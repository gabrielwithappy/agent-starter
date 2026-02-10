---
description: Update installed plugin(s) to latest version
---
# Update Plugin Command

Pull latest changes from Git and re-copy skills.

## Usage

```powershell
# Update all plugins
python .claude/skills/plugin-manager/scripts/manage.py update

# Update specific plugin
python .claude/skills/plugin-manager/scripts/manage.py update --plugin-name "$ARGUMENTS"
```

## Examples

```
/plugin-manager:update
/plugin-manager:update skills
```

This runs `git pull` on the cloned repo, re-copies skill files, and updates the commit hash in the registry.
