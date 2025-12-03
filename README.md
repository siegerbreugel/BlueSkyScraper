# Bluesky Scraper for Python

A quickly written tool for scraping posts from Bluesky, developed for a cultural data analysis project at the University
of Amsterdam.

**Author:** Sieger van Breugel

## Installation

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Basic Usage

Import and use the scraper in your Python code:

```bash
from BlueSkyScraper import BlueSkyScraper

scraper = BlueSkyScraper()
scaper.login(user, password) # e.g. handle.bsky.social, secretpassword
posts = scraper.search_posts(
    query="your search term",
    start_date=start_datetime,
    end_date=end_datetime,
    limit=25,
    per_hour=False
)
```

### per_hour Parameter

Because the Bluesky API sets a limit on 100 requests, we cannot be sure that we get unique posts if we implement
pagination in this tool.
That's why the per_hour parameter, when set to ``True``, makes sure you get ``limit`` amount of posts per hour within
the given timeframe.
Unless there's a smart workaround, this is our limitation.

When ``per_hour`` is set to ``False`` (default), the scraper gets a ``limit`` amount of posts within the given timeframe.

## Notes

This tool was developed quickly for research purposes and may lack extensive error handling.
For questions or contributions, please contact the author: Sieger van Breugel.