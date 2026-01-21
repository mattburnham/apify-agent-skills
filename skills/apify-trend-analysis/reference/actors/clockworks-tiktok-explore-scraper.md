# TikTok Explore Scraper

**Actor ID:** `clockworks/tiktok-explore-scraper`

Extract data from TikTok explore categories including post, author, video, and music data. Export scraped data, run the scraper via API, schedule and monitor runs or integrate with other tools.

## Key Input Parameters

```json
{
  "exploreCategoryTypes": ["pc_web_explorePage_all"],
  "resultsPerPage": 100,
  "shouldDownloadVideos": false,
  "shouldDownloadCovers": false,
  "shouldDownloadSubtitles": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `exploreCategoryTypes` | array | TikTok Explore categories to scrape (required). Options: "pc_web_explorePage_all" (All), "pc_web_explorePage_topics_singing_dancing" (Singing & Dancing), "pc_web_explorePage_topics_comedy" (Comedy), "pc_web_explorePage_topics_sports" (Sports), "pc_web_explorePage_topics_anime_comics" (Anime & Comics), "pc_web_explorePage_topics_relationship" (Relationship), "pc_web_explorePage_topics_shows" (Shows), "pc_web_explorePage_topics_lipsync" (Lipsync), "pc_web_explorePage_topics_daily_life" (Daily Life), "pc_web_explorePage_topics_beauty_care" (Beauty Care), "pc_web_explorePage_topics_games" (Games), "pc_web_explorePage_topics_society" (Society), "pc_web_explorePage_topics_outfit" (Outfit), "pc_web_explorePage_topics_cars" (Cars), "pc_web_explorePage_topics_food" (Food), "pc_web_explorePage_topics_animals" (Animals), "pc_web_explorePage_topics_family" (Family), "pc_web_explorePage_topics_drama" (Drama), "pc_web_explorePage_topics_fitness_health" (Fitness & Health), "pc_web_explorePage_topics_education" (Education), "pc_web_explorePage_topics_technology" (Technology) |
| `resultsPerPage` | integer | Maximum number of posts per category (default: 100, up to ~300 posts - hard limit by TikTok) |
| `shouldDownloadVideos` | boolean | Download TikTok videos (default: false) |
| `shouldDownloadCovers` | boolean | Download TikTok video cover images/thumbnails (default: false) |
| `shouldDownloadSubtitles` | boolean | Download TikTok video subtitles when present (default: false) |
| `shouldDownloadSlideshowImages` | boolean | Download TikTok slideshow images (default: false) |
| `videoKvStoreIdOrName` | string | Name or ID of the Key Value Store for videos and media (optional, uses default if omitted) |
| `proxyCountryCode` | string | Country code for proxy (default: "None", uses RESIDENTIAL proxy group) |

## Output Fields

### Post Data

| Field | Description |
|-------|-------------|
| `url` | Post URL |
| `coverImage` | Cover image URL |
| `text` | Post text content |
| `diggs` | Number of likes/diggs |
| `shares` | Number of shares |
| `plays` | Number of plays |
| `comments` | Number of comments |
| `duration` | Video duration |
| `location` | Location where post was created |
| `isAd` | Whether the post is an ad |

### Author Data

| Field | Description |
|-------|-------------|
| `name` | Author name |
| `nickname` | Author nickname |
| `verified` | Whether account is verified |
| `signature` | Author signature/bio |
| `fans` | Number of fans/followers |
| `videos` | Number of videos |
| `bioLink` | Bio link URL |

### Music Data

| Field | Description |
|-------|-------------|
| `name` | Music name |
| `author` | Music author |
| `album` | Album name |
| `isOriginal` | Whether it's original sound |
| `id` | Music ID |

### Video Data

| Field | Description |
|-------|-------------|
| `duration` | Video duration |
| `definition` | Video definition/quality |
| `format` | Video format |
| `height` | Video height |
| `width` | Video width |
