import urllib.request
import json

url = "https://raw.githubusercontent.com/anthropics/claude-code/main/.claude-plugin/marketplace.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Plugin-Manager'})

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
        # Save to file
        with open('marketplace_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        plugins = data.get('plugins', [])
        print(f"Successfully fetched {len(plugins)} plugins")
        print("Data saved to marketplace_data.json")
        
except Exception as e:
    print(f"Error: {e}")
