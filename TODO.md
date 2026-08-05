# WordPress REST API RSS Generator Roadmap

## Version 0.1.0 (Current)

### Feed Generation
- [x] Fetch posts from the WordPress REST API
- [x] Generate valid RSS 2.0
- [x] Include full article HTML
- [x] Preserve publication dates
- [x] Configurable via config.json

### HTML Cleaning
- [x] Remove Like/Dislike widget
- [x] Fix lazy-loaded images
- [x] Remove unnecessary image attributes

### Publishing
- [x] Git repository
- [x] GitHub Pages support
- [ ] Verify in Readwise Reader

---

## Version 0.2.0

### RSS Improvements
- [ ] Use content:encoded
- [ ] Short summary in description
- [ ] Add author
- [ ] Add categories
- [ ] Add tags
- [ ] Add last modified date
- [ ] Feed logo

### HTML Improvements
- [ ] Better image handling
- [ ] Remove unnecessary WordPress classes
- [ ] Improve code block formatting

---

## Version 0.3.0

### Automation
- [ ] Windows Task Scheduler
- [ ] Automatic git commit
- [ ] Automatic git push

---

## Version 0.4.0

### Multiple Sites
- [ ] Support multiple WordPress sites
- [ ] Generate multiple RSS feeds
- [ ] Shared HTML cleaner

---

## Future Ideas

- [ ] CLI interface
- [ ] Docker support
- [ ] OPML export
- [ ] Unit tests
- [ ] Logging
- [ ] Retry/backoff for failed requests