---
description: Find local businesses via Google Maps and export to CSV or JSON
---

# Find Businesses on Google Maps

Find local businesses using Google Maps Scraper. Collect business names, addresses, phone numbers, websites, ratings, and reviews.

## User Input Required

Ask the user for:
1. **Search term** (e.g., "coffee shops", "restaurants", "gyms")
2. **Location** (e.g., "New York, USA", "London, UK")
3. **Number of results** (default: 50)
4. **Output format** (CSV or JSON, default: CSV)

## Execution

Run the lead finder script:

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "compass~crawler-google-places" \
  --input '{"searchStringsArray": ["SEARCH_TERM"], "locationQuery": "LOCATION", "maxCrawledPlacesPerSearch": MAX_RESULTS, "language": "en"}' \
  --output leads-businesses.FORMAT \
  --format FORMAT
```

Replace:
- `SEARCH_TERM` - User's search query
- `LOCATION` - Target location
- `MAX_RESULTS` - Number of results (default: 50)
- `FORMAT` - csv or json

The script handles token loading, polling, and result download automatically.

## Example

User wants: "50 Italian restaurants in Chicago, as JSON"

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "compass~crawler-google-places" \
  --input '{"searchStringsArray": ["Italian restaurants"], "locationQuery": "Chicago, USA", "maxCrawledPlacesPerSearch": 50, "language": "en"}' \
  --output italian-restaurants-chicago.json \
  --format json
```

## Output Fields

| Field | Description |
|-------|-------------|
| title | Business name |
| address | Full address |
| phone | Phone number |
| website | Business website |
| totalScore | Star rating (1-5) |
| reviewsCount | Number of reviews |
| categoryName | Business category |
| location.lat/lng | GPS coordinates |
