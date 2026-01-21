# YouTube Video Scraper by Hashtag

**Actor ID:** `streamers/youtube-video-scraper-by-hashtag`

Extract information about YouTube videos by specific hashtags. Get video URL, caption, timestamp, likes, dislikes, views and comments count, and basic channel info.

## Key Input Parameters

```json
{
  "hashtags": ["apify"],
  "maxResults": 10,
  "scrapeShortsOnly": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `hashtags` | array | Hashtags to scrape (required) |
| `maxResults` | integer | Limit the number of videos per hashtag (default: 1) |
| `scrapeShortsOnly` | boolean | Whether to scrape all videos or shorts only. `false (default)=all videos`, `true=shorts` |

## Output Fields

| Field | Description |
|-------|-------------|
| `thumbnailUrl` | Video thumbnail URL |
| `title` | Video title |
| `id` | Video ID |
| `url` | Direct video URL |
| `viewCount` | Number of views |
| `type` | Content type (e.g., "video") |
| `hashtagCategoryData.categoryInfoText` | Hashtag category statistics (videos count, channels count) |
