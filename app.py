import os
from datetime import datetime
import pytz
import json

from dotenv import load_dotenv

from BlueSkyScraper import BlueSkyScraper

# Initialize environment variables
load_dotenv()
BLUESKY_USER = os.getenv('BLUESKY_USER')
BLUESKY_PASSWORD = os.getenv('BLUESKY_PASSWORD')

# Initialize scraper with user credentials
scraper = BlueSkyScraper()
scraper.login(BLUESKY_USER, BLUESKY_PASSWORD)

# Get the posts
# start_date = datetime.datetime(2025, 10, 16, tzinfo=pytz.timezone('America/New_York'))
# end_date = datetime.datetime(2025, 11, 4, tzinfo=pytz.timezone('America/New_York'))
start_date = datetime(2025, 12, 1, tzinfo=pytz.timezone('America/New_York'))
end_date = datetime(2025, 12, 2, tzinfo=pytz.timezone('America/New_York'))

posts = scraper.search_posts('Mamdani', start_date=start_date, end_date=end_date, limit=1, per_hour=True)

# To convert to dataframe:
# import pandas as pd
# df = pd.json_normalize(posts)

# Write to file:
now = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
with open(f"./data/scraped_posts_{now}.json", 'w') as f:
    json.dump(posts, f)