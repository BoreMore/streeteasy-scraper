# AGENTS.md

## Mission

Build a local, single-user NYC apartment-search application that:

* Searches StreetEasy through the user's visible browser session.
* Enriches listings with HPD and public Openigloo data.
* Applies deterministic app-side filtering.
* Presents transparent, explainable results.

Prioritize correctness, compliance, and simplicity over feature breadth.

## Decision Priorities

When tradeoffs exist:

1. Correctness
2. Compliance with source restrictions
3. Transparency
4. Simplicity
5. Performance

Do not guess missing data.

## Architecture

* Backend: Python, FastAPI, SQLAlchemy, SQLite.
* Frontend: React + TypeScript.
* Browser automation: Playwright.

Keep browser automation, provider integrations, domain logic, persistence, and UI concerns separate.

External sources must be accessed through replaceable provider interfaces.

Keep domain logic testable without network, browser, or database dependencies.

## Data Sources

### StreetEasy

* Scrape StreetEasy listings.
* Respect the site's rate limits and access controls; do not attempt to bypass CAPTCHAs or bot-detection.
* Represent missing values as unknown.
* Preserve source URLs and timestamps.

### HPD

* Prefer official NYC Open Data sources.
* Do not silently resolve ambiguous matches.
* Preserve source status and match confidence.

### Openigloo

* Use only publicly accessible information.
* Do not collect review text or paywalled content.
* Treat unavailable fields as unknown.

## Core Rules

* Keep StreetEasy filters separate from app-side filters.
* Required filters must be deterministic and independently testable.
* Missing required data should fail the filter rather than be assumed valid.
* Preserve original source values alongside normalized values.
* Enrichment failures should not invalidate otherwise usable listings.
* Support partial results and clearly communicate source status.

## Privacy

Never store:

* Credentials
* Session cookies
* Browser profile contents
* Raw HTML
* Downloaded images
* Review text
* Paywalled content

Never log secrets or authentication data.

## Testing

Tests must not require:

* Live services
* Real credentials
* Real browser profiles

Use fixtures and fake providers.

Verify parsing, filtering, enrichment, error handling, and data-quality rules.

## Engineering Standards

* Use strong typing.
* Validate inputs at boundaries.
* Keep external I/O out of domain logic.
* Use transactions for coherent writes.
* Make repeated operations idempotent.
* Return structured errors.
* Prefer simple local architecture for V1.

When uncertain, choose the more conservative interpretation of data and source restrictions.
