# Facebook Marketplace Scraper

**Actor ID:** `apify/facebook-marketplace-scraper`

Extract data from one or multiple Facebook Marketplace listings. Scrape data on apartments, whole categories, items for sale, prices, location and sellers.

## Key Input Parameters

```json
{
  "startUrls": [
    {"url": "https://www.facebook.com/marketplace/prague/home-improvements"},
    {"url": "https://www.facebook.com/marketplace/prague/search/?query=apartment"}
  ],
  "resultsLimit": 20,
  "includeListingDetails": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Facebook Marketplace URLs (required) - location, category, or search query URLs |
| `resultsLimit` | integer | Number of listings to scrape (default: 20) |
| `includeListingDetails` | boolean | Add extra details for each listing including description, location coordinates, timestamp, and attributes (default: false) |

### Supported URL Types

- **Location:** `https://www.facebook.com/marketplace/sanfrancisco/`
- **Category:** `https://www.facebook.com/marketplace/sanfrancisco/instruments`
- **Search query:** `https://www.facebook.com/marketplace/sanfrancisco/search/?query=crane`

## Output Fields

### Basic Listing Information

| Field | Description |
|-------|-------------|
| `facebookUrl` | Facebook Marketplace URL (input URL) |
| `listingUrl` | Direct listing URL |
| `id` | Listing ID |
| `marketplace_listing_title` | Listing title |
| `custom_title` | Custom title (if available) |
| `marketplace_listing_category_id` | Category ID |

### Pricing Information

| Field | Description |
|-------|-------------|
| `listing_price` | Object with price details (formatted_amount, amount_with_offset_in_currency, amount) |
| `listing_price.formatted_amount` | Price formatted as string (e.g., "$65") |
| `listing_price.amount` | Price as decimal string (e.g., "65.00") |
| `listing_price.amount_with_offset_in_currency` | Price in cents (e.g., "6500") |
| `strikethrough_price` | Original price if item is on sale |
| `comparable_price` | Comparable price (if available) |
| `comparable_price_type` | Type of comparable price |
| `min_listing_price` | Minimum price for variable pricing |
| `max_listing_price` | Maximum price for variable pricing |

### Media

| Field | Description |
|-------|-------------|
| `primary_listing_photo` | Object with image information |
| `primary_listing_photo.image.uri` | Primary listing image URL |
| `primary_listing_photo.id` | Image ID |
| `listing_video` | Video object (if available) |

### Location Information

| Field | Description |
|-------|-------------|
| `location` | Object with location details |
| `location.reverse_geocode.city` | City name |
| `location.reverse_geocode.state` | State abbreviation |
| `location.reverse_geocode.city_page.display_name` | Full location display name |
| `location.reverse_geocode.city_page.id` | City page ID |

### Seller Information

| Field | Description |
|-------|-------------|
| `marketplace_listing_seller` | Object with seller information |
| `marketplace_listing_seller.name` | Seller name |
| `marketplace_listing_seller.id` | Seller ID |
| `marketplace_listing_seller.__typename` | Type (typically "User") |

### Status Flags

| Field | Description |
|-------|-------------|
| `is_hidden` | Whether listing is hidden |
| `is_live` | Whether listing is active |
| `is_pending` | Whether listing is pending sale |
| `is_sold` | Whether listing is sold |
| `is_viewer_seller` | Whether current user is the seller |

### Additional Information

| Field | Description |
|-------|-------------|
| `delivery_types` | Array of delivery options (e.g., ["IN_PERSON"]) |
| `custom_sub_titles_with_rendering_flags` | Array of custom subtitles |
| `origin_group` | Origin group (if posted in a group) |
| `parent_listing` | Parent listing reference (if applicable) |
