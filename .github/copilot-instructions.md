# Agent Skills Instruction

You have access to a set of specialized capabilities called **Skills**. These skills are structured directories containing instructions (`SKILL.md`), scripts, and resources.

## Skill Structure
Each skill is located in its own directory (e.g., `.agent/skills/<skill-name>/` or `obsidianKMS/.agent/skills/<skill-name>/`) and contains:

1.  **`SKILL.md` (Required)**: The core instruction file.
    *   **Frontmatter**: Contains metadata like `name` and `description`.
    *   **Body**: Detailed step-by-step instructions, usage examples, and edge cases.
2.  **`scripts/` (Optional)**: Executable scripts (Python, Bash, Node.js) that perform the skill's actions.
3.  **`references/` (Optional)**: Documentation, templates (`FORMS.md`), and domain-specific knowledge.
4.  **`assets/` (Optional)**: Templates and static resources.

## How to Use Skills

1.  **Discovery**: When a user request implies a task covered by a skill (e.g., "manage git plugins", "update obsidian notes"), **search for relevant skills** by looking into the `.agent/skills` or `obsidianKMS/.agent/skills` directories.
2.  **Activation**:
    *   Use the `view_file` tool to read the `SKILL.md` of the relevant skill.
    *   **CRITICAL**: Read the *entire* `SKILL.md` content to understand the procedure, especially the `scripts/` availability and usage arguments.
3.  **Execution**:
    *   Follow the "Instructions" or "Workflow" section in `SKILL.md` precisely.
    *   If the skill provides scripts in the `scripts/` folder, prioritize using `run_command` to execute them over manual manual steps, unless instructed otherwise.
    *   Always check strictly for `compatibility` requirements in the frontmatter.

## Example Workflow
If the user asks to "install a new plugin":
1.  Locate `plugin-manager/SKILL.md`.
2.  Read `plugin-manager/SKILL.md` to find the install command (e.g., `python scripts/install.py <url>`).
3.  Execute the command using `run_command`.

## Skill Locations
- Primary: `.agent/skills/`
