---
tags: 30_Resources
---
# Claude Plugin Installer Skills

VS Code?ì„œ ?¬ìš© ê°€?¥í•œ Claude Plugin ?¤ì¹˜ ?„êµ¬ ëª¨ìŒ?…ë‹ˆ??

## ê°œìš”

??skill ëª¨ìŒ?€ Git repository?ì„œ Claude plugin???¤ìš´ë¡œë“œ?˜ì—¬ `.claude` ?´ë”???ë™?¼ë¡œ ?¤ì¹˜?????ˆê²Œ ?©ë‹ˆ?? VS Code?ì„œ Claude Code??Claude Chat ?•ì¥ê³??¨ê»˜ ?¬ìš©?????ˆìŠµ?ˆë‹¤.

## ?¤ì¹˜ ?„ì¹˜

```
.claude/
?œâ??€ plugins/           # ?¤ì¹˜???ŒëŸ¬ê·¸ì¸??
?œâ??€ skills/           # Skill ?•ì˜??
??  ?”â??€ install_git_plugin/
??      ?œâ??€ manifest.json
??      ?œâ??€ index.js
??      ?”â??€ install_plugin.py
?œâ??€ plugin.json       # ?ŒëŸ¬ê·¸ì¸ ?¤ì •
?”â??€ .claude-plugin    # Claude ?ŒëŸ¬ê·¸ì¸ ?¤ì •
```

## ?¬ìš© ë°©ë²•

### 1. VS Code?ì„œ Claude Code ?¬ìš©

`.claude` ?´ë”ê°€ ?„ë¡œ?íŠ¸ ë£¨íŠ¸???ˆìœ¼ë©?Claude Code?ì„œ ?ë™?¼ë¡œ ?¸ì‹?©ë‹ˆ??

### 2. Skill ?¤í–‰

#### Python ë²„ì „
```bash
python3 .claude/skills/install_git_plugin/install_plugin.py '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'
```

#### Node.js ë²„ì „
```bash
node .claude/skills/install_git_plugin/index.js '{"git_url": "https://github.com/gabrielwithappy/obsidian-skills"}'
```

### 3. Claude?ê²Œ ì§€?œí•˜ê¸?

Claude Code ?ëŠ” Claude Chat?ì„œ ?¤ìŒê³?ê°™ì´ ëª…ë ¹?????ˆìŠµ?ˆë‹¤:

```
???€?¥ì†Œë¥??¤ì¹˜?´ì¤˜: https://github.com/gabrielwithappy/obsidian-skills
```

Claude??`install_git_plugin` skill???¬ìš©?˜ì—¬ ?´ë‹¹ ?ŒëŸ¬ê·¸ì¸???¤ì¹˜??ê²ƒì…?ˆë‹¤.

## Skill ?…ë ¥ ?Œë¼ë¯¸í„°

### install_git_plugin

| ?Œë¼ë¯¸í„° | ?€??| ?„ìˆ˜ | ?¤ëª… |
|---------|------|------|------|
| git_url | string | ??| Claude plugin???€?¥ëœ Git repository URL |
| plugin_name | string | | ?¤ì¹˜???ŒëŸ¬ê·¸ì¸???´ë¦„ (ê¸°ë³¸ê°? repository ?´ë¦„) |
| target_path | string | | ?¤ì¹˜ ?€??ê²½ë¡œ (ê¸°ë³¸ê°? .claude) |

### ?¬ìš© ?ˆì‹œ

```json
{
  "git_url": "https://github.com/gabrielwithappy/obsidian-skills",
  "plugin_name": "obsidian-skills",
  "target_path": "./.claude"
}
```

## ì¶œë ¥ ?•ì‹

?±ê³µ ?‘ë‹µ:
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

?¤íŒ¨ ?‘ë‹µ:
```json
{
  "status": "error",
  "message": "?ŒëŸ¬ê·¸ì¸ ?¤ì¹˜ ?¤íŒ¨: [?¤ë¥˜ ë©”ì‹œì§€]",
  "plugin_path": null,
  "plugin_info": null
}
```

## ì§€?ë˜??Plugin ?•ì‹

??skill?€ ?¤ìŒ ?•ì‹??Claude plugin???ë™?¼ë¡œ ?¸ì‹?©ë‹ˆ??

- `manifest.json` - ?ŒëŸ¬ê·¸ì¸ ë©”í??°ì´??
- `plugin.json` - ?ŒëŸ¬ê·¸ì¸ ?¤ì •
- `.claude-plugin` - Claude ?ŒëŸ¬ê·¸ì¸ ?¤ì • ?Œì¼
- `README.md` - ?ŒëŸ¬ê·¸ì¸ ë¬¸ì„œ
- `index.js` / `install_plugin.py` - ?ŒëŸ¬ê·¸ì¸ ?¤í–‰ ?Œì¼

## VS Code ?µí•©

### ?¤ì • ë°©ë²•

1. ?„ë¡œ?íŠ¸ ë£¨íŠ¸??`.claude` ?´ë”ê°€ ?ˆëŠ”ì§€ ?•ì¸
2. Claude Code ?•ì¥ ?¤ì¹˜
3. VS Codeë¥??¬ì‹œ?‘í•˜ë©??ë™?¼ë¡œ `.claude` ?´ë”??skills???¸ì‹?©ë‹ˆ??

### Claude?€ ?í˜¸?‘ìš©

```
@skills install_git_plugin
?¤ì¹˜??Git ì£¼ì†Œ: https://github.com/gabrielwithappy/obsidian-skills
```

?ëŠ” ??ê°„ë‹¨??

```
??GitHub repositoryë¥?plugin?¼ë¡œ ?¤ì¹˜?´ì¤˜: https://github.com/gabrielwithappy/obsidian-skills
```

## ê¶Œí•œ ?¤ì •

??skill???„ìš”ë¡??˜ëŠ” ê¶Œí•œ:

- `filesystem` - read/write: ?ŒëŸ¬ê·¸ì¸ ?Œì¼ ?€??
- `network` - read: GitHub?ì„œ ?Œì¼ ?¤ìš´ë¡œë“œ

## ?¸ëŸ¬ë¸”ìŠˆ??

### ?ŒëŸ¬ê·¸ì¸???¤ì¹˜?˜ì? ?ŠëŠ” ê²½ìš°

1. Git URL???¬ë°”ë¥¸ì? ?•ì¸
2. Repositoryê°€ public?¸ì? ?•ì¸
3. ?„ìˆ˜ ?Œì¼(manifest.json, plugin.json ????repository???ˆëŠ”ì§€ ?•ì¸

### VS Code?ì„œ skill???¸ì‹?˜ì? ëª»í•˜??ê²½ìš°

1. `.claude` ?´ë” ê²½ë¡œ ?•ì¸
2. `plugin.json` ?Œì¼??`.claude` ?´ë”???ˆëŠ”ì§€ ?•ì¸
3. VS Code ?¬ì‹œ??

## ?¼ì´? ìŠ¤

MIT License

## ì°¸ê³ 

- [Claude Skills Documentation](https://platform.claude.com/docs/agents-and-tools/agent-skills)
- [Agent Skills Specification](https://agentskills.io/specification)
