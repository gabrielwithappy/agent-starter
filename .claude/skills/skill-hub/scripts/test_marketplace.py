import urllib.request
import json

url = "https://raw.githubusercontent.com/anthropics/claude-code/main/.claude-plugin/marketplace.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Plugin-Manager'})

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        plugins = data.get('plugins', [])
        
        print(f"\n=== Anthropic Claude Code Marketplace ===")
        print(f"Total: {len(plugins)} plugins available\n")
        print("=" * 80)
        
        for idx, plugin in enumerate(plugins, 1):
            name = plugin.get('name', 'Unknown')
            desc = plugin.get('description', 'N/A')
            version = plugin.get('version', 'N/A')
            category = plugin.get('category', 'N/A')
            
            print(f"\n{idx}. {name}")
            print(f"   Description: {desc[:70]}...")
            print(f"   Version: {version}")
            print(f"   Category: {category}")
            
        print("\n" + "=" * 80)
        
except Exception as e:
    print(f"Error: {e}")
