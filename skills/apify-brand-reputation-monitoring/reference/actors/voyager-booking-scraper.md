# Booking.com Scraper

**Actor ID:** `voyager/booking-scraper`

Scrape hotel listings, prices, availability, and basic information from Booking.com for reputation monitoring and competitive analysis.

## Key Input Parameters

```json
{
  "search": "New York",
  "checkIn": "2026-03-01",
  "checkOut": "2026-03-03",
  "rooms": 1,
  "adults": 2,
  "maxItems": 50,
  "sortBy": "review_score_and_price",
  "propertyType": "Hotels"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `search` | string | Destination name (required) |
| `startUrls` | array | Alternative to search: Insert URLs to start with instead of a destination name. Hotel search URL's filters will be applied |
| `checkIn` | string | Check-in date in YYYY-MM-DD format or {number} {unit}. Input the date in the UTC timezone |
| `checkOut` | string | Check-out date in YYYY-MM-DD format or {number} {unit}. Input the date in the UTC timezone |
| `flexWindow` | string | Stay date flexibility in days: "0", "1", "2", "3", "7" (e.g., setting "3" will scrape hotels with date range up to 3 days before/after) |
| `rooms` | integer | Number of rooms (default: 1) |
| `adults` | integer | Number of adults (default: 2) |
| `children` | integer | Number of children (default: 0) |
| `currency` | string | Currency code: "ARS", "AUD", "AZN", "BHD", "BRL", "BGN", "CAD", "XOF", "CLP", "CNY", "COP", "CZK", "DKK", "EGP", "EUR", "FJD", "GEL", "HKD", "HUF", "INR", "IDR", "ILS", "JPY", "JOD", "KZT", "KRW", "KWD", "MYR", "MXN", "MDL", "NAD", "TWD", "NZD", "NOK", "OMR", "PLN", "GBP", "QAR", "RON", "RUB", "SAR", "SGD", "ZAR", "SEK", "CHF", "THB", "TRY", "AED", "USD", "UAH" (default: "USD") |
| `language` | string | Language code: "en-gb", "en-us", "de", "nl", "fr", "es", "es-ar", "ca", "it", "pt-pt", "pt-br", "no", "fi", "sv", "da", "cs", "hu", "ro", "ja", "zh-cn", "zh-tw", "pl", "el", "ru", "tr", "bg", "ar", "ko", "he", "lv", "uk", "id", "ms", "th", "et", "hr", "lt", "sk", "sr", "sl", "vi", "tl", "is" (default: "en-gb") |
| `maxItems` | integer | Maximum number of properties to scrape. Input a value over 1000 to activate the 'overcome 1000 results limit' feature (default: 10) |
| `sortBy` | string | Sort order: "bayesian_review_score", "distance_from_search", "class_asc", "price", "review_score_and_price", "class_and_price" (default: "distance_from_search") |
| `minScore` | string | Minimum rating in "8.4" format. Searching below rating of 5 may be inefficient as it's not natively supported by Booking |
| `propertyType` | string | Property type: "none", "Hotels", "Apartments", "Hostels", "Guest houses", "Homestays", "Bed and breakfasts", "Holiday homes", "Boats", "Villas", "Motels", "Resorts", "Holiday parks", "Campsites", "Luxury tents" (default: "none") |
| `starsCountFilter` | string | Stars count filter: "any", "1", "2", "3", "4", "5", "unrated" (default: "any"). Also includes Booking's apartment-like properties 'square' rating |
| `minMaxPrice` | string | Price range per night (e.g., "100-150" or "100+") (default: "0-999999") |

## Output Fields

### Basic Property Information

| Field | Description |
|-------|-------------|
| `url` | Direct URL to the property on Booking.com |
| `name` | Property name |
| `type` | Property type (hotel, apartment, resort, etc.) |
| `address` | Full property address |
| `city` | City name |
| `country` | Country name |
| `zipcode` | Postal/ZIP code |
| `countryCode` | ISO country code |

### Location Details

| Field | Description |
|-------|-------------|
| `latitude` | Geographic latitude coordinate |
| `longitude` | Geographic longitude coordinate |
| `district` | District or neighborhood name |
| `distanceToCityCenter` | Distance to city center (with unit) |

### Ratings and Reviews

| Field | Description |
|-------|-------------|
| `rating` | Overall review score (0-10 scale) |
| `reviews` | Total number of reviews |
| `reviewScore` | Numeric review score |
| `reviewCount` | Review count |
| `guestReviews` | Object containing review breakdown by category |

### Pricing Information

| Field | Description |
|-------|-------------|
| `price` | Current price per night |
| `currency` | Currency code |
| `originalPrice` | Original price before discount (if applicable) |
| `pricePerNight` | Price per night value |
| `totalPrice` | Total price for entire stay |

### Property Features

| Field | Description |
|-------|-------------|
| `stars` | Star rating (1-5) |
| `facilities` | Array of available facilities/amenities |
| `description` | Property description text |
| `accommodationType` | Type of accommodation |
| `roomType` | Room type for the listed price |

### Availability

| Field | Description |
|-------|-------------|
| `available` | Boolean indicating availability |
| `urgencyMessage` | Urgency text (e.g., "Only 2 rooms left") |
| `soldOut` | Boolean indicating if property is sold out |

### Images

| Field | Description |
|-------|-------------|
| `image` | Main property image URL |
| `images` | Array of additional image URLs |

### Additional Information

| Field | Description |
|-------|-------------|
| `id` | Unique property identifier |
| `hotelId` | Booking.com hotel ID |
| `checkIn` | Check-in date used in search |
| `checkOut` | Check-out date used in search |
| `rooms` | Number of rooms searched |
| `adults` | Number of adults searched |
