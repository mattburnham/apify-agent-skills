# YouTube Shorts Scraper

**Actor ID:** `streamers/youtube-shorts-scraper`

Extract YouTube Shorts data from one or multiple YouTube channels. Get video URL, caption, timestamp, likes, dislikes, views and comments count, basic channel info, and more.

## Key Input Parameters

```json
{
  "channels": ["rainbowicecream9780"],
  "maxResultsShorts": 10,
  "oldestPostDate": "2025-06-03",
  "sortChannelShortsBy": "NEWEST"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `channels` | array | Username of a channel (without @ sign) or a link to it (required) |
| `maxResultsShorts` | integer | Limit the number of Shorts videos to crawl from the channel (default: 1) |
| `oldestPostDate` | string | Only posts uploaded after or on this date will be scraped. Use date format (YYYY-MM-DD) or relative time like "1 day", "2 days" |
| `sortChannelShortsBy` | string | Sort shorts by: "NEWEST", "POPULAR", "OLDEST" |

## Output Fields

### Basic Video Information

| Field | Description |
|-------|-------------|
| `title` | Video title |
| `type` | Type of content (shorts) |
| `id` | Video ID |
| `url` | Direct video URL |
| `thumbnailUrl` | Video thumbnail URL |
| `viewCount` | Number of views |
| `date` | Upload date (ISO format) |
| `likes` | Number of likes |
| `location` | Video location (if available) |
| `duration` | Video duration (HH:MM:SS format) |
| `commentsCount` | Number of comments |
| `text` | Video description text |
| `subtitles` | Subtitle information (if available) |
| `commentsTurnedOff` | Whether comments are disabled |
| `isMonetized` | Monetization status |
| `hashtags` | Array of hashtags used |
| `isMembersOnly` | Whether content is members-only |
| `isAgeRestricted` | Whether content is age-restricted |
| `order` | Order in the result set |

### Channel Information

| Field | Description |
|-------|-------------|
| `channelName` | Channel name |
| `channelUrl` | Channel URL |
| `channelId` | Channel ID |
| `channelUsername` | Channel username |
| `channelDescription` | Channel description |
| `channelJoinedDate` | Date channel was created |
| `channelDescriptionLinks` | Array of links in channel description |
| `channelLocation` | Channel location |
| `channelAvatarUrl` | Channel avatar/profile picture URL |
| `channelBannerUrl` | Channel banner image URL |
| `channelTotalVideos` | Total number of videos on channel |
| `channelTotalViews` | Total channel views |
| `numberOfSubscribers` | Number of subscribers |
| `isChannelVerified` | Whether channel is verified |
| `inputChannelUrl` | Original input channel URL |

### Additional Metadata

| Field | Description |
|-------|-------------|
| `aboutChannelInfo` | Object containing detailed channel information |
| `formats` | Array of available video formats |
| `fromYTUrl` | Source YouTube URL |
| `input` | Original input parameter |
| `fromChannelListPage` | Source page type (shorts) |
