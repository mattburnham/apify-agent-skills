# Google Search Scraper

**Actor ID:** `apify/google-search-scraper`

Scrape Google search results for lead discovery.

## Key Input Parameters

```json
{
  "queries": "software companies in Austin\nSaaS startups in Texas",
  "maxPagesPerQuery": 1,
  "resultsPerPage": 100,
  "countryCode": "us",
  "maximumLeadsEnrichmentRecords": 10
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `queries` | string | Search queries - use newlines to separate multiple queries (required). Can use advanced Google search techniques like "AI site:twitter.com" or "javascript OR python". Max 32 words per query. |
| `maxPagesPerQuery` | integer | Max pages to scrape per query (default: 1) |
| `resultsPerPage` | integer | Results per page: 10, 20, 30, 40, 50, 100 (default: 100). Note: actual results may differ due to Google's internal filtering. |
| `countryCode` | string | Country code for results (e.g., "us", "uk", "de"). Specifies Google domain and search country. |
| `languageCode` | string | Interface language code (e.g., "en", "es", "zh-CN"). Affects menus/buttons and may affect search results. |
| `searchLanguage` | string | Restricts search results to specific language (e.g., "en", "de", "ja"). Different from languageCode. |
| `mobileResults` | boolean | Use mobile user agent (default: false) |

## Date Filters

| Parameter | Type | Description |
|-----------|------|-------------|
| `afterDate` | string | Filter results after date. Absolute (e.g., "2024-05-03") or relative (e.g., "8 days", "3 months"). UTC timezone. |
| `beforeDate` | string | Filter results before date. Absolute (e.g., "2024-05-03") or relative (e.g., "8 days", "3 months"). UTC timezone. |
| `quickDateRange` | string | Quick date range filter: d[number] for days, h[number] for hours, w[number] for weeks, m[number] for months, y[number] for years (e.g., "d10", "m3", "y1"). Don't combine with afterDate/beforeDate. |

## Business Leads Enrichment ($)

| Parameter | Type | Description |
|-----------|------|-------------|
| `maximumLeadsEnrichmentRecords` | integer | Max business leads per domain with employee names, job titles, emails, LinkedIn profiles, company data (default: 0 = disabled). Contains personal data - comply with GDPR. |
| `leadsEnrichmentDepartments` | array | Filter leads by department: "c_suite", "sales", "marketing", "product", "engineering_technical", "design", "education", "finance", "human_resources", "information_technology", "legal", "medical_health", "operations", "consulting". Only works when maximumLeadsEnrichmentRecords > 0. |

## AI Features ($)

| Parameter | Type | Description |
|-----------|------|-------------|
| `aiMode` | string | Google AI Mode for Answer Engine Optimization (AEO), GEO targeting, brand visibility tracking: "aiModeOff" (default), "aiModeWithSearchResults", "aiModeOnly" |
| `perplexitySearch` | object | Perplexity AI search for cross-platform analysis. Object with: `enablePerplexity` (boolean), `searchRecency` ("day", "week", "month", "year"), `returnImages` (boolean), `returnRelatedQuestions` (boolean) |

## Advanced Search Filters

| Parameter | Type | Description |
|-----------|------|-------------|
| `site` | string | Restrict search to specific site (e.g., "twitter.com") |
| `relatedToSite` | string | Find sites related to specified domain |
| `wordsInText` | string | Search for words in page text |
| `wordsInTitle` | string | Search for words in page title |
| `wordsInUrl` | string | Search for words in URL |
| `fileTypes` | array | Filter by file types (e.g., ["pdf", "doc"]) |
| `includeUnfilteredResults` | boolean | Include results Google normally filters out (may return more results) |
| `saveHtml` | boolean | Save HTML of results pages (default: false) |
| `saveHtmlToKeyValueStore` | boolean | Save HTML to key-value store instead of dataset (default: false) |

## Output Fields

### Basic Search Result

| Field | Description |
|-------|-------------|
| `title` | Result title |
| `url` | Result URL |
| `displayedUrl` | Displayed URL |
| `description` | Result snippet/description |
| `emphasizedKeywords` | Keywords highlighted in description |
| `siteLinks` | Additional site links |
| `searchQuery` | Object with search query details (term, url, device, page, type, domain, countryCode, languageCode, resultsPerPage) |
| `rank` | Result ranking position |

### Business Leads (Add-on)

Available when `maximumLeadsEnrichmentRecords` > 0:

| Field | Description |
|-------|-------------|
| `leadsEnrichment` | Array of enriched business leads with full name, email, job title, department, seniority, LinkedIn profile, company information (name, domain, industry, employee count) |

### AI Results (Add-on)

Available when `aiMode` is enabled or `perplexitySearch.enablePerplexity` is true:

| Field | Description |
|-------|-------------|
| `aiOverview` | Google AI Mode overview and analysis (when aiMode enabled) |
| `perplexityAnswer` | Perplexity AI generated answer with citations (when perplexitySearch enabled) |
