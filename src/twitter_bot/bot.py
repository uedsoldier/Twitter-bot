from twitter_bot.redis_store import RedisStore
from twitter_bot.phrase_manager import PhraseManager
from twitter_bot.twitter_client import TwitterClient
from twitter_bot.event_tracker import EventTracker

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

    def run(self):
        days = self.event_tracker.increment_days_if_no_event()
        message = self.phrase_manager.generate(days)
        self.twitter_client.publish_tweet(message)
