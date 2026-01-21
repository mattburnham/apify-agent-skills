# Tripadvisor Reviews Scraper

**Actor ID:** `maxcopell/tripadvisor-reviews`

Get and download reviews for chosen places on Tripadvisor. Extract the review text, URL, rating, date of travel, published date, basic reviewer info, owner's response, helpful votes, images, review language, place details. Download reviews in XML, JSON, CSV.

## Key Input Parameters

```json
{
  "startUrls": [
    {
      "url": "https://www.tripadvisor.com/Hotel_Review-g60763-d208453-Reviews-Hilton_New_York_Times_Square-New_York_City_New_York.html"
    }
  ],
  "maxItemsPerQuery": 50,
  "scrapeReviewerInfo": true,
  "lastReviewDate": "",
  "reviewRatings": ["ALL_REVIEW_RATINGS"],
  "reviewsLanguages": ["ALL_REVIEW_LANGUAGES"]
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | URLs of specific Tripadvisor places to get reviews from (required) |
| `sourceDatasetId` | string | Dataset ID of a finished Tripadvisor Scraper run to get start URLs from |
| `maxItemsPerQuery` | integer | Limit reviews for each place (default: 50, use large value like 1 million to get all reviews) |
| `scrapeReviewerInfo` | boolean | Scrape reviewer info (name, profile picture, location etc.) (default: true) |
| `lastReviewDate` | string | Date where scraper stops loading older reviews (format: YYYY-MM-DD or relative like "3 days", "1 week") |
| `reviewRatings` | array | Filter by review ratings: "ALL_REVIEW_RATINGS", "1", "2", "3", "4", "5" (default: ["ALL_REVIEW_RATINGS"]) |
| `reviewsLanguages` | array | Filter by review languages (default: ["ALL_REVIEW_LANGUAGES"]) |

## Output Fields

### Review Information

| Field | Description |
|-------|-------------|
| `id` | Review ID |
| `url` | Direct review URL |
| `title` | Review title |
| `text` | Review text content |
| `lang` | Review language code |
| `locationId` | Location ID |
| `publishedDate` | Date review was published (ISO format) |
| `publishedPlatform` | Platform used to publish (e.g., "Mobile", "Desktop") |
| `rating` | Rating given (1-5) |
| `helpfulVotes` | Number of helpful votes |
| `travelDate` | Date of travel (YYYY-MM format) |
| `machineTranslated` | Whether review is machine translated |
| `machineTranslatable` | Whether review can be machine translated |

### Reviewer Information

| Field | Description |
|-------|-------------|
| `user` | Object with reviewer information |
| `user.userId` | Reviewer's user ID |
| `user.firstName` | Reviewer's first name |
| `user.lastInitial` | Reviewer's last initial |
| `user.name` | Reviewer's full name |
| `user.reviewerType` | Type of reviewer |
| `user.contributions` | Object with contribution statistics |
| `user.contributions.reviews` | Total number of reviews |
| `user.contributions.reviewCityCount` | Number of cities reviewed |
| `user.contributions.restaurantReviews` | Number of restaurant reviews |
| `user.contributions.hotelReviews` | Number of hotel reviews |
| `user.contributions.attractionReviews` | Number of attraction reviews |
| `user.contributions.helpfulVotes` | Number of helpful votes received |
| `user.contributions.photosCount` | Number of photos uploaded |
| `user.contributions.badgesCount` | Number of badges earned |
| `user.memberId` | Member ID |
| `user.username` | Username |
| `user.userLocation` | Object with location information (name, id) |
| `user.avatar` | Avatar image URL |
| `user.link` | Link to user profile |
| `user.points` | User points |
| `user.createdTime` | Account creation timestamp (ISO format) |
| `user.locale` | User locale |

### Owner Response

| Field | Description |
|-------|-------------|
| `ownerResponse` | Object with owner's response (null if no response) |
| `ownerResponse.id` | Response ID |
| `ownerResponse.title` | Response title |
| `ownerResponse.text` | Response text content |
| `ownerResponse.lang` | Response language |
| `ownerResponse.publishedDate` | Date response was published (ISO format) |
| `ownerResponse.responder` | Name of responder |

### Subratings

| Field | Description |
|-------|-------------|
| `subratings` | Array of subrating objects |

Subrating object fields:

| Field | Description |
|-------|-------------|
| `name` | Subrating category (e.g., "Value", "Location", "Service") |
| `value` | Rating value (1-5) |

### Photos

| Field | Description |
|-------|-------------|
| `photos` | Array of photo objects |

Photo object fields:

| Field | Description |
|-------|-------------|
| `id` | Photo ID |
| `locations` | Array of location objects associated with photo |
| `publishedDate` | Date photo was published (ISO format) |
| `user` | User object who uploaded the photo |
| `helpfulVotes` | Number of helpful votes for photo |
| `isBlessed` | Whether photo is blessed |
| `uploadedDate` | Date photo was uploaded (ISO format) |
| `image` | Photo image URL |

### Place Information

| Field | Description |
|-------|-------------|
| `placeInfo` | Object with place information |
| `placeInfo.id` | Place ID |
| `placeInfo.name` | Place name |
| `placeInfo.numberOfReviews` | Total number of reviews for place |
| `placeInfo.locationString` | Location string (e.g., "New York City, New York") |
| `placeInfo.latitude` | Latitude coordinate |
| `placeInfo.longitude` | Longitude coordinate |
| `placeInfo.webUrl` | Web URL of place |
| `placeInfo.website` | Official website of place |
| `placeInfo.address` | Full address string |
| `placeInfo.addressObj` | Object with structured address information |
| `placeInfo.addressObj.street1` | Street address line 1 |
| `placeInfo.addressObj.street2` | Street address line 2 |
| `placeInfo.addressObj.city` | City |
| `placeInfo.addressObj.state` | State |
| `placeInfo.addressObj.country` | Country |
| `placeInfo.addressObj.postalcode` | Postal code |
