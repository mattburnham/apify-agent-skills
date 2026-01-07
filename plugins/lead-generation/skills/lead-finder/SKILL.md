---
name: lead-finder
description: Generate B2B/B2C leads using Apify web scrapers. Use when user asks to find leads, prospects, businesses, contacts, build a lead list, or enrich contact data.
---

# Lead Finder Skill

When the user asks for leads, prospects, business contacts, or wants to build a lead list, use the Apify lead-finder scripts.

## Prerequisites

- `.env` file must contain `APIFY_TOKEN` (the script loads it automatically at runtime)
- Python 3.9+ and `uv` must be available

## When to Use This Skill

Trigger this skill when the user asks about:
- Finding leads or prospects
- Building a lead list
- Finding local businesses
- Getting contact information (emails, phones)
- Enriching existing data with contacts
- Scraping social media profiles
- Finding buying intent in groups/communities

## Workflow

### Step 1: Determine Lead Source

Based on user request, select the appropriate actor:

| User Need | Actor ID |
|-----------|----------|
| Local businesses (restaurants, gyms, etc.) | `compass~crawler-google-places` |
| Contact details from URLs | `vdrmota~contact-info-scraper` |
| Instagram profiles | `apify~instagram-profile-scraper` |
| TikTok profiles | `clockworks~tiktok-profile-scraper` |
| Facebook pages | `apify~facebook-pages-scraper` |
| Facebook group posts | `apify~facebook-groups-scraper` |

### Step 2: Ask User Preferences

Before running, ask the user:
1. **Output format**: "Would you like the results in CSV or JSON?" (default: CSV)
2. **Output filename**: Suggest a descriptive name based on the search

### Step 3: Run the Lead Finder Script

Execute the Python script using `uv run`:

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output OUTPUT_FILE \
  --format csv|json
```

The script handles:
- Loading `APIFY_TOKEN` from `.env` automatically
- Starting the actor run
- Polling for completion (every 5 seconds)
- Downloading results in the requested format
- Reporting record count and file size

### Step 4: Summarize Results

After the script completes, report to user:
- Number of leads found
- File location
- Key fields available in the data
- Suggest next steps (filtering, enrichment)

## Examples

### Google Maps - Find Local Businesses

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "compass~crawler-google-places" \
  --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA", "maxCrawledPlacesPerSearch": 50, "language": "en"}' \
  --output coffee-shops-seattle.csv \
  --format csv
```

**Output fields**: title, address, phone, website, totalScore, reviewsCount, categoryName

### Contact Details - Extract from Websites

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "vdrmota~contact-info-scraper" \
  --input '{"startUrls": [{"url": "https://example.com"}, {"url": "https://test.com"}], "maxRequestsPerStartUrl": 20, "mergeContacts": true}' \
  --output contacts.json \
  --format json
```

**Output fields**: domain, emails, phones, linkedIns, twitters, instagrams, facebooks

### Instagram - Scrape Profiles

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "apify~instagram-profile-scraper" \
  --input '{"usernames": ["nike", "adidas"]}' \
  --output instagram-profiles.csv \
  --format csv
```

**Output fields**: username, fullName, biography, followersCount, postsCount, isVerified

### Facebook Groups - Find Buying Intent

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "apify~facebook-groups-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/groups/example"}], "maxPosts": 100}' \
  --output group-posts.json \
  --format json
```

**Output fields**: text, authorName, authorUrl, likes, comments, shares, postUrl

## Error Handling

The script provides clear error messages:

| Error | Meaning |
|-------|---------|
| "APIFY_TOKEN not found in .env file" | Create `.env` with your token |
| "Actor not found" | Check actor ID spelling |
| "Run FAILED" | Check Apify console link for details |
| "Timeout" | Actor took too long, try smaller input |

If errors occur, help the user:
1. Verify `.env` file exists with `APIFY_TOKEN=...`
2. Check the Apify console link provided in error
3. Adjust input parameters if needed

## Example Interactions

**User:** "Find me coffee shops in Seattle"
**Action:** Ask format preference, then run Google Maps scraper

**User:** "Get contact info from these websites: example.com, test.com - give me JSON"
**Action:** Run Contact Details scraper with JSON format

**User:** "Find Instagram influencers in the fitness niche"
**Action:** Ask for specific usernames or search terms, then run Instagram scraper

**User:** "Build a lead list for my B2B SaaS product"
**Action:** Ask clarifying questions about target industry, then use appropriate scraper
