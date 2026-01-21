---
name: apify-content-analytics
description: Track engagement metrics, measure campaign ROI, and analyze content performance across Instagram, Facebook, YouTube, and TikTok.
---

# Content Analytics

Track and analyze content performance using Apify Actors to extract engagement metrics from multiple platforms.

## Prerequisites

- `.env` file with `APIFY_TOKEN`
- Python 3.9+ and `uv`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Identify content analytics type (select Actor)
- [ ] Step 2: Read Actor schema from reference docs
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the analytics script
- [ ] Step 5: Summarize findings
```

### Step 1: Identify Content Analytics Type

Select the appropriate Actor based on analytics needs:

| User Need | Actor ID | Best For | Reference Doc |
|-----------|----------|----------|---------------|
| Post engagement metrics | `apify/instagram-post-scraper` | Post performance | [Schema](reference/actors/apify-instagram-post-scraper.md) |
| Reel performance | `apify/instagram-reel-scraper` | Reel analytics | [Schema](reference/actors/apify-instagram-reel-scraper.md) |
| Follower growth tracking | `apify/instagram-followers-count-scraper` | Growth metrics | [Schema](reference/actors/apify-instagram-followers-count-scraper.md) |
| Comment engagement | `apify/instagram-comment-scraper` | Comment analysis | [Schema](reference/actors/apify-instagram-comment-scraper.md) |
| Hashtag performance | `apify/instagram-hashtag-scraper` | Branded hashtags | [Schema](reference/actors/apify-instagram-hashtag-scraper.md) |
| Mention tracking | `apify/instagram-tagged-scraper` | Tag tracking | [Schema](reference/actors/apify-instagram-tagged-scraper.md) |
| Comprehensive metrics | `apify/instagram-scraper` | Full data | [Schema](reference/actors/apify-instagram-scraper.md) |
| API-based analytics | `apify/instagram-api-scraper` | API access | [Schema](reference/actors/apify-instagram-api-scraper.md) |
| Facebook post performance | `apify/facebook-posts-scraper` | Post metrics | [Schema](reference/actors/apify-facebook-posts-scraper.md) |
| Reaction analysis | `apify/facebook-likes-scraper` | Engagement types | [Schema](reference/actors/apify-facebook-likes-scraper.md) |
| Facebook Reels metrics | `apify/facebook-reels-scraper` | Reels performance | [Schema](reference/actors/apify-facebook-reels-scraper.md) |
| Ad performance tracking | `apify/facebook-ads-scraper` | Ad analytics | [Schema](reference/actors/apify-facebook-ads-scraper.md) |
| Facebook comment analysis | `apify/facebook-comments-scraper` | Comment engagement | [Schema](reference/actors/apify-facebook-comments-scraper.md) |
| Page performance audit | `apify/facebook-pages-scraper` | Page metrics | [Schema](reference/actors/apify-facebook-pages-scraper.md) |
| YouTube video metrics | `streamers/youtube-scraper` | Video performance | [Schema](reference/actors/streamers-youtube-scraper.md) |
| YouTube Shorts analytics | `streamers/youtube-shorts-scraper` | Shorts performance | [Schema](reference/actors/streamers-youtube-shorts-scraper.md) |
| TikTok content metrics | `clockworks/tiktok-scraper` | TikTok analytics | [Schema](reference/actors/clockworks-tiktok-scraper.md) |

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
2. **Output filename** (if file output selected): Suggest descriptive name based on analysis

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
- Number of content pieces analyzed
- File location
- Key performance insights
- Suggested next steps (deeper analysis, content optimization)

## Quick Examples

**Quick answer - display top 5 Instagram posts in chat:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-post-scraper" \
  --input '{"directUrls": ["https://www.instagram.com/p/ABC123/"], "resultsLimit": 10}'
```

**Instagram Reels performance - CSV with basic fields:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-reel-scraper" \
  --input '{"directUrls": ["https://www.instagram.com/reels/ABC123/"], "resultsLimit": 20}' \
  --output reels-analytics.csv \
  --format csv \
  --fields basic
```

**Facebook ad performance - full JSON export:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-ads-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/ads/library/?..."}]}' \
  --output ad-performance.json \
  --format json
```

**TikTok content metrics:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-scraper" \
  --input '{"profiles": ["username"], "resultsPerPage": 50}' \
  --output tiktok-analytics.csv \
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
