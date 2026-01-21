# TikTok Discover Scraper

**Actor ID:** `clockworks/tiktok-discover-scraper`

Scrape TikTok Discover data. Just add one or more hashtags and the scraper will extract related videos, tag breadcrumbs, similar trends, and subtopics. Export scraped data, run the scraper via API, schedule and monitor runs, or integrate with other tools.

## Key Input Parameters

```json
{
  "hashtags": ["tokyo"],
  "resultsPerPage": 100,
  "shouldDownloadVideos": false,
  "shouldDownloadCovers": false,
  "shouldDownloadSubtitles": false,
  "shouldDownloadSlideshowImages": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `hashtags` | array | TikTok hashtags to scrape (required) |
| `resultsPerPage` | integer | Maximum number of posts per hashtag, up to ~100 posts (hard limit by TikTok) (default: 100) |
| `shouldDownloadVideos` | boolean | Download TikTok videos (costs $0.001 per video) (default: false) |
| `shouldDownloadCovers` | boolean | Download TikTok video cover images/thumbnails (default: false) |
| `shouldDownloadSubtitles` | boolean | Download TikTok video subtitles when present (default: false) |
| `shouldDownloadSlideshowImages` | boolean | Download TikTok slideshow images (default: false) |
| `videoKvStoreIdOrName` | string | Name or ID of the Key Value Store where videos and media will be stored (optional) |

## Output Fields

### Basic Video Information

| Field | Description |
|-------|-------------|
| `id` | Video ID |
| `text` | Video caption/description |
| `createTime` | Unix timestamp of video creation |
| `createTimeISO` | ISO format timestamp of video creation |
| `webVideoUrl` | Direct TikTok video URL |
| `mediaUrls` | Array of video media URLs |
| `isAd` | Whether the video is an ad |
| `isMuted` | Whether the video is muted |
| `isSlideshow` | Whether the content is a slideshow |
| `isPinned` | Whether the video is pinned |
| `input` | Input hashtag used for scraping |

### Author Information

| Field | Description |
|-------|-------------|
| `authorMeta` | Object containing author information |
| `authorMeta.id` | Author ID |
| `authorMeta.name` | Author username |
| `authorMeta.nickName` | Author display name |
| `authorMeta.verified` | Whether the author is verified |
| `authorMeta.signature` | Author bio/signature |
| `authorMeta.bioLink` | Bio link URL |
| `authorMeta.avatar` | Author avatar URL |
| `authorMeta.privateAccount` | Whether the account is private |
| `authorMeta.following` | Number of accounts following |
| `authorMeta.fans` | Number of followers |
| `authorMeta.heart` | Total hearts received |
| `authorMeta.video` | Total video count |
| `authorMeta.digg` | Total diggs count |

### Music Information

| Field | Description |
|-------|-------------|
| `musicMeta` | Object containing music information |
| `musicMeta.musicName` | Music track name |
| `musicMeta.musicAuthor` | Music author/artist |
| `musicMeta.musicOriginal` | Whether music is original |
| `musicMeta.musicAlbum` | Album name |
| `musicMeta.playUrl` | Music playback URL |
| `musicMeta.coverMediumUrl` | Music cover image URL |
| `musicMeta.musicId` | Music track ID |

### Video Metadata

| Field | Description |
|-------|-------------|
| `videoMeta` | Object containing video metadata |
| `videoMeta.height` | Video height in pixels |
| `videoMeta.width` | Video width in pixels |
| `videoMeta.duration` | Video duration in seconds |
| `videoMeta.coverUrl` | Video cover/thumbnail URL |
| `videoMeta.originalCoverUrl` | Original cover image URL |
| `videoMeta.definition` | Video quality definition |
| `videoMeta.format` | Video format |
| `videoMeta.originalDownloadAddr` | Original video download URL |
| `videoMeta.downloadAddr` | Video download URL |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `diggCount` | Number of likes/digs |
| `shareCount` | Number of shares |
| `playCount` | Number of plays |
| `collectCount` | Number of collections/saves |
| `commentCount` | Number of comments |

### Hashtags and Metadata

| Field | Description |
|-------|-------------|
| `hashtags` | Array of hashtag objects used in the video |
| `mentions` | Array of mentioned users |
| `effectStickers` | Array of effect stickers used |

Hashtag object fields:

| Field | Description |
|-------|-------------|
| `id` | Hashtag ID |
| `name` | Hashtag name |
| `title` | Hashtag title/description |
| `cover` | Hashtag cover image URL |

### Discovery Information

| Field | Description |
|-------|-------------|
| `discoveryInfo` | Object containing TikTok Discover page information |
| `discoveryInfo.breadcrumbs` | Array of breadcrumb navigation items |
| `discoveryInfo.relatedTags` | Array of related hashtags |
| `discoveryInfo.url` | TikTok Discover page URL |
| `discoveryInfo.tag` | Scraped hashtag/tag |
| `discoveryInfo.type` | Type indicator (discover) |
