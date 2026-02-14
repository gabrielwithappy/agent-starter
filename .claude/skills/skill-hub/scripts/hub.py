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
import subprocess
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List, Tuple

# Fix Windows cp949 encoding issue
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

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

REGISTRY_VERSION = "2.0.0"


# ──────────────────────────────────────────────
# Git Operations
# ──────────────────────────────────────────────

def check_git_available() -> bool:
    """git이 설치되어 있는지 확인"""
    try:
        result = subprocess.run(
            ["git", "--version"],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def git_clone(url: str, target_dir: Path) -> bool:
    """shallow clone (--depth 1)"""
    try:
        result = subprocess.run(
            ["git", "clone", "--depth", "1", url, str(target_dir)],
            capture_output=True, text=True, timeout=300,
            encoding='utf-8', errors='replace'
        )
        if result.returncode != 0:
            print(f"[ERROR] git clone failed: {result.stderr.strip()}")
            return False
        return True
    except subprocess.TimeoutExpired:
        print("[ERROR] git clone timed out (5 min)")
        return False
    except Exception as e:
        print(f"[ERROR] git clone exception: {e}")
        return False


def git_pull(repo_dir: Path) -> bool:
    """git pull in repo directory"""
    try:
        result = subprocess.run(
            ["git", "pull"],
            capture_output=True, text=True, timeout=120,
            cwd=str(repo_dir),
            encoding='utf-8', errors='replace'
        )
        if result.returncode != 0:
            print(f"[ERROR] git pull failed: {result.stderr.strip()}")
            return False
        return True
    except subprocess.TimeoutExpired:
        print("[ERROR] git pull timed out (2 min)")
        return False
    except Exception as e:
        print(f"[ERROR] git pull exception: {e}")
        return False


def git_get_commit_hash(repo_dir: Path) -> Optional[str]:
    """HEAD commit hash"""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=10,
            cwd=str(repo_dir),
            encoding='utf-8', errors='replace'
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def git_get_remote_url(repo_dir: Path) -> Optional[str]:
    """origin remote URL"""
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            capture_output=True, text=True, timeout=10,
            cwd=str(repo_dir),
            encoding='utf-8', errors='replace'
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def cleanup_partial_clone(target_dir: Path) -> None:
    """실패한 clone 디렉토리 정리"""
    if target_dir.exists():
        shutil.rmtree(target_dir, ignore_errors=True)


# ──────────────────────────────────────────────
# Path Utilities
# ──────────────────────────────────────────────

def parse_git_url(url: str) -> Tuple[str, str]:
    """Git URL에서 (owner, repo) 추출"""
    url = url.rstrip("/").replace(".git", "")
    parts = url.split("/")
    if len(parts) < 2:
        raise ValueError(f"Invalid Git URL: {url}")
    owner = parts[-2]
    repo = parts[-1]
    return owner, repo


def make_repo_dirname(owner: str, repo: str) -> str:
    """owner-repo 형식의 디렉토리 이름"""
    return f"{owner}-{repo}"


def get_repo_dir(owner: str, repo: str) -> Path:
    """repos/ 아래의 clone 디렉토리 절대 경로"""
    return REPOS_DIR / make_repo_dirname(owner, repo)


def detect_skill_prefix(repo_dir: Path) -> Optional[str]:
    """저장소에서 skill 디렉토리 prefix 탐지.
    우선순위: .claude/skills/ > .agent/skills/ > skills/
    """
    candidates = [".claude/skills", ".agent/skills", "skills"]
    for candidate in candidates:
        candidate_path = repo_dir / candidate
        if candidate_path.is_dir():
            # 실제 skill 하위 디렉토리가 있는지 확인
            subdirs = [d for d in candidate_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
            if subdirs:
                return candidate
    return None


def discover_skills_in_repo(repo_dir: Path, prefix: str) -> List[str]:
    """저장소에서 skill 이름 리스트 반환"""
    skill_base = repo_dir / prefix
    if not skill_base.is_dir():
        return []
    skills = []
    for item in sorted(skill_base.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            # SKILL.md가 있는 디렉토리만 skill로 인정
            if (item / "SKILL.md").exists():
                skills.append(item.name)
    return skills


# ──────────────────────────────────────────────
# Registry
# ──────────────────────────────────────────────

def load_registry() -> Dict[str, Any]:
    """registry.json 로드"""
    if REGISTRY_PATH.exists():
        try:
            with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
                registry = json.load(f)
            return migrate_registry(registry)
        except Exception:
            pass

    return {"version": REGISTRY_VERSION, "plugins": []}


def save_registry(registry: Dict[str, Any]) -> None:
    """registry.json 저장"""
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)


def migrate_registry(registry: Dict[str, Any]) -> Dict[str, Any]:
    """v1.0.0 -> v2.0.0 마이그레이션"""
    version = registry.get("version", "1.0.0")
    if version == REGISTRY_VERSION:
        return registry

    # v1 -> v2 migration
    new_plugins = []
    for plugin in registry.get("plugins", []):
        owner = plugin.get("owner", "unknown")
        repo = plugin.get("repo", plugin.get("name", "unknown"))
        new_plugin = {
            "name": plugin.get("name", repo),
            "git_url": plugin.get("git_url", ""),
            "owner": owner,
            "repo": repo,
            "repo_path": make_repo_dirname(owner, repo),
            "skill_prefix": "",  # will be filled on next update
            "commit_hash": "",   # will be filled on next update
            "installed_at": plugin.get("installed_at", ""),
            "updated_at": plugin.get("installed_at", ""),
            "skills": plugin.get("skills", []),
            "status": plugin.get("status", "installed"),
        }
        # Remove old fields
        # target_path, last_updated are dropped
        new_plugins.append(new_plugin)

    return {"version": REGISTRY_VERSION, "plugins": new_plugins}


def find_plugin_in_registry(registry: Dict[str, Any], plugin_name: str) -> Optional[Dict[str, Any]]:
    """이름으로 plugin 찾기"""
    for plugin in registry.get("plugins", []):
        if plugin["name"] == plugin_name:
            return plugin
    return None


def add_or_update_plugin(registry: Dict[str, Any], plugin_info: Dict[str, Any]) -> None:
    """plugin 추가 또는 업데이트"""
    for i, plugin in enumerate(registry["plugins"]):
        if plugin["name"] == plugin_info["name"]:
            registry["plugins"][i] = plugin_info
            return
    registry["plugins"].append(plugin_info)


def remove_plugin_from_registry(registry: Dict[str, Any], plugin_name: str) -> bool:
    """registry에서 plugin 제거"""
    original = len(registry["plugins"])
    registry["plugins"] = [p for p in registry["plugins"] if p["name"] != plugin_name]
    return len(registry["plugins"]) < original


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
    print(f"
{'='*60}")
    print("[REMINDER] Update SKILLS-INVENTORY.md")
    print('='*60)
    print(f"
Action: {action.upper()}")
    print(f"Skills: {', '.join(skills)}")
    print(f"
Location: {SKILLS_INVENTORY_PATH}")
    print("
Next step:")
    if action == "install":
        print("  1. Open SKILLS-INVENTORY.md")
        print("  2. Find the appropriate category section (Design, Documents, Development, Content)")
        print("  3. Add the new skills to the category table")
        print("  4. Update the Summary section (Total Managed Skills count)")
    elif action == "uninstall":
        print("  1. Open SKILLS-INVENTORY.md")
        print("  2. Remove the skills from their category tables")
        print("  3. Update the Summary section (Total Managed Skills count)")
    print(f"
Or run: git add SKILLS-INVENTORY.md && git commit -m 'docs: update skills inventory'")
    print("="*60 + "
")


# ──────────────────────────────────────────────
# File Copy
# ──────────────────────────────────────────────

def copy_skills_to_target(repo_dir: Path, prefix: str, skills: List[str], target_dir: Path) -> int:
    """skill 디렉토리들을 target으로 복사. 반환: 복사된 skill 수"""
    copied = 0
    for skill_name in skills:
        src = repo_dir / prefix / skill_name
        dst = target_dir / skill_name
        if not src.is_dir():
            print(f"  [WARNING] Skill directory not found: {src}")
            continue
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        copied += 1
    return copied


def remove_skill_directories(skills: List[str], target_dir: Path) -> int:
    """skill 디렉토리들 삭제. 반환: 삭제된 수"""
    removed = 0
    for skill_name in skills:
        skill_path = target_dir / skill_name
        if skill_path.exists():
            shutil.rmtree(skill_path)
            removed += 1
    return removed


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
    repo_dir = get_repo_dir(owner, repo)

    # Check if already cloned
    registry = load_registry()
    existing = find_plugin_in_registry(registry, plugin_name)
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
        "repo_path": make_repo_dirname(owner, repo),
        "skill_prefix": prefix,
        "commit_hash": commit_hash,
        "installed_at": now,
        "updated_at": now,
        "skills": skills_to_install,
        "status": "installed",
    }
    add_or_update_plugin(registry, plugin_info)
    save_registry(registry)

    print(f"[OK] Plugin '{plugin_name}' installed successfully ({commit_hash[:12]})")
    for s in skills_to_install:
        print(f"  - {s}")

    # Auto-update and remind user
    update_skills_inventory("install", skills_to_install)
    print_inventory_update_reminder("install", skills_to_install)

    return {"status": "success", "plugin": plugin_name, "skills": skills_to_install, "commit": commit_hash}


def cmd_uninstall(plugin_name: str) -> Dict[str, Any]:
    """remove skills -> remove repo -> registry"""
    registry = load_registry()
    plugin = find_plugin_in_registry(registry, plugin_name)

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
            shutil.rmtree(clone_dir, ignore_errors=True)
            print(f"  Removed repo: {clone_dir.name}")

    # Update registry
    remove_plugin_from_registry(registry, plugin_name)
    save_registry(registry)

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

    registry = load_registry()
    plugins_to_update = []

    if plugin_name:
        plugin = find_plugin_in_registry(registry, plugin_name)
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
            clone_dir = get_repo_dir(owner, repo)
            REPOS_DIR.mkdir(parents=True, exist_ok=True)
            if not git_clone(git_url, clone_dir):
                print(f"  [ERROR] Failed to clone '{name}'")
                continue
            plugin["repo_path"] = make_repo_dirname(owner, repo)

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

    save_registry(registry)
    return {"status": "success", "updated": updated}


def cmd_list() -> Dict[str, Any]:
    """설치된 plugins 목록 출력"""
    registry = load_registry()
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
