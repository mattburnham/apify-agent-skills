---
description: Find leads from Facebook groups with buying intent
---

# Prospect Facebook Groups

Find potential leads from Facebook groups by identifying users showing buying intent, asking for recommendations, or discussing products.

## User Input Required

Ask the user for:
1. **Facebook Group URLs** (one or more group URLs)
2. **Number of posts to scan** (default: 100)
3. **Keywords for buying intent** (optional, e.g., "recommend", "looking for", "need help")
4. **Output format** (CSV or JSON, default: CSV)

## Execution

Run the lead finder script:

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "apify~facebook-groups-scraper" \
  --input '{"startUrls": [{"url": "GROUP_URL"}], "maxPosts": MAX_POSTS, "maxPostComments": 50, "maxReviews": 0}' \
  --output leads-groups.FORMAT \
  --format FORMAT
```

Replace:
- `GROUP_URL` - Facebook group URL
- `MAX_POSTS` - Number of posts to scan (default: 100)
- `FORMAT` - csv or json

The script handles token loading, polling, and result download automatically.

## Example

User wants: "Scan 200 posts from a marketing group, as JSON"

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "apify~facebook-groups-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/groups/marketinggroup"}], "maxPosts": 200, "maxPostComments": 50, "maxReviews": 0}' \
  --output marketing-group-posts.json \
  --format json
```

## Post-Processing: Filter for Buying Intent

After downloading, analyze the posts for buying intent signals. Suggest the user filter for these phrases:
- "recommend", "recommendations"
- "looking for", "searching for"
- "need help", "need advice"
- "where can I buy", "where to find"
- "anyone know", "does anyone"
- "best place to", "good place to"
- "suggestions", "thoughts on"

## Output Fields

| Field | Description |
|-------|-------------|
| text | Post content |
| authorName | Who posted |
| authorUrl | Link to author profile |
| likes | Number of likes |
| comments | Number of comments |
| shares | Number of shares |
| postUrl | Direct link to post |
| timestamp | When posted |
