import json
from atproto import Client

""" 
    @Author: Sieger van Breugel, 2025
"""
class BlueSkyScraper:
    def __init__(self):
        self.client = Client()

    def login(self, user, password):
        self.client.login(user, password)


    """
        Get an amount of posts from the BlueSky search engine,
        Filter using query (a search string), start_date and end_date should be datetime objects.
        The limit is set to 25, but can be customized.
    """
    def search_posts(self, query, start_date, end_date, limit=25):
        start = start_date.strftime('%Y-%m-%dT%H:%M:%S.') + f'{int(start_date.microsecond / 1000):03d}Z'
        end = end_date.strftime('%Y-%m-%dT%H:%M:%S.') + f'{int(end_date.microsecond / 1000):03d}Z'

        try:
            posts = self.client.app.bsky.feed.search_posts(
                {'q': query,
                 'since': str(start),
                 'until': str(end),
                 'limit': limit,
                 }
            ).model_dump_json()

            return json.loads(posts)
        except Exception as e:
            print(e)