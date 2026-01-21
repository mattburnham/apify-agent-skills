# Trend Analysis Workflows

Multi-step workflows that combine multiple Actors for comprehensive trend discovery and analysis.

---

## Workflow 1: Cross-Platform Trend Discovery

Discover trending topics across multiple platforms to identify viral content opportunities.

### Checklist

```
Task Progress:
- [ ] Get topic/keyword from user
- [ ] Step 1: Run Google Trends for search interest
- [ ] Step 2: Run TikTok Trends Scraper for viral content
- [ ] Step 3: Run Instagram Hashtag Stats for social validation
- [ ] Analyze cross-platform trend alignment
- [ ] Generate trend report with content opportunities
```

### Example Interaction

**User:** "What's trending in the fitness space right now?"

**Response:**
1. Step 1 - Check Google Trends:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/google-trends-scraper" \
  --input '{"searchTerms": ["HIIT workout", "pilates", "strength training", "walking workout"], "geo": "US"}' \
  --output fitness-search-trends.json \
  --format json
```

2. Step 2 - Check TikTok viral content:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-trends-scraper" \
  --input '{"maxItems": 50}' \
  --output tiktok-trending.csv \
  --format csv \
  --fields basic
```

3. Step 3 - Validate with Instagram:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-stats" \
  --input '{"hashtags": ["fitness", "workout", "gym", "fitnessmotivation"]}' \
  --output instagram-hashtag-stats.json \
  --format json
```

4. Report: "Walking workouts up 120% on Google Trends. #walkingworkout has 2.1M TikTok views daily. Instagram #fitness at 500M posts with 1.2% weekly growth."

---

## Workflow 2: Hashtag Trend Analysis

Deep dive into hashtag performance across Instagram and TikTok.

### Checklist

```
Task Progress:
- [ ] Get hashtags/niche from user
- [ ] Step 1: Run Instagram Hashtag Stats for volume
- [ ] Step 2: Run Instagram Hashtag Scraper for content
- [ ] Step 3: Run TikTok Hashtag Scraper for comparison
- [ ] Analyze engagement rates and content themes
- [ ] Generate hashtag strategy report
```

### Example Interaction

**User:** "Analyze hashtag trends for sustainable living content"

**Response:**
1. Step 1 - Get hashtag volume:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-stats" \
  --input '{"hashtags": ["sustainableliving", "zerowaste", "ecofriendly", "sustainable"]}' \
  --output sustainable-hashtag-stats.json \
  --format json
```

2. Step 2 - Analyze top content:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-scraper" \
  --input '{"hashtags": ["sustainableliving"], "resultsLimit": 100}' \
  --output sustainable-instagram-posts.csv \
  --format csv \
  --fields basic
```

3. Step 3 - Compare with TikTok:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-hashtag-scraper" \
  --input '{"hashtags": ["sustainableliving"], "resultsPerPage": 100}' \
  --output sustainable-tiktok-posts.csv \
  --format csv \
  --fields basic
```

---

## Workflow 3: YouTube Shorts Trend Research

Identify trending short-form video content on YouTube.

### Checklist

```
Task Progress:
- [ ] Get topic/niche from user
- [ ] Step 1: Run YouTube Shorts Scraper for trending content
- [ ] Step 2: Run YouTube Video Scraper by Hashtag for hashtag trends
- [ ] Analyze view counts and engagement patterns
- [ ] Identify content gaps and opportunities
```

### Example Interaction

**User:** "What cooking content is trending on YouTube Shorts?"

**Response:**
1. Step 1 - Get trending Shorts:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "streamers/youtube-shorts-scraper" \
  --input '{"searchQuery": "cooking recipe", "maxResults": 50}' \
  --output cooking-shorts.csv \
  --format csv \
  --fields basic
```

2. Step 2 - Check hashtag trends:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "streamers/youtube-video-scraper-by-hashtag" \
  --input '{"hashtag": "cooking", "maxResults": 50}' \
  --output cooking-hashtag-videos.csv \
  --format csv
```

3. Report: "Top performing: 30-second recipes, kitchen hacks, meal prep. Average views: 500K. Best posting times: 6-8 PM. Trending formats: POV cooking, ASMR prep."

---

## Workflow 4: TikTok Sound and Music Trends

Track trending sounds and music on TikTok for content creation.

### Checklist

```
Task Progress:
- [ ] Step 1: Run TikTok Trends Scraper for trending content
- [ ] Step 2: Run TikTok Sound Scraper for specific sounds
- [ ] Step 3: Run TikTok Discover Scraper for emerging trends
- [ ] Identify trending audio and music patterns
- [ ] Generate sound trend report
```

### Example Interaction

**User:** "What sounds are trending on TikTok right now?"

**Response:**
1. Step 1 - Get overall trending content:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-trends-scraper" \
  --input '{"maxItems": 100}' \
  --output tiktok-trends.json \
  --format json
```

2. Step 2 - Explore discover page:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-discover-scraper" \
  --input '{"maxItems": 50}' \
  --output tiktok-discover.json \
  --format json
```

3. Analyze: Extract music metadata, identify recurring sounds, track usage counts.

---

## Workflow 5: Product Trend Research

Identify trending products using Facebook Marketplace and social signals.

### Checklist

```
Task Progress:
- [ ] Get product category from user
- [ ] Step 1: Run Facebook Marketplace Scraper for demand signals
- [ ] Step 2: Run Instagram Hashtag Scraper for product content
- [ ] Step 3: Run TikTok Hashtag Scraper for viral products
- [ ] Analyze pricing trends and demand patterns
- [ ] Generate product trend report
```

### Example Interaction

**User:** "What home decor products are trending?"

**Response:**
1. Step 1 - Check Marketplace demand:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-marketplace-scraper" \
  --input '{"searchQuery": "home decor", "location": "United States", "maxItems": 100}' \
  --output marketplace-decor.csv \
  --format csv \
  --fields basic
```

2. Step 2 - Check Instagram trends:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-scraper" \
  --input '{"hashtags": ["homedecor", "interiordesign"], "resultsLimit": 100}' \
  --output decor-instagram.csv \
  --format csv \
  --fields basic
```

3. Report: "Trending: Minimalist shelving, LED strip lights, vintage mirrors. Price range: $30-150. Top sellers: Scandinavian style, boho accents."

---

## Workflow 6: Community Trend Monitoring

Track emerging trends through Facebook Groups and community discussions.

### Checklist

```
Task Progress:
- [ ] Get topic/interest area from user
- [ ] Step 1: Run Facebook Groups Scraper for community activity
- [ ] Step 2: Run Instagram Search Scraper for related content
- [ ] Analyze discussion themes and sentiment
- [ ] Identify emerging trends from community signals
```

### Example Interaction

**User:** "What trends are emerging in the DIY crafts community?"

**Response:**
1. Step 1 - Find active craft groups:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-groups-scraper" \
  --input '{"searchQuery": "DIY crafts handmade", "maxItems": 50}' \
  --output craft-groups.json \
  --format json
```

2. Step 2 - Check Instagram content:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-search-scraper" \
  --input '{"search": "DIY crafts 2024", "resultsLimit": 100}' \
  --output craft-search.csv \
  --format csv
```

3. Report: "Growing communities: Resin art (250K members), punch needle (180K members). Trending: Tufting, beaded jewelry, upcycled fashion."

---

## Workflow 7: TikTok Advertising Trends

Analyze TikTok advertising trends and successful ad formats.

### Checklist

```
Task Progress:
- [ ] Get industry/niche from user
- [ ] Step 1: Run TikTok Ads Scraper for ad content
- [ ] Step 2: Run TikTok Explore Scraper for organic benchmarks
- [ ] Analyze ad formats and performance
- [ ] Generate advertising trend report
```

### Example Interaction

**User:** "What TikTok ad formats are working for beauty brands?"

**Response:**
1. Step 1 - Analyze beauty ads:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-ads-scraper" \
  --input '{"searchQuery": "beauty skincare", "maxItems": 50}' \
  --output beauty-ads.csv \
  --format csv \
  --fields basic
```

2. Step 2 - Compare with organic content:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-explore-scraper" \
  --input '{"maxItems": 50}' \
  --output tiktok-explore.csv \
  --format csv \
  --fields basic
```

3. Report: "Top ad formats: Before/after transformations, GRWM, ingredient education. Average engagement: 4.2%. Best performing: UGC-style content, creator partnerships."

---

## Tips for Trend Analysis

- **Multi-platform validation**: Confirm trends across 2-3 platforms before acting
- **Velocity matters**: Look for acceleration in engagement, not just volume
- **Regional variations**: Trends often start in specific markets before going global
- **Content format trends**: Track not just topics but how content is presented
- **Sound/music tracking**: Audio trends on TikTok often precede visual trends
- **Community signals**: Facebook Groups often surface trends before mainstream
- **Seasonal patterns**: Account for recurring seasonal interest spikes
- **Early adopter signals**: Small but growing engagement often indicates emerging trends
