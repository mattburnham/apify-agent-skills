# Market Research Workflows

Multi-step workflows that combine multiple Actors for comprehensive market research and analysis.

---

## Workflow 1: Geographic Market Analysis

Analyze market density and business landscape in a specific geographic area.

### Checklist

```
Task Progress:
- [ ] Clarify business type and location
- [ ] Step 1: Run Google Maps Scraper for business density
- [ ] Step 2: Run Google Maps Extractor for detailed data
- [ ] Analyze market saturation and gaps
- [ ] Export market analysis report
```

### Example Interaction

**User:** "Analyze the yoga studio market in Austin, Texas"

**Response:**
1. Start with Google Maps to find all yoga studios
2. Extract top 50 businesses with ratings/reviews
3. Analyze:
   - Market density by neighborhood
   - Average ratings and review counts
   - Price range indicators
   - Service offerings (hot yoga, aerial, etc.)
4. Identify underserved areas or niches

---

## Workflow 2: Consumer Trend Research

Research consumer interest and trends using Google Trends and social signals.

### Checklist

```
Task Progress:
- [ ] Get keywords/topics from user
- [ ] Step 1: Run Google Trends Scraper for search interest
- [ ] Step 2: Run Instagram Hashtag Stats for social validation
- [ ] Step 3: Analyze regional variations
- [ ] Generate trend report with market sizing
```

### Example Interaction

**User:** "Research interest in sustainable fashion"

**Response:**
1. Step 1 - Get Google Trends data:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/google-trends-scraper" \
  --input '{"searchTerms": ["sustainable fashion", "ethical clothing", "slow fashion"], "geo": "US"}' \
  --output fashion-trends.json \
  --format json
```

2. Step 2 - Validate with Instagram hashtag stats:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-stats" \
  --input '{"hashtags": ["sustainablefashion", "ethicalfashion", "slowfashion"]}' \
  --output hashtag-stats.json \
  --format json
```

3. Report: "Sustainable fashion searches up 45% YoY. #sustainablefashion has 12.5M posts with 2.3% weekly growth. Peak interest in Q1 and Q4. Top markets: California, New York, Texas."

---

## Workflow 3: Pricing and Demand Research

Analyze market pricing using Facebook Marketplace data.

### Checklist

```
Task Progress:
- [ ] Get product category and location from user
- [ ] Step 1: Run Facebook Marketplace Scraper
- [ ] Analyze pricing distribution
- [ ] Identify demand signals (listing frequency, sell-through)
- [ ] Generate pricing strategy report
```

### Example Interaction

**User:** "What's the market price for vintage furniture in Los Angeles?"

**Response:**
1. Scrape Facebook Marketplace listings:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-marketplace-scraper" \
  --input '{"searchQuery": "vintage furniture", "location": "Los Angeles, CA", "maxItems": 200}' \
  --output vintage-furniture-prices.csv \
  --format csv
```

2. Analyze:
   - Price range distribution
   - Most common price points
   - Premium vs budget segments
   - Condition impact on pricing

3. Report: "Found 200 listings. Price range: $50-$2,500. Median: $275. Mid-century modern commands 40% premium. Refinished pieces priced 2x higher than as-is."

---

## Workflow 4: Event Market Analysis

Research event market opportunities and community interests.

### Checklist

```
Task Progress:
- [ ] Get event type and location from user
- [ ] Step 1: Run Facebook Events Scraper
- [ ] Analyze event frequency and attendance
- [ ] Identify market gaps and timing patterns
- [ ] Generate event market report
```

### Example Interaction

**User:** "Research the wellness event market in Denver"

**Response:**
1. Scrape wellness-related events:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-events-scraper" \
  --input '{"searchQuery": "wellness yoga meditation", "location": "Denver, CO", "maxItems": 100}' \
  --output denver-wellness-events.csv \
  --format csv \
  --fields basic
```

2. Analyze:
   - Event frequency by type
   - Average attendance (going/interested)
   - Pricing patterns (free vs paid)
   - Peak days and times

---

## Workflow 5: Community and Consumer Insights

Research consumer needs through Facebook Groups discussions.

### Checklist

```
Task Progress:
- [ ] Get topic/niche from user
- [ ] Step 1: Run Facebook Groups Scraper for relevant groups
- [ ] Analyze group sizes and activity levels
- [ ] Identify common pain points and needs
- [ ] Report on market opportunities
```

### Example Interaction

**User:** "What do parents in the homeschool community need?"

**Response:**
1. Find homeschool groups:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/facebook-groups-scraper" \
  --input '{"searchQuery": "homeschool parents", "maxItems": 50}' \
  --output homeschool-groups.json \
  --format json
```

2. Analyze:
   - Total addressable market (combined membership)
   - Regional distribution
   - Sub-niches (curriculum, special needs, secular, religious)
   - Activity levels indicating engagement

---

## Workflow 6: Hospitality Market Research

Analyze hotel and accommodation market using Booking.com and TripAdvisor.

### Checklist

```
Task Progress:
- [ ] Get destination and hotel type from user
- [ ] Step 1: Run Booking Scraper for property data
- [ ] Step 2: Run TripAdvisor Reviews for guest feedback
- [ ] Analyze pricing, ratings, and amenities
- [ ] Generate market positioning report
```

### Example Interaction

**User:** "Research the boutique hotel market in Nashville"

**Response:**
1. Step 1 - Get hotel listings:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "voyager/booking-scraper" \
  --input '{"search": "Nashville, Tennessee", "maxItems": 50}' \
  --output nashville-hotels.csv \
  --format csv
```

2. Step 2 - Analyze guest reviews:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "maxcopell/tripadvisor-reviews" \
  --input '{"startUrls": [{"url": "https://www.tripadvisor.com/Hotel_Review-..."}], "maxReviews": 100}' \
  --output hotel-reviews.json \
  --format json
```

3. Report: "Found 50 boutique hotels. Rating range: 7.5-9.4. Price range: $180-$450/night. Top amenities: Rooftop bars, live music, local art. Common complaints: Parking, noise from Broadway."

---

## Workflow 7: Social Media Market Validation

Validate product/service ideas through Instagram engagement analysis.

### Checklist

```
Task Progress:
- [ ] Get product category/niche from user
- [ ] Step 1: Run Instagram Hashtag Scraper for content analysis
- [ ] Step 2: Run Instagram Reel Scraper for engagement patterns
- [ ] Analyze content performance and audience signals
- [ ] Generate market validation report
```

### Example Interaction

**User:** "Is there a market for plant-based pet food?"

**Response:**
1. Step 1 - Analyze hashtag content:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-scraper" \
  --input '{"hashtags": ["veganpetfood", "plantbaseddog", "vegancat"], "resultsLimit": 100}' \
  --output vegan-pet-content.csv \
  --format csv
```

2. Step 2 - Check reel engagement:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-reel-scraper" \
  --input '{"hashtag": "veganpetfood", "resultsLimit": 50}' \
  --output vegan-pet-reels.json \
  --format json
```

3. Report engagement rates, follower counts of key accounts, content themes, and audience sentiment.

---

## Tips for Market Research

- **Triangulate data**: Use multiple sources to validate findings
- **Geographic segmentation**: Compare markets across regions
- **Trend analysis**: Look for growth patterns, not just current state
- **Competitive density**: High competition may indicate strong demand
- **Consumer voice**: Groups and comments reveal unmet needs
- **Pricing signals**: Marketplace data shows willingness to pay
- **Timing patterns**: Events and posts reveal seasonal demand
