"""
    @Author: Sieger van Breugel, 2025

    Usage:
        1) Create instance, for example: 'scraper = BlueSkyScraper()'
        2) Log client into bluesky: 'scraper.login(BLUESKY_USER, BLUESKY_PASSWORD)'
        3) Use 'scraper.search_posts(query="Mamdani")' to get posts
"""

import json
import math

from datetime import timedelta
from atproto import Client


def format_date(date):
    return date.strftime('%Y-%m-%dT%H:%M:%S.') + f'{int(date.microsecond / 1000):03d}Z'


class BlueSkyScraper:
    def __init__(self):
        self.client = Client()

    def login(self, user, password):
        self.client.login(user, password)

    def query_posts(self, query_dict):
        try:
            return self.client.app.bsky.feed.search_posts(query_dict).model_dump_json()
        except Exception as e:
            print(e)

    """
        Get an amount of posts from the BlueSky search engine,
        Filter using query (a search string), start_date and end_date should be datetime objects.
        The limit is set to 25, but can be customized.
        
        values: 
        - query: (str) query string -> https://web.archive.org/web/20250714214139/https://bsky.social/about/blog/05-31-2024-search
        - start_date: (datetime.datetime)
        - end_date: (datetime.datetime)
        - sort: (str) either 'top', or 'latest'
    """
    def search_posts(self, query, start_date, end_date, limit=25, per_hour=False, sort='top'):
        if limit > 100:
            raise ValueError('Limit cannot be greater than 100')

        if per_hour:
            delta = end_date - start_date
            hours = math.ceil((delta.total_seconds() / 3600))
            print(f"Searching for {limit} posts per hour for {hours} hour(s)")

            posts = []
            for i in range(hours):
                start = format_date(start_date + timedelta(hours=i))
                end = format_date(start_date + timedelta(hours=i + 1))

                print(f"Hour {i}, start: {start}, end: {end}")

                query_dict = {
                    'q': query,
                    'since': start,
                    'until': end,
                    'limit': limit,
                    'sort': sort
                }

                results = self.query_posts(query_dict)

                posts.extend(json.loads(results)['posts'])

            return posts
        else:
            start = format_date(start_date)
            end = format_date(end_date)

            query_dict = {
                'q': query,
                'since': start,
                'until': end,
                'limit': limit,
            }

            posts = self.query_posts(query_dict)

            return json.loads(posts)['posts']
