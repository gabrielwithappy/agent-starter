---
tags: 30_Resources
---
# Plugin Manager

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

- Install skills from any public GitHub repository
- Automatic installation to `.claude/skills` directory
- Track installed skills in a registry
- List all installed skills with metadata
- Remove skills you no longer need
- Command-line interface (CLI)

## Documentation

For detailed usage instructions, see [SKILL.md](SKILL.md).

## Requirements

- Python 3.6+
- Internet connection (for GitHub API access)
- Git (for cloning repositories)

## Structure

```
plugin-manager/
├── SKILL.md              # Main skill documentation
├── README.md             # This file
├── scripts/              # Executable scripts
│   ├── manage.py         # Main management script
│   ├── example.py        # Usage examples
│   └── validate.py       # Validation script
├── assets/               # Data and templates
│   └── registry.json     # Installation registry
├── commands/             # Command implementations
├── output/               # Runtime output (gitignored)
└── repos/                # Cloned repositories
```

## License

MIT
