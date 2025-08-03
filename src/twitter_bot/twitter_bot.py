from twitter_bot.redis_store import RedisStore
from twitter_bot.phrase_manager import PhraseManager
from twitter_bot.twitter_client import TwitterClient
from twitter_bot.event_tracker import EventTracker
from twitter_bot.log_manager import LogManager

from twitter_bot.config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)


class TwitterBot:

    def __init__(self):
        self.redis_store = RedisStore()
        self.phrase_manager = PhraseManager(self.redis_store)
        self.twitter_client = TwitterClient(
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
        )
        self.event_tracker = EventTracker(self.redis_store)
        self.logger = LogManager.get_logger(__name__)

    def run(self): 
        days = self.event_tracker.compute_days_since_start()
        twitt = self.phrase_manager.generate(days)
        twitt_with_hashtags = twitt + self.phrase_manager.hashtag
        self.logger.info(f'Generated tweet: {twitt_with_hashtags}')
        response = self.twitter_client.publish_tweet(twitt_with_hashtags)

        if 'error' in response:
            self.logger.error(f'Error publishing tweet: {response['error']}')
        else:
            self.phrase_manager.add_phrase_to_used(twitt)
            self.logger.info(f'Published tweet: https://twitter.com/user/status/{response.data["id"]}')
