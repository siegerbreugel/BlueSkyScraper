import os
import datetime

import pandas as pd
import pytz
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
start_date = datetime.datetime(2025, 10, 16, tzinfo=pytz.timezone('America/New_York'))
end_date = datetime.datetime(2025, 11, 4, tzinfo=pytz.timezone('America/New_York'))

posts = scraper.search_posts('Mamdani', start_date=start_date, end_date=end_date, limit=10)

# Pandas
df = pd.json_normalize(posts['posts'])
print(df.head())