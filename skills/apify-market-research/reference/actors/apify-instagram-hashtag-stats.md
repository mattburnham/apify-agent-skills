# Instagram Related Hashtag Stats Scraper

**Actor ID:** `apify/instagram-hashtag-stats`

Extract detailed Instagram hashtag statistics fast. Get total post count, posts per day, top and latest posts, related hashtags (literal and semantic), and their usage frequency. Export scraped stats, run the scraper via API, schedule and monitor runs or integrate with other tools.

## Key Input Parameters

```json
{
  "hashtags": ["webscraping"],
  "includeLatestPosts": true,
  "includeTopPosts": true
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `hashtags` | array | Hashtag(s) to scrape with or without # symbol (required) |
| `includeLatestPosts` | boolean | Include latest posts related to the hashtag (default: true, requires paid plan) |
| `includeTopPosts` | boolean | Include top most popular posts related to the hashtag (default: true, requires paid plan) |

## Output Fields

### Hashtag Statistics

| Field | Description |
|-------|-------------|
| `hashtag` | The hashtag being analyzed |
| `totalPostCount` | Total number of posts using this hashtag |
| `postsPerDay` | Average number of posts per day |
| `relatedHashtags` | Array of related hashtags (literal and semantic) |
| `relatedHashtagsFrequency` | Usage frequency of related hashtags |

### Latest Posts

| Field | Description |
|-------|-------------|
| `latestPosts` | Array of recent post objects (if includeLatestPosts is enabled) |

### Top Posts

| Field | Description |
|-------|-------------|
| `topPosts` | Array of most popular post objects (if includeTopPosts is enabled) |
