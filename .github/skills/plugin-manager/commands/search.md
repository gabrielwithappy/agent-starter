---
description: Search for plugins in marketplaces
---
# Search Plugins Command

Search for available plugins across all configured marketplaces.

## Usage

Search for plugins (automatically saves to file):

```powershell
python .agent/skills/plugin-manager/scripts/marketplace.py search "$ARGUMENTS"
```

**Features:**
- Results automatically saved to `.agent/skills/plugin-manager/output/search_QUERY_YYYYMMDD_HHMMSS.txt`
- First 50 lines displayed in terminal as preview
- Full file path shown for manual viewing
- Old output files (>24 hours) automatically cleaned up

## Example

```
/plugin:search commit
```

Searches the anthropics/claude-code marketplace for plugins matching "commit" in name or description.

