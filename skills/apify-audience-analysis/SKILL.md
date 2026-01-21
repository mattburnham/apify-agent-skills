---
name: apify-audience-analysis
description: Understand audience demographics, preferences, behavior patterns, and engagement quality across Facebook, Instagram, YouTube, and TikTok.
---

# Audience Analysis

Analyze and understand your audience using Apify Actors to extract follower demographics, engagement patterns, and behavior data from multiple platforms.

## Prerequisites

- `.env` file with `APIFY_TOKEN`
- Python 3.9+ and `uv`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Identify audience analysis type (select Actor)
- [ ] Step 2: Read Actor schema from reference docs
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the analysis script
- [ ] Step 5: Summarize findings
```

### Step 1: Identify Audience Analysis Type

Select the appropriate Actor based on analysis needs:

| User Need | Actor ID | Best For | Reference Doc |
|-----------|----------|----------|---------------|
| Facebook follower demographics | `apify/facebook-followers-following-scraper` | FB followers/following lists | [Schema](reference/actors/apify-facebook-followers-following-scraper.md) |
| Facebook engagement behavior | `apify/facebook-likes-scraper` | FB post likes analysis | [Schema](reference/actors/apify-facebook-likes-scraper.md) |
| Facebook video audience | `apify/facebook-reels-scraper` | FB Reels viewers | [Schema](reference/actors/apify-facebook-reels-scraper.md) |
| Facebook comment analysis | `apify/facebook-comments-scraper` | FB post/video comments | [Schema](reference/actors/apify-facebook-comments-scraper.md) |
| Facebook content engagement | `apify/facebook-posts-scraper` | FB post engagement metrics | [Schema](reference/actors/apify-facebook-posts-scraper.md) |
| Instagram audience sizing | `apify/instagram-profile-scraper` | IG profile demographics | [Schema](reference/actors/apify-instagram-profile-scraper.md) |
| Instagram location-based | `apify/instagram-search-scraper` | IG geo-tagged audience | [Schema](reference/actors/apify-instagram-search-scraper.md) |
| Instagram tagged network | `apify/instagram-tagged-scraper` | IG tag network analysis | [Schema](reference/actors/apify-instagram-tagged-scraper.md) |
| Instagram comprehensive | `apify/instagram-scraper` | Full IG audience data | [Schema](reference/actors/apify-instagram-scraper.md) |
| Instagram API-based | `apify/instagram-api-scraper` | IG API access | [Schema](reference/actors/apify-instagram-api-scraper.md) |
| Instagram follower counts | `apify/instagram-followers-count-scraper` | IG follower tracking | [Schema](reference/actors/apify-instagram-followers-count-scraper.md) |
| Instagram comment export | `apify/export-instagram-comments-posts` | IG comment bulk export | [Schema](reference/actors/apify-export-instagram-comments-posts.md) |
| Instagram comment analysis | `apify/instagram-comment-scraper` | IG comment sentiment | [Schema](reference/actors/apify-instagram-comment-scraper.md) |
| YouTube viewer feedback | `streamers/youtube-comments-scraper` | YT comment analysis | [Schema](reference/actors/streamers-youtube-comments-scraper.md) |
| YouTube channel audience | `streamers/youtube-channel-scraper` | YT channel subscribers | [Schema](reference/actors/streamers-youtube-channel-scraper.md) |
| TikTok follower demographics | `clockworks/tiktok-followers-scraper` | TT follower lists | [Schema](reference/actors/clockworks-tiktok-followers-scraper.md) |
| TikTok profile analysis | `clockworks/tiktok-profile-scraper` | TT profile demographics | [Schema](reference/actors/clockworks-tiktok-profile-scraper.md) |
| TikTok comment analysis | `clockworks/tiktok-comments-scraper` | TT comment engagement | [Schema](reference/actors/clockworks-tiktok-comments-scraper.md) |

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
- Number of audience members/profiles analyzed
- File location
- Key demographic insights
- Suggested next steps (deeper analysis, segmentation)

## Quick Examples

**Quick answer - display top 5 Facebook followers in chat:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-followers-following-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/profile/123/followers"}], "resultsLimit": 50}'
```

**Instagram audience profile - CSV with basic fields:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-profile-scraper" \
  --input '{"usernames": ["username1", "username2"]}' \
  --output audience-profiles.csv \
  --format csv \
  --fields basic
```

**TikTok follower analysis - full JSON export:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-followers-scraper" \
  --input '{"profiles": ["username"], "resultsPerPage": 100}' \
  --output tiktok-followers.json \
  --format json
```

**YouTube comment sentiment analysis:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "streamers/youtube-comments-scraper" \
  --input '{"startUrls": [{"url": "https://www.youtube.com/watch?v=VIDEO_ID"}], "maxComments": 200}' \
  --output youtube-comments.csv \
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
