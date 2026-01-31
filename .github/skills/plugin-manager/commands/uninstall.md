---
description: Uninstall a skill/plugin by name
---
# Uninstall Plugin Command

Remove an installed skill or plugin.

## Usage

Uninstall a plugin by providing its skill name:

```powershell
python .agent/skills/plugin-manager/scripts/manage.py uninstall --skill-name "$ARGUMENTS"
```

Use `/plugin:list` first to see the exact skill names available.

## Example

```
/plugin:uninstall json-canvas
```

This will delete the skill directory and remove it from the registry.
