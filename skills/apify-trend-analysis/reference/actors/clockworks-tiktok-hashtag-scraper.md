# TikTok Hashtag Scraper

**Actor ID:** `clockworks/tiktok-hashtag-scraper`

Scrape TikTok hashtag data. Just add one or more hashtags and extract TikTok videos with that hashtag: URLs, likes, country of creation, video and music metadata, TikTok creator data.

## Key Input Parameters

```json
{
  "hashtags": ["followforfollowback"],
  "resultsPerPage": 100,
  "shouldDownloadVideos": false,
  "shouldDownloadCovers": false,
  "shouldDownloadSubtitles": false,
  "shouldDownloadSlideshowImages": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `hashtags` | array | TikTok hashtags to scrape from (required) |
| `resultsPerPage` | integer | Maximum number of posts per hashtag (max ~800 - hard limit by TikTok, default: 100) |
| `shouldDownloadVideos` | boolean | Download TikTok videos (default: false) |
| `shouldDownloadCovers` | boolean | Download TikTok video cover images/thumbnails (default: false) |
| `shouldDownloadSubtitles` | boolean | Download TikTok video subtitles when present (default: false) |
| `shouldDownloadSlideshowImages` | boolean | Download TikTok slideshow images (default: false) |
| `videoKvStoreIdOrName` | string | Name or ID of the Key Value Store where videos and media will be stored |

## Output Fields

### Basic Post Information

| Field | Description |
|-------|-------------|
| `id` | TikTok video ID |
| `text` | Video caption text |
| `createTime` | Unix timestamp of creation |
| `createTimeISO` | ISO format timestamp |
| `isAd` | Whether the post is an ad |
| `isMuted` | Whether the video is muted |
| `webVideoUrl` | TikTok web URL for the video |
| `mediaUrls` | Array of video media URLs |
| `mentions` | Array of user mentions |
| `hashtags` | Array of hashtag objects |

### Author Information

| Field | Description |
|-------|-------------|
| `authorMeta` | Object with complete author information |
| `authorMeta.id` | Author's TikTok ID |
| `authorMeta.name` | Author's username |
| `authorMeta.nickName` | Author's display name |
| `authorMeta.verified` | Verification status |
| `authorMeta.signature` | Author's bio text |
| `authorMeta.bioLink` | Bio link if present |
| `authorMeta.avatar` | Profile picture URL |
| `authorMeta.privateAccount` | Whether account is private |
| `authorMeta.ttSeller` | Whether user is a TikTok seller |
| `authorMeta.following` | Number of accounts following |
| `authorMeta.fans` | Number of followers |
| `authorMeta.heart` | Total hearts received |
| `authorMeta.video` | Total number of videos |
| `authorMeta.digg` | Number of videos liked |

### Music Information

| Field | Description |
|-------|-------------|
| `musicMeta` | Object with music metadata |
| `musicMeta.musicName` | Name of the music track |
| `musicMeta.musicAuthor` | Music author/artist |
| `musicMeta.musicOriginal` | Whether music is original |
| `musicMeta.musicAlbum` | Album name |
| `musicMeta.playUrl` | Music play URL |
| `musicMeta.coverMediumUrl` | Music cover image URL |
| `musicMeta.musicId` | Music track ID |

### Video Metadata

| Field | Description |
|-------|-------------|
| `videoMeta` | Object with video metadata |
| `videoMeta.height` | Video height in pixels |
| `videoMeta.width` | Video width in pixels |
| `videoMeta.duration` | Video duration in seconds |
| `videoMeta.coverUrl` | Video cover/thumbnail URL |
| `videoMeta.originalCoverUrl` | Original cover URL |
| `videoMeta.definition` | Video quality definition |
| `videoMeta.format` | Video format (e.g., mp4) |
| `videoMeta.originalDownloadAddr` | Original download address |
| `videoMeta.downloadAddr` | Download address |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `diggCount` | Number of likes |
| `shareCount` | Number of shares |
| `playCount` | Number of plays/views |
| `collectCount` | Number of saves/bookmarks |
| `commentCount` | Number of comments |
