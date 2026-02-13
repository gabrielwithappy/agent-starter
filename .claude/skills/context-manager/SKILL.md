---
name: context-manager
description: Manage AI Context documents for preserving knowledge across conversations. Use when the user wants to (1) save current work as a Context document at conversation end, (2) search and load relevant Context documents at conversation start, or (3) reorganize Context document content for better AI comprehension. Triggers include mentions of "context", "save this session", "find related context", or when wrapping up complex work.
---

# AI Context Manager

Manage AI Context documents to preserve and reuse knowledge across conversations.

## Core Workflows

### 1. Create Context from Current Session

When finishing a conversation with valuable learnings:

```bash
python scripts/create_context.py \
  --topic "주제명" \
  --vault-path "obsidianKMS" \
  --location "03.Resource/개발"
```

This creates `(Context) [주제명].md` with:
- Frontmatter (created, tags, status, review-cycle)
- Template structure from references/template.md
- Ready for manual content population

### 2. Search Existing Context Documents

When starting a new conversation that might benefit from prior context:

```bash
python scripts/search_context.py \
  --vault-path "obsidianKMS" \
  --query "검색어" \
  --search-mode all
```

Search modes:
- `title`: Search in filenames only (fast)
- `tags`: Search in frontmatter tags
- `content`: Full-text search
- `all`: Search all locations (default)

### 3. Update Existing Context

Add new discoveries to an existing Context document:

```bash
python scripts/update_context.py \
  --file "obsidianKMS/03.Resource/(Context) React.md" \
  --section "발견 및 학습 내용" \
  --content "새로 발견한 내용"
```

## Context Document Structure

See [references/template.md](references/template.md) for the full template structure.

**Key sections:**
- **개요**: High-level summary
- **핵심 개념**: Core concepts and terminology
- **반복 패턴 및 규칙**: Patterns discovered through practice
- **발견 및 학습 내용**: Recent discoveries (keep only 10-20 recent items)

## Best Practices

1. **Progressive Knowledge Building**: Start with discoveries, promote validated patterns to "핵심 개념" or "반복 패턴"
2. **Size Management**: Keep discovery sections lean (10-20 items), archive older learnings
3. **Regular Review**: Update based on frontmatter `review-cycle` field
4. **Clear Naming**: Use `(Context) [주제명].md` format for easy searching in Obsidian

## Reference Files

- [template.md](references/template.md): Full AI Context document template
