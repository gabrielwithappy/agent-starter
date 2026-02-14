---
description: Uninstall a plugin and all its skills
---
# Uninstall Plugin Command

Remove a plugin and all its associated skills.

## Usage

```powershell
python .claude/skills/skill-hub/scripts/hub.py uninstall --plugin-name "$ARGUMENTS"
```

Use `/skill-hub:list` first to see plugin names.

## Example

```
/skill-hub:uninstall skills
/skill-hub:uninstall obsidian-skills
```

This removes all skill directories installed by the plugin, deletes the cloned repo, and updates the registry.
