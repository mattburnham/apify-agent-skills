# TikTok Sound Scraper

**Actor ID:** `clockworks/tiktok-sound-scraper`

Scrape TikTok videos with a chosen sound. Extract video URLs, likes, country of creation, video and music metadata, and creator data from all videos that include a specific TikTok sound.

## Key Input Parameters

```json
{
  "musics": [
    "https://www.tiktok.com/music/a-negroni-sbagliato-w-prosecco-l-hbo-max-7149523537730997035"
  ],
  "resultsPerPage": 100,
  "shouldDownloadVideos": false,
  "shouldDownloadCovers": false,
  "shouldDownloadSubtitles": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `musics` | array | Music URL(s) to scrape videos using them (required). Can use full URLs or IDs only |
| `resultsPerPage` | integer | Number of results to scrape from every music (default: 100) |
| `shouldDownloadVideos` | boolean | Download TikTok videos (increases time and costs, default: false) |
| `shouldDownloadCovers` | boolean | Download TikTok video cover images/thumbnails (increases time and costs, default: false) |
| `shouldDownloadSubtitles` | boolean | Download TikTok video subtitles when present (increases time and costs, default: false) |
| `shouldDownloadSlideshowImages` | boolean | Download TikTok slideshow images (increases time and costs, default: false) |
| `shouldDownloadMusicCovers` | boolean | Download cover images of sounds used in posts (increases time and costs, default: false) |
| `videoKvStoreIdOrName` | string | Name or ID of the Key Value Store where videos and media will be stored (optional) |

## Output Fields

### Basic Video Information

| Field | Description |
|-------|-------------|
| `id` | TikTok video ID |
| `text` | Video description text |
| `createTime` | Creation timestamp (Unix format) |
| `createTimeISO` | Creation timestamp (ISO 8601 format) |
| `locationCreated` | Country code where video was created |
| `isAd` | Whether the video is an ad |
| `isMuted` | Whether the video is muted |
| `webVideoUrl` | Direct URL to the video on TikTok |
| `mediaUrls` | Array of video media URLs |

### Author Information

| Field | Description |
|-------|-------------|
| `authorMeta` | Object containing author information |
| `authorMeta.id` | Author's user ID |
| `authorMeta.name` | Author's username |
| `authorMeta.nickName` | Author's display name |
| `authorMeta.verified` | Whether author is verified |
| `authorMeta.signature` | Author's bio/signature |
| `authorMeta.bioLink` | Link in author's bio |
| `authorMeta.avatar` | Author's profile picture URL |
| `authorMeta.privateAccount` | Whether account is private |
| `authorMeta.roomId` | Author's room ID |
| `authorMeta.ttSeller` | Whether author is a TikTok seller |

### Music Metadata

| Field | Description |
|-------|-------------|
| `musicMeta` | Object containing music/sound information |
| `musicMeta.musicName` | Name of the music/sound |
| `musicMeta.musicAuthor` | Music/sound author name |
| `musicMeta.musicOriginal` | Whether music is original |
| `musicMeta.musicAlbum` | Album name (if applicable) |
| `musicMeta.playUrl` | URL to play the music |
| `musicMeta.coverMediumUrl` | URL to music cover image |
| `musicMeta.musicId` | Music/sound ID |

### Video Metadata

| Field | Description |
|-------|-------------|
| `videoMeta` | Object containing video technical information |
| `videoMeta.height` | Video height in pixels |
| `videoMeta.width` | Video width in pixels |
| `videoMeta.duration` | Video duration in seconds |
| `videoMeta.coverUrl` | Video cover/thumbnail URL |
| `videoMeta.originalCoverUrl` | Original cover image URL |
| `videoMeta.definition` | Video quality definition |
| `videoMeta.format` | Video file format |
| `videoMeta.originalDownloadAddr` | Original download address |
| `videoMeta.downloadAddr` | Download address |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `diggCount` | Number of likes |
| `shareCount` | Number of shares |
| `playCount` | Number of plays/views |
| `commentCount` | Number of comments |

### Content Tags

| Field | Description |
|-------|-------------|
| `mentions` | Array of mentioned usernames |
| `hashtags` | Array of hashtag objects with id, name, title, and cover |
| `effectStickers` | Array of effect stickers used |

### Search Music Info

| Field | Description |
|-------|-------------|
| `searchMusic` | Object with music search information |
| `searchMusic.musicTag` | Music tag identifier |
| `searchMusic.videos` | Number of videos using this sound |
