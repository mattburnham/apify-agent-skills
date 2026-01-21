# TikTok Hashtag Analytics

**Actor ID:** `clockworks/tiktok-ads-scraper`

Scrape TikTok hashtag analytics data. Just add one or more hashtags, and the scraper will extract posts' text, details, country, longevity, audience interests, scores, countries, labels, and age range.

## Key Input Parameters

```json
{
  "hashtags": ["thailand", "coffee"],
  "adsCountryCode": "us",
  "adsTimeRange": "7"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `hashtags` | array | List of TikTok hashtags to scrape analytics from (required) |
| `adsCountryCode` | string | Country code for targeted analytics: "us", "af", "al", "dz", "as", "ad", "ao", "ai", "aq", "ag", "ar", "am", "aw", "au", "at", "az", "bs", "bh", "bd", "bb", "by", "be", "bz", "bj", "bm", "bt", "bo", "ba", "bw", "bv", "br", "io", "bn", "bg", "bf", "bi", "kh", "cm", "ca", "cv", "ky", "cf", "td", "cl", "cn", "cx", "cc", "co", "km", "cg", "cd", "ck", "cr", "ci", "hr", "cu", "cy", "cz", "dk", "dj", "dm", "do", "ec", "eg", "sv", "gq", "er", "ee", "et", "fk", "fo", "fj", "fi", "fr", "gf", "pf", "tf", "ga", "gm", "ge", "de", "gh", "gi", "gr", "gl", "gd", "gp", "gu", "gt", "gn", "gw", "gy", "ht", "hm", "va", "hn", "hk", "hu", "is", "in", "id", "ir", "iq", "ie", "il", "it", "jm", "jp", "jo", "kz", "ke", "ki", "kp", "kr", "kw", "kg", "la", "lv", "lb", "ls", "lr", "ly", "li", "lt", "lu", "mo", "mk", "mg", "mw", "my", "mv", "ml", "mt", "mh", "mq", "mr", "mu", "yt", "mx", "fm", "md", "mc", "mn", "me", "ms", "ma", "mz", "mm", "na", "nr", "np", "nl", "an", "nc", "nz", "ni", "ne", "ng", "nu", "nf", "mp", "no", "om", "pk", "pw", "ps", "pa", "pg", "py", "pe", "ph", "pn", "pl", "pt", "pr", "qa", "re", "ro", "ru", "rw", "sh", "kn", "lc", "pm", "vc", "ws", "sm", "st", "sa", "sn", "rs", "sc", "sl", "sg", "sk", "si", "sb", "so", "za", "gs", "ss", "es", "lk", "sd", "sr", "sj", "sz", "se", "ch", "sy", "tw", "tj", "tz", "th", "tl", "tg", "tk", "to", "tt", "tn", "tr", "tm", "tc", "tv", "ug", "ua", "ae", "gb", "um", "uy", "uz", "vu", "ve", "vn", "vg", "vi", "wf", "eh", "ye", "zm", "zw" |
| `adsTimeRange` | string | Time span for hashtag analytics: "7" (7 days), "30" (30 days), "120" (120 days), "365" (365 days), "1095" (1095 days) |

## Output Fields

### Basic Hashtag Information

| Field | Description |
|-------|-------------|
| `hashtagName` | The hashtag name |
| `hashtagId` | Unique hashtag identifier |
| `videoUrl` | TikTok URL for the hashtag |
| `description` | Hashtag description |
| `period` | Analysis period |
| `countryCode` | Country code for the analysis |

### Video Metrics

| Field | Description |
|-------|-------------|
| `publishCnt` | Number of videos published during the analysis period |
| `videoViews` | Total views during the analysis period |
| `publishCntAll` | Total count of all videos published with this hashtag |
| `videoViewsAll` | Total views of all videos with this hashtag |

### Trend Data

| Field | Description |
|-------|-------------|
| `trend` | Array of trend data points showing popularity over time |
| `isPromoted` | Boolean indicating if hashtag is promoted |
| `trendingType` | Type of trending status |

Trend data object fields:

| Field | Description |
|-------|-------------|
| `time` | Unix timestamp |
| `value` | Popularity value (0-1 scale) |

### Longevity

| Field | Description |
|-------|-------------|
| `longevity` | Object containing longevity information |
| `longevity.popularDays` | Number of days the hashtag has been popular |
| `longevity.currentPopularity` | Current popularity score |

### Geographic Information

| Field | Description |
|-------|-------------|
| `countryInfo` | Object with country information for the analysis |
| `countryInfo.id` | Country code |
| `countryInfo.value` | Country name |
| `countryInfo.label` | Country label |

### Industry Information

| Field | Description |
|-------|-------------|
| `industryInfo` | Object with industry category information |
| `industryInfo.id` | Industry identifier |
| `industryInfo.value` | Industry category name |
| `industryInfo.label` | Industry label |

### Audience Demographics

| Field | Description |
|-------|-------------|
| `audienceAges` | Array of audience age distribution objects |

Audience age object fields:

| Field | Description |
|-------|-------------|
| `score` | Proportion of this age category |
| `ageLevel` | Age level identifier (3, 4, 5 correspond to different age ranges) |

### Audience Interests

| Field | Description |
|-------|-------------|
| `audienceInterests` | Array of audience interest objects with scores |

Audience interest object fields:

| Field | Description |
|-------|-------------|
| `score` | Interest score |
| `interestInfo` | Object with interest details |
| `interestInfo.id` | Interest identifier |
| `interestInfo.label` | Interest label |
| `interestInfo.value` | Interest category name |

### Audience Countries

| Field | Description |
|-------|-------------|
| `audienceCountries` | Array of countries where the hashtag is popular |

Audience country object fields:

| Field | Description |
|-------|-------------|
| `score` | Popularity score in this country |
| `countryInfo` | Object with country details |
| `countryInfo.id` | Country identifier |
| `countryInfo.label` | Country code |
| `countryInfo.value` | Country name |

### Related Hashtags

| Field | Description |
|-------|-------------|
| `relatedHashtags` | Array of related hashtag objects |

Related hashtag object fields:

| Field | Description |
|-------|-------------|
| `hashtagId` | Hashtag identifier |
| `hashtagName` | Hashtag name |
| `videoUrl` | TikTok URL for the hashtag |

### Recommended Hashtags

| Field | Description |
|-------|-------------|
| `recList` | Array of recommended hashtag objects (same structure as relatedHashtags) |

### Related Videos

| Field | Description |
|-------|-------------|
| `relatedVideos` | Array of related video objects |

Related video object fields:

| Field | Description |
|-------|-------------|
| `coverUri` | Video cover image URL |
| `url` | TikTok video URL |
