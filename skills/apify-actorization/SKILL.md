---
name: apify-actorization
description: Convert existing projects into Apify Actors. Supports JavaScript/TypeScript (SDK with Actor.init/exit), Python (SDK with async context manager), and other languages (CLI-based wrapper scripts).
---

# Apify Actorization

Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs packaged as Docker images that accept well-defined JSON input, perform an action, and optionally produce structured JSON output.

## When to Use This Skill

Use this skill when:
- Converting an existing project to run on Apify platform
- Adding Apify SDK integration to a project
- Wrapping a CLI tool or script as an Actor
- Migrating a Crawlee project to Apify

## Prerequisites

Before actorizing a project, verify that `apify` CLI is installed:

```bash
apify --help
```

If not installed:

```bash
curl -fsSL https://apify.com/install-cli.sh | bash

# Or (Mac): brew install apify-cli
# Or (Windows): irm https://apify.com/install-cli.ps1 | iex
# Or: npm install -g apify-cli
```

Verify CLI is logged in:

```bash
apify info  # Should return your username
```

If not logged in, check if `APIFY_TOKEN` environment variable is defined. If not, ask the user to generate one at https://console.apify.com/settings/integrations, then:

```bash
apify login -t $APIFY_TOKEN
```

## Actorization Workflow

### Step 1: Analyze the Project

Before making changes, understand the project:

1. **Identify the language** - JavaScript/TypeScript, Python, or other
2. **Find the entry point** - The main file that starts execution
3. **Identify inputs** - Command-line arguments, environment variables, config files
4. **Identify outputs** - Files, console output, API responses
5. **Check for state** - Does it need to persist data between runs?

### Step 2: Initialize Actor Structure

Run in the project root:

```bash
apify init
```

This creates:
- `.actor/actor.json` - Actor configuration and metadata
- `.actor/input_schema.json` - Input definition for the Apify Console
- `Dockerfile` (if not present) - Container image definition

### Step 3: Apply Language-Specific Changes

#### JavaScript/TypeScript Projects

**Install the Apify SDK:**

```bash
npm install apify
```

**Wrap the main code with Actor lifecycle methods:**

```javascript
import { Actor } from 'apify';

// Initialize connection to Apify platform
await Actor.init();

// ============================================
// Your existing code goes here
// ============================================

// Example: Get input from Apify Console or API
const input = await Actor.getInput();
console.log('Input:', input);

// Example: Your crawler or processing logic
// const crawler = new PlaywrightCrawler({ ... });
// await crawler.run([input.startUrl]);

// Example: Push results to dataset
// await Actor.pushData({ result: 'data' });

// ============================================
// End of your code
// ============================================

// Graceful shutdown
await Actor.exit();
```

**Key points:**
- `Actor.init()` configures storage to use Apify API when running on platform
- `Actor.exit()` handles graceful shutdown and cleanup
- Both calls must be awaited
- Local execution remains unchanged - the SDK automatically detects the environment

#### Python Projects

**Install the Apify SDK:**

```bash
pip install apify
```

**Wrap the main function with the Actor context manager:**

```python
import asyncio
from apify import Actor

async def main() -> None:
    async with Actor:
        # ============================================
        # Your existing code goes here
        # ============================================

        # Example: Get input from Apify Console or API
        actor_input = await Actor.get_input()
        print(f'Input: {actor_input}')

        # Example: Your crawler or processing logic
        # crawler = PlaywrightCrawler(...)
        # await crawler.run([actor_input.get('startUrl')])

        # Example: Push results to dataset
        # await Actor.push_data({'result': 'data'})

        # ============================================
        # End of your code
        # ============================================

if __name__ == '__main__':
    asyncio.run(main())
```

**Key points:**
- `async with Actor:` handles both initialization and cleanup
- Automatically manages platform event listeners and graceful shutdown
- Local execution remains unchanged - the SDK automatically detects the environment

#### Other Languages (CLI-based)

For languages without an SDK (Go, Rust, Java, etc.), create a wrapper script:

**1. Create `start.sh` in project root:**

```bash
#!/bin/bash
set -e

# Get input from Apify key-value store
INPUT=$(apify actor:get-input)

# Parse input values (adjust based on your input schema)
MY_PARAM=$(echo "$INPUT" | jq -r '.myParam // "default"')

# Run your application with the input
./your-application --param "$MY_PARAM"

# If your app writes to a file, push it to key-value store
# apify actor:set-value OUTPUT --contentType application/json < output.json

# Or push structured data to dataset
# apify actor:push-data '{"result": "value"}'
```

**2. Update Dockerfile:**

```dockerfile
FROM your-base-image

# Install apify-cli and jq
RUN npm install -g apify-cli
RUN apt-get update && apt-get install -y jq

# Copy your application
COPY . .

# Build your application if needed
RUN ./build.sh

# Make start script executable
RUN chmod +x start.sh

# Run the wrapper script
CMD ["./start.sh"]
```

### Step 4: Configure Input Schema

Map your application's inputs to `.actor/input_schema.json`. Validate your schema against the official JSON Schema from the `@apify/json_schemas` npm package (`input.schema.json`).

```json
{
    "title": "My Actor Input",
    "type": "object",
    "schemaVersion": 1,
    "properties": {
        "startUrl": {
            "title": "Start URL",
            "type": "string",
            "description": "The URL to start processing from",
            "editor": "textfield",
            "prefill": "https://example.com"
        },
        "maxItems": {
            "title": "Max Items",
            "type": "integer",
            "description": "Maximum number of items to process",
            "default": 100,
            "minimum": 1
        }
    },
    "required": ["startUrl"]
}
```

**Mapping guidelines:**
- Command-line arguments → input schema properties
- Environment variables → input schema or Actor env vars in actor.json
- Config files → input schema with object/array types
- Flatten deeply nested structures for better UX

### Step 5: Configure Output

Define output structure in `.actor/output_schema.json`. Validate against the JSON Schema from the `@apify/json_schemas` npm package (`output.schema.json`).

**For table-like data (multiple items):**
- Use `Actor.pushData()` (JS) or `Actor.push_data()` (Python)
- Each item becomes a row in the dataset

**For single files or blobs:**
- Use key-value store: `Actor.setValue()` / `Actor.set_value()`
- Get the public URL and include it in the dataset:

```javascript
// Store file with public access
await Actor.setValue('report.pdf', pdfBuffer, { contentType: 'application/pdf' });

// Get the public URL
const storeInfo = await Actor.openKeyValueStore();
const publicUrl = `https://api.apify.com/v2/key-value-stores/${storeInfo.id}/records/report.pdf`;

// Include URL in dataset output
await Actor.pushData({ reportUrl: publicUrl });
```

**For multiple files with a common prefix (collections):**

```javascript
// Store multiple files with a prefix
for (const [name, data] of files) {
    await Actor.setValue(`screenshots/${name}`, data, { contentType: 'image/png' });
}
// Files are accessible at: .../records/screenshots%2F{name}
```

### Step 6: Handle State (Optional)

For long-running or resumable actors:

**Request Queue** - For pausable, resumable task processing:

The request queue works for any task processing, not just web scraping. Use a dummy URL with custom `uniqueKey` and `userData` for non-URL tasks:

```javascript
const requestQueue = await Actor.openRequestQueue();

// Add tasks to the queue (works for any processing, not just URLs)
await requestQueue.addRequest({
    url: 'https://placeholder.local',  // Dummy URL for non-scraping tasks
    uniqueKey: `task-${taskId}`,       // Unique identifier for deduplication
    userData: { itemId: 123, action: 'process' },  // Your custom task data
});

// Process tasks from the queue (with Crawlee)
const crawler = new BasicCrawler({
    requestQueue,
    requestHandler: async ({ request }) => {
        const { itemId, action } = request.userData;
        // Process your task using userData
        await processTask(itemId, action);
    },
});
await crawler.run();

// Or manually consume without Crawlee:
let request;
while ((request = await requestQueue.fetchNextRequest())) {
    await processTask(request.userData);
    await requestQueue.markRequestHandled(request);
}
```

**Key-Value Store** - For checkpoint state:
```javascript
// Save state
await Actor.setValue('STATE', { processedCount: 100 });

// Restore state on restart
const state = await Actor.getValue('STATE') || { processedCount: 0 };
```

### Step 7: Update actor.json

Configure `.actor/actor.json`. Validate against the JSON Schema from the `@apify/json_schemas` npm package (`actor.schema.json`).

```json
{
    "actorSpecification": 1,
    "name": "my-actor",
    "title": "My Actor",
    "description": "Brief description of what the actor does",
    "version": "1.0.0",
    "meta": {
        "templateId": "ts_empty",
        "generatedBy": "Claude Code with Claude Opus 4.5"
    },
    "input": "./input_schema.json",
    "dockerfile": "../Dockerfile"
}
```

**Important:** Fill in the `generatedBy` property with the tool/model used (e.g., "Claude Code with Claude Sonnet 4.5").

### Step 8: Test Locally

Run the actor with inline input (for JS/TS and Python actors):

```bash
apify run --input '{"startUrl": "https://example.com", "maxItems": 10}'
```

Or use an input file:

```bash
apify run --input-file ./test-input.json
```

**Important:** Always use `apify run`, not `npm start` or `python main.py`. The CLI sets up the proper environment and storage.

**Note:** For CLI-based actors (shell wrapper scripts), you may need to test the underlying application directly with mock input, as `apify run` requires a Node.js or Python entry point.

### Step 9: Deploy

```bash
apify push
```

This uploads and builds your actor on the Apify platform.

### Step 10: Monetization (Optional)

After deploying, you can monetize your actor in the Apify Store. The recommended model for actorized projects is **Pay Per Event (PPE)**:

**Pay Per Event** - Charge users based on specific events:
- Per result/item scraped
- Per page processed
- Per API call made
- Per file generated

Configure PPE in the Apify Console under Actor > Monetization. Define:
- Event name (e.g., "result", "page", "request")
- Price per event
- Charge for events in your code with `await Actor.charge('result')` or track via dataset items

Other monetization options:
- **Rental** - Monthly subscription for unlimited usage
- **Free** - Open source, community contribution

## Common Patterns

### Crawlee Projects

Crawlee projects require minimal changes - just wrap with Actor lifecycle:

```javascript
import { Actor } from 'apify';
import { PlaywrightCrawler } from 'crawlee';

await Actor.init();

// Get and validate input
const input = await Actor.getInput();
const {
    startUrl = 'https://example.com',
    maxItems = 100,
} = input ?? {};

let itemCount = 0;

const crawler = new PlaywrightCrawler({
    requestHandler: async ({ page, request, pushData }) => {
        if (itemCount >= maxItems) return;

        const title = await page.title();
        await pushData({ url: request.url, title });
        itemCount++;
    },
});

await crawler.run([startUrl]);

await Actor.exit();
```

### Express/HTTP Servers

For web servers, use standby mode in actor.json:

```json
{
    "actorSpecification": 1,
    "name": "my-api",
    "usesStandbyMode": true
}
```

Then implement readiness probe. See [standby-mode.md](../apify-actor-development/references/standby-mode.md).

### Batch Processing Scripts

```javascript
import { Actor } from 'apify';

await Actor.init();

const input = await Actor.getInput();
const items = input.items || [];

for (const item of items) {
    const result = processItem(item);
    await Actor.pushData(result);
}

await Actor.exit();
```

## Checklist

Before deploying, verify:

- [ ] `.actor/actor.json` exists with correct name and description
- [ ] `.actor/actor.json` validates against `@apify/json_schemas` (`actor.schema.json`)
- [ ] `.actor/input_schema.json` defines all required inputs
- [ ] `.actor/input_schema.json` validates against `@apify/json_schemas` (`input.schema.json`)
- [ ] `.actor/output_schema.json` defines output structure (if applicable)
- [ ] `.actor/output_schema.json` validates against `@apify/json_schemas` (`output.schema.json`)
- [ ] `Dockerfile` is present and builds successfully
- [ ] `Actor.init()` / `Actor.exit()` wraps main code (JS/TS)
- [ ] `async with Actor:` wraps main code (Python)
- [ ] Inputs are read via `Actor.getInput()` / `Actor.get_input()`
- [ ] Outputs use `Actor.pushData()` or key-value store
- [ ] `apify run` executes successfully with test input
- [ ] `generatedBy` is set in actor.json meta section

## Resources

- [Actorization Academy](https://docs.apify.com/academy/actorization) - Comprehensive guide
- [Apify SDK for JavaScript](https://docs.apify.com/sdk/js) - Full SDK reference
- [Apify SDK for Python](https://docs.apify.com/sdk/python) - Full SDK reference
- [Apify CLI Reference](https://docs.apify.com/cli) - CLI commands
- [Actor Specification](https://raw.githubusercontent.com/apify/actor-whitepaper/refs/heads/master/README.md) - Complete specification
