import tweepy
import os, sys
from twitter_bot.redis_store import RedisStore
from twitter_bot.twitter_client import TwitterClient
from twitter_bot.log_manager import LogManager
from dotenv import load_dotenv, dotenv_values

HEALTHCHECK_STR = '[HealthCheck]'
logger = LogManager.get_logger(__name__)


def check_env():
    # Variables que deben estar presentes
    required_vars = [
        'CONSUMER_KEY',
        'CONSUMER_SECRET',
        'ACCESS_TOKEN',
        'ACCESS_TOKEN_SECRET',
        'REDIS_HOST',
        'REDIS_PORT',
        'REDIS_USER',
        'REDIS_PASSWORD'
    ]

    missing = []

    logger.info('{HEALTHCHECK_STR} Verifying environment variables...')

    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)
    if missing:
        logger.error(f'{HEALTHCHECK_STR} ERROR: Critical variables are missing: {", ".join(missing)}')
        sys.exit(1)
    else:
        logger.info(f'{HEALTHCHECK_STR} All required variables are loaded.')

def check_redis():
    logger.info(f'{HEALTHCHECK_STR} Checking Redis connection...')
    try:
        redis_store = RedisStore()
        if redis_store.ping():
            logger.info('{HEALTHCHECK_STR} ✅ Redis PING successful.')
        else:
            logger.error('{HEALTHCHECK_STR} ❌ Redis PING failed.')
            sys.exit(1)
       
    except Exception as e:
        logger.error(f'{HEALTHCHECK_STR} ❌ Error connecting to Redis: {e}.')
        sys.exit(1)
    logger.info('{HEALTHCHECK_STR} ✅ Redis connection is healthy.')

def check_twitter():
    logger.info('{HEALTHCHECK_STR} Checking Twitter API connection...')
    try:
        twitter_client = TwitterClient(
            access_token=os.getenv('ACCESS_TOKEN'),
            access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'),
            consumer_key=os.getenv('CONSUMER_KEY'),
            consumer_secret=os.getenv('CONSUMER_SECRET')
        )
        logger.info(f'User data: {twitter_client.get_me()}')
        logger.info('{HEALTHCHECK_STR} ✅ Twitter API connection is healthy.')
    except Exception as e:
        logger.error(f'{HEALTHCHECK_STR} ❌ Error connecting to Twitter API: {e}.')
        sys.exit(1)

if __name__ == '__main__':
    check_env()
    check_redis()
    check_twitter()
    sys.exit(0)