---
name: apify-trend-analysis
description: Discover and track emerging trends across Google Trends, Instagram, Facebook, YouTube, and TikTok to inform content strategy.
---

# Trend Analysis

Discover and track emerging trends using Apify Actors to extract data from multiple platforms.

## Prerequisites

- `.env` file with `APIFY_TOKEN`
- Python 3.9+ and `uv`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Identify trend type (select Actor)
- [ ] Step 2: Read Actor schema from reference docs
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the analysis script
- [ ] Step 5: Summarize findings
```

### Step 1: Identify Trend Type

Select the appropriate Actor based on research needs:

| User Need | Actor ID | Best For | Reference Doc |
|-----------|----------|----------|---------------|
| Search trends | `apify/google-trends-scraper` | Google Trends data | [Schema](reference/actors/apify-google-trends-scraper.md) |
| Hashtag tracking | `apify/instagram-hashtag-scraper` | Hashtag content | [Schema](reference/actors/apify-instagram-hashtag-scraper.md) |
| Hashtag metrics | `apify/instagram-hashtag-stats` | Performance stats | [Schema](reference/actors/apify-instagram-hashtag-stats.md) |
| Visual trends | `apify/instagram-post-scraper` | Post analysis | [Schema](reference/actors/apify-instagram-post-scraper.md) |
| Trending discovery | `apify/instagram-search-scraper` | Search trends | [Schema](reference/actors/apify-instagram-search-scraper.md) |
| Comprehensive tracking | `apify/instagram-scraper` | Full data | [Schema](reference/actors/apify-instagram-scraper.md) |
| API-based trends | `apify/instagram-api-scraper` | API access | [Schema](reference/actors/apify-instagram-api-scraper.md) |
| Engagement trends | `apify/export-instagram-comments-posts` | Comment tracking | [Schema](reference/actors/apify-export-instagram-comments-posts.md) |
| Product trends | `apify/facebook-marketplace-scraper` | Marketplace data | [Schema](reference/actors/apify-facebook-marketplace-scraper.md) |
| Visual analysis | `apify/facebook-photos-scraper` | Photo trends | [Schema](reference/actors/apify-facebook-photos-scraper.md) |
| Community trends | `apify/facebook-groups-scraper` | Group monitoring | [Schema](reference/actors/apify-facebook-groups-scraper.md) |
| YouTube Shorts | `streamers/youtube-shorts-scraper` | Short-form trends | [Schema](reference/actors/streamers-youtube-shorts-scraper.md) |
| YouTube hashtags | `streamers/youtube-video-scraper-by-hashtag` | Hashtag videos | [Schema](reference/actors/streamers-youtube-video-scraper-by-hashtag.md) |
| TikTok hashtags | `clockworks/tiktok-hashtag-scraper` | Hashtag content | [Schema](reference/actors/clockworks-tiktok-hashtag-scraper.md) |
| Trending sounds | `clockworks/tiktok-sound-scraper` | Audio trends | [Schema](reference/actors/clockworks-tiktok-sound-scraper.md) |
| TikTok ads | `clockworks/tiktok-ads-scraper` | Ad trends | [Schema](reference/actors/clockworks-tiktok-ads-scraper.md) |
| Discover page | `clockworks/tiktok-discover-scraper` | Discover trends | [Schema](reference/actors/clockworks-tiktok-discover-scraper.md) |
| Explore trends | `clockworks/tiktok-explore-scraper` | Explore content | [Schema](reference/actors/clockworks-tiktok-explore-scraper.md) |
| Trending content | `clockworks/tiktok-trends-scraper` | Viral content | [Schema](reference/actors/clockworks-tiktok-trends-scraper.md) |

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
2. **Output filename** (if file output selected): Suggest descriptive name based on research

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

### Step 5: Summarize Findings

After completion, report:
- Number of results found
- File location
- Key trend insights
- Suggested next steps (deeper analysis, content opportunities)

## Quick Examples

**Quick answer - display top 5 trending topics:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/google-trends-scraper" \
  --input '{"searchTerms": ["AI tools", "ChatGPT", "Claude"], "geo": "US"}'
```

**Hashtag trend analysis - Instagram hashtag stats:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-stats" \
  --input '{"hashtags": ["fitness", "workout", "gym"]}' \
  --output hashtag-trends.json \
  --format json
```

**TikTok trending content:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-trends-scraper" \
  --input '{"maxItems": 50}' \
  --output tiktok-trends.csv \
  --format csv \
  --fields basic
```

**YouTube Shorts trends:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "streamers/youtube-shorts-scraper" \
  --input '{"searchQuery": "cooking tips", "maxResults": 50}' \
  --output youtube-shorts-trends.csv \
  --format csv
```

See [reference/workflows.md](reference/workflows.md) for detailed step-by-step guides for each use case.

## Error Handling

| Error | Solution |
|-------|----------|
| `APIFY_TOKEN not found` | Ask user to create `.env` with `APIFY_TOKEN=your_token` |
| `Actor not found` | Check Actor ID spelling |
| `Run FAILED` | Ask user to check Apify console link in error output |
| `Timeout` | Reduce input size or increase `--timeout` |
