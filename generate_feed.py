import json
import requests

# Load configuration
with open("config.json", encoding="utf-8") as file:
    config = json.load(file)

url = (
    f"{config['site']}/wp-json/wp/v2/posts"
    f"?_embed&per_page={config['posts_to_keep']}"
)

print(f"Fetching posts from:\n{url}\n")

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(
    url,
    headers=headers,
    timeout=30
)
response.raise_for_status()

posts = response.json()

print(f"Retrieved {len(posts)} posts.\n")

for i, post in enumerate(posts, start=1):
    print(f"{i}. {post['title']['rendered']}")
