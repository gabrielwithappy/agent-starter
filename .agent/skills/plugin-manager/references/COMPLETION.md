---
tags:
- 30_Resources
---
# ??Install Git Plugin Skill - ?„ë£Œ ë³´ê³ ??

## ?¯ ?‘ì—… ?„ë£Œ

**install_git_plugin**??Claude plugin ?•íƒœ?ì„œ **Agent Skills ?œì?**??ì¤€?˜í•˜??skillë¡??±ê³µ?ìœ¼ë¡?ë³€?˜í–ˆ?µë‹ˆ??

---

## ?“‚ ìµœì¢… êµ¬ì¡°

```
install_git_plugin/
?œâ??€ SKILL.md              # Agent Skills ?œì? ë¬¸ì„œ (?„ìˆ˜)
?œâ??€ README.md             # ?¬ìš©??ë¹ ë¥¸ ?œì‘ ê°€?´ë“œ
?œâ??€ QUICKREF.md           # ë¹ ë¥¸ ì°¸ì¡° ì¹´ë“œ
?œâ??€ MIGRATION.md          # ë§ˆì´ê·¸ë ˆ?´ì…˜ ?ì„¸ ë¬¸ì„œ
?œâ??€ data/                 # ?°ì´???€?¥ì†Œ
??  ?”â??€ registry.json    # Plugin ?ˆì??¤íŠ¸ë¦?(?¤ì¹˜ ì¶”ì )
?”â??€ scripts/              # ?¤í–‰ ?¤í¬ë¦½íŠ¸ ?´ë”
    ?œâ??€ manage.py        # ë©”ì¸ CLI ê´€ë¦??¤í¬ë¦½íŠ¸
    ?”â??€ example.py       # ?¬ìš© ?ˆì‹œ ?¤í¬ë¦½íŠ¸
```

---

## ??ì£¼ìš” ë³€ê²??¬í•­

### 1ï¸âƒ£ Agent Skills ?œì? ì¤€??
- ??**SKILL.md** ?ì„± (YAML frontmatter ?¬í•¨)
- ??**scripts/** ?´ë”ë¡??¤í–‰ ?Œì¼ ?´ë™
- ???œì? skill ?”ë ‰? ë¦¬ êµ¬ì¡° ?ìš©
- ??`allowed-tools` ë©”í??°ì´???•ì˜

### 2ï¸âƒ£ ê¸°ëŠ¥ ?µí•© ë°?ê°œì„ 
**?´ì „ (ë¶„ì‚°??êµ¬ì¡°):**
- ??`install_plugin.py` - ?¤ì¹˜ë§?
- ??`list_plugins.py` - ëª©ë¡ë§?
- ??`remove_plugin.py` - ?œê±°ë§?
- ??`index.js` - Node.js ë²„ì „
- ??`manifest.json`, `plugin.json` - Plugin ë©”í??°ì´??

**?„ì¬ (?µí•©??êµ¬ì¡°):**
- ??`scripts/manage.py` - ëª¨ë“  ê¸°ëŠ¥ ?µí•© (install/list/uninstall)
- ??`scripts/example.py` - ?¬ìš© ?ˆì‹œ
- ??`SKILL.md` - ?œì? ë¬¸ì„œ

### 3ï¸âƒ£ ?¬ìš©??ê²½í—˜ ê°œì„ 

**?´ì „ ?¸í„°?˜ì´??(ë³µì¡):**
```bash
python install_plugin.py '{"action":"install","git_url":"https://..."}'
```

**?ˆë¡œ???¸í„°?˜ì´??(ì§ê???:**
```bash
python scripts/manage.py install --git-url "https://..."
python scripts/manage.py list
python scripts/manage.py uninstall --skill-name "name"
```

**ê°œì„ ???¼ë“œë°?**
- ?“¦ ?¤ìš´ë¡œë“œ ì§„í–‰ ?í™©
- ???±ê³µ ë©”ì‹œì§€ (?´ëª¨ì§€ ?¬í•¨)
- ??ëª…í™•???ëŸ¬ ë©”ì‹œì§€
- ?—‘ï¸??œê±° ì§„í–‰ ?í™©
- ?“‹ ê¹”ë”??ëª©ë¡ ?œì‹œ

---

## ?”§ ?µì‹¬ ê¸°ëŠ¥

### 1. Plugin ?¤ì¹˜
```bash
python scripts/manage.py install --git-url "https://github.com/user/repo"
```
- GitHub repository?ì„œ ?ë™ ?¤ìš´ë¡œë“œ
- `.claude/skills/` ?´ë”???¤ì¹˜
- Registry???ë™ ?±ë¡
- ?¤ì¹˜??skill ëª©ë¡ ì¶œë ¥

### 2. Plugin ëª©ë¡ ì¡°íšŒ
```bash
python scripts/manage.py list
```
- ?¤ì¹˜??ëª¨ë“  plugin ?œì‹œ
- Repository URL, owner, ?¤ì¹˜ ?œê°„
- ?¬í•¨??skills ëª©ë¡
- Registry ë§ˆì?ë§??…ë°?´íŠ¸ ?œê°„

### 3. Plugin ?œê±°
```bash
python scripts/manage.py uninstall --skill-name "skill-name"
```
- Skill ?”ë ‰? ë¦¬ ?„ì „ ?? œ
- Registry?ì„œ ?ë™ ?œê±°
- ?? œ???Œì¼ ê°œìˆ˜ ?œì‹œ

---

## ?“š ë¬¸ì„œ??

### SKILL.md (5.2KB)
- **Purpose**: Skill??ëª©ì ê³?ê¸°ëŠ¥ ?¤ëª…
- **Usage**: ??ê°€ì§€ ëª…ë ¹ (install/list/uninstall) ?ì„¸ ?¤ëª…
- **Instructions**: ?¨ê³„ë³??¬ìš© ê°€?´ë“œ
- **Parameters**: ëª¨ë“  ë§¤ê°œë³€???¤ëª…
- **Examples**: ?¤ì œ ?¬ìš© ?ˆì‹œ
- **Registry Management**: ?ˆì??¤íŠ¸ë¦?êµ¬ì¡° ?¤ëª…
- **Error Handling**: ?ëŸ¬ ì²˜ë¦¬ ë°©ë²•

### README.md (1.4KB)
- Quick Start ê°€?´ë“œ
- ì£¼ìš” ê¸°ëŠ¥ ?”ì•½
- ë¹ ë¥¸ ëª…ë ¹ ì°¸ì¡°
- ?”êµ¬?¬í•­ ë°?êµ¬ì¡°

### QUICKREF.md (2.9KB)
- ëª…ë ¹??ë¹ ë¥¸ ì°¸ì¡° ì¹´ë“œ
- ?µì…˜ ?¤ëª…
- Tips & Tricks
- ë¬¸ì œ ?´ê²° ê°€?´ë“œ

### MIGRATION.md (5.4KB)
- ?´ì „ vs ?ˆë¡œ??êµ¬ì¡° ë¹„êµ
- ë³€ê²??¬í•­ ?ì„¸ ?¤ëª…
- ?¸í™˜???•ë³´
- ?ŒìŠ¤??ì²´í¬ë¦¬ìŠ¤??

---

## ?§ª ?ŒìŠ¤???„ë£Œ

| ??ª© | ?íƒœ | ?¤ëª… |
|------|------|------|
| SKILL.md ?ì„± | ??| Agent Skills ?œì? ì¤€??|
| scripts/ ?´ë” | ??| ëª¨ë“  ?¤í¬ë¦½íŠ¸ ?´ë™ |
| manage.py ?µí•© | ??| install/list/uninstall ?µí•© |
| CLI --help | ??| ?„ì?ë§??•ìƒ ?™ì‘ |
| list ëª…ë ¹ | ??| ëª©ë¡ ì¡°íšŒ ?•ìƒ ?™ì‘ |
| example.py | ??| ?ˆì‹œ ?¤í¬ë¦½íŠ¸ ?¤í–‰ |
| registry.json | ??| ?ˆì??¤íŠ¸ë¦?ì´ˆê¸°??|
| ?´ì „ ?Œì¼ ?? œ | ??| plugin.json, index.js ???œê±° |
| ë¬¸ì„œ??| ??| 4ê°?ë¬¸ì„œ ?‘ì„± ?„ë£Œ |

---

## ?? ?¬ìš© ë°©ë²•

### ?„ë¡œ?íŠ¸ ë£¨íŠ¸?ì„œ:
```bash
# Plugin ?¤ì¹˜
python .claude/skills/install_git_plugin/scripts/manage.py install \
  --git-url "https://github.com/kepano/obsidian-skills"

# ëª©ë¡ ì¡°íšŒ
python .claude/skills/install_git_plugin/scripts/manage.py list

# Skill ?œê±°
python .claude/skills/install_git_plugin/scripts/manage.py uninstall \
  --skill-name "json-canvas"
```

### Skill ?´ë”?ì„œ:
```bash
cd .claude/skills/install_git_plugin

# Plugin ?¤ì¹˜
python scripts/manage.py install --git-url "https://github.com/user/repo"

# ëª©ë¡ ì¡°íšŒ
python scripts/manage.py list

# ?„ì?ë§?
python scripts/manage.py --help
```

---

## ?’¡ ì£¼ìš” ?´ì 

1. **?œì? ì¤€??*: Agent Skills ?œì????„ë²½???°ë¦„
2. **ê°„ë‹¨??CLI**: ì§ê??ì¸ ëª…ë ¹ì¤??¸í„°?˜ì´??
3. **?µí•© ê´€ë¦?*: ?˜ë‚˜???¤í¬ë¦½íŠ¸ë¡?ëª¨ë“  ?‘ì—…
4. **?ë???ë¬¸ì„œ**: 4ê°€ì§€ ë¬¸ì„œë¡??¤ì–‘???¬ìš© ?œë‚˜ë¦¬ì˜¤ ì§€??
5. **?œê°???¼ë“œë°?*: ?´ëª¨ì§€?€ ëª…í™•??ë©”ì‹œì§€
6. **?ëŸ¬ ì²˜ë¦¬**: ëª…í™•???ëŸ¬ ë©”ì‹œì§€?€ ?´ê²° ê°€?´ë“œ
7. **?•ì¥ ê°€??*: ?½ê²Œ ?ˆë¡œ??ê¸°ëŠ¥ ì¶”ê? ê°€??

---

## ?“‹ ì²´í¬ë¦¬ìŠ¤??

- [x] Agent Skills ?œì? SKILL.md ?‘ì„±
- [x] scripts/ ?´ë”???¤í¬ë¦½íŠ¸ ë°°ì¹˜
- [x] ëª¨ë“  ê¸°ëŠ¥??manage.pyë¡??µí•©
- [x] CLI ?¸í„°?˜ì´??êµ¬í˜„ (argparse)
- [x] ?¬ìš©??ì¹œí™”??ì¶œë ¥ ë©”ì‹œì§€
- [x] ?´ì „ plugin ?Œì¼???œê±°
- [x] Registry ?œìŠ¤??? ì?
- [x] ?¬ê´„?ì¸ ë¬¸ì„œ ?‘ì„± (4ê°?ë¬¸ì„œ)
- [x] ?ˆì‹œ ?¤í¬ë¦½íŠ¸ ?‘ì„±
- [x] ë¹ ë¥¸ ì°¸ì¡° ì¹´ë“œ ?‘ì„±
- [x] ë§ˆì´ê·¸ë ˆ?´ì…˜ ë¬¸ì„œ ?‘ì„±
- [x] ?ŒìŠ¤??ë°?ê²€ì¦?

---

## ?‰ ê²°ë¡ 

**install_git_plugin** skill?€ ?´ì œ ?¤ìŒê³?ê°™ìŠµ?ˆë‹¤:

??Agent Skills ?œì? ?„ë²½ ì¤€?? 
??ì§ê??ì´ê³??¬ìš©?˜ê¸° ?¬ìš´ CLI  
???µí•©?˜ê³  ? ì?ë³´ìˆ˜?˜ê¸° ?¬ìš´ ì½”ë“œ  
???¬ê´„?ì´ê³?ëª…í™•??ë¬¸ì„œ?? 
??GitHub?ì„œ skill plugin???½ê²Œ ?¤ì¹˜/ê´€ë¦? 

?´ì œ ??skill???¬ìš©?˜ì—¬ ?¤ë¥¸ GitHub repository??skill plugin???ì‰½ê²??¤ì¹˜?˜ê³  ê´€ë¦¬í•  ???ˆìŠµ?ˆë‹¤! ??

---

**ë¬¸ì„œ ì°¸ì¡°:**
- [SKILL.md](SKILL.md) - ?„ì²´ ë¬¸ì„œ
- [README.md](README.md) - ë¹ ë¥¸ ?œì‘
- [QUICKREF.md](QUICKREF.md) - ë¹ ë¥¸ ì°¸ì¡°
- [MIGRATION.md](MIGRATION.md) - ë³€ê²??´ì—­
