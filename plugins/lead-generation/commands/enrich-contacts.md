---
description: Extract contact details (emails, phones, socials) from website URLs
---

# Enrich Contacts from URLs

Extract emails, phone numbers, and social media profiles from a list of website URLs using Contact Details Scraper.

## User Input Required

Ask the user for:
1. **List of URLs** to scrape (one or more website URLs)
2. **Max pages per URL** (default: 20)
3. **Output format** (CSV or JSON, default: CSV)

## Execution

Run the lead finder script:

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "vdrmota~contact-info-scraper" \
  --input '{"startUrls": [{"url": "URL_1"}, {"url": "URL_2"}], "maxRequestsPerStartUrl": MAX_PAGES, "mergeContacts": true, "maxDepth": 2, "sameDomain": true}' \
  --output leads-contacts.FORMAT \
  --format FORMAT
```

Replace:
- `URL_1`, `URL_2` - User's website URLs
- `MAX_PAGES` - Pages to crawl per URL (default: 20)
- `FORMAT` - csv or json

The script handles token loading, polling, and result download automatically.

## Example

User wants: "Get contacts from example.com and test.com as JSON"

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "vdrmota~contact-info-scraper" \
  --input '{"startUrls": [{"url": "https://example.com"}, {"url": "https://test.com"}], "maxRequestsPerStartUrl": 20, "mergeContacts": true, "maxDepth": 2, "sameDomain": true}' \
  --output contacts.json \
  --format json
```

## Output Fields

| Field | Description |
|-------|-------------|
| domain | Website domain |
| emails | List of email addresses found |
| phones | List of phone numbers |
| linkedIns | LinkedIn profile URLs |
| twitters | Twitter/X profile URLs |
| instagrams | Instagram profile URLs |
| facebooks | Facebook page URLs |
| youtubes | YouTube channel URLs |
| tiktoks | TikTok profile URLs |
