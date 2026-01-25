---
tags:
- 30_Resources
---
# Git Skill Manager - ìµœì¢… ?„ë£Œ ?”ì•½

## ???‘ì—… ?„ë£Œ

**install_git_plugin** skill??**Agent Skills ê³µì‹ ?œì?**???„ë²½??ì¤€?˜í•˜?„ë¡ ?¬êµ¬?±í–ˆ?µë‹ˆ??

---

## ?”„ ì£¼ìš” ë³€ê²½ì‚¬??

### 1. Skill ?´ë¦„ ë³€ê²?
- **?´ì „**: `install_git_plugin` (snake_case)
- **?„ì¬**: `plugin-manager` (kebab-case) ??

### 2. ?´ë” êµ¬ì¡° ?œì???
- `data/` ??`assets/` ??
- ì°¸ì¡° ë¬¸ì„œ ??`references/` ??
- `scripts/` ? ì? ??

### 3. ?Œì¼ ?´ë™
- `data/registry.json` ??`assets/registry.json`
- `MIGRATION.md` ??`references/MIGRATION.md`
- `QUICKREF.md` ??`references/QUICKREF.md`
- `COMPLETION.md` ??`references/COMPLETION.md`

### 4. SKILL.md ?…ë°?´íŠ¸
- `name`: `plugin-manager` (kebab-case)
- `description`: "what" + "when to use" ?¬í•¨
- `keywords`: ë©”í??°ì´??ì¶”ê?
- ëª¨ë“  ê²½ë¡œ ?…ë°?´íŠ¸

### 5. Registry ?…ë°?´íŠ¸
- ê¸°ì¡´ ?¤ì¹˜??`obsidian-skills` plugin ?±ë¡ ??
- 3ê°?skills: json-canvas, obsidian-bases, obsidian-markdown

---

## ?“‚ ìµœì¢… êµ¬ì¡°

```
plugin-manager/
?œâ??€ SKILL.md                      # Agent Skills ?œì? ë¬¸ì„œ
?œâ??€ README.md                     # ë¹ ë¥¸ ?œì‘ ê°€?´ë“œ
?œâ??€ scripts/                      # ?¤í–‰ ?¤í¬ë¦½íŠ¸
??  ?œâ??€ manage.py                # ë©”ì¸ CLI ?¤í¬ë¦½íŠ¸
??  ?œâ??€ example.py               # ?¬ìš© ?ˆì‹œ
??  ?”â??€ validate.py              # ê²€ì¦??¤í¬ë¦½íŠ¸
?œâ??€ assets/                       # ?°ì´??ë°??œí”Œë¦?
??  ?”â??€ registry.json            # Plugin ?ˆì??¤íŠ¸ë¦?
?”â??€ references/                   # ì°¸ì¡° ë¬¸ì„œ
    ?œâ??€ QUICKREF.md              # ë¹ ë¥¸ ì°¸ì¡°
    ?œâ??€ MIGRATION.md             # ë§ˆì´ê·¸ë ˆ?´ì…˜ ê°€?´ë“œ
    ?œâ??€ COMPLETION.md            # ?´ì „ ?„ë£Œ ë³´ê³ ??
    ?”â??€ FINAL_COMPLETION.md      # ìµœì¢… ?„ë£Œ ë³´ê³ ??
```

---

## ?¯ Agent Skills ?œì? ì¤€??

### ???„ìˆ˜ ?”êµ¬?¬í•­
- [x] SKILL.md ?Œì¼ ì¡´ì¬
- [x] YAML frontmatter ?¬í•¨
- [x] name: kebab-case, 64???´í•˜
- [x] description: 1024???´í•˜, what+when ?¬í•¨
- [x] XML ?œê·¸ ?†ìŒ
- [x] ?ˆì•½??ë¯¸ì‚¬??

### ??ê¶Œì¥ ?¬í•­
- [x] scripts/ ?´ë” ?¬ìš©
- [x] references/ ?´ë” ?¬ìš©
- [x] assets/ ?´ë” ?¬ìš©
- [x] ëª…í™•??Instructions
- [x] êµ¬ì²´?ì¸ Examples
- [x] README.md ?¬í•¨

### ??ê²€ì¦?ê²°ê³¼
- **?ìˆ˜**: 15/16 (93.8%)
- **?íƒœ**: ??ì¢‹ìŠµ?ˆë‹¤! ?€ë¶€ë¶„ì˜ ?”êµ¬?¬í•­??ì¶©ì¡±?©ë‹ˆ??

---

## ?? ?¬ìš© ë°©ë²•

```bash
# Skill ?¤ì¹˜
python .claude/skills/plugin-manager/scripts/manage.py install \
  --git-url "https://github.com/user/repo"

# ëª©ë¡ ì¡°íšŒ
python .claude/skills/plugin-manager/scripts/manage.py list

# Skill ?œê±°
python .claude/skills/plugin-manager/scripts/manage.py uninstall \
  --skill-name "skill-name"
```

---

## ?“Š ?„ì¬ ?íƒœ

### ?¤ì¹˜??Plugin
- **obsidian-skills** (kepano/obsidian-skills)
  - json-canvas
  - obsidian-bases
  - obsidian-markdown

### Registry ?„ì¹˜
- `d:\00_PRJ\agent-starter\.claude\skills\plugin-manager\assets\registry.json`

---

## ?“š ë¬¸ì„œ

- **SKILL.md**: ?„ì²´ skill ë¬¸ì„œ
- **README.md**: ë¹ ë¥¸ ?œì‘
- **references/QUICKREF.md**: ëª…ë ¹??ì°¸ì¡°
- **references/MIGRATION.md**: ë§ˆì´ê·¸ë ˆ?´ì…˜ ê°€?´ë“œ
- **references/FINAL_COMPLETION.md**: ?ì„¸ ?„ë£Œ ë³´ê³ ??

---

## ?‰ ?„ë£Œ!

**plugin-manager** skill?€ ?´ì œ Agent Skills ê³µì‹ ?œì????„ë²½??ì¤€?˜í•©?ˆë‹¤! ??

---

**ì°¸ì¡°**:
- [Agent Skills Specification](https://agentskills.io/specification)
- [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
