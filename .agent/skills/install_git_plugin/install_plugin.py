#!/usr/bin/env python3

"""
Install/Uninstall Git Plugin Skill

설명: Git repository에서 Claude plugin을 설치/제거합니다.
설치된 plugins은 registry.json으로 관리됩니다.

사용 예시:
설치:
{
  "action": "install",
  "git_url": "https://github.com/gabrielwithappy/obsidian-skills",
  "plugin_name": "obsidian-skills"
}

제거:
{
  "action": "uninstall",
  "skill_name": "json-canvas"
}

목록 조회:
{
  "action": "list"
}
"""

import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List
import shutil


def get_registry_path(target_path: str) -> str:
    """registry.json 파일 경로 반환"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    registry_file = os.path.join(script_dir, 'data', 'registry.json')
    return registry_file


def load_registry(target_path: str) -> Dict[str, Any]:
    """설치된 plugins 레지스트리 로드"""
    registry_path = get_registry_path(target_path)
    
    if os.path.exists(registry_path):
        try:
            with open(registry_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    
    return {
        'version': '1.0.0',
        'plugins': [],
        'last_updated': datetime.now().isoformat()
    }


def save_registry(target_path: str, registry: Dict[str, Any]) -> None:
    """레지스트리 저장"""
    registry_path = get_registry_path(target_path)
    registry['last_updated'] = datetime.now().isoformat()
    
    os.makedirs(os.path.dirname(registry_path), exist_ok=True)
    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)


def add_to_registry(target_path: str, plugin_info: Dict[str, Any]) -> None:
    """레지스트리에 plugin 추가"""
    registry = load_registry(target_path)
    
    # 중복 확인
    for plugin in registry['plugins']:
        if plugin['name'] == plugin_info['name']:
            plugin.update(plugin_info)
            save_registry(target_path, registry)
            return
    
    registry['plugins'].append(plugin_info)
    save_registry(target_path, registry)


def remove_from_registry(target_path: str, skill_name: str) -> bool:
    """레지스트리에서 plugin 제거"""
    registry = load_registry(target_path)
    original_count = len(registry['plugins'])
    registry['plugins'] = [p for p in registry['plugins'] if p['name'] != skill_name]
    
    if len(registry['plugins']) < original_count:
        save_registry(target_path, registry)
        return True
    return False


def extract_repo_name(git_url: str) -> str:
    """Git URL에서 repository 이름 추출"""
    return git_url.rstrip('/').split('/')[-1].replace('.git', '')


def ensure_directory_exists(dir_path: str) -> None:
    """디렉토리 생성"""
    Path(dir_path).mkdir(parents=True, exist_ok=True)


def fetch_github_file(owner: str, repo: str, file_path: str) -> Optional[str]:
    """GitHub에서 파일 다운로드"""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{file_path}"
    
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise Exception(f"HTTP {e.code}: {e.reason}")
    except Exception as e:
        return None


def fetch_github_directory_structure(owner: str, repo: str, path: str = '') -> list:
    """GitHub API를 사용하여 디렉토리 구조 조회"""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            if isinstance(data, list):
                return data
            return []
    except Exception as e:
        return []


def download_directory_recursively(owner: str, repo: str, path: str, files: Dict, max_depth: int = 3, current_depth: int = 0) -> None:
    """GitHub 디렉토리를 재귀적으로 다운로드"""
    if current_depth >= max_depth:
        return
    
    try:
        contents = fetch_github_directory_structure(owner, repo, path)
        for item in contents:
            if item['type'] == 'file':
                file_path = item['path']
                try:
                    content = fetch_github_file(owner, repo, file_path)
                    if content:
                        files[file_path] = content
                except Exception:
                    pass
            elif item['type'] == 'dir':
                download_directory_recursively(owner, repo, item['path'], files, max_depth, current_depth + 1)
    except Exception as e:
        pass


def fetch_plugin_config(owner: str, repo: str) -> Optional[Dict]:
    """GitHub 저장소의 .claude-plugin/plugin.json 설정 읽기"""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/.claude-plugin/plugin.json"
    
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            return json.loads(content)
    except Exception:
        return None


def download_plugin_files(git_url: str, plugin_name: str) -> Dict[str, Optional[str]]:
    """Git repository에서 플러그인 파일들 다운로드"""
    api_url = git_url.replace('https://github.com/', '').replace('http://github.com/', '').replace('.git', '')
    
    parts = api_url.split('/')
    if len(parts) < 2:
        raise Exception(f"Invalid Git URL: {git_url}")
    
    owner, repo = parts[0], parts[1]
    files = {}
    
    # 주요 파일들
    main_files = ['manifest.json', 'README.md', 'index.js', 'LICENSE']
    
    for file_name in main_files:
        try:
            content = fetch_github_file(owner, repo, file_name)
            if content:
                files[file_name] = content
        except Exception as e:
            pass
    
    # .claude-plugin/plugin.json
    try:
        plugin_config = fetch_plugin_config(owner, repo)
        if plugin_config:
            files['.claude-plugin/plugin.json'] = json.dumps(plugin_config, indent=2, ensure_ascii=False)
    except Exception as e:
        pass
    
    # skills 디렉토리
    try:
        download_directory_recursively(owner, repo, 'skills', files)
    except Exception as e:
        pass
    
    return files


def save_plugin_files(plugin_path: str, files: Dict[str, Optional[str]]) -> None:
    """플러그인 파일들 저장"""
    for file_name, content in files.items():
        if content:
            file_path = os.path.join(plugin_path, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)


def read_plugin_info(git_url: str) -> Dict[str, Any]:
    """플러그인 정보 생성"""
    api_url = git_url.replace('https://github.com/', '').replace('http://github.com/', '').replace('.git', '')
    parts = api_url.split('/')
    
    owner = parts[0] if len(parts) > 0 else 'unknown'
    repo = parts[1] if len(parts) > 1 else 'unknown-plugin'
    
    return {
        'name': repo,
        'repository': git_url,
        'owner': owner,
        'installed_at': datetime.now().isoformat(),
        'status': 'active'
    }


def install_plugin(params: Dict[str, Any]) -> Dict[str, Any]:
    """Claude plugin/skills 설치"""
    try:
        git_url = params.get('git_url')
        if not git_url:
            raise Exception("git_url 파라미터가 필요합니다")
        
        plugin_name = params.get('plugin_name') or extract_repo_name(git_url)
        target_path = params.get('target_path', '.claude')
        
        # 파일 다운로드
        api_url = git_url.replace('https://github.com/', '').replace('http://github.com/', '').replace('.git', '')
        parts = api_url.split('/')
        owner, repo = parts[0], parts[1]
        
        plugin_config = fetch_plugin_config(owner, repo)
        files = download_plugin_files(git_url, plugin_name)
        plugin_info = read_plugin_info(git_url)
        
        # 설치
        skills_path = os.path.join(target_path, 'skills')
        ensure_directory_exists(skills_path)
        
        skill_paths = []
        for file_path, content in files.items():
            if file_path.startswith('skills/') and content:
                parts = file_path.split('/')
                if len(parts) >= 3:
                    skill_name = parts[1]
                    skill_file = '/'.join(parts[2:])
                    skill_dir = os.path.join(skills_path, skill_name)
                    ensure_directory_exists(skill_dir)
                    
                    file_full_path = os.path.join(skill_dir, skill_file)
                    ensure_directory_exists(os.path.dirname(file_full_path))
                    with open(file_full_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    if skill_dir not in skill_paths:
                        skill_paths.append(skill_dir)
        
        # plugin.json 저장
        if '.claude-plugin/plugin.json' in files and files['.claude-plugin/plugin.json']:
            plugin_dir = os.path.join(target_path, '.claude-plugin')
            ensure_directory_exists(plugin_dir)
            with open(os.path.join(plugin_dir, 'plugin.json'), 'w', encoding='utf-8') as f:
                f.write(files['.claude-plugin/plugin.json'])
        
        # 레지스트리 기록
        registry_info = {
            'name': plugin_name,
            'git_url': git_url,
            'owner': owner,
            'repo': repo,
            'target_path': target_path,
            'installed_at': datetime.now().isoformat(),
            'skills': [os.path.basename(p) for p in skill_paths],
            'status': 'installed'
        }
        add_to_registry(target_path, registry_info)
        
        return {
            'status': 'success',
            'action': 'install',
            'message': f"플러그인 '{plugin_name}'이(가) 성공적으로 설치되었습니다.",
            'install_path': os.path.join(target_path, 'skills'),
            'skills_count': len(set(skill_paths)),
            'skill_paths': list(set(skill_paths))
        }
    except Exception as error:
        return {
            'status': 'error',
            'action': 'install',
            'message': f"플러그인 설치 실패: {str(error)}"
        }


def uninstall_plugin(params: Dict[str, Any]) -> Dict[str, Any]:
    """설치된 skill 제거"""
    try:
        skill_name = params.get('skill_name')
        if not skill_name:
            raise Exception("skill_name 파라미터가 필요합니다")
        
        target_path = params.get('target_path', '.claude')
        skill_path = os.path.join(target_path, 'skills', skill_name)
        
        if not os.path.exists(skill_path):
            raise Exception(f"스킬 '{skill_name}'을(를) 찾을 수 없습니다")
        
        # 삭제
        deleted_files = []
        for root, dirs, files in os.walk(skill_path):
            for file in files:
                deleted_files.append(os.path.join(root, file))
        
        shutil.rmtree(skill_path)
        
        # 레지스트리 업데이트
        removed = remove_from_registry(target_path, skill_name)
        
        return {
            'status': 'success',
            'action': 'uninstall',
            'message': f"스킬 '{skill_name}'이(가) 성공적으로 제거되었습니다.",
            'removed_path': skill_path,
            'deleted_file_count': len(deleted_files),
            'registry_updated': removed
        }
    except Exception as error:
        return {
            'status': 'error',
            'action': 'uninstall',
            'message': f"스킬 제거 실패: {str(error)}"
        }


def list_plugins(params: Dict[str, Any]) -> Dict[str, Any]:
    """설치된 plugins 목록 조회"""
    try:
        target_path = params.get('target_path', '.claude')
        registry = load_registry(target_path)
        
        return {
            'status': 'success',
            'action': 'list',
            'message': f"{len(registry['plugins'])}개의 플러그인이 설치되어 있습니다.",
            'plugins': registry['plugins'],
            'last_updated': registry.get('last_updated'),
            'target_path': target_path
        }
    except Exception as error:
        return {
            'status': 'error',
            'action': 'list',
            'message': f"플러그인 목록 조회 실패: {str(error)}"
        }


def main(params: Dict[str, Any]) -> Dict[str, Any]:
    """메인 함수"""
    action = params.get('action', 'install')
    
    if action == 'install':
        return install_plugin(params)
    elif action == 'uninstall':
        return uninstall_plugin(params)
    elif action == 'list':
        return list_plugins(params)
    else:
        return {
            'status': 'error',
            'message': f"알 수 없는 action: {action}. (install, uninstall, list 중 선택)"
        }


if __name__ == '__main__':
    params = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
    result = main(params)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result['status'] == 'success' else 1)
