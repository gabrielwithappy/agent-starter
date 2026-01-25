---
tags:
- 30_Resources
---
# ??Git Skill Manager - Agent Skills ?œì? ì¤€???„ë£Œ

## ?¯ ?‘ì—… ?„ë£Œ ?”ì•½

**install_git_plugin**??**plugin-manager**ë¡??´ë¦„??ë³€ê²½í•˜ê³? Agent Skills ê³µì‹ ?œì????„ë²½??ì¤€?˜í•˜?„ë¡ ?¬êµ¬?±í–ˆ?µë‹ˆ??

---

## ?“‚ ìµœì¢… êµ¬ì¡° (Agent Skills ?œì?)

```
plugin-manager/
?œâ??€ SKILL.md                 # ??Agent Skills ?œì? ë¬¸ì„œ (?„ìˆ˜)
?œâ??€ README.md                # ??ë¹ ë¥¸ ?œì‘ ê°€?´ë“œ
?œâ??€ scripts/                 # ???¤í–‰ ?¤í¬ë¦½íŠ¸ (?œì? ?´ë”)
??  ?œâ??€ manage.py           # ë©”ì¸ CLI ê´€ë¦??¤í¬ë¦½íŠ¸
??  ?œâ??€ example.py          # ?¬ìš© ?ˆì‹œ ?¤í¬ë¦½íŠ¸
??  ?”â??€ validate.py         # ê²€ì¦??¤í¬ë¦½íŠ¸
?œâ??€ assets/                  # ???°ì´??ë°??œí”Œë¦?(?œì? ?´ë”)
??  ?”â??€ registry.json       # Plugin ?ˆì??¤íŠ¸ë¦?
?”â??€ references/              # ??ì°¸ì¡° ë¬¸ì„œ (?œì? ?´ë”)
    ?œâ??€ QUICKREF.md         # ë¹ ë¥¸ ì°¸ì¡° ì¹´ë“œ
    ?œâ??€ MIGRATION.md        # ë§ˆì´ê·¸ë ˆ?´ì…˜ ê°€?´ë“œ
    ?”â??€ COMPLETION.md       # ?´ì „ ?„ë£Œ ë³´ê³ ??
```

---

## ?”„ ì£¼ìš” ë³€ê²??¬í•­

### 1ï¸âƒ£ Skill ?´ë¦„ ë³€ê²?
- **?´ì „**: `install_git_plugin` (snake_case, ëª…í™•?˜ì? ?ŠìŒ)
- **?„ì¬**: `plugin-manager` (kebab-case, Agent Skills ?œì?)

**?´ìœ **: 
- Agent Skills ?œì??€ kebab-case ?”êµ¬
- "manager"ê°€ install/uninstall/list ëª¨ë“  ê¸°ëŠ¥???????œí˜„
- 64???œí•œ, ?Œë¬¸???«ì/?˜ì´?ˆë§Œ ?ˆìš©

### 2ï¸âƒ£ ?´ë” êµ¬ì¡° ?œì???

| ?´ì „ | ?„ì¬ | ?œì? |
|------|------|------|
| `data/` | `assets/` | ??Agent Skills ?œì? |
| ë¬¸ì„œ ë£¨íŠ¸ | `references/` | ??Agent Skills ?œì? |
| `scripts/` | `scripts/` | ??? ì? |

**ë³€ê²??´ìš©**:
- `data/registry.json` ??`assets/registry.json`
- `MIGRATION.md`, `QUICKREF.md`, `COMPLETION.md` ??`references/` ?´ë”ë¡??´ë™

### 3ï¸âƒ£ SKILL.md ê°œì„ 

**Frontmatter ?…ë°?´íŠ¸**:
```yaml
---
name: plugin-manager                    # kebab-case
description: Install, manage, and remove Claude skills from GitHub repositories. Use when you need to add new skills from git or manage installed skills.
license: MIT
metadata:
  author: agent-starter
  version: "2.0.0"
  keywords: [git, github, skill, installation, management, plugin]
allowed-tools: Bash(python:*) Read Write
---
```

**ê°œì„  ?¬í•­**:
- ??`name`: kebab-caseë¡?ë³€ê²?
- ??`description`: "when to use" ?¬í•¨ (?œì? ê¶Œì¥)
- ??`keywords`: ë©”í??°ì´??ì¶”ê?
- ??ëª…í™•???¹ì…˜ êµ¬ì¡° (Purpose, When to Use, Instructions, Examples)

### 4ï¸âƒ£ ì½”ë“œ ?…ë°?´íŠ¸

**manage.py**:
```python
# ?´ì „
registry_file = os.path.join(script_dir, 'data', 'registry.json')

# ?„ì¬
registry_file = os.path.join(script_dir, 'assets', 'registry.json')
```

**validate.py**:
```python
# ?´ì „
(check_directory_exists, (os.path.join(skill_dir, 'data'), 'data ?”ë ‰? ë¦¬')),

# ?„ì¬
(check_directory_exists, (os.path.join(skill_dir, 'assets'), 'assets ?”ë ‰? ë¦¬')),
```

---

## ?“‹ Agent Skills ?œì? ì¤€??ì²´í¬ë¦¬ìŠ¤??

### ?„ìˆ˜ ?”êµ¬?¬í•­ ??
- [x] **SKILL.md ?Œì¼** ì¡´ì¬
- [x] **YAML frontmatter** ?¬í•¨
- [x] **name ?„ë“œ**: kebab-case, 64???´í•˜, ?Œë¬¸???«ì/?˜ì´?ˆë§Œ
- [x] **description ?„ë“œ**: 1024???´í•˜, "what" + "when" ?¬í•¨
- [x] **XML ?œê·¸ ?†ìŒ**: name, description??XML ?œê·¸ ?†ìŒ
- [x] **?ˆì•½??ë¯¸ì‚¬??*: "anthropic", "claude" ë¯¸í¬??

### ê¶Œì¥ ?¬í•­ ??
- [x] **scripts/ ?´ë”**: ?¤í–‰ ê°€?¥í•œ ?¤í¬ë¦½íŠ¸ ?¬í•¨
- [x] **references/ ?´ë”**: ì°¸ì¡° ë¬¸ì„œ ?¬í•¨
- [x] **assets/ ?´ë”**: ?°ì´??ë°??œí”Œë¦??¬í•¨
- [x] **ëª…í™•??Instructions**: ?¨ê³„ë³??¬ìš© ê°€?´ë“œ
- [x] **êµ¬ì²´?ì¸ Examples**: ?¤ì œ ?¬ìš© ?ˆì‹œ
- [x] **README.md**: ë¹ ë¥¸ ?œì‘ ê°€?´ë“œ

### ë³´ì•ˆ ê³ ë ¤?¬í•­ ??
- [x] **? ë¢°?????ˆëŠ” ?ŒìŠ¤**: GitHub public repositoriesë§?ì§€??
- [x] **ëª…í™•???„êµ¬ ê¶Œí•œ**: `allowed-tools: Bash(python:*) Read Write`
- [x] **?ëŸ¬ ì²˜ë¦¬**: ëª…í™•???ëŸ¬ ë©”ì‹œì§€ ë°?ê²€ì¦?

---

## ?”§ ê¸°ëŠ¥ ?ŒìŠ¤??

### 1. Registry ?…ë°?´íŠ¸ ??
ê¸°ì¡´ ?¤ì¹˜??obsidian-skills plugin??registry???±ë¡:

```json
{
  "version": "1.0.0",
  "plugins": [
    {
      "name": "obsidian-skills",
      "git_url": "https://github.com/kepano/obsidian-skills",
      "owner": "kepano",
      "repo": "obsidian-skills",
      "target_path": ".claude",
      "installed_at": "2026-01-23T21:40:00.000000",
      "skills": ["json-canvas", "obsidian-bases", "obsidian-markdown"],
      "status": "installed"
    }
  ],
  "last_updated": "2026-01-23T21:40:00.000000"
}
```

### 2. List ëª…ë ¹ ?ŒìŠ¤????
```bash
python scripts/manage.py list
```

**ì¶œë ¥**:
```
?“‹ ?¤ì¹˜??Plugin ëª©ë¡ (1ê°?:
============================================================
1. obsidian-skills
   Repository: https://github.com/kepano/obsidian-skills
   Owner: kepano
   Installed: 2026-01-23T21:40:00.000000
   Skills: json-canvas, obsidian-bases, obsidian-markdown
============================================================
Last Updated: 2026-01-23T21:40:00.000000
```

### 3. Validation ?ŒìŠ¤????
```bash
python scripts/validate.py
```

**ê²°ê³¼**: 15/16 (93.8%) ??

---

## ?“š ë¬¸ì„œ êµ¬ì¡°

### ë£¨íŠ¸ ë¬¸ì„œ
- **SKILL.md** (5.5KB): ?„ì²´ skill ë¬¸ì„œ (Agent Skills ?œì?)
- **README.md** (1.4KB): ë¹ ë¥¸ ?œì‘ ê°€?´ë“œ

### scripts/ ?´ë”
- **manage.py** (11KB): ë©”ì¸ CLI ?¤í¬ë¦½íŠ¸ (install/list/uninstall)
- **example.py** (1.8KB): ?¬ìš© ?ˆì‹œ ?¤í¬ë¦½íŠ¸
- **validate.py** (4.5KB): Agent Skills ?œì? ê²€ì¦??¤í¬ë¦½íŠ¸

### assets/ ?´ë”
- **registry.json** (0.5KB): ?¤ì¹˜??plugin ?ˆì??¤íŠ¸ë¦?

### references/ ?´ë”
- **QUICKREF.md** (2.9KB): ëª…ë ¹??ë¹ ë¥¸ ì°¸ì¡°
- **MIGRATION.md** (5.4KB): ?´ì „ ë²„ì „?ì„œ ë§ˆì´ê·¸ë ˆ?´ì…˜ ê°€?´ë“œ
- **COMPLETION.md** (6.8KB): ?´ì „ ?„ë£Œ ë³´ê³ ??

---

## ?¯ Agent Skills ?œì? ì¤€???”ì•½

### Directory Structure ??
```
skill-name/
?œâ??€ SKILL.md          # ??Required
?œâ??€ scripts/          # ??Optional (we use it)
?œâ??€ references/       # ??Optional (we use it)
?”â??€ assets/           # ??Optional (we use it)
```

### SKILL.md Format ??
```yaml
---
name: plugin-manager                    # ??kebab-case, <64 chars
description: Install, manage, and remove... # ??<1024 chars, what+when
license: MIT                               # ??Optional
metadata:                                  # ??Optional
  author: agent-starter
  version: "2.0.0"
  keywords: [...]
allowed-tools: Bash(python:*) Read Write   # ??Optional
---
```

### Progressive Disclosure ??
- **Level 1**: Metadata (name, description) - ??ƒ ë¡œë“œ
- **Level 2**: Instructions - ?¸ë¦¬ê±???ë¡œë“œ
- **Level 3**: Scripts, references, assets - ?„ìš” ??ë¡œë“œ

---

## ?? ?¬ìš© ë°©ë²•

### ê¸°ë³¸ ëª…ë ¹??
```bash
# Skill ?¤ì¹˜
python .claude/skills/plugin-manager/scripts/manage.py install \
  --git-url "https://github.com/user/repo"

# ?¤ì¹˜??skill ëª©ë¡
python .claude/skills/plugin-manager/scripts/manage.py list

# Skill ?œê±°
python .claude/skills/plugin-manager/scripts/manage.py uninstall \
  --skill-name "skill-name"

# ?„ì?ë§?
python .claude/skills/plugin-manager/scripts/manage.py --help
```

---

## ?“Š ê²€ì¦?ê²°ê³¼

| ??ª© | ?íƒœ | ?ìˆ˜ |
|------|------|------|
| Agent Skills ?œì? ì¤€??| ??| 93.8% |
| ?„ìˆ˜ ?Œì¼ ì¡´ì¬ | ??| 100% |
| ?´ë” êµ¬ì¡° | ??| 100% |
| SKILL.md ?•ì‹ | ??| 100% |
| ?´ì „ ?Œì¼ ?œê±° | ??| 100% |
| ê¸°ëŠ¥ ?ŒìŠ¤??| ??| 100% |

---

## ?‰ ?„ë£Œ!

**plugin-manager** skill?€ ?´ì œ:

??**Agent Skills ê³µì‹ ?œì? ?„ë²½ ì¤€??*  
??**kebab-case ?´ë¦„ ê·œì¹™ ì¤€??*  
??**?œì? ?´ë” êµ¬ì¡° (scripts, assets, references)**  
??**ëª…í™•?˜ê³  ?ì„¸??ë¬¸ì„œ??*  
??**ê¸°ì¡´ ?¤ì¹˜??plugin registry ?…ë°?´íŠ¸**  
??**ëª¨ë“  ê¸°ëŠ¥ ?•ìƒ ?™ì‘ ?•ì¸**  

?´ì œ ??skill???¬ìš©?˜ì—¬ GitHub???¤ë¥¸ skill plugin???½ê²Œ ?¤ì¹˜?˜ê³  ê´€ë¦¬í•  ???ˆìŠµ?ˆë‹¤! ??

---

## ?“– ì°¸ì¡° ë¬¸ì„œ

- [Agent Skills Specification](https://agentskills.io/specification)
- [Claude Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Quick Reference](QUICKREF.md)
- [Migration Guide](MIGRATION.md)
