# Audience Analysis Workflows

Multi-step workflows that combine multiple Actors for comprehensive audience understanding.

---

## Workflow 1: Instagram Audience Demographics

Understand your Instagram audience through profile and follower analysis.

### Checklist

```
Task Progress:
- [ ] Get Instagram usernames to analyze
- [ ] Step 1: Run Profile Scraper for audience demographics
- [ ] Step 2: Run Followers Count Scraper for growth tracking
- [ ] Step 3: Analyze follower engagement patterns
- [ ] Generate demographic report
```

### Example Interaction

**User:** "Analyze my Instagram audience demographics"

**Response:**
1. Ask: "Please provide your Instagram username and any competitor usernames for comparison"
2. Step 1 - Get profile demographics:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-profile-scraper" \
  --input '{"usernames": ["yourusername", "competitor1", "competitor2"]}' \
  --output audience-profiles.csv \
  --format csv
```

3. Step 2 - Track follower metrics:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-followers-count-scraper" \
  --input '{"usernames": ["yourusername", "competitor1", "competitor2"]}' \
  --output follower-counts.json \
  --format json
```

4. Report: "Your audience: 50K followers, 3.2% engagement rate. Competitor comparison: You have 20% more followers than competitor1 but 15% lower engagement. Recommendation: Focus on engagement quality over growth."

---

## Workflow 2: Facebook Follower Network Analysis

Map and analyze Facebook follower networks and relationships.

### Checklist

```
Task Progress:
- [ ] Get Facebook page or profile URL
- [ ] Step 1: Run Followers/Following Scraper for network data
- [ ] Step 2: Run Likes Scraper for engagement behavior
- [ ] Step 3: Analyze network patterns
- [ ] Generate network analysis report
```

### Example Interaction

**User:** "Analyze our Facebook page followers"

**Response:**
1. Step 1 - Get follower data:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-followers-following-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/yourpage"}], "resultsLimit": 100, "followType": "follower"}' \
  --output fb-followers.csv \
  --format csv
```

2. Step 2 - Analyze engagement behavior:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-likes-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/yourpage/posts/123"}], "resultsLimit": 200}' \
  --output fb-engagement.csv \
  --format csv
```

3. Report: "Analyzed 100 followers. Profile types: 60% personal accounts, 30% business pages, 10% groups. Top engaging segments: Local businesses (highest interaction rate)."

---

## Workflow 3: TikTok Audience Deep Dive

Comprehensive analysis of TikTok followers and their behavior.

### Checklist

```
Task Progress:
- [ ] Get TikTok username
- [ ] Step 1: Run Profile Scraper for account demographics
- [ ] Step 2: Run Followers Scraper for follower data
- [ ] Step 3: Run Comments Scraper for engagement quality
- [ ] Generate audience insights
```

### Example Interaction

**User:** "Who is our TikTok audience?"

**Response:**
1. Step 1 - Get profile overview:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-profile-scraper" \
  --input '{"profiles": ["yourusername"], "resultsPerPage": 50}' \
  --output tiktok-profile.csv \
  --format csv
```

2. Step 2 - Analyze followers:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-followers-scraper" \
  --input '{"profiles": ["yourusername"], "resultsPerPage": 100}' \
  --output tiktok-followers.csv \
  --format csv
```

3. Step 3 - Analyze comment engagement:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-comments-scraper" \
  --input '{"postURLs": ["https://www.tiktok.com/@user/video/123"], "commentsPerPost": 200}' \
  --output tiktok-comments.csv \
  --format csv
```

4. Report: "Followers: 80K, avg engagement 8.5%. Audience breakdown: 70% Gen Z, 25% Millennials. Top comment sentiment: Positive (85%). Peak engagement times: 7-10 PM."

---

## Workflow 4: YouTube Channel Audience Analysis

Understand your YouTube subscriber base and viewer engagement.

### Checklist

```
Task Progress:
- [ ] Get YouTube channel URL
- [ ] Step 1: Run Channel Scraper for subscriber data
- [ ] Step 2: Run Comments Scraper for viewer feedback
- [ ] Step 3: Analyze viewer sentiment and topics
- [ ] Generate audience report
```

### Example Interaction

**User:** "Analyze our YouTube audience"

**Response:**
1. Step 1 - Get channel and subscriber info:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "streamers/youtube-channel-scraper" \
  --input '{"startUrls": [{"url": "https://www.youtube.com/@yourchannel"}], "maxResults": 20}' \
  --output youtube-channel.json \
  --format json
```

2. Step 2 - Analyze viewer comments:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "streamers/youtube-comments-scraper" \
  --input '{"startUrls": [{"url": "https://www.youtube.com/watch?v=VIDEO_ID"}], "maxComments": 300}' \
  --output youtube-comments.csv \
  --format csv
```

3. Report: "Subscribers: 25K. Total views: 2.5M. Top viewer interests: Tutorials (45%), Reviews (30%), Entertainment (25%). Comment sentiment: 80% positive. Top requested content: More beginner tutorials."

---

## Workflow 5: Cross-Platform Audience Comparison

Compare audience characteristics across multiple platforms.

### Checklist

```
Task Progress:
- [ ] Get account handles for all platforms
- [ ] Step 1: Run Instagram profile analysis
- [ ] Step 2: Run TikTok profile analysis
- [ ] Step 3: Run YouTube channel analysis
- [ ] Step 4: Run Facebook page analysis
- [ ] Generate cross-platform comparison
```

### Example Interaction

**User:** "Compare our audience across all social platforms"

**Response:**
1. Run profile scrapers for each platform
2. Normalize and compare metrics
3. Generate comparative report:

| Platform | Followers | Engagement Rate | Audience Type |
|----------|-----------|-----------------|---------------|
| Instagram | 50K | 4.2% | Visual content enthusiasts |
| TikTok | 80K | 8.5% | Gen Z, entertainment seekers |
| YouTube | 25K | 3.8% | Tutorial seekers, professionals |
| Facebook | 30K | 2.1% | Older demographic, community |

4. Recommendations: "TikTok has highest engagement - cross-post short-form content. YouTube audience seeks educational content. Instagram audience responds to visual storytelling."

---

## Workflow 6: Engagement Quality Analysis

Analyze the quality and authenticity of audience engagement.

### Checklist

```
Task Progress:
- [ ] Get content URLs to analyze
- [ ] Step 1: Run Comment Scrapers for each platform
- [ ] Step 2: Analyze comment quality and patterns
- [ ] Step 3: Identify bot/spam patterns
- [ ] Generate engagement quality report
```

### Example Interaction

**User:** "Analyze the quality of engagement on our posts"

**Response:**
1. Step 1 - Get Instagram comments:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-comment-scraper" \
  --input '{"directUrls": ["https://www.instagram.com/p/POST_ID/"], "resultsLimit": 200}' \
  --output ig-comments.csv \
  --format csv
```

2. Step 2 - Get Facebook comments:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-comments-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/post/123"}], "maxComments": 200}' \
  --output fb-comments.csv \
  --format csv
```

3. Analyze patterns:
   - Comment length distribution
   - Unique vs. duplicate comments
   - Profile authenticity indicators
   - Response timing patterns

4. Report: "Engagement quality score: 85%. Genuine comments: 92%. Spam/bot patterns detected: 8%. High-value commenters: 15 accounts with consistent engagement."

---

## Workflow 7: Audience Segmentation

Segment your audience based on behavior and characteristics.

### Checklist

```
Task Progress:
- [ ] Get profile and engagement data
- [ ] Step 1: Collect follower profiles
- [ ] Step 2: Collect engagement data
- [ ] Step 3: Analyze patterns for segmentation
- [ ] Generate audience segments report
```

### Example Interaction

**User:** "Help me segment our audience"

**Response:**
1. Step 1 - Get follower data:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-profile-scraper" \
  --input '{"usernames": ["follower1", "follower2", "follower3"]}' \
  --output follower-profiles.csv \
  --format csv
```

2. Step 2 - Get engagement patterns:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/export-instagram-comments-posts" \
  --input '{"usernames": ["yourusername"], "resultsLimit": 500}' \
  --output engagement-data.csv \
  --format csv
```

3. Segment report:
   - **Power Users** (10%): High engagement, frequent commenters
   - **Passive Followers** (60%): View but rarely engage
   - **Occasional Engagers** (25%): Like but don't comment
   - **New Followers** (5%): Recently followed, testing content

---

## Tips for Audience Analysis

- **Combine multiple data sources**: Use profile + engagement data for complete picture
- **Track over time**: Run analysis periodically to spot trends
- **Compare to competitors**: Benchmark your audience against similar accounts
- **Focus on quality**: Engagement rate matters more than follower count
- **Segment your audience**: Different content for different audience groups
- **Monitor sentiment**: Comments reveal audience feelings and needs
- **Look for patterns**: Timing, content type, and format preferences
