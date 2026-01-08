# Facebook Pages Scraper

**Actor ID:** `apify/facebook-pages-scraper`

Extract data from Facebook pages including contact info and engagement metrics.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.facebook.com/copperkettleyqr/"}]
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Facebook page URLs (required) - only works on pages, not personal profiles |

## Output Fields

### Basic Page Information

| Field | Description |
|-------|-------------|
| `facebookUrl` | Original Facebook URL |
| `title` | Page name |
| `pageId` | Numeric page ID |
| `pageName` | Page username/handle |
| `pageUrl` | Canonical Facebook page URL |
| `facebookId` | Facebook ID |
| `categories` | Page categories array |
| `info` | Array of page information strings |

### Contact Information

| Field | Description |
|-------|-------------|
| `email` | Contact email (if available) |
| `phone` | Phone number (if available) |
| `address` | Business address (if available) |
| `websites` | Array of website URLs |
| `website` | Primary website URL |
| `messenger` | Messenger link (if available) |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `likes` | Page likes count |
| `followers` | Page followers count |
| `followings` | Number of pages this page follows (if available) |

### Ratings & Reviews

| Field | Description |
|-------|-------------|
| `rating` | Page rating with review count string (e.g., "94% recommend (839 Reviews)") |
| `ratingOverall` | Numeric rating percentage |
| `ratingCount` | Number of ratings |

### Media & Visuals

| Field | Description |
|-------|-------------|
| `profilePictureUrl` | Profile picture URL |
| `coverPhotoUrl` | Cover photo URL |
| `profilePhoto` | Profile photo Facebook URL |

### Page Details

| Field | Description |
|-------|-------------|
| `intro` | Page description/bio |
| `about_me` | Object with detailed about information (text, urls array) |

### Ownership & Verification

| Field | Description |
|-------|-------------|
| `CONFIRMED_OWNER_LABEL` | Confirmed owner label text |
| `confirmed_owner` | Full confirmed owner statement |

### Advertising Information

| Field | Description |
|-------|-------------|
| `creation_date` | Page creation date |
| `ad_status` | Current ad running status |
| `pageAdLibrary` | Ad library information object (is_business_page_active, id) |

### Profile-Specific Fields

Available only when scraping Facebook profiles (not pages):

| Field | Description |
|-------|-------------|
| `personalProfile` | Object with personal profile data (name, gender, profile photos: small, medium, large) |
