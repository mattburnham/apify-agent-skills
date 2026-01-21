# Facebook Photos Scraper

**Actor ID:** `apify/facebook-photos-scraper`

Extract data from one or multiple Facebook images. Get image ID, Facebook photo URL, image URL, OCR text, and more. Download the data in JSON, CSV, and Excel and use it in apps, spreadsheets, and reports.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.facebook.com/humansofnewyork"}],
  "resultsLimit": 10
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Valid Facebook page/profile URLs (required) |
| `resultsLimit` | integer | Maximum number of results to return (default: 10, max: ~5000) |

## Output Fields

| Field | Description |
|-------|-------------|
| `id` | Photo ID |
| `image` | Direct image URL |
| `url` | Direct Facebook photo URL |
| `dataType` | Data type (e.g., "photo") |
| `ocrText` | OCR extracted text from image |
| `facebookUrl` | Source Facebook page/profile URL |
