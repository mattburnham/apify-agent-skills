# Google Trends Scraper

**Actor ID:** `apify/google-trends-scraper`

Scrape data from Google Trends by search terms or URLs. Specify locations, define time ranges, select categories to get interest by subregion and over time, related queries and topics, and more.

## Key Input Parameters

```json
{
  "searchTerms": ["webscraping"],
  "timeRange": "today 3-m",
  "geo": "US",
  "category": "0"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `searchTerms` | array | List of search terms to be scraped (required if `spreadsheetId` not provided) |
| `isMultiple` | boolean | If checked comma will be handled as search for multiple terms (default: false) |
| `startUrls` | array | Google Trends URLs with applied filters |
| `timeRange` | string | Predefined search time range: "now 1-H", "now 4-H", "now 1-d", "now 7-d", "today 1-m", "today 3-m", "today 5-y", "all" (default: "today 12-m") |
| `customTimeRange` | string | Custom time range in format: `YYYY-MM-DD YYYY-MM-DD`. Takes precedence over `timeRange` |
| `geo` | string | Geo area code to get results from (defaults to "Worldwide"). Returns different fields based on country size |
| `viewedFrom` | string | Country code for residential proxies to ensure correct results |
| `category` | string | Category to filter the search: "3" (Arts & Entertainment), "47" (Autos & Vehicles), "44" (Beauty & Fitness), "22" (Business & Industrial), "12" (Computers & Electronics), "5" (Finance), "7" (Food & Drink), "71" (Games), "8" (Health), "45" (Hobbies & Leisure), "65" (Home & Garden), "11" (Internet & Telecom), "13" (Jobs & Education), "958" (Law & Government), "19" (News), "16" (Online Communities), "299" (People & Society), "14" (Pets & Animals), "66" (Real Estate), "29" (Reference), "533" (Science), "174" (Shopping), "18" (Sports), "20" (Travel), "67" (World Localities) (default: "All categories") |
| `spreadsheetId` | string | Google Sheet ID to load search terms from. Must be publicly available with one column (row 1 is title) |
| `searchGroupKeyword` | string | Search by letter or keywords (limited without login) |
| `searchGroupYear` | string | Filter posts by year (requires searchGroupKeyword) |
| `maxItems` | integer | Limit of product items to be scraped. Zero means no limit (default: 0) |
| `maxConcurrency` | integer | Number of pages to open in parallel (default: 10) |
| `maxRequestRetries` | integer | Number of retry attempts for failed requests (default: 7) |
| `pageLoadTimeoutSecs` | integer | Page load timeout in seconds before retry (default: 180) |
| `skipDebugScreen` | boolean | Do not save snapshot to KV Store (default: false) |

## Output Fields

### Basic Information

| Field | Description |
|-------|-------------|
| `inputUrlOrTerm` | Original search term or URL input |
| `searchTerm` | The search term used |

### Interest Over Time

| Field | Description |
|-------|-------------|
| `interestOverTime_timelineData` | Array of timeline data points with interest values |
| `interestOverTime_averages` | Average interest values |

Timeline data object fields:

| Field | Description |
|-------|-------------|
| `time` | Unix timestamp |
| `formattedTime` | Human-readable time range |
| `formattedAxisTime` | Axis-formatted time |
| `value` | Array of interest values (0-100) |
| `hasData` | Array of booleans indicating data availability |
| `formattedValue` | Array of formatted value strings |
| `isPartial` | Boolean indicating if data is partial (optional) |

### Geographic Interest

| Field | Description |
|-------|-------------|
| `interestBySubregion` | Interest data by subregion (for larger countries) |
| `interestByCity` | Interest data by city (for smaller countries) |
| `interestBy` | Interest by area (when geo is omitted/Worldwide) |

Geographic data object fields:

| Field | Description |
|-------|-------------|
| `geoCode` | Geographic area code |
| `geoName` | Geographic area name |
| `value` | Array of interest values |
| `formattedValue` | Array of formatted values |
| `maxValueIndex` | Index of maximum value |
| `hasData` | Array of booleans indicating data availability |

### Related Topics

| Field | Description |
|-------|-------------|
| `relatedTopics_top` | Array of top related topic objects |
| `relatedTopics_rising` | Array of rising related topic objects |

Related topic object fields:

| Field | Description |
|-------|-------------|
| `topic` | Object with mid, title, and type |
| `topic.mid` | Topic machine ID |
| `topic.title` | Topic title |
| `topic.type` | Topic type classification |
| `value` | Relative interest value or percentage increase |
| `formattedValue` | Formatted value string (e.g., "100" or "+50%") |
| `hasData` | Boolean indicating data availability |
| `link` | Google Trends exploration link |

### Related Queries

| Field | Description |
|-------|-------------|
| `relatedQueries_top` | Array of top related query objects |
| `relatedQueries_rising` | Array of rising related query objects |

Related query object fields:

| Field | Description |
|-------|-------------|
| `query` | Query string |
| `value` | Relative interest value or percentage increase |
| `formattedValue` | Formatted value string (e.g., "100" or "+4,250%") |
| `hasData` | Boolean indicating data availability |
| `link` | Google Trends exploration link |
