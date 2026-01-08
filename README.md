# Apify Claude Code plugin marketplace

Official Apify plugin marketplace for Claude Code - enabling web scraping, data extraction, and automation directly from Claude's CLI.

## Installation

### Add the marketplace

```bash
/plugin marketplace add apify/claude-code-marketplace
```

### Install a plugin

```bash
/plugin install lead-generation@apify-marketplace
```

## Prerequisites

1. **Apify Account**: Sign up at [apify.com](https://apify.com)
2. **API Token**: Get your token from [Apify Console > Integrations](https://console.apify.com/account/integrations)
3. **Set Environment Variable**: Add to your `.env` file:
   ```
   APIFY_TOKEN=your_token_here
   ```

## Available plugins

### lead-generation

Generate and enrich B2B/B2C leads using Apify scrapers across Google Maps, social media, and websites.

#### Skills

The `lead-finder` skill allows Claude to automatically invoke lead generation when you ask for prospects, leads, or business contacts.

**Example prompts:**
- "Find me coffee shops in Seattle"
- "Get contact info from these websites"
- "Build a lead list for fitness influencers"


## Supported Apify Actors

| Actor | Use Case |
|-------|----------|
| Google Maps Scraper | Find local businesses |
| Contact Details Scraper | Extract emails & socials from URLs |
| Instagram Profile Scraper | Influencer data |
| TikTok Profile Scraper | Creator metrics |
| Facebook Pages Scraper | Business page data |
| Facebook Groups Scraper | Community prospecting |

## Output format

All commands export data to CSV format for easy import into CRMs, spreadsheets, or other tools.

## Pricing

Apify actors use pay-per-result pricing. Check individual actor pricing on [apify.com](https://apify.com).

## Future plugins

### Outcome-based
- `brand-monitoring` - Review tracking, sentiment analysis
- `competitor-intelligence` - Benchmarking, feature comparison
- `influencer-discovery` - Find and vet influencers
- `trend-analysis` - Hashtag tracking, viral content

### Platform-based
- `google-intelligence` - Maps, Search, Trends, Booking
- `instagram-intelligence` - Profiles, Posts, Reels, Hashtags
- `facebook-intelligence` - Pages, Posts, Groups, Ads
- `tiktok-intelligence` - Profiles, Videos, Hashtags, Sounds
- `youtube-intelligence` - Channels, Videos, Shorts, Comments

## Contributing

1. Fork this repository
2. Create your plugin in `plugins/your-plugin-name/`
3. Add entry to `.claude-plugin/marketplace.json`
4. Submit a pull request


## Support

- [Apify Documentation](https://docs.apify.com)
- [Apify Discord](https://discord.gg/jyEM2PRvMU)
