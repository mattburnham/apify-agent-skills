# Facebook Likes Scraper

**Actor ID:** `apify/facebook-likes-scraper`

Scrape people who liked a Facebook post or page to analyze engagement and find potential leads.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.facebook.com/YourPage/posts/123456789"}],
  "resultsLimit": 100
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Facebook post or page URLs to scrape likes from (required) |
| `resultsLimit` | integer | Maximum number of likes to scrape (default: 100) |

## Output Fields

### User Information

| Field | Description |
|-------|-------------|
| `profileUrl` | User's Facebook profile URL |
| `name` | User's display name |
| `profileId` | User's Facebook profile ID |
| `profilePicture` | User's profile picture URL |

### Interaction Details

| Field | Description |
|-------|-------------|
| `postUrl` | URL of the liked post |
| `pageUrl` | URL of the page (if applicable) |
| `inputUrl` | Original input URL |

### Additional Fields

| Field | Description |
|-------|-------------|
| `reactionType` | Type of reaction (like, love, care, haha, wow, sad, angry) |
| `timestamp` | When the like was recorded (ISO format) |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `name` | User name |
| 2 | `profileUrl` | Profile URL |
| 3 | `profileId` | Profile ID |
| 4 | `reactionType` | Reaction type |
| 5 | `postUrl` | Liked post URL |
