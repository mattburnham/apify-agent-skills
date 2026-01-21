---
name: apify-market-research
description: Analyze market conditions, geographic opportunities, pricing, consumer behavior, and product validation across Google Maps, Facebook, Instagram, Booking.com, and TripAdvisor.
---

# Market Research

Conduct market research using Apify Actors to extract data from multiple platforms.

## Prerequisites

- `.env` file with `APIFY_TOKEN`
- Python 3.9+ and `uv`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Identify market research type (select Actor)
- [ ] Step 2: Read Actor schema from reference docs
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the analysis script
- [ ] Step 5: Summarize findings
```

### Step 1: Identify Market Research Type

Select the appropriate Actor based on research needs:

| User Need | Actor ID | Best For | Reference Doc |
|-----------|----------|----------|---------------|
| Market density | `compass/crawler-google-places` | Location analysis | [Schema](reference/actors/compass-crawler-google-places.md) |
| Geospatial analysis | `compass/google-maps-extractor` | Business mapping | [Schema](reference/actors/compass-google-maps-extractor.md) |
| Regional interest | `apify/google-trends-scraper` | Trend data | [Schema](reference/actors/apify-google-trends-scraper.md) |
| Pricing and demand | `apify/facebook-marketplace-scraper` | Market pricing | [Schema](reference/actors/apify-facebook-marketplace-scraper.md) |
| Event market | `apify/facebook-events-scraper` | Event analysis | [Schema](reference/actors/apify-facebook-events-scraper.md) |
| Consumer needs | `apify/facebook-groups-scraper` | Group research | [Schema](reference/actors/apify-facebook-groups-scraper.md) |
| Market landscape | `apify/facebook-pages-scraper` | Business pages | [Schema](reference/actors/apify-facebook-pages-scraper.md) |
| Business density | `apify/facebook-page-contact-information` | Contact data | [Schema](reference/actors/apify-facebook-page-contact-information.md) |
| Cultural insights | `apify/facebook-photos-scraper` | Visual research | [Schema](reference/actors/apify-facebook-photos-scraper.md) |
| Niche targeting | `apify/instagram-hashtag-scraper` | Hashtag research | [Schema](reference/actors/apify-instagram-hashtag-scraper.md) |
| Hashtag stats | `apify/instagram-hashtag-stats` | Market sizing | [Schema](reference/actors/apify-instagram-hashtag-stats.md) |
| Market activity | `apify/instagram-reel-scraper` | Activity analysis | [Schema](reference/actors/apify-instagram-reel-scraper.md) |
| Market intelligence | `apify/instagram-scraper` | Full data | [Schema](reference/actors/apify-instagram-scraper.md) |
| Product launch research | `apify/instagram-api-scraper` | API access | [Schema](reference/actors/apify-instagram-api-scraper.md) |
| Hospitality market | `voyager/booking-scraper` | Hotel data | [Schema](reference/actors/voyager-booking-scraper.md) |
| Tourism insights | `maxcopell/tripadvisor-reviews` | Review analysis | [Schema](reference/actors/maxcopell-tripadvisor-reviews.md) |

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
- Key market insights
- Suggested next steps (deeper analysis, validation)

## Quick Examples

**Quick answer - display top 5 businesses in a market:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "compass/crawler-google-places" \
  --input '{"searchStringsArray": ["yoga studio"], "locationQuery": "Austin, Texas", "maxCrawledPlacesPerSearch": 50}'
```

**Market pricing research - Facebook Marketplace CSV:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-marketplace-scraper" \
  --input '{"searchQuery": "vintage furniture", "location": "Los Angeles", "maxItems": 100}' \
  --output market-pricing.csv \
  --format csv \
  --fields basic
```

**Hashtag market sizing - Instagram hashtag stats:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-stats" \
  --input '{"hashtags": ["sustainablefashion", "ethicalfashion", "slowfashion"]}' \
  --output hashtag-market-size.json \
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
