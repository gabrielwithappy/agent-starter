---
name: plugin-manager
description: Install, manage, and remove Claude skills from GitHub repositories. Use
  when you need to add new skills from git or manage installed skills.
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
allowed-tools: Bash(python:*) Read Write
tags: 30_Resources
---
# Git Skill Manager

A skill for installing, managing, and removing Claude skills directly from GitHub repositories. This skill automates the process of downloading skill packages from git and integrating them into your `.claude/skills` directory.

## Purpose

This skill enables you to:
- **Install skills from GitHub**: Automatically download and install skill packages from any public GitHub repository
- **Track installations**: Maintain a registry of all installed skills with metadata
- **Manage skills**: List all installed skills with their details
- **Remove skills**: Clean up skills you no longer need

## When to Use This Skill

Use this skill when you need to:
- Add new capabilities to Claude/Antigravity by installing skills from GitHub
- Search for plugins in the official Claude Code marketplace
- Browse available plugins before installing
- Check what skills are currently installed
- Remove skills that are no longer needed
- Manage skill dependencies and versions

## Instructions

### Searching for Plugins in the Marketplace

To search for available plugins:

```bash
python .agent/skills/plugin-manager/scripts/marketplace.py search "QUERY"
```

This searches the official Anthropic Claude Code marketplace (`anthropics/claude-code`) for plugins matching your query.

**Example:**
```bash
python .agent/skills/plugin-manager/scripts/marketplace.py search "commit"
```

### Browsing the Marketplace

To see all available plugins in the marketplace:

```bash
python .agent/skills/plugin-manager/scripts/marketplace.py list-marketplace
```

This displays all plugins from the default marketplace with their descriptions and versions.

### Installing a Skill from GitHub

To install a skill from a GitHub repository:

1. Identify the GitHub repository URL containing the skill (must be a public repository)
2. Run the install command with the repository URL
3. The skill will automatically:
   - Download all skill files from the repository
   - Extract skills from the `.agent/skills/` directory (or `.claude/skills/` if present)
   - Install them to your local `.agent/skills/` folder
   - Register the installation in the registry

**Command:**
```bash
python .agent/skills/plugin-manager/scripts/manage.py install --git-url "REPOSITORY_URL"
```

**Optional parameters:**
- `--plugin-name`: Custom name for the plugin (default: repository name)
- `--target-path`: Installation directory (default: `.agent`)

### Installing a Plugin by Name from Marketplace

To install a plugin by name from the marketplace:

1. First, get the Git URL from the marketplace:
```bash
python .agent/skills/plugin-manager/scripts/marketplace.py get-url "PLUGIN_NAME"
```

2. Then install using the returned URL:
```bash
python .agent/skills/plugin-manager/scripts/manage.py install --git-url "RETURNED_URL"
```

### Listing Installed Skills

To see all currently installed skills:

```bash
python .agent/skills/plugin-manager/scripts/manage.py list
```

This displays:
- Plugin name
- Repository URL
- Owner
- Installation timestamp
- List of skills included in the plugin

### Removing a Skill

To remove an installed skill:

1. First, list installed skills to find the exact skill name
2. Run the uninstall command with the skill name

```bash
python .agent/skills/plugin-manager/scripts/manage.py uninstall --skill-name "SKILL_NAME"
```

This will:
- Delete the skill directory and all its files
- Remove the entry from the registry
- Report the number of files deleted

## Examples

### Example 1: Installing Obsidian Skills

```bash
python scripts/manage.py install --git-url "https://github.com/kepano/obsidian-skills"
```

**Output:**
```
?�� 'obsidian-skills' ?�운로드 �?..
???�러그인 'obsidian-skills'??가) ?�공?�으�??�치?�었?�니??
??3개의 skill???�치?�었?�니??
  - .agent/skills/json-canvas
  - .agent/skills/obsidian-bases
  - .agent/skills/obsidian-markdown
```

### Example 2: Listing Installed Skills

```bash
python scripts/manage.py list
```

**Output:**
```
?�� ?�치??Plugin 목록 (1�?:
============================================================
1. obsidian-skills
   Repository: https://github.com/kepano/obsidian-skills
   Owner: kepano
   Installed: 2026-01-23T21:00:00
   Skills: json-canvas, obsidian-bases, obsidian-markdown
============================================================
```

### Example 3: Removing a Skill

```bash
python scripts/manage.py uninstall --skill-name "json-canvas"
```

**Output:**
```
?���? 'json-canvas' ?�거 �?..
???�킬 'json-canvas'??가) ?�공?�으�??�거?�었?�니??
??5개의 ?�일????��?�었?�니??
```

## Registry Management

Installed skills are tracked in `assets/registry.json`:

```json
{
  "version": "1.0.0",
  "plugins": [
    {
      "name": "obsidian-skills",
      "git_url": "https://github.com/kepano/obsidian-skills",
      "owner": "kepano",
      "repo": "obsidian-skills",
      "target_path": ".agent",
      "installed_at": "2026-01-23T21:00:00.000000",
      "skills": ["obsidian-markdown", "obsidian-bases", "json-canvas"],
      "status": "installed"
    }
  ],
  "last_updated": "2026-01-23T21:00:00.000000"
}
```

## Error Handling

Common errors and solutions:

**"Invalid Git URL"**
- Ensure the URL is in the format: `https://github.com/owner/repo`
- Verify the repository exists and is public

**"Skill not found"**
- Use the `list` command to see exact skill names
- Skill names are case-sensitive

**"HTTP Error"**
- Check your internet connection
- Verify the repository is accessible
- Ensure the repository has a `.agent/skills/` or `.claude/skills` directory

**"Permission denied"**
- Ensure you have write permissions to the `.agent/skills` directory
- Check file system permissions

## Requirements

- Python 3.6 or higher
- Internet connection for GitHub API access
- Write permissions to `.agent/skills` directory

## File Structure

```
plugin-manager/
?��??� SKILL.md              # This file
?��??� README.md             # Quick start guide
?��??� scripts/              # Executable scripts
??  ?��??� manage.py        # Main CLI script
??  ?��??� example.py       # Usage examples
??  ?��??� validate.py      # Validation script
?��??� assets/               # Data and templates
??  ?��??� registry.json    # Installation registry
?��??� references/           # Reference documentation
    ?��??� QUICKREF.md      # Quick reference card
    ?��??� MIGRATION.md     # Migration guide
    ?��??� COMPLETION.md    # Completion report
```

## References

For more information, see:
- [Quick Reference](references/QUICKREF.md) - Command cheat sheet
- [Migration Guide](references/MIGRATION.md) - Changes from previous version
- [Agent Skills Specification](https://agentskills.io/specification)
- [GitHub API Documentation](https://docs.github.com/en/rest)
