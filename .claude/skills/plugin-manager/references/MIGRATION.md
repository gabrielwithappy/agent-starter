---
tags: 30_Resources
---
# Install Git Plugin ë§ˆì´ê·¸ë ˆ?´ì…˜ ?„ë£Œ

## ë³€ê²??¬í•­ ?”ì•½

`install_git_plugin`??Claude plugin ?•íƒœ?ì„œ Agent Skills ?œì? skill ?•íƒœë¡??±ê³µ?ìœ¼ë¡?ë³€?˜í–ˆ?µë‹ˆ??

## ?´ì „ êµ¬ì¡° (Plugin ?•íƒœ)

```
install_git_plugin/
?œâ??€ .claude-plugin          # ??Plugin ?¤ì • (?? œ??
?œâ??€ plugin.json             # ??Plugin ë©”í??°ì´??(?? œ??
?œâ??€ manifest.json           # ??Plugin manifest (?? œ??
?œâ??€ index.js                # ??Node.js ?¤í–‰ ?Œì¼ (?? œ??
?œâ??€ install_plugin.py       # ??ê°œë³„ ?¤ì¹˜ ?¤í¬ë¦½íŠ¸ (?µí•©??
?œâ??€ list_plugins.py         # ??ê°œë³„ ëª©ë¡ ?¤í¬ë¦½íŠ¸ (?µí•©??
?œâ??€ remove_plugin.py        # ??ê°œë³„ ?œê±° ?¤í¬ë¦½íŠ¸ (?µí•©??
?”â??€ data/
    ?”â??€ (empty)
```

## ?ˆë¡œ??êµ¬ì¡° (Skill ?•íƒœ)

```
install_git_plugin/
?œâ??€ SKILL.md                # ??Agent Skills ?œì? ë¬¸ì„œ
?œâ??€ README.md               # ???¬ìš©??ê°€?´ë“œ
?œâ??€ scripts/                # ???¤í–‰ ?¤í¬ë¦½íŠ¸ ?´ë”
??  ?”â??€ manage.py          # ???µí•© CLI ?¤í¬ë¦½íŠ¸
?”â??€ data/                   # ???°ì´???€?¥ì†Œ
    ?”â??€ registry.json      # ??Plugin ?ˆì??¤íŠ¸ë¦?
```

## ì£¼ìš” ê°œì„  ?¬í•­

### 1. Agent Skills ?œì? ì¤€????
- YAML frontmatterê°€ ?¬í•¨??`SKILL.md` ?ì„±
- `scripts/` ?´ë”???¤í–‰ ?Œì¼ ë°°ì¹˜
- ?œì? skill êµ¬ì¡° ?°ë¦„

### 2. ê¸°ëŠ¥ ?µí•© ??
?´ì „?ëŠ” 3ê°œì˜ ë³„ë„ Python ?Œì¼:
- `install_plugin.py`
- `list_plugins.py`
- `remove_plugin.py`

?„ì¬??1ê°œì˜ ?µí•© ?¤í¬ë¦½íŠ¸:
- `scripts/manage.py` (ëª¨ë“  ê¸°ëŠ¥ ?¬í•¨)

### 3. ê°œì„ ??CLI ?¸í„°?˜ì´????
```bash
# ?´ì „ ë°©ì‹ (JSON ?Œë¼ë¯¸í„°)
python install_plugin.py '{"action":"install","git_url":"..."}'

# ?ˆë¡œ??ë°©ì‹ (?œì? CLI)
python scripts/manage.py install --git-url "..."
python scripts/manage.py list
python scripts/manage.py uninstall --skill-name "..."
```

### 4. ???˜ì? ?¬ìš©???¼ë“œë°???
- ?´ëª¨ì§€ë¥??¬ìš©???œê°???¼ë“œë°?(?“¦, ?? ?? ?—‘ï¸? ?“‹)
- ì§„í–‰ ?í™© ë©”ì‹œì§€
- ëª…í™•???ëŸ¬ ë©”ì‹œì§€
- ?ì„¸???¤ì¹˜/?œê±° ?•ë³´

### 5. ?¥ìƒ??ë¬¸ì„œ????
- ?ì„¸??`SKILL.md` (?¬ìš©ë²? ?ˆì‹œ, ?ëŸ¬ ì²˜ë¦¬)
- ê°„ë‹¨??`README.md` (ë¹ ë¥¸ ?œì‘ ê°€?´ë“œ)
- ?¸ë¼??ì½”ë“œ ì£¼ì„

## ?¬ìš© ?ˆì‹œ

### Plugin ?¤ì¹˜
```bash
cd d:\00_PRJ\agent-starter
python .claude/skills/install_git_plugin/scripts/manage.py install --git-url "https://github.com/kepano/obsidian-skills"
```

ì¶œë ¥:
```
?“¦ 'obsidian-skills' ?¤ìš´ë¡œë“œ ì¤?..
???ŒëŸ¬ê·¸ì¸ 'obsidian-skills'??ê°€) ?±ê³µ?ìœ¼ë¡??¤ì¹˜?˜ì—ˆ?µë‹ˆ??
??3ê°œì˜ skill???¤ì¹˜?˜ì—ˆ?µë‹ˆ??
  - .claude/skills/json-canvas
  - .claude/skills/obsidian-bases
  - .claude/skills/obsidian-markdown
```

### ?¤ì¹˜??Plugin ëª©ë¡
```bash
python .claude/skills/install_git_plugin/scripts/manage.py list
```

ì¶œë ¥:
```
?“‹ ?¤ì¹˜??Plugin ëª©ë¡ (1ê°?:
============================================================
1. obsidian-skills
   Repository: https://github.com/kepano/obsidian-skills
   Owner: kepano
   Installed: 2026-01-23T21:00:00
   Skills: json-canvas, obsidian-bases, obsidian-markdown
============================================================
Last Updated: 2026-01-23T21:00:00
```

### Plugin ?œê±°
```bash
python .claude/skills/install_git_plugin/scripts/manage.py uninstall --skill-name "json-canvas"
```

ì¶œë ¥:
```
?—‘ï¸? 'json-canvas' ?œê±° ì¤?..
???¤í‚¬ 'json-canvas'??ê°€) ?±ê³µ?ìœ¼ë¡??œê±°?˜ì—ˆ?µë‹ˆ??
??5ê°œì˜ ?Œì¼???? œ?˜ì—ˆ?µë‹ˆ??
```

## ?¸í™˜??

### ? ì??˜ëŠ” ê¸°ëŠ¥ ??
- Git repository?ì„œ skill plugin ?¤ìš´ë¡œë“œ
- `.claude/skills` ?´ë”???ë™ ?¤ì¹˜
- Registry ê¸°ë°˜ plugin ì¶”ì 
- Plugin ?œê±° ê¸°ëŠ¥
- ëª¨ë“  ?µì‹¬ ê¸°ëŠ¥ ?™ì¼

### ë³€ê²½ëœ ?¸í„°?˜ì´??? ï¸
- JSON ?Œë¼ë¯¸í„° ??CLI arguments
- ?¬ëŸ¬ ?¤í¬ë¦½íŠ¸ ???¨ì¼ ?¤í¬ë¦½íŠ¸
- Plugin ?•íƒœ ??Skill ?•íƒœ

## Registry ?•ì‹

`data/registry.json` êµ¬ì¡°???™ì¼?˜ê²Œ ? ì??©ë‹ˆ??

```json
{
  "version": "1.0.0",
  "plugins": [
    {
      "name": "plugin-name",
      "git_url": "https://github.com/user/repo",
      "owner": "user",
      "repo": "repo",
      "target_path": ".claude",
      "installed_at": "2026-01-23T21:00:00.000000",
      "skills": ["skill1", "skill2"],
      "status": "installed"
    }
  ],
  "last_updated": "2026-01-23T21:00:00.000000"
}
```

## ?ŒìŠ¤???„ë£Œ ??

- [x] SKILL.md ?ì„± (Agent Skills ?œì?)
- [x] scripts/manage.py ?µí•© ?¤í¬ë¦½íŠ¸ ?‘ì„±
- [x] CLI --help ?™ì‘ ?•ì¸
- [x] list ëª…ë ¹ ?™ì‘ ?•ì¸
- [x] ?´ì „ plugin ?Œì¼???œê±°
- [x] data/registry.json ì´ˆê¸°??
- [x] README.md ?‘ì„±
- [x] ?”ë ‰? ë¦¬ êµ¬ì¡° ê²€ì¦?

## ?¤ìŒ ?¨ê³„

?´ì œ ??skill???¬ìš©?˜ì—¬ ?¤ë¥¸ GitHub repository??skill plugin???¤ì¹˜?????ˆìŠµ?ˆë‹¤:

```bash
# ?ˆì‹œ: ?¤ë¥¸ skill plugin ?¤ì¹˜
python .claude/skills/install_git_plugin/scripts/manage.py install \
  --git-url "https://github.com/your-org/your-skill-plugin"
```

## ë§ˆì´ê·¸ë ˆ?´ì…˜ ?„ë£Œ! ?‰

`install_git_plugin`?€ ?´ì œ Agent Skills ?œì????„ì „??ì¤€?˜í•˜??skill?…ë‹ˆ??
