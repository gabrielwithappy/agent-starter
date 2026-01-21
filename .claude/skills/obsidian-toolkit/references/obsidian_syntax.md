# Obsidian Flavored Markdown Syntax Guide

This reference guide describes the syntax extensions supported by Obsidian. Use this format when creating or editing content in the vault.

## 1. Internal Links (Wikilinks)

Use `[[Wikilinks]]` to link between notes. This is preferred over standard Markdown links `[Title](url)`.

### Basic Links
```markdown
[[Note Name]]                 # Links to "Note Name.md"
[[Folder/Note Name]]          # Links to file in specific folder
[[Note Name|Custom Text]]     # Links to note but displays "Custom Text"
```

### Advanced Links (Anchors)
```markdown
[[Note Name#Heading]]         # Link to specific heading
[[Note Name#^block-id]]       # Link to specific block (paragraph/list item)
```

## 2. Callouts

Use Callouts to highlight information.

### Syntax
```markdown
> [!type] Title (Optional)
> Content of the callout
```

### Supported Types
- **Info/Note**: `[!info]`, `[!note]` (Blue)
- **Tip/Important**: `[!tip]`, `[!important]` (Cyan/Green)
- **Warning**: `[!warning]` (Orange)
- **Danger/Error**: `[!danger]`, `[!error]` (Red)
- **Task/Todo**: `[!todo]`
- **Question/FAQ**: `[!question]`, `[!faq]`
- **Example**: `[!example]`

### Foldable Callouts
Add `+` (open) or `-` (closed) after the type.
```markdown
> [!faq]- Click to expand
> Hidden content
```

## 3. Embeds (Transclusion)

Display the content of another note or image within the current note using `!`.

```markdown
![[Image.png]]                # Embed image
![[Note Name]]                # Embed entire note
![[Note Name#Heading]]        # Embed specific section
```

## 4. Properties (Frontmatter)

Metadata must be at the very top of the file, enclosed in `---`.

```yaml
---
tags:
  - project/active
  - status/draft
aliases: ["My Alias", "Another Name"]
date: 2024-01-22
priority: high
completed: false
related: "[[Other Note]]"
---
```

### Standard Keys
- `tags`: List of tags (can also use inline `#tags`).
- `aliases`: Alternate titles for the note (for search/linking).
- `cssclasses`: Apply custom CSS to the note.
- `created`, `updated`: Timestamps (optional, handled by some plugins).

## 5. Task Lists

```markdown
- [ ] Incomplete task
- [x] Completed task
- [ ] Task with due date 📅 2024-01-25
```
