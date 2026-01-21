# Content Analytics Workflows

Multi-step workflows that combine multiple Actors for comprehensive content performance analysis.

---

## Workflow 1: Instagram Content Performance Analysis

Track engagement metrics across posts, reels, and comments.

### Checklist

```
Task Progress:
- [ ] Get Instagram content URLs or usernames
- [ ] Step 1: Run Post Scraper for post metrics
- [ ] Step 2: Run Reel Scraper for reel performance
- [ ] Step 3: Analyze engagement patterns
- [ ] Generate performance report
```

### Example Interaction

**User:** "Analyze my Instagram content performance for the last month"

**Response:**
1. Ask: "Please provide your Instagram username or specific post URLs"
2. Step 1 - Get post metrics:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-scraper" \
  --input '{"directUrls": ["https://instagram.com/yourusername"], "resultsLimit": 30}' \
  --output instagram-posts.csv \
  --format csv
```

3. Step 2 - Analyze reels:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-reel-scraper" \
  --input '{"directUrls": ["https://www.instagram.com/yourusername/reels/"], "resultsLimit": 20}' \
  --output instagram-reels.csv \
  --format csv
```

4. Report: "Analyzed 30 posts and 20 reels. Average engagement rate: 4.2%. Top performing content: Reels (6.1% engagement), Carousels (3.8%), Single images (2.9%). Best posting times: 6-8 PM weekdays."

---

## Workflow 2: Hashtag Campaign Performance

Track branded hashtag performance and reach.

### Checklist

```
Task Progress:
- [ ] Get campaign hashtags from user
- [ ] Step 1: Run Hashtag Scraper for content discovery
- [ ] Step 2: Run Tagged Scraper for brand mentions
- [ ] Step 3: Analyze reach and engagement
- [ ] Generate campaign report
```

### Example Interaction

**User:** "Track performance of our #BrandCampaign hashtag"

**Response:**
1. Step 1 - Scrape hashtag content:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-scraper" \
  --input '{"hashtags": ["BrandCampaign"], "resultsLimit": 100}' \
  --output hashtag-posts.csv \
  --format csv
```

2. Step 2 - Get tagged content:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-tagged-scraper" \
  --input '{"usernames": ["yourbrand"], "resultsLimit": 50}' \
  --output tagged-posts.csv \
  --format csv
```

3. Report campaign metrics: Total posts, reach estimates, top contributors, engagement breakdown.

---

## Workflow 3: Facebook Content ROI Analysis

Measure Facebook content performance and ad effectiveness.

### Checklist

```
Task Progress:
- [ ] Get Facebook page URL or ad library link
- [ ] Step 1: Run Posts Scraper for organic content
- [ ] Step 2: Run Ads Scraper for paid content
- [ ] Step 3: Compare organic vs paid performance
- [ ] Generate ROI analysis
```

### Example Interaction

**User:** "Analyze our Facebook content and ad performance"

**Response:**
1. Step 1 - Get organic post performance:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-posts-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/yourpage"}], "maxPosts": 50}' \
  --output fb-posts.csv \
  --format csv
```

2. Step 2 - Analyze ad performance:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-ads-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/ads/library/?..."}]}' \
  --output fb-ads.json \
  --format json
```

3. Step 3 - Get page metrics:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-pages-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/yourpage"}]}' \
  --output fb-page.json \
  --format json
```

4. Report: "Organic posts average 2.5% engagement. Top ad creative: Video (3.2x higher CTR than images). Recommended: Increase video content budget."

---

## Workflow 4: YouTube Video Performance Tracking

Analyze video metrics and audience engagement.

### Checklist

```
Task Progress:
- [ ] Get YouTube video URLs or channel
- [ ] Step 1: Run YouTube Scraper for video metrics
- [ ] Step 2: Run Shorts Scraper for short-form content
- [ ] Step 3: Compare long-form vs short-form performance
- [ ] Generate content strategy insights
```

### Example Interaction

**User:** "Analyze our YouTube channel performance"

**Response:**
1. Step 1 - Get video performance:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "streamers/youtube-scraper" \
  --input '{"startUrls": [{"url": "https://www.youtube.com/@yourchannel"}], "maxResults": 50}' \
  --output youtube-videos.csv \
  --format csv
```

2. Step 2 - Analyze Shorts:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "streamers/youtube-shorts-scraper" \
  --input '{"startUrls": [{"url": "https://www.youtube.com/@yourchannel/shorts"}], "maxResults": 30}' \
  --output youtube-shorts.csv \
  --format csv
```

3. Report: "Long-form videos average 5K views, Shorts average 15K views. Shorts driving 3x more subscriber growth. Top performing topics: Tutorials (8K avg views), Behind-the-scenes (6K avg views)."

---

## Workflow 5: TikTok Content Analytics

Track TikTok video performance and trending content.

### Checklist

```
Task Progress:
- [ ] Get TikTok username or video URLs
- [ ] Step 1: Run TikTok Scraper for profile/video data
- [ ] Step 2: Analyze engagement patterns
- [ ] Step 3: Identify viral content factors
- [ ] Generate optimization recommendations
```

### Example Interaction

**User:** "What TikTok content is performing best for us?"

**Response:**
1. Get content metrics:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-scraper" \
  --input '{"profiles": ["yourusername"], "resultsPerPage": 50}' \
  --output tiktok-analytics.csv \
  --format csv
```

2. Analyze patterns:
   - Play count distribution
   - Like-to-view ratio
   - Comment engagement
   - Share patterns

3. Report: "Top 5 videos by views. Average engagement rate: 8.2%. Videos with trending sounds: 2.5x more engagement. Optimal length: 15-30 seconds. Best posting time: 7-9 PM."

---

## Workflow 6: Cross-Platform Content Comparison

Compare content performance across multiple platforms.

### Checklist

```
Task Progress:
- [ ] Get account handles for all platforms
- [ ] Step 1: Run Instagram analytics
- [ ] Step 2: Run Facebook analytics
- [ ] Step 3: Run TikTok analytics
- [ ] Step 4: Run YouTube analytics
- [ ] Generate cross-platform comparison
```

### Example Interaction

**User:** "Compare our content performance across all social platforms"

**Response:**
1. Run scrapers for each platform (Instagram, Facebook, TikTok, YouTube)
2. Normalize metrics for comparison
3. Generate comparative report:

| Platform | Followers | Avg Engagement | Best Content Type |
|----------|-----------|----------------|-------------------|
| Instagram | 50K | 4.2% | Reels |
| Facebook | 30K | 2.1% | Videos |
| TikTok | 80K | 8.5% | Trending sounds |
| YouTube | 25K | 3.8% | Shorts |

4. Recommendations: "Focus resources on TikTok (highest engagement). Repurpose TikTok content to Instagram Reels. Reduce Facebook posting frequency."

---

## Workflow 7: Follower Growth Tracking

Monitor audience growth over time.

### Checklist

```
Task Progress:
- [ ] Get Instagram usernames to track
- [ ] Step 1: Run Followers Count Scraper
- [ ] Step 2: Record baseline metrics
- [ ] Step 3: Schedule periodic tracking
- [ ] Generate growth report
```

### Example Interaction

**User:** "Track our Instagram follower growth"

**Response:**
1. Get current metrics:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-followers-count-scraper" \
  --input '{"usernames": ["yourusername", "competitor1", "competitor2"]}' \
  --output follower-count.json \
  --format json
```

2. Report: "Current followers: 50,234. Growth this week: +1,234 (2.5%). Competitor comparison: You're growing 1.5x faster than industry average."

---

## Tips for Content Analytics

- **Track consistently**: Run analytics weekly for trend detection
- **Benchmark competitors**: Compare your metrics to industry standards
- **Focus on engagement rate**: Raw follower count matters less than engagement
- **Test content types**: Use A/B testing across formats (video, carousel, static)
- **Timing matters**: Analyze when your audience is most active
- **Attribution**: Track which content drives conversions, not just engagement
