---
name: apify-brand-reputation-monitoring
description: Track reviews, ratings, sentiment, and brand mentions across Google Maps, Booking.com, TripAdvisor, Facebook, Instagram, YouTube, and TikTok. Use when user asks to monitor brand reputation, analyze reviews, track mentions, or gather customer feedback.
---

# Brand Reputation Monitoring

Scrape reviews, ratings, and brand mentions from multiple platforms using Apify Actors.

## Prerequisites

- `.env` file with `APIFY_TOKEN`
- Python 3.9+ and `uv`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Determine data source (select Actor)
- [ ] Step 2: Read Actor schema from reference docs
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the monitoring script
- [ ] Step 5: Summarize results
```

### Step 1: Determine Data Source

Select the appropriate Actor based on user needs:

| User Need | Actor ID | Best For | Reference Doc |
|-----------|----------|----------|---------------|
| Google Maps reviews | `compass/crawler-google-places` | Business reviews, ratings | [Schema](reference/actors/compass-crawler-google-places.md) |
| Google Maps review export | `compass/Google-Maps-Reviews-Scraper` | Dedicated review scraping | [Schema](reference/actors/compass-google-maps-reviews-scraper.md) |
| Booking.com hotels | `voyager/booking-scraper` | Hotel data, scores | [Schema](reference/actors/voyager-booking-scraper.md) |
| Booking.com reviews | `voyager/booking-reviews-scraper` | Detailed hotel reviews | [Schema](reference/actors/voyager-booking-reviews-scraper.md) |
| TripAdvisor reviews | `maxcopell/tripadvisor-reviews` | Attraction/restaurant reviews | [Schema](reference/actors/maxcopell-tripadvisor-reviews.md) |
| Facebook reviews | `apify/facebook-reviews-scraper` | Page reviews | [Schema](reference/actors/apify-facebook-reviews-scraper.md) |
| Facebook comments | `apify/facebook-comments-scraper` | Post comment monitoring | [Schema](reference/actors/apify-facebook-comments-scraper.md) |
| Facebook page metrics | `apify/facebook-pages-scraper` | Page ratings overview | [Schema](reference/actors/apify-facebook-pages-scraper.md) |
| Facebook reactions | `apify/facebook-likes-scraper` | Reaction type analysis | [Schema](reference/actors/apify-facebook-likes-scraper.md) |
| Instagram comments | `apify/instagram-comment-scraper` | Comment sentiment | [Schema](reference/actors/apify-instagram-comment-scraper.md) |
| Instagram hashtags | `apify/instagram-hashtag-scraper` | Brand hashtag monitoring | [Schema](reference/actors/apify-instagram-hashtag-scraper.md) |
| Instagram search | `apify/instagram-search-scraper` | Brand mention discovery | [Schema](reference/actors/apify-instagram-search-scraper.md) |
| Instagram tagged posts | `apify/instagram-tagged-scraper` | Brand tag tracking | [Schema](reference/actors/apify-instagram-tagged-scraper.md) |
| Instagram export | `apify/export-instagram-comments-posts` | Bulk comment export | [Schema](reference/actors/apify-export-instagram-comments-posts.md) |
| Instagram comprehensive | `apify/instagram-scraper` | Full Instagram monitoring | [Schema](reference/actors/apify-instagram-scraper.md) |
| Instagram API | `apify/instagram-api-scraper` | API-based monitoring | [Schema](reference/actors/apify-instagram-api-scraper.md) |
| YouTube comments | `streamers/youtube-comments-scraper` | Video comment sentiment | [Schema](reference/actors/streamers-youtube-comments-scraper.md) |
| TikTok comments | `clockworks/tiktok-comments-scraper` | TikTok sentiment | [Schema](reference/actors/clockworks-tiktok-comments-scraper.md) |

### Step 2: Read Actor Schema

Read the corresponding reference doc from the table above to understand:
- Required and optional input parameters
- Output fields available
- Actor-specific requirements

### Step 3: Ask User Preferences

Before running, ask:
1. **Output format**:
   - **Quick answer** - Display top 5 results in chat (no file saved)
   - **CSV (all data)** - Full export with all fields
   - **CSV (basic fields)** - Export with essential fields only
   - **JSON (all data)** - Full export in JSON format
2. **Output filename** (if file output selected): Suggest descriptive name based on search

### Step 4: Run the Script

**Quick answer (display in chat, no file):**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**CSV (all data):**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output OUTPUT_FILE.csv \
  --format csv
```

**CSV (basic fields):**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output OUTPUT_FILE.csv \
  --format csv \
  --fields basic
```

**JSON (all data):**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output OUTPUT_FILE.json \
  --format json
```

The script handles:
- Loading `APIFY_TOKEN` from `.env`
- Starting and polling the Actor run
- Downloading results in requested format (or displaying in chat)
- Reporting record count and file size

### Step 5: Summarize Results

After completion, report:
- Number of reviews/mentions found
- File location
- Key fields available
- Suggested next steps (sentiment analysis, filtering)

## Quick Examples

**Quick answer - display top 5 in chat:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "compass/crawler-google-places" \
  --input '{"searchStringsArray": ["Starbucks"], "locationQuery": "New York, USA", "maxCrawledPlacesPerSearch": 20}'
```

**Google Maps reviews - CSV with basic fields:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "compass/Google-Maps-Reviews-Scraper" \
  --input '{"placeUrls": ["https://www.google.com/maps/place/..."], "maxReviews": 100}' \
  --output starbucks-reviews.csv \
  --format csv \
  --fields basic
```

**TripAdvisor reviews - full JSON export:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "maxcopell/tripadvisor-reviews" \
  --input '{"startUrls": [{"url": "https://www.tripadvisor.com/..."}], "maxReviews": 200}' \
  --output tripadvisor-reviews.json \
  --format json
```

See [reference/workflows.md](reference/workflows.md) for detailed step-by-step guides for each use case.

## Error Handling

| Error | Solution |
|-------|----------|
| `APIFY_TOKEN not found` | Ask user to create `.env` with `APIFY_TOKEN=your_token` |
| `Actor not found` | Check Actor ID spelling |
| `Run FAILED` | Ask user to check Apify console link in error output |
| `Timeout` | Reduce input size or increase `--timeout` |
