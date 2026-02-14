#!/usr/bin/env python3

"""
Plugin Manager v2.0.0

Git clone + shutil.copytree 기반 스킬 관리자.
GitHub 저장소를 repos/에 clone하고 필요한 skill을 .claude/skills/로 복사합니다.

사용 예시:
  설치:   python hub.py install --git-url "https://github.com/anthropics/skills"
  업데이트: python hub.py update
  제거:   python hub.py uninstall --plugin-name "skills"
  목록:   python hub.py list
"""

import json
import sys
import io
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List

# Fix Windows cp949 encoding issue
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Import modules
from git_ops import (
    check_git_available, git_clone, git_pull,
    git_get_commit_hash, git_get_remote_url
)
from file_ops import copy_skills_to_target, remove_skill_directories, cleanup_partial_clone
from path_utils import (
    parse_git_url, make_repo_dirname, get_repo_dir,
    detect_skill_prefix, discover_skills_in_repo
)
from registry_manager import RegistryManager

# ──────────────────────────────────────────────
# Constants
# ──────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_MANAGER_DIR = SCRIPT_DIR.parent
REPOS_DIR = PLUGIN_MANAGER_DIR / "repos"
REGISTRY_PATH = PLUGIN_MANAGER_DIR / "assets" / "registry.json"

# .claude/skills/ directory (two levels up from skill-hub)
SKILLS_DIR = PLUGIN_MANAGER_DIR.parent

# .claude directory (one level up from skill-hub)
CLAUDE_DIR = PLUGIN_MANAGER_DIR.parent
SKILLS_INVENTORY_PATH = PLUGIN_MANAGER_DIR / "assets" / "SKILLS-INVENTORY.md"

# Registry manager instance
registry_mgr = RegistryManager(REGISTRY_PATH)


# ──────────────────────────────────────────────
# SKILLS-INVENTORY.md Management
# ──────────────────────────────────────────────

def update_skills_inventory(action: str, skills: List[str]) -> None:
    """Auto-update SKILLS-INVENTORY.md after install/uninstall operations"""
    if not SKILLS_INVENTORY_PATH.exists():
        print(f"[WARNING] SKILLS-INVENTORY.md not found at {SKILLS_INVENTORY_PATH}")
        return

    try:
        with open(SKILLS_INVENTORY_PATH, 'r', encoding='utf-8') as f:
            content = f.read()

        from datetime import datetime
        today = datetime.now().strftime('%Y-%m-%d')

        # Update last updated date
        import re
        content = re.sub(
            r'\*\*마지막 업데이트\*\*: \d{4}-\d{2}-\d{2}',
            f'**마지막 업데이트**: {today}',
            content
        )

        # Save updated content
        with open(SKILLS_INVENTORY_PATH, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[OK] Updated SKILLS-INVENTORY.md (action: {action}, skills: {len(skills)})")
    except Exception as e:
        print(f"[WARNING] Failed to auto-update SKILLS-INVENTORY.md: {e}")


def print_inventory_update_reminder(action: str, skills: List[str]) -> None:
    """Print reminder to update SKILLS-INVENTORY.md manually"""
    print("=" * 60)
    print("[REMINDER] Update SKILLS-INVENTORY.md")
    print("=" * 60)
    print(f"Action: {action.upper()}")
    print(f"Skills: {', '.join(skills)}")
    print(f"Location: {SKILLS_INVENTORY_PATH}")
    print("Next step:")
    if action == "install":
        print("  1. Open SKILLS-INVENTORY.md")
        print("  2. Find the appropriate category section (Design, Documents, Development, Content)")
        print("  3. Add the new skills to the category table")
        print("  4. Update the Summary section (Total Managed Skills count)")
    elif action == "uninstall":
        print("  1. Open SKILLS-INVENTORY.md")
        print("  2. Remove the skills from their category tables")
        print("  3. Update the Summary section (Total Managed Skills count)")
    print("Or run: git add SKILLS-INVENTORY.md && git commit -m 'docs: update skills inventory'")
    print("=" * 60)


# ──────────────────────────────────────────────
# Commands
# ──────────────────────────────────────────────

def cmd_install(git_url: str, plugin_name: Optional[str] = None, selected_skills: Optional[List[str]] = None) -> Dict[str, Any]:
    """clone -> detect prefix -> discover skills -> copy -> registry

    Args:
        git_url: Git repository URL
        plugin_name: Custom plugin name (default: repo name)
        selected_skills: List of specific skills to install (None = all skills)
    """
    if not check_git_available():
        print("[ERROR] git is not installed or not in PATH")
        return {"status": "error", "message": "git is not installed"}

    try:
        owner, repo = parse_git_url(git_url)
    except ValueError as e:
        print(f"[ERROR] {e}")
        return {"status": "error", "message": str(e)}

    plugin_name = plugin_name or repo
    repo_dir = get_repo_dir(REPOS_DIR, owner, repo)

    # Check if already cloned
    registry = registry_mgr.load()
    existing = registry_mgr.find_plugin(registry, plugin_name)
    if existing and repo_dir.exists():
        print(f"Plugin '{plugin_name}' is already installed. Use 'update' to refresh.")
        return {"status": "error", "message": f"Plugin '{plugin_name}' already installed"}

    # Clone
    REPOS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Cloning '{git_url}' ...")
    if not git_clone(git_url, repo_dir):
        cleanup_partial_clone(repo_dir)
        return {"status": "error", "message": "git clone failed"}

    # Detect skill prefix
    prefix = detect_skill_prefix(repo_dir)
    if not prefix:
        print(f"[ERROR] No skill directory found in repository")
        cleanup_partial_clone(repo_dir)
        return {"status": "error", "message": "No skill directory found"}

    # Discover skills
    all_skills = discover_skills_in_repo(repo_dir, prefix)
    if not all_skills:
        print(f"[ERROR] No skills (with SKILL.md) found under '{prefix}/'")
        cleanup_partial_clone(repo_dir)
        return {"status": "error", "message": "No skills found"}

    print(f"Found {len(all_skills)} skills: {', '.join(all_skills)}")

    # Filter skills if specific skills requested
    if selected_skills:
        # Validate requested skills exist
        invalid_skills = [s for s in selected_skills if s not in all_skills]
        if invalid_skills:
            print(f"[ERROR] Skills not found in repository: {', '.join(invalid_skills)}")
            print(f"Available skills: {', '.join(all_skills)}")
            cleanup_partial_clone(repo_dir)
            return {"status": "error", "message": f"Invalid skills: {', '.join(invalid_skills)}"}

        skills_to_install = selected_skills
        print(f"Installing {len(skills_to_install)} selected skills: {', '.join(skills_to_install)}")
    else:
        skills_to_install = all_skills
        print(f"Installing all {len(skills_to_install)} skills")

    # Copy to .claude/skills/
    copied = copy_skills_to_target(repo_dir, prefix, skills_to_install, SKILLS_DIR)
    print(f"Copied {copied} skills to {SKILLS_DIR}")

    # Get commit hash
    commit_hash = git_get_commit_hash(repo_dir) or ""
    now = datetime.now().isoformat()

    # Update registry
    plugin_info = {
        "name": plugin_name,
        "git_url": git_url,
        "owner": owner,
        "repo": repo,
        "repo_path": f"{owner}-{repo}",
        "skill_prefix": prefix,
        "commit_hash": commit_hash,
        "installed_at": now,
        "updated_at": now,
        "skills": skills_to_install,
        "status": "installed",
    }
    registry_mgr.add_or_update_plugin(registry, plugin_info)
    registry_mgr.save(registry)

    print(f"[OK] Plugin '{plugin_name}' installed successfully ({commit_hash[:12]})")
    for s in skills_to_install:
        print(f"  - {s}")

    # Auto-update and remind user
    update_skills_inventory("install", skills_to_install)
    print_inventory_update_reminder("install", skills_to_install)

    return {"status": "success", "plugin": plugin_name, "skills": skills_to_install, "commit": commit_hash}


def cmd_uninstall(plugin_name: str) -> Dict[str, Any]:
    """remove skills -> remove repo -> registry"""
    registry = registry_mgr.load()
    plugin = registry_mgr.find_plugin(registry, plugin_name)

    if not plugin:
        print(f"[ERROR] Plugin '{plugin_name}' not found in registry")
        return {"status": "error", "message": f"Plugin '{plugin_name}' not found"}

    skills = plugin.get("skills", [])
    repo_path = plugin.get("repo_path", "")

    # Remove skill directories from .claude/skills/
    print(f"Removing {len(skills)} skills ...")
    removed = remove_skill_directories(skills, SKILLS_DIR)
    print(f"  Removed {removed} skill directories")

    # Remove cloned repo
    if repo_path:
        clone_dir = REPOS_DIR / repo_path
        if clone_dir.exists():
            import shutil
            shutil.rmtree(clone_dir, ignore_errors=True)
            print(f"  Removed repo: {clone_dir.name}")

    # Update registry
    registry_mgr.remove_plugin(registry, plugin_name)
    registry_mgr.save(registry)

    print(f"[OK] Plugin '{plugin_name}' uninstalled")

    # Auto-update and remind user
    update_skills_inventory("uninstall", skills)
    print_inventory_update_reminder("uninstall", skills)

    return {"status": "success", "plugin": plugin_name, "removed_skills": removed}


def cmd_update(plugin_name: Optional[str] = None) -> Dict[str, Any]:
    """git pull -> re-copy -> update registry. plugin_name=None이면 전체 업데이트."""
    if not check_git_available():
        print("[ERROR] git is not installed or not in PATH")
        return {"status": "error", "message": "git is not installed"}

    registry = registry_mgr.load()
    plugins_to_update = []

    if plugin_name:
        plugin = registry_mgr.find_plugin(registry, plugin_name)
        if not plugin:
            print(f"[ERROR] Plugin '{plugin_name}' not found in registry")
            return {"status": "error", "message": f"Plugin '{plugin_name}' not found"}
        plugins_to_update = [plugin]
    else:
        plugins_to_update = [p for p in registry["plugins"] if p["status"] == "installed"]

    if not plugins_to_update:
        print("No plugins to update.")
        return {"status": "success", "message": "No plugins to update", "updated": []}

    updated = []
    for plugin in plugins_to_update:
        name = plugin["name"]
        rp = plugin.get("repo_path", "")
        clone_dir = REPOS_DIR / rp if rp else None

        if not clone_dir or not clone_dir.exists():
            # Try to re-clone
            git_url = plugin.get("git_url", "")
            if not git_url:
                print(f"  [WARNING] Skipping '{name}': no git_url and no local repo")
                continue
            print(f"  Re-cloning '{name}' ...")
            owner, repo = parse_git_url(git_url)
            clone_dir = get_repo_dir(REPOS_DIR, owner, repo)
            REPOS_DIR.mkdir(parents=True, exist_ok=True)
            if not git_clone(git_url, clone_dir):
                print(f"  [ERROR] Failed to clone '{name}'")
                continue
            plugin["repo_path"] = f"{owner}-{repo}"

        old_hash = plugin.get("commit_hash", "")

        # Pull latest
        print(f"Updating '{name}' ...")
        if not git_pull(clone_dir):
            print(f"  [ERROR] Failed to pull '{name}'")
            continue

        new_hash = git_get_commit_hash(clone_dir) or ""

        # Re-detect prefix and skills
        prefix = detect_skill_prefix(clone_dir)
        if not prefix:
            print(f"  [WARNING] No skill directory found for '{name}'")
            continue

        skills = discover_skills_in_repo(clone_dir, prefix)
        if not skills:
            print(f"  [WARNING] No skills found for '{name}'")
            continue

        # Re-copy
        copy_skills_to_target(clone_dir, prefix, skills, SKILLS_DIR)

        # Update plugin info
        plugin["skill_prefix"] = prefix
        plugin["commit_hash"] = new_hash
        plugin["updated_at"] = datetime.now().isoformat()
        plugin["skills"] = skills

        if old_hash and old_hash == new_hash:
            print(f"  [OK] '{name}' already up to date ({new_hash[:12]})")
        else:
            print(f"  [OK] '{name}' updated ({old_hash[:12] if old_hash else 'none'} -> {new_hash[:12]})")

        updated.append(name)

    registry_mgr.save(registry)
    return {"status": "success", "updated": updated}


def cmd_list() -> Dict[str, Any]:
    """설치된 plugins 목록 출력"""
    registry = registry_mgr.load()
    plugins = registry.get("plugins", [])

    print(f"\nInstalled Plugins ({len(plugins)}):")
    print("=" * 60)

    if not plugins:
        print("No plugins installed.")
    else:
        for idx, plugin in enumerate(plugins, 1):
            name = plugin.get("name", "?")
            git_url = plugin.get("git_url", "N/A")
            commit = plugin.get("commit_hash", "")[:12] or "N/A"
            skills = plugin.get("skills", [])
            installed = plugin.get("installed_at", "N/A")
            updated = plugin.get("updated_at", "")

            print(f"\n{idx}. {name}")
            print(f"   Repository : {git_url}")
            print(f"   Commit     : {commit}")
            print(f"   Installed  : {installed}")
            if updated and updated != installed:
                print(f"   Updated    : {updated}")
            print(f"   Skills ({len(skills)}): {', '.join(skills)}")

    print("\n" + "=" * 60)

    return {"status": "success", "plugins": plugins}


# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Git clone 기반 Claude skill plugin 관리자 (v2.0.0)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s install --git-url "https://github.com/anthropics/skills"
  %(prog)s update
  %(prog)s update --plugin-name "skills"
  %(prog)s uninstall --plugin-name "skills"
  %(prog)s list
        """
    )

    subparsers = parser.add_subparsers(dest='action', help='Command')

    # install
    install_p = subparsers.add_parser('install', help='Install plugin from Git repo')
    install_p.add_argument('--git-url', required=True, help='Git repository URL')
    install_p.add_argument('--plugin-name', help='Custom plugin name (default: repo name)')
    install_p.add_argument('--skills', help='Comma-separated list of specific skills to install (e.g., "docx,pdf,xlsx"). If omitted, all skills are installed.')

    # uninstall
    uninstall_p = subparsers.add_parser('uninstall', help='Uninstall plugin')
    uninstall_p.add_argument('--plugin-name', required=True, help='Plugin name to remove')

    # update
    update_p = subparsers.add_parser('update', help='Update plugin(s)')
    update_p.add_argument('--plugin-name', help='Plugin name (omit for all)')

    # list
    subparsers.add_parser('list', help='List installed plugins')

    args = parser.parse_args()

    if not args.action:
        parser.print_help()
        sys.exit(1)

    if args.action == 'install':
        selected_skills = None
        if hasattr(args, 'skills') and args.skills:
            # Parse comma-separated skills list
            selected_skills = [s.strip() for s in args.skills.split(',') if s.strip()]
        result = cmd_install(args.git_url, getattr(args, 'plugin_name', None), selected_skills)
    elif args.action == 'uninstall':
        result = cmd_uninstall(args.plugin_name)
    elif args.action == 'update':
        result = cmd_update(getattr(args, 'plugin_name', None))
    elif args.action == 'list':
        result = cmd_list()
    else:
        print(f"Unknown action: {args.action}")
        sys.exit(1)

    sys.exit(0 if result.get('status') == 'success' else 1)


if __name__ == '__main__':
    main()
