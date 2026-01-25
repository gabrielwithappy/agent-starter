---
description: Browse all plugins in marketplaces
---
# Browse Marketplace Command

List all available plugins from configured marketplaces.

## Usage

Browse all plugins (automatically saves to file):

```powershell
python .agent/skills/plugin-manager/scripts/marketplace.py list-marketplace
```

**Features:**
- Results automatically saved to `.agent/skills/plugin-manager/output/marketplace_YYYYMMDD_HHMMSS.txt`
- First 50 lines displayed in terminal as preview
- Full file path shown for manual viewing
- Old output files (>24 hours) automatically cleaned up

## Example

```
/plugin:browse
```

Displays all 13 plugins from the Anthropic Claude Code marketplace with complete details.

