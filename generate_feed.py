from datetime import datetime, UTC
import json
import requests
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup
from src.html_cleaner import clean_html

# ---------------------------------------------------
# Load configuration
# ---------------------------------------------------

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

# ---------------------------------------------------
# Download posts
# ---------------------------------------------------

url = (
    f"{config['site']}/wp-json/wp/v2/posts"
    f"?_embed&per_page={config['posts_to_keep']}"
)

headers = {
    "User-Agent": "WordPress FullText RSS Generator"
}

response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

posts = response.json()

print(f"Retrieved {len(posts)} posts")

# ---------------------------------------------------
# Create RSS Feed
# ---------------------------------------------------

fg = FeedGenerator()

fg.title(config["title"])
fg.description(config["description"])
fg.link(href=config["site"])
fg.language("en")

for post in posts:

    title = BeautifulSoup(
        post["title"]["rendered"],
        "html.parser"
    ).get_text()

    content = clean_html(post["content"]["rendered"])

    entry = fg.add_entry()

    entry.guid(post["link"], permalink=True)
    entry.title(title)
    entry.link(href=post["link"])

    # FULL ARTICLE
    entry.content(content, type="CDATA")

    published = datetime.fromisoformat(post["date_gmt"]).replace(tzinfo=UTC)

    entry.pubDate(published)

# ---------------------------------------------------
# Save
# ---------------------------------------------------

from pathlib import Path

output = Path(config["output_folder"])
output.mkdir(exist_ok=True)

fg.rss_file(output / "feed.xml")

print("feed.xml generated successfully!")