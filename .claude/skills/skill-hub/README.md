---
tags: 30_Resources
---
# Skill Hub

Git 저장소에서 스킬을 설치하고 로컬 스킬을 통합 관리하는 중앙 허브입니다.

## Quick Start

### Install a Skill
```bash
python .claude/skills/skill-hub/scripts/hub.py install --git-url "https://github.com/kepano/obsidian-skills"
```

### List Installed Skills
```bash
python .claude/skills/skill-hub/scripts/hub.py list
```

### Remove a Skill
```bash
python .claude/skills/skill-hub/scripts/hub.py uninstall --skill-name "json-canvas"
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
skill-hub/
├── SKILL.md              # Main skill documentation
├── README.md             # This file
├── scripts/              # Executable scripts
│   ├── hub.py            # Main management script
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
