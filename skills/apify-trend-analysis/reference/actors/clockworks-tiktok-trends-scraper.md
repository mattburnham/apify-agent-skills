# TikTok Trends Scraper

**Actor ID:** `clockworks/tiktok-trends-scraper`

Scrape TikTok Trends data. Just add one or more channels and the scraper will extract related videos, posts, authors, music, and channel information. Export scraped data, run the scraper via API, schedule and monitor runs, or integrate with other tools.

## Key Input Parameters

```json
{
  "adsScrapeHashtags": true,
  "resultsPerPage": 100,
  "adsCountryCode": "US",
  "adsTimeRange": "7"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `adsScrapeHashtags` | boolean | Scrape Trending Hashtags (default: true) |
| `resultsPerPage` | integer | Number of trending creators, hashtags, videos or sounds. Maximum ~100 for hashtags/sounds, ~500 for creators/videos (default: 1) |
| `adsCountryCode` | string | Hashtag Region - country code (default: "US") |
| `adsTimeRange` | string | Time Range - "7", "30", or "120" days (default: "7", ignored for trending creators) |
| `adsHashtagIndustry` | string | Hashtag Industry filter: "Apparel & Accessories", "Baby, Kids & Maternity", "Beauty & Personal Care", "Business Services", "Education", "Financial Services", "Food & Beverage", "Games", "Health", "Home Improvement", "Household Products", "Life Services", "News & Entertainment", "Pets", "Sports & Outdoor", "Tech & Electronics", "Travel", "Vehicle & Transportation" |
| `adsNewOnBoard` | boolean | New to Top 100 (Hashtags/Songs) |
| `adsScrapeSounds` | boolean | Scrape Trending Songs (default: false) |
| `adsSoundsCountryCode` | string | Song Region - country code (default: "US") |
| `adsRankType` | string | Song Leaderboard Type: "popular" or "surging" (default: "popular") |
| `adsApprovedForBusinessUse` | boolean | Songs Approved for Business Use |
| `adsScrapeCreators` | boolean | Scrape Trending Creators (default: false) |
| `adsCreatorsCountryCode` | string | Creator Region - country code (default: "US") |
| `adsSortCreatorsBy` | string | Sort Creators By: "follower", "engagement", or "avg_views" (default: "follower") |
| `adsFollowers` | string | Creator Follower Range: "1", "2", "3", or "4" |
| `adsAudienceCountry` | string | Creator Audience Country - country code |
| `adsScrapeVideos` | boolean | Scrape Trending Videos (Ads) (default: false) |
| `adsVideosCountryCode` | string | Video Region - country code (default: "US") |
| `adsSortVideosBy` | string | Sort Videos By: "vv" (views), "like", "comment", or "repost" (default: "vv") |

## Output Fields

### Hashtag Output

| Field | Description |
|-------|-------------|
| `id` | Hashtag ID |
| `name` | Hashtag name |
| `url` | TikTok hashtag URL |
| `countryCode` | Country code |
| `rank` | Ranking position |
| `industryName` | Industry name |
| `videoCount` | Number of videos using this hashtag |
| `viewCount` | Total view count |
| `rankDiff` | Rank difference |
| `markedAsNew` | Whether marked as new |
| `isPromoted` | Whether the hashtag is promoted |

### Creator Output

| Field | Description |
|-------|-------------|
| `id` | Creator ID |
| `name` | Creator name |
| `url` | TikTok creator URL |
| `countryCode` | Country code |
| `rank` | Ranking position |

### Sound Output

| Field | Description |
|-------|-------------|
| `id` | Sound ID |
| `name` | Sound name |
| `url` | TikTok sound URL |
| `countryCode` | Country code |
| `rank` | Ranking position |
| `rankDiff` | Rank difference |
| `markedAsNew` | Whether marked as new |
| `isPromoted` | Whether the sound is promoted |

### Video Output

| Field | Description |
|-------|-------------|
| `id` | Video ID |
| `name` | Video name |
| `url` | TikTok video URL |
| `countryCode` | Country code |
| `rank` | Ranking position |
