from twitter_bot.redis_store import RedisStore
from twitter_bot.phrase_manager import PhraseManager
from twitter_bot.twitter_client import TwitterClient
from twitter_bot.event_tracker import EventTracker
from twitter_bot.log_manager import LogManager
from twitter_bot.responses import TweetResponse
import tweepy
import time

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
        self.logger.info(f'Generated tweet message: {twitt_with_hashtags}')

        try:
            response: TweetResponse = self.twitter_client.publish_tweet(twitt_with_hashtags)
            if response.success:
                self.phrase_manager.add_phrase_to_used(twitt)
                self.logger.info(f'Published tweet: {response.url}')
            else:
                self.logger.error(f'Error publishing tweet: {response.error} (Status code: {response.status_code})')
        except tweepy.TooManyRequests as e:
            reset_timestamp = int(e.response.headers.get('x-rate-limit-reset', 0))
            wait_minutes: int = int((reset_timestamp - time.time()) / 60)
            self.logger.warning(f'Rate limit exceeded. Try again in {wait_minutes} minutes.')
        
        except tweepy.Unauthorized as e:
            self.logger.error(f'Invalid Twitter API credentials: {e}')

        except Exception as e:
            self.logger.error(f'An unexpected error occurred: {e}')
            
        
        

       
       
