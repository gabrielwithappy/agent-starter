---
description: Install a skill/plugin from a Git repository or marketplace
---
# Install Plugin Command

Install a skill or plugin from a GitHub repository or from a marketplace by name.

## Usage

**Option 1: Install from Git URL**

```powershell
python .agent/skills/plugin-manager/scripts/manage.py install --git-url "$ARGUMENTS"
```

**Option 2: Install from Marketplace by Name**

First, get the Git URL from the marketplace:

```powershell
$url = python .agent/skills/plugin-manager/scripts/marketplace.py get-url "$ARGUMENTS"
if ($url) {
    python .agent/skills/plugin-manager/scripts/manage.py install --git-url $url
}
```

If the user provides just a plugin name, search the marketplace first and install if found.

## Examples

```
/plugin:install https://github.com/user/repo
/plugin:install commit-commands
```

The first example installs from a direct Git URL.
The second example searches the marketplace for "commit-commands" and installs it if found.

