#!/usr/bin/env python3
"""
Notion API 테스트 스크립트
환경 변수에서 API 토큰과 페이지 ID를 읽어옵니다.
"""
import os
import sys
import io
import requests
import json

# Windows 인코딩 문제 해결
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def test_notion_api():
    """Notion API를 사용하여 블록 추가 테스트"""

    # 환경 변수에서 설정 읽기
    token = os.getenv('NOTION_API_TOKEN')
    page_id = os.getenv('NOTION_PAGE_ID')
    api_version = os.getenv('NOTION_API_VERSION', '2022-06-28')

    if not token or not page_id:
        print('[ERROR] 환경 변수가 설정되지 않았습니다.')
        print('필수 변수: NOTION_API_TOKEN, NOTION_PAGE_ID')
        print('\n사용법:')
        print('  1. .env 파일에 설정을 저장하거나')
        print('  2. 다음 명령으로 환경 변수 설정:')
        print('     export NOTION_API_TOKEN="your_token"')
        print('     export NOTION_PAGE_ID="your_page_id"')
        return False

    url = f"https://api.notion.com/v1/blocks/{page_id}/children"

    print(f'[INFO] URL: {url}')
    print(f'[INFO] Token: {token[:20]}...')

    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": api_version,
        "Content-Type": "application/json",
    }

    # 간단한 heading 테스트
    payload = {
        "children": [
            {
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "성공 기준"}
                        }
                    ]
                }
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f'\n[OK] Status: {response.status_code}')
        print(f'[INFO] Response: {response.text[:500]}')
        return response.status_code == 200
    except Exception as e:
        print(f'[ERROR] 요청 실패: {str(e)}')
        return False

if __name__ == '__main__':
    success = test_notion_api()
    sys.exit(0 if success else 1)
