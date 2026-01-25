---
description: Manage skills and plugins (install, list, uninstall, search, browse)
---
# Plugin Management Workflow

This workflow allows you to manage skills (plugins) using the `plugin-manager`.

## Usage

When the user types `/plugin [command] [args]`, follow these steps:

1. **Search for Plugins**
   - Search the marketplace for plugins:
     ```powershell
     python .agent/skills/plugin-manager/scripts/marketplace.py search "[QUERY]"
     ```
   - Results automatically saved to `output/search_QUERY_YYYYMMDD_HHMMSS.txt`

2. **Browse Marketplace**
   - List all available plugins in the marketplace:
     ```powershell
     python .agent/skills/plugin-manager/scripts/marketplace.py list-marketplace
     ```
   - Results automatically saved to `output/marketplace_YYYYMMDD_HHMMSS.txt`

3. **Install a Plugin**
   - If the user provides a Git URL:
     ```powershell
     python .agent/skills/plugin-manager/scripts/manage.py install --git-url "[GIT_URL]"
     ```
   - If the user provides a plugin name (without a URL):
     ```powershell
     $url = python .agent/skills/plugin-manager/scripts/marketplace.py get-url "[PLUGIN_NAME]"
     if ($url) {
         python .agent/skills/plugin-manager/scripts/manage.py install --git-url $url
     }
     ```

4. **List Installed Plugins**
   - Run the list command:
     ```powershell
     python .agent/skills/plugin-manager/scripts/manage.py list
     ```

5. **Uninstall a Plugin**
   - Run the uninstall command with the skill/plugin name:
     ```powershell
     python .agent/skills/plugin-manager/scripts/manage.py uninstall --skill-name "[NAME]"
     ```

## Notes
- The default installation path is `.agent/skills/`.
- Default marketplace: `anthropics/claude-code` (Official Anthropic Claude Code demo marketplace)
- Search and browse results are automatically saved to `.agent/skills/plugin-manager/output/`
- Output files older than 24 hours are automatically cleaned up
- First 50 lines displayed in terminal with full file path for complete viewing
- Ensure you have the `plugin-manager` skill installed (which handles these scripts).

