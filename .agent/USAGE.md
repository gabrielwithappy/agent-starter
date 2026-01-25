---
tags: 30_Resources
---
# Claude Plugin Installer ?¬ìš© ?ˆì‹œ

## 1. ê¸°ë³¸ ?¬ìš©ë²?

### VS Code?ì„œ Claude Codeë¡??¬ìš©

```
@skills install_git_plugin
?˜ëŠ” ???ŒëŸ¬ê·¸ì¸???¤ì¹˜?˜ê³  ?¶ì–´:
https://github.com/gabrielwithappy/obsidian-skills
```

?ëŠ” ??ê°„ë‹¨?˜ê²Œ:

```
???€?¥ì†Œë¥?.claude ?´ë”??plugin?¼ë¡œ ?¤ì¹˜?´ì¤˜:
https://github.com/gabrielwithappy/obsidian-skills
```

## 2. ?°ë??ì—??ì§ì ‘ ?¤í–‰

### Python ?¬ìš© (ê¶Œì¥)
```bash
cd d:\00_PRJ\agent-starter

# obsidian-skills ?¤ì¹˜
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'

# ì»¤ìŠ¤?€ ?´ë¦„?¼ë¡œ ?¤ì¹˜
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills", "plugin_name": "my-obsidian"}'
```

### Node.js ?¬ìš©
```bash
node .claude/skills/install_git_plugin/index.js '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'
```

## 3. ?¤ì¹˜???ŒëŸ¬ê·¸ì¸ ?•ì¸

```bash
# ?¤ì¹˜??ëª¨ë“  ?ŒëŸ¬ê·¸ì¸ ëª©ë¡ ì¡°íšŒ
python3 .claude/skills/list_plugins.py './.claude'
```

## 4. ?ŒëŸ¬ê·¸ì¸ ?œê±°

```bash
# ?ŒëŸ¬ê·¸ì¸ ?œê±°
python3 .claude/skills/remove_plugin.py '{"plugin_name": "obsidian-skills"}'
```

## 5. ?¬ëŸ¬ ?€?¥ì†Œ ?¤ì¹˜ ?ˆì‹œ

```bash
# obsidian-skills ?¤ì¹˜
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'

# ?¤ë¥¸ ?ŒëŸ¬ê·¸ì¸ ?¤ì¹˜
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/user/another-plugin"}'

# ?¤ì¹˜??ëª©ë¡ ?•ì¸
python3 .claude/skills/list_plugins.py './.claude'
```

## 6. VS Code ?µí•© ?Œí¬?Œë¡œ??

### ?¨ê³„ë³?ê°€?´ë“œ

1. **?„ë¡œ?íŠ¸ ë£¨íŠ¸ ?•ì¸**
   ```bash
   # .claude ?´ë”ê°€ d:\00_PRJ\agent-starter???„ì¹˜
   ls -la .claude/
   ```

2. **VS Code?ì„œ Claude Code ?•ì¥ ?¤ì¹˜**
   - Extensions?ì„œ "Claude Code" ?ëŠ” "Claude" ê²€??ë°??¤ì¹˜

3. **VS Code ?¬ì‹œ??*
   - ?´ì œ Claude Codeê°€ `.claude/skills` ?´ë”??skillsë¥??ë™?¼ë¡œ ?¸ì‹

4. **Claude?€ ?í˜¸?‘ìš©**
   ```
   ??GitHub ?€?¥ì†Œë¥??¤ì¹˜?´ì¤˜: https://github.com/gabrielwithappy/obsidian-skills
   ```

5. **?¤ì¹˜ ?•ì¸**
   - `.claude/plugins/obsidian-skills/` ?´ë”ê°€ ?ì„±?˜ë©´ ?±ê³µ

## 7. ?¤í‚¬ ë§¤ê°œë³€???µì…˜

### install_git_plugin ?¤í‚¬

```json
{
  "git_url": "https://github.com/gabrielwithappy/obsidian-skills",  // ?„ìˆ˜
  "plugin_name": "obsidian-skills",                                   // ? íƒ?¬í•­ (ê¸°ë³¸ê°? repo ?´ë¦„)
  "target_path": "./.claude"                                          // ? íƒ?¬í•­ (ê¸°ë³¸ê°? .claude)
}
```

## 8. ?‘ë‹µ ë©”ì‹œì§€ ?ˆì‹œ

### ?±ê³µ
```json
{
  "status": "success",
  "message": "?ŒëŸ¬ê·¸ì¸ 'obsidian-skills'??ê°€) ?±ê³µ?ìœ¼ë¡??¤ì¹˜?˜ì—ˆ?µë‹ˆ??",
  "plugin_path": "./.claude/plugins/obsidian-skills",
  "plugin_info": {
    "name": "obsidian-skills",
    "repository": "https://github.com/gabrielwithappy/obsidian-skills",
    "owner": "gabrielwithappy",
    "installed_at": "2026-01-23T20:31:00.000000",
    "status": "active"
  }
}
```

### ?¤íŒ¨
```json
{
  "status": "error",
  "message": "?ŒëŸ¬ê·¸ì¸ ?¤ì¹˜ ?¤íŒ¨: ?¤ë¥˜ ë©”ì‹œì§€",
  "plugin_path": null,
  "plugin_info": null
}
```

## 9. ì§€?ë˜???ŒëŸ¬ê·¸ì¸ ?•ì‹

??skill?€ ?¤ìŒê³?ê°™ì? Claude plugin ?•ì‹??ì§€?í•©?ˆë‹¤:

- **Standard Claude Plugin**
  - manifest.json (?ŒëŸ¬ê·¸ì¸ ë©”í??°ì´??
  - plugin.json (?¤ì •)
  - index.js / install_plugin.py (?¤í–‰ ?Œì¼)

- **Obsidian Skills Plugin**
  - .claude-plugin (?¤ì • ?Œì¼)
  - skills/ (?¤í‚¬ ëª¨ìŒ)
  - README.md (ë¬¸ì„œ)

## 10. ?¸ëŸ¬ë¸”ìŠˆ??

### Q: "ëª¨ë“ˆ??ì°¾ì„ ???†ìŒ" ?¤ë¥˜

**A:** Python???¤ì¹˜?˜ì–´ ?ˆëŠ”ì§€ ?•ì¸?˜ì„¸??
```bash
python3 --version
```

### Q: "repositoryë¥?ì°¾ì„ ???†ìŒ" ?¤ë¥˜

**A:** Git URL???¬ë°”ë¥¸ì? ?•ì¸?˜ì„¸??
```bash
# ?¬ë°”ë¥??•ì‹
https://github.com/owner/repo
https://github.com/owner/repo.git
```

### Q: VS Code?ì„œ skill??ë³´ì´ì§€ ?ŠìŒ

**A:** ?¤ìŒ???•ì¸?˜ì„¸??
1. `.claude` ?´ë”ê°€ ?„ë¡œ?íŠ¸ ë£¨íŠ¸???ˆëŠ”ì§€
2. `plugin.json` ?Œì¼??`.claude` ?´ë”???ˆëŠ”ì§€
3. VS Codeë¥??¤ì‹œ ?œì‘?ˆëŠ”ì§€

### Q: ê¶Œí•œ ê±°ë? ?¤ë¥˜

**A:** Python ?¤í¬ë¦½íŠ¸???¤í–‰ ê¶Œí•œ??ë¶€?¬í•˜?¸ìš”.
```bash
chmod +x .claude/skills/install_git_plugin/install_plugin.py
```

## 11. ê³ ê¸‰ ?¬ìš©ë²?

### ?˜ê²½ ë³€?˜ë¡œ ?¤ì •

```bash
# Windows PowerShell
$env:CLAUDE_PLUGINS_PATH = ".\.claude"

# Linux/macOS
export CLAUDE_PLUGINS_PATH="./.claude"
```

### ?¤í¬ë¦½íŠ¸ë¡??ë™ ?¤ì¹˜

```bash
# install_plugins.sh (Linux/macOS)
#!/bin/bash
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/user/another-plugin"}'
```

```powershell
# install_plugins.ps1 (Windows)
$plugins = @(
    "https://github.com/gabrielwithappy/obsidian-skills",
    "https://github.com/user/another-plugin"
)

foreach ($url in $plugins) {
    python3 .claude/skills/install_git_plugin/install_plugin.py "{`"git_url`": `"$url`"}"
}
```
