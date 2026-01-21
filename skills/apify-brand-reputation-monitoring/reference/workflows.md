# Brand Reputation Monitoring Workflows

Multi-step workflows that combine multiple Actors for comprehensive brand reputation monitoring.

---

## Workflow 1: Multi-Platform Review Aggregation

Collect reviews from multiple platforms for a single brand/business.

### Checklist

```
Task Progress:
- [ ] Clarify brand name and platforms to monitor
- [ ] Step 1: Collect Google Maps reviews
- [ ] Step 2: Collect TripAdvisor reviews (if applicable)
- [ ] Step 3: Collect Facebook reviews
- [ ] Combine and analyze results
- [ ] Generate reputation summary
```

### Example Interaction

**User:** "Monitor reviews for Hilton Hotel in Times Square"

**Response:**
1. Collect Google Maps reviews for the location
2. Scrape TripAdvisor reviews for the property
3. Gather Facebook page reviews
4. Combine into unified report with:
   - Overall rating trends
   - Common praise themes
   - Common complaint themes
   - Sentiment breakdown

---

## Workflow 2: Social Media Brand Mention Tracking

Track brand mentions across social platforms.

### Checklist

```
Task Progress:
- [ ] Get brand name/hashtag from user
- [ ] Ask which platforms to monitor
- [ ] Step 1: Search Instagram hashtags and mentions
- [ ] Step 2: Scrape TikTok comments on brand content
- [ ] Step 3: Collect YouTube video comments
- [ ] Compile mention analysis
```

### Example Interaction

**User:** "Track mentions of #Nike across social media"

**Response:**
1. Ask: "Which platforms should I monitor? (Instagram, TikTok, YouTube)"
2. Step 1 - Instagram hashtag monitoring:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-scraper" \
  --input '{"hashtags": ["nike"], "resultsLimit": 100}' \
  --output nike-instagram-hashtags.json \
  --format json
```

3. Step 2 - Extract post URLs and get comments:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-comment-scraper" \
  --input '{"directUrls": ["https://www.instagram.com/p/..."], "resultsPerPost": 50}' \
  --output nike-instagram-comments.csv \
  --format csv
```

4. Report: "Found 100 posts with #nike hashtag. Analyzed 500 comments. Sentiment breakdown: 72% positive, 18% neutral, 10% negative. Top themes: quality, style, price."

---

## Workflow 3: Competitor Review Comparison

Compare reviews between your brand and competitors.

### Checklist

```
Task Progress:
- [ ] Get brand name and competitor names
- [ ] Select review platform (Google Maps, TripAdvisor, etc.)
- [ ] Step 1: Collect your brand's reviews
- [ ] Step 2: Collect competitor reviews
- [ ] Generate comparative analysis
```

### Example Interaction

**User:** "Compare reviews for Starbucks vs Dunkin in Boston"

**Response:**
1. Step 1 - Collect Starbucks reviews:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "compass/crawler-google-places" \
  --input '{"searchStringsArray": ["Starbucks"], "locationQuery": "Boston, MA", "maxCrawledPlacesPerSearch": 20}' \
  --output starbucks-boston.json \
  --format json
```

2. Step 2 - Collect Dunkin reviews:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "compass/crawler-google-places" \
  --input '{"searchStringsArray": ["Dunkin"], "locationQuery": "Boston, MA", "maxCrawledPlacesPerSearch": 20}' \
  --output dunkin-boston.json \
  --format json
```

3. Compare: Average ratings, review counts, common themes

---

## Workflow 4: Hotel/Travel Review Deep Dive

Comprehensive analysis of hotel reviews from multiple travel sites.

### Checklist

```
Task Progress:
- [ ] Get hotel name and location
- [ ] Step 1: Scrape Booking.com reviews
- [ ] Step 2: Scrape TripAdvisor reviews
- [ ] Step 3: Get Google Maps reviews
- [ ] Generate unified review report
```

### Example Interaction

**User:** "Get all reviews for The Plaza Hotel NYC"

**Response:**
1. Step 1 - Booking.com reviews:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "voyager/booking-reviews-scraper" \
  --input '{"hotelUrls": ["https://www.booking.com/hotel/us/the-plaza.html"], "maxReviews": 100}' \
  --output plaza-booking-reviews.csv \
  --format csv
```

2. Step 2 - TripAdvisor reviews:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "maxcopell/tripadvisor-reviews" \
  --input '{"startUrls": [{"url": "https://www.tripadvisor.com/Hotel_Review-..."}], "maxReviews": 100}' \
  --output plaza-tripadvisor-reviews.csv \
  --format csv
```

3. Report: Combined analysis of 200+ reviews across platforms

### Tips
- Compare ratings across platforms (Booking tends to score higher)
- Look for platform-specific feedback patterns
- Track review recency for trend analysis
- Identify staff-mentioned reviews for service quality insights

---

## Workflow 5: Facebook Engagement Analysis

Analyze engagement and sentiment on Facebook content.

### Checklist

```
Task Progress:
- [ ] Get Facebook page URL
- [ ] Step 1: Scrape page metrics and reviews
- [ ] Step 2: Get comments on recent posts
- [ ] Step 3: Analyze reaction types
- [ ] Generate engagement report
```

### Example Interaction

**User:** "Analyze engagement on Nike's Facebook page"

**Response:**
1. Step 1 - Get page overview and reviews:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-pages-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/nike"}]}' \
  --output nike-facebook-page.json \
  --format json
```

2. Step 2 - Get post comments:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-comments-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/nike/posts/..."}], "maxComments": 200}' \
  --output nike-comments.csv \
  --format csv
```

3. Report: Page followers, engagement rates, comment sentiment analysis
