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

response = requests.get(url, timeout=30)
response.raise_for_status()

posts = response.json()

print(f"Retrieved {len(posts)} posts.\n")

for i, post in enumerate(posts, start=1):
    print(f"{i}. {post['title']['rendered']}")
