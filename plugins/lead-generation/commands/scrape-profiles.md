---
description: Scrape social media profiles for lead enrichment (Instagram, TikTok, Facebook)
---

# Scrape Social Media Profiles

Scrape social media profiles to collect follower counts, contact info, and engagement metrics for lead enrichment.

## User Input Required

Ask the user for:
1. **Platform** (Instagram, TikTok, or Facebook)
2. **Usernames or search query**
3. **Number of profiles** (default: 50)
4. **Output format** (CSV or JSON, default: CSV)

## Execution by Platform

### Instagram Profiles

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "apify~instagram-profile-scraper" \
  --input '{"usernames": ["USERNAME_1", "USERNAME_2"], "resultsLimit": 50}' \
  --output instagram-profiles.FORMAT \
  --format FORMAT
```

### TikTok Profiles

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "clockworks~tiktok-profile-scraper" \
  --input '{"profiles": ["USERNAME_1", "USERNAME_2"], "resultsPerPage": 50}' \
  --output tiktok-profiles.FORMAT \
  --format FORMAT
```

### Facebook Pages

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "apify~facebook-pages-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/PAGE_NAME"}]}' \
  --output facebook-pages.FORMAT \
  --format FORMAT
```

The script handles token loading, polling, and result download automatically.

## Example

User wants: "Scrape Nike and Adidas Instagram profiles as CSV"

```bash
uv run --with python-dotenv --with requests ${CLAUDE_PLUGIN_ROOT}/skills/lead-finder/scripts/run_actor.py \
  --actor "apify~instagram-profile-scraper" \
  --input '{"usernames": ["nike", "adidas"], "resultsLimit": 50}' \
  --output nike-adidas-instagram.csv \
  --format csv
```

## Output Fields by Platform

### Instagram
| Field | Description |
|-------|-------------|
| username | Instagram handle |
| fullName | Display name |
| followersCount | Number of followers |
| followsCount | Number following |
| postsCount | Total posts |
| biography | Bio text |
| externalUrl | Website in bio |
| businessEmail | Contact email (if available) |

### TikTok
| Field | Description |
|-------|-------------|
| uniqueId | TikTok username |
| nickname | Display name |
| followerCount | Number of followers |
| followingCount | Number following |
| videoCount | Total videos |
| signature | Bio text |

### Facebook
| Field | Description |
|-------|-------------|
| name | Page name |
| likes | Page likes |
| followers | Page followers |
| about | Page description |
| phone | Contact phone |
| email | Contact email |
| website | Website URL |
