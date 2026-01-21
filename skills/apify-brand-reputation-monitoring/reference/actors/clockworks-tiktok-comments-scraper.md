# TikTok Comments Scraper

**Actor ID:** `clockworks/tiktok-comments-scraper`

Extract TikTok comments. Just add a TikTok URL and get TikTok video and profile data: comments, URLs, numbers of shares, followers, hashtags, hearts, video, and music metadata. Export scraped data, run the scraper via API, schedule and monitor runs or integrate with other tools.

## Key Input Parameters

```json
{
  "postURLs": [
    "https://www.tiktok.com/@bellapoarch/video/6862153058223197445"
  ],
  "commentsPerPost": 100,
  "maxRepliesPerComment": 0
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `postURLs` | array | TikTok video URLs to extract comments from |
| `commentsPerPost` | integer | Maximum number of comments extracted from every result (default: 100) |
| `maxRepliesPerComment` | integer | Maximum number of replies per comment (default: 0) |
| `profiles` | array | One or multiple TikTok usernames to scrape |
| `resultsPerPage` | integer | Number of videos per profile (default: 1) |
| `profileScrapeSections` | array | Profile sections to scrape: "videos", "reposts" (default: ["videos"]) |
| `profileSorting` | string | Profile video sorting: "latest", "popular", "oldest" (default: "latest") |
| `oldestPostDateUnified` | string | Scrape profile videos published after date (date format or number of days) |
| `newestPostDate` | string | Scrape videos published before date |
| `excludePinnedPosts` | boolean | Exclude pinned posts from profiles (default: false) |

## Output Fields

| Field | Description |
|-------|-------------|
| `text` | Comment text content |
| `diggCount` | Number of likes on the comment |
| `replyCommentTotal` | Total number of replies to the comment |
| `createTimeISO` | Comment creation timestamp (ISO format) |
| `uniqueId` | User's unique identifier |
| `videoWebUrl` | TikTok video URL |
| `uid` | User ID |
| `cid` | Comment ID |
| `avatarThumbnail` | User's avatar thumbnail URL |
