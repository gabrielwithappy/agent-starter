---
description: Uninstall a plugin and all its skills
---
# Uninstall Plugin Command

Remove a plugin and all its associated skills.

## Usage

```powershell
python .claude/skills/plugin-manager/scripts/manage.py uninstall --plugin-name "$ARGUMENTS"
```

Use `/plugin-manager:list` first to see plugin names.

## Example

```
/plugin-manager:uninstall skills
/plugin-manager:uninstall obsidian-skills
```

This removes all skill directories installed by the plugin, deletes the cloned repo, and updates the registry.
