#!/usr/bin/env python3

"""
Plugin Marketplace Manager

설명: Claude Code 플러그인 마켓플레이스에서 플러그인을 검색하고 설치합니다.
기본 마켓플레이스: anthropics/claude-code

사용 예시:
검색:
python marketplace.py search "commit"

마켓플레이스 목록:
python marketplace.py list-marketplace

플러그인 설치 (이름으로):
python marketplace.py install-from-marketplace "commit-commands"
"""

import json
import os
import sys
import urllib.request
import urllib.error
from typing import Dict, Any, Optional, List

# 기본 마켓플레이스 설정
DEFAULT_MARKETPLACES = [
    {
        "name": "anthropics-claude-code",
        "source": "github",
        "repo": "anthropics/claude-code",
        "description": "Official Anthropic Claude Code demo marketplace"
    }
]


def get_marketplace_config_path() -> str:
    """마켓플레이스 설정 파일 경로 반환"""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_file = os.path.join(script_dir, 'assets', 'marketplaces.json')
    return config_file


def load_marketplaces() -> List[Dict[str, Any]]:
    """마켓플레이스 목록 로드"""
    config_path = get_marketplace_config_path()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('marketplaces', DEFAULT_MARKETPLACES)
        except Exception:
            pass
    
    return DEFAULT_MARKETPLACES


def save_marketplaces(marketplaces: List[Dict[str, Any]]) -> None:
    """마켓플레이스 목록 저장"""
    config_path = get_marketplace_config_path()
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump({
            'marketplaces': marketplaces,
            'last_updated': datetime.now().isoformat()
        }, f, indent=2, ensure_ascii=False)


def fetch_marketplace_json(owner: str, repo: str) -> Optional[Dict]:
    """GitHub에서 marketplace.json 파일 가져오기"""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/.claude-plugin/marketplace.json"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Plugin-Manager'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            return json.loads(content)
    except Exception as e:
        print(f"⚠️  마켓플레이스 파일을 가져올 수 없습니다: {e}")
        return None


def get_output_dir() -> str:
    """출력 디렉토리 경로 반환"""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(script_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def get_output_file_path(command_type: str, query: str = "") -> str:
    """타임스탬프가 포함된 출력 파일 경로 생성"""
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = get_output_dir()
    
    if command_type == 'search' and query:
        # 파일명에 사용할 수 없는 문자 제거
        safe_query = "".join(c for c in query if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_query = safe_query.replace(' ', '_')
        filename = f"search_{safe_query}_{timestamp}.txt"
    elif command_type == 'marketplace':
        filename = f"marketplace_{timestamp}.txt"
    else:
        filename = f"output_{timestamp}.txt"
    
    return os.path.join(output_dir, filename)


def cleanup_old_outputs(max_age_hours: int = 24) -> int:
    """오래된 출력 파일 삭제"""
    from datetime import datetime, timedelta
    
    output_dir = get_output_dir()
    cutoff_time = datetime.now() - timedelta(hours=max_age_hours)
    deleted_count = 0
    
    try:
        for filename in os.listdir(output_dir):
            if not filename.endswith('.txt'):
                continue
            
            file_path = os.path.join(output_dir, filename)
            if os.path.isfile(file_path):
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_time < cutoff_time:
                    os.remove(file_path)
                    deleted_count += 1
    except Exception:
        pass
    
    return deleted_count


def display_file_preview(file_path: str, max_lines: int = 50) -> None:
    """파일 내용 미리보기 표시"""
    print(f"\n{'='*80}")
    print(f"Results saved to: {file_path}")
    print(f"{'='*80}\n")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        preview_lines = lines[:max_lines]
        print(''.join(preview_lines))
        
        if len(lines) > max_lines:
            print(f"\n... ({len(lines) - max_lines} more lines)")
            print(f"\nTo view complete results, open: {file_path}")
    except Exception as e:
        print(f"Error displaying preview: {e}")


def search_plugins(query: str) -> List[Dict[str, Any]]:
    """모든 마켓플레이스에서 플러그인 검색"""
    marketplaces = load_marketplaces()
    results = []
    
    for marketplace in marketplaces:
        if marketplace['source'] == 'github':
            owner, repo = marketplace['repo'].split('/')
            marketplace_data = fetch_marketplace_json(owner, repo)
            
            if marketplace_data and 'plugins' in marketplace_data:
                for plugin in marketplace_data['plugins']:
                    plugin_name = plugin.get('name', '')
                    plugin_desc = plugin.get('description', '')
                    
                    if query.lower() in plugin_name.lower() or query.lower() in plugin_desc.lower():
                        results.append({
                            'name': plugin_name,
                            'description': plugin_desc,
                            'marketplace': marketplace['name'],
                            'source': plugin.get('source', {}),
                            'version': plugin.get('version', 'unknown')
                        })
    
    return results


def list_marketplace_plugins(marketplace_name: Optional[str] = None, output_file: Optional[str] = None) -> None:
    """마켓플레이스의 모든 플러그인 나열"""
    # Cleanup old files
    deleted = cleanup_old_outputs()
    if deleted > 0:
        print(f"Cleaned up {deleted} old output file(s)")
    
    # Auto-generate output file if not specified
    if not output_file:
        output_file = get_output_file_path('marketplace')
    
    marketplaces = load_marketplaces()
    output_lines = []
    
    for marketplace in marketplaces:
        if marketplace_name and marketplace['name'] != marketplace_name:
            continue
            
        header = f"\n=== Marketplace: {marketplace['name']} ==="
        repo_line = f"Repository: {marketplace['repo']}"
        separator = "=" * 80
        
        output_lines.append(header)
        output_lines.append(repo_line)
        output_lines.append(separator)
        
        if marketplace['source'] == 'github':
            owner, repo = marketplace['repo'].split('/')
            marketplace_data = fetch_marketplace_json(owner, repo)
            
            if marketplace_data and 'plugins' in marketplace_data:
                output_lines.append(f"\nTotal plugins: {len(marketplace_data['plugins'])}\n")
                
                for idx, plugin in enumerate(marketplace_data['plugins'], 1):
                    name = plugin.get('name', 'Unknown')
                    desc = plugin.get('description', 'N/A')
                    version = plugin.get('version', 'N/A')
                    category = plugin.get('category', 'N/A')
                    
                    output_lines.append(f"\n{idx}. {name}")
                    output_lines.append(f"   Description: {desc}")
                    output_lines.append(f"   Version: {version}")
                    output_lines.append(f"   Category: {category}")
                    
                    if 'author' in plugin:
                        author = plugin['author']
                        if isinstance(author, dict):
                            output_lines.append(f"   Author: {author.get('name', 'N/A')}")
                        else:
                            output_lines.append(f"   Author: {author}")
            else:
                output_lines.append("   No plugins found.")
        
        output_lines.append("\n" + separator)
    
    # Save to file
    output_text = '\n'.join(output_lines)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text)
    
    # Display preview
    display_file_preview(output_file)


def get_plugin_git_url(plugin_name: str, marketplace_name: Optional[str] = None) -> Optional[str]:
    """플러그인 이름으로 Git URL 찾기"""
    marketplaces = load_marketplaces()
    
    for marketplace in marketplaces:
        if marketplace_name and marketplace['name'] != marketplace_name:
            continue
            
        if marketplace['source'] == 'github':
            owner, repo = marketplace['repo'].split('/')
            marketplace_data = fetch_marketplace_json(owner, repo)
            
            if marketplace_data and 'plugins' in marketplace_data:
                for plugin in marketplace_data['plugins']:
                    if plugin.get('name') == plugin_name:
                        source = plugin.get('source', {})
                        
                        # GitHub 소스
                        if source.get('source') == 'github':
                            return f"https://github.com/{source.get('repo')}"
                        
                        # Git URL
                        elif source.get('source') == 'git':
                            return source.get('url')
                        
                        # 상대 경로 (마켓플레이스 저장소 내)
                        elif source.get('source') == 'path':
                            return f"https://github.com/{marketplace['repo']}"
    
    return None


def main():
    """메인 함수"""
    import argparse
    from datetime import datetime
    
    parser = argparse.ArgumentParser(
        description='Claude Code 플러그인 마켓플레이스 관리',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='action', help='수행할 작업')
    
    # Search subcommand
    search_parser = subparsers.add_parser('search', help='플러그인 검색')
    search_parser.add_argument('query', help='검색어')
    search_parser.add_argument('--output-file', '-o', help='결과를 파일로 저장')
    
    # List marketplace subcommand
    list_parser = subparsers.add_parser('list-marketplace', help='마켓플레이스 플러그인 목록')
    list_parser.add_argument('--marketplace', help='특정 마켓플레이스 이름')
    list_parser.add_argument('--output-file', '-o', help='결과를 파일로 저장')
    
    # Get plugin URL subcommand
    url_parser = subparsers.add_parser('get-url', help='플러그인 Git URL 가져오기')
    url_parser.add_argument('plugin_name', help='플러그인 이름')
    url_parser.add_argument('--marketplace', help='마켓플레이스 이름')
    
    args = parser.parse_args()
    
    if not args.action:
        parser.print_help()
        sys.exit(1)
    
    if args.action == 'search':
        # Cleanup old files
        deleted = cleanup_old_outputs()
        if deleted > 0:
            print(f"Cleaned up {deleted} old output file(s)")
        
        # Auto-generate output file if not specified
        output_file = args.output_file if hasattr(args, 'output_file') and args.output_file else get_output_file_path('search', args.query)
        
        results = search_plugins(args.query)
        output_lines = []
        
        if results:
            output_lines.append(f"\n=== Search Results for '{args.query}' ===")
            output_lines.append(f"Total: {len(results)} plugins found\n")
            output_lines.append("=" * 80)
            
            for idx, plugin in enumerate(results, 1):
                output_lines.append(f"\n{idx}. {plugin['name']}")
                output_lines.append(f"   Description: {plugin['description']}")
                output_lines.append(f"   Marketplace: {plugin['marketplace']}")
                output_lines.append(f"   Version: {plugin['version']}")
            
            output_lines.append("\n" + "=" * 80)
        else:
            output_lines.append(f"No results found for '{args.query}'")
        
        # Save to file
        output_text = '\n'.join(output_lines)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output_text)
        
        # Display preview
        display_file_preview(output_file)
    
    elif args.action == 'list-marketplace':
        output_file = args.output_file if hasattr(args, 'output_file') else None
        list_marketplace_plugins(args.marketplace, output_file)
    
    elif args.action == 'get-url':
        url = get_plugin_git_url(args.plugin_name, args.marketplace)
        if url:
            print(url)
        else:
            print(f"⚠️  플러그인 '{args.plugin_name}'을(를) 찾을 수 없습니다.", file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
