# Output Directory

This directory stores temporary output files from plugin marketplace commands.

## Files

- `marketplace_*.txt` - Results from `list-marketplace` command
- `search_*.txt` - Results from `search` command

## Automatic Cleanup

Output files older than 24 hours are automatically deleted when running marketplace commands.

## Manual Access

You can open these files directly to view complete plugin information without terminal truncation:

```powershell
# View latest marketplace listing
notepad .agent/skills/plugin-manager/output/marketplace_*.txt

# View search results
notepad .agent/skills/plugin-manager/output/search_*.txt
```
