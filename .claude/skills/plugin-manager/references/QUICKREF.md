---
tags:
- 30_Resources
---
# Git Skill Manager - Quick Reference

## ?“¦ ?¤ì¹˜ (Install)

```bash
python .claude/skills/plugin-manager/scripts/manage.py install --git-url "URL"
```

**?µì…˜:**
- `--git-url` (?„ìˆ˜): GitHub repository URL
- `--plugin-name` (? íƒ): ì»¤ìŠ¤?€ ?ŒëŸ¬ê·¸ì¸ ?´ë¦„
- `--target-path` (? íƒ): ?¤ì¹˜ ê²½ë¡œ (ê¸°ë³¸: `.claude`)

**?ˆì‹œ:**
```bash
# ê¸°ë³¸ ?¤ì¹˜
python scripts/manage.py install --git-url "https://github.com/kepano/obsidian-skills"

# ì»¤ìŠ¤?€ ?´ë¦„?¼ë¡œ ?¤ì¹˜
python scripts/manage.py install --git-url "https://github.com/user/repo" --plugin-name "my-plugin"
```

---

## ?“‹ ëª©ë¡ ì¡°íšŒ (List)

```bash
python .claude/skills/plugin-manager/scripts/manage.py list
```

**?µì…˜:**
- `--target-path` (? íƒ): ?€??ê²½ë¡œ (ê¸°ë³¸: `.claude`)

**?ˆì‹œ:**
```bash
# ?¤ì¹˜??ëª¨ë“  plugin ë³´ê¸°
python scripts/manage.py list
```

---

## ?—‘ï¸??œê±° (Uninstall)

```bash
python .claude/skills/plugin-manager/scripts/manage.py uninstall --skill-name "NAME"
```

**?µì…˜:**
- `--skill-name` (?„ìˆ˜): ?œê±°??skill ?´ë¦„
- `--target-path` (? íƒ): ?€??ê²½ë¡œ (ê¸°ë³¸: `.claude`)

**?ˆì‹œ:**
```bash
# skill ?œê±°
python scripts/manage.py uninstall --skill-name "json-canvas"
```

---

## ?’¡ Tips

### ?¤ì¹˜??skill ?´ë¦„ ?•ì¸
```bash
python scripts/manage.py list
```

### ?„ì?ë§?ë³´ê¸°
```bash
python scripts/manage.py --help
python scripts/manage.py install --help
python scripts/manage.py uninstall --help
python scripts/manage.py list --help
```

### ?ë? ê²½ë¡œ?ì„œ ?¤í–‰
?„ì¬ ?„ì¹˜ê°€ ?„ë¡œ?íŠ¸ ë£¨íŠ¸????
```bash
python .claude/skills/plugin-manager/scripts/manage.py list
```

?„ì¬ ?„ì¹˜ê°€ skill ?´ë”????
```bash
python scripts/manage.py list
```

---

## ?“ ?Œì¼ ?„ì¹˜

- **?¤ì¹˜ ?¤í¬ë¦½íŠ¸**: `.claude/skills/plugin-manager/scripts/manage.py`
- **?ˆì??¤íŠ¸ë¦?*: `.claude/skills/plugin-manager/assets/registry.json`
- **?¤ì¹˜??skills**: `.claude/skills/[skill-name]/`

---

## ? ï¸ ì£¼ì˜?¬í•­

1. **?¸í„°???°ê²° ?„ìš”**: GitHub APIë¥??¬ìš©?˜ë?ë¡??¤íŠ¸?Œí¬ ?°ê²°???„ìš”?©ë‹ˆ??
2. **GitHub URL ?•ì‹**: `https://github.com/owner/repo` ?•ì‹?´ì–´???©ë‹ˆ??
3. **Skill ?´ë¦„**: ?œê±°???ŒëŠ” plugin ?´ë¦„???„ë‹Œ ê°œë³„ skill ?´ë¦„???¬ìš©?©ë‹ˆ??

---

## ?”§ ë¬¸ì œ ?´ê²°

### "skill??ì°¾ì„ ???†ìŠµ?ˆë‹¤" ?ëŸ¬
??`list` ëª…ë ¹?¼ë¡œ ?•í™•??skill ?´ë¦„ ?•ì¸

### HTTP ?ëŸ¬
??GitHub URL???¬ë°”ë¥¸ì? ?•ì¸
???¸í„°???°ê²° ?•ì¸
??Repositoryê°€ public?¸ì? ?•ì¸

### ê¶Œí•œ ?ëŸ¬
??`.claude/skills` ?´ë”???°ê¸° ê¶Œí•œ???ˆëŠ”ì§€ ?•ì¸

---

**?ì„¸??ë¬¸ì„œ**: [SKILL.md](SKILL.md) | [README.md](README.md) | [MIGRATION.md](MIGRATION.md)
