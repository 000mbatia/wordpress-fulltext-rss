import json
import requests

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

url = (
    f"{config['site']}/wp-json/wp/v2/posts"
    f"?_embed&per_page={config['posts_to_keep']}"
)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

print("\nHeaders:")
for k, v in response.headers.items():
    print(f"{k}: {v}")

print("\nBody:")
print(response.text[:2000])
