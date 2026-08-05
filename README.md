# WordPress Full-Text RSS Generator

Generate a full-text RSS feed from any WordPress website that exposes the WordPress REST API.

This project was created to generate a high-quality RSS feed for websites that have disabled or removed their native RSS feed while still exposing their content through the WordPress REST API.

## Features

- Fetches posts via the WordPress REST API
- Generates a valid RSS 2.0 feed
- Includes full article content
- Fixes lazy-loaded images
- Removes unwanted website widgets from articles
- Configurable through `config.json`
- Designed for use with readers such as Readwise Reader

## Requirements

- Python 3.11+
- pip

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Edit `config.json`:

```json
{
  "site": "https://bikozulu.co.ke",
  "title": "Biko Zulu",
  "description": "Full-text RSS feed generated from the WordPress REST API",
  "posts_to_keep": 30
}
```

## Generate the feed

Run:

```bash
python generate_feed.py
```

The generated feed is written to:

```
docs/feed.xml
```

## Planned Improvements

- Featured images
- Author metadata
- Categories and tags
- Better RSS metadata
- Multi-site support
- Automatic publishing to GitHub Pages
- Windows Task Scheduler automation

## License

MIT