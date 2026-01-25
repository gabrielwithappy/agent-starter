---
tags: 30_Resources
---
# Git Skill Manager

Install and manage Claude skills directly from GitHub repositories.

## Quick Start

### Install a Skill
```bash
python .claude/skills/plugin-manager/scripts/manage.py install --git-url "https://github.com/kepano/obsidian-skills"
```

### List Installed Skills
```bash
python .claude/skills/plugin-manager/scripts/manage.py list
```

### Remove a Skill
```bash
python .claude/skills/plugin-manager/scripts/manage.py uninstall --skill-name "json-canvas"
```

## Features

- ??Install skills from any public GitHub repository
- ??Automatic installation to `.claude/skills` directory
- ??Track installed skills in a registry
- ??List all installed skills with metadata
- ??Remove skills you no longer need
- ??Command-line interface (CLI)

## Documentation

For detailed usage instructions, see [SKILL.md](SKILL.md).

For quick command reference, see [references/QUICKREF.md](references/QUICKREF.md).

## Requirements

- Python 3.6+
- Internet connection (for GitHub API access)

## Structure

```
plugin-manager/
?œâ??€ SKILL.md              # Main skill documentation
?œâ??€ README.md             # This file
?œâ??€ scripts/              # Executable scripts
??  ?œâ??€ manage.py        # Main management script
??  ?œâ??€ example.py       # Usage examples
??  ?”â??€ validate.py      # Validation script
?œâ??€ assets/               # Data and templates
??  ?”â??€ registry.json    # Installation registry
?”â??€ references/           # Reference documentation
    ?œâ??€ QUICKREF.md      # Quick reference
    ?œâ??€ MIGRATION.md     # Migration guide
    ?”â??€ COMPLETION.md    # Completion report
```

## License

MIT
