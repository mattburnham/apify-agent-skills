# Google Maps Scraper

**Actor ID:** `compass/crawler-google-places`

Scrape local businesses from Google Maps with contact details, ratings, and reviews.

**Pricing:** Event-based pricing starting at $4 per 1,000 places (FREE tier). Additional features and add-ons have separate pricing. See [detailed pricing](https://help.apify.com/en/articles/10774732-google-maps-scraper-is-going-to-pay-per-event-pricing).

## Basic Search Parameters

```json
{
  "searchStringsArray": ["restaurant"],
  "locationQuery": "New York, USA",
  "maxCrawledPlacesPerSearch": 50,
  "language": "en"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `searchStringsArray` | array | Search terms (e.g., "restaurant", "gym") |
| `locationQuery` | string | Location using free text (city + country recommended) |
| `maxCrawledPlacesPerSearch` | integer | Max results per search term (leave empty for all) |
| `language` | string | Results language (default: "en") - supports 100+ languages |
| `allPlacesNoSearchAction` | string | Scrape all visible places on map: "all_places_no_search_ocr" or "all_places_no_search_mouse" |

## Search Filters & Categories ($)

| Parameter | Type | Description |
|-----------|------|-------------|
| `categoryFilterWords` | array | Filter by place categories (e.g., "restaurant", "hotel"). See 4,000+ [available categories](https://api.apify.com/v2/key-value-stores/epxZwNRgmnzzBpNJd/records/categories) |
| `searchMatching` | string | Name matching: "all" (default), "only_includes", or "only_exact" |
| `placeMinimumStars` | string | Min star rating: "two", "twoAndHalf", "three", "threeAndHalf", "four", "fourAndHalf" |
| `website` | string | Filter by website: "allPlaces" (default), "withWebsite", "withoutWebsite" |
| `skipClosedPlaces` | boolean | Skip temporarily or permanently closed places (default: false) |

## Place Details ($)

| Parameter | Type | Description |
|-----------|------|-------------|
| `scrapePlaceDetailPage` | boolean | Scrape detail page for additional fields like opening hours, popular times, reviews distribution (default: false) |
| `scrapeTableReservationProvider` | boolean | Scrape restaurant reservation provider data (name, email, phone) |
| `includeWebResults` | boolean | Include "Web results" section from place listing |
| `scrapeDirectories` | boolean | Scrape businesses inside malls/shopping centers |
| `maxQuestions` | integer | Number of questions to extract (0 = first question only, 999 = all) |

## Reviews

| Parameter | Type | Description |
|-----------|------|-------------|
| `maxReviews` | integer | Number of reviews per place (leave empty for all, max 5,000 per output item) |
| `reviewsStartDate` | string | Extract reviews after date (e.g., "2024-05-03" or "8 days", "3 months") |
| `reviewsSort` | string | Sort by: "newest" (default), "mostRelevant", "highestRanking", "lowestRanking" |
| `reviewsFilterString` | string | Filter reviews by keywords (leave blank for all) |
| `reviewsOrigin` | string | Review source: "all" (default) or "google" only |
| `scrapeReviewsPersonalData` | boolean | Include reviewer ID, name, URL, photo (default: true) |

## Images ($)

| Parameter | Type | Description |
|-----------|------|-------------|
| `maxImages` | integer | Number of images per place (leave empty for all) |
| `scrapeImageAuthors` | boolean | Include image author names (slower processing) |

## Add-ons ($)

| Parameter | Type | Description |
|-----------|------|-------------|
| `scrapeContacts` | boolean | Company contacts enrichment from website (emails, social media profiles) |
| `scrapeSocialMediaProfiles` | object | Detailed social media profile enrichment (follower counts, descriptions, verification) |
| `scrapeSocialMediaProfiles.facebooks` | boolean | Enable Facebook profile scraping |
| `scrapeSocialMediaProfiles.instagrams` | boolean | Enable Instagram profile scraping |
| `scrapeSocialMediaProfiles.youtubes` | boolean | Enable YouTube channel scraping |
| `scrapeSocialMediaProfiles.tiktoks` | boolean | Enable TikTok profile scraping |
| `scrapeSocialMediaProfiles.twitters` | boolean | Enable X (Twitter) profile scraping |
| `maximumLeadsEnrichmentRecords` | integer | Business leads enrichment - max leads per place (default: 0) |
| `leadsEnrichmentDepartments` | array | Filter leads by department: "c_suite", "sales", "marketing", "product", "engineering_technical", etc. |

## Geolocation Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `countryCode` | string | Country code (e.g., "us", "uk", "de") |
| `city` | string | City name (do not include state/country here) |
| `state` | string | State/province name |
| `county` | string | County/regional district/département |
| `postalCode` | string | Postal code (combine only with countryCode, not city) |
| `customGeolocation` | object | Custom search area using GeoJSON (Polygon, MultiPolygon, Point with radiusKm) |

## Direct Input

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Google Maps URLs (max 300 results per URL) |
| `placeIds` | array | List of Google Place IDs (format: "ChIJreV9aqYWdkgROM_boL6YbwA") |

## Output Fields

### Basic Information

| Field | Description |
|-------|-------------|
| `title` | Business name |
| `subTitle` | Subtitle (if available) |
| `categoryName` | Primary business category |
| `categories` | Array of all business categories |
| `description` | Place description |
| `price` | Price level (e.g., "$10–20", "$$") |

### Contact & Location

| Field | Description |
|-------|-------------|
| `address` | Full address with street, city, state, zip, country |
| `street` | Street address |
| `city` | City name |
| `postalCode` | Postal/ZIP code |
| `state` | State/province |
| `countryCode` | Country code |
| `neighborhood` | Neighborhood name |
| `phone` | Formatted phone number |
| `phoneUnformatted` | Phone in international format (e.g., +17183565168) |
| `website` | Website URL |
| `location` | Object with latitude (lat) and longitude (lng) coordinates |
| `plusCode` | Google Plus Code |

### Identifiers

| Field | Description |
|-------|-------------|
| `placeId` | Google Place ID |
| `cid` | Google CID (Company ID) |
| `fid` | Google FID |
| `url` | Google Maps URL |
| `searchPageUrl` | Original search page URL |

### Ratings & Reviews

| Field | Description |
|-------|-------------|
| `totalScore` | Average rating (1-5) |
| `reviewsCount` | Total number of reviews |
| `reviewsDistribution` | Object with review counts by star rating (oneStar, twoStar, etc.) |
| `reviews` | Array of review objects (if maxReviews > 0) |
| `reviewsTags` | Popular review topics with counts |

### Images

| Field | Description |
|-------|-------------|
| `imageUrl` | Primary image URL |
| `imagesCount` | Total number of images |
| `imageCategories` | Array of image categories (e.g., "Menu", "Food & drink", "Vibe") |
| `images` | Array of image objects with URL, author, upload date (if maxImages > 0) |
| `imageUrls` | Array of all image URLs |

### Business Details

| Field | Description |
|-------|-------------|
| `openingHours` | Array of operating hours by day |
| `permanentlyClosed` | Boolean flag for permanently closed |
| `temporarilyClosed` | Boolean flag for temporarily closed |
| `claimThisBusiness` | Boolean flag indicating if business is unclaimed |
| `isAdvertisement` | Boolean flag for ad placements |
| `locatedIn` | Parent location (for businesses inside malls, etc.) |

### Additional Features

| Field | Description |
|-------|-------------|
| `additionalInfo` | Object with detailed characteristics (service options, accessibility, payments, etc.) |
| `menu` | Menu URL |
| `peopleAlsoSearch` | Array of similar places users search for |
| `placesTags` | Array of place-related tags |
| `questionsAndAnswers` | Q&A section data (if maxQuestions > 0) |
| `updatesFromCustomers` | Customer updates/posts |
| `ownerUpdates` | Updates from business owner |

### Restaurant-Specific

| Field | Description |
|-------|-------------|
| `reserveTableUrl` | Table reservation URL |
| `tableReservationLinks` | Array of reservation provider links |
| `orderBy` | Array of online ordering options |
| `restaurantData` | Object with restaurant-specific data (reservation provider info) |

### Hotel-Specific

| Field | Description |
|-------|-------------|
| `hotelStars` | Hotel star rating |
| `hotelDescription` | Hotel description text |
| `checkInDate` | Check-in date (if provided in input) |
| `checkOutDate` | Check-out date (if provided in input) |
| `similarHotelsNearby` | Array of similar hotels with pricing |
| `hotelAds` | Array of hotel booking ads |
| `hotelReviewSummary` | Summary of hotel reviews |

### Enrichment Data (Add-ons)

| Field | Description |
|-------|-------------|
| `emails` | Extracted email addresses (from scrapeContacts) |
| `instagrams` | Instagram profile URLs (from scrapeContacts) |
| `facebooks` | Facebook page/profile URLs (from scrapeContacts) |
| `linkedIns` | LinkedIn profile URLs (from scrapeContacts) |
| `youtubes` | YouTube channel URLs (from scrapeContacts) |
| `tiktoks` | TikTok profile URLs (from scrapeContacts) |
| `twitters` | Twitter/X profile URLs (from scrapeContacts) |
| `pinterests` | Pinterest profile URLs (from scrapeContacts) |
| `discords` | Discord server URLs (from scrapeContacts) |
| `leadsEnrichment` | Array of business leads with full name, email, job title, LinkedIn (from maximumLeadsEnrichmentRecords) |

### Metadata

| Field | Description |
|-------|-------------|
| `searchString` | Original search string used |
| `rank` | Result ranking position |
| `scrapedAt` | Timestamp when place was scraped |
| `webResults` | Web search results (if includeWebResults enabled) |
