import tweepy
import os, sys
from twitter_bot.redis_store import RedisStore
from twitter_bot.twitter_client import TwitterClient
from dotenv import load_dotenv, dotenv_values

HEALTHCHECK_STR = '[HealthCheck]'

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

    print('{HEALTHCHECK_STR} Verifying environment variables...')

    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)
            print(f'{HEALTHCHECK_STR} ❌ Variable {var} is missing.')
        else:
            print(f'{HEALTHCHECK_STR} ✅ {var} loaded.')    

    if missing:
        print('{HEALTHCHECK_STR} ERROR: Critical variables are missing.')
        sys.exit(1)
    else:
        print('{HEALTHCHECK_STR} All required variables are loaded.')

def check_redis():
    print('Checking Redis connection...')
    try:
        redis_store = RedisStore()
        if redis_store.ping():
            print('{HEALTHCHECK_STR} ✅ Redis PING successful.')
        else:
            print('{HEALTHCHECK_STR} ❌ Redis PING failed.')
            sys.exit(1)
       
    except Exception as e:
        print(f'{HEALTHCHECK_STR} ❌ Error connecting to Redis: {e}.')
        sys.exit(1)
    print('{HEALTHCHECK_STR} ✅ Redis connection is healthy.')

def check_twitter():
    print('{HEALTHCHECK_STR} Checking Twitter API connection...')
    try:
        twitter_client = TwitterClient(
            access_token=os.getenv('ACCESS_TOKEN'),
            access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'),
            consumer_key=os.getenv('CONSUMER_KEY'),
            consumer_secret=os.getenv('CONSUMER_SECRET')
        )
        print(f'User data: {twitter_client.get_me()}')
        print('{HEALTHCHECK_STR} ✅ Twitter API connection is healthy.')
    except Exception as e:
        print(f'{HEALTHCHECK_STR} ❌ Error connecting to Twitter API: {e}.')
        sys.exit(1)

if __name__ == '__main__':
    check_env()
    check_redis()
    check_twitter()
    sys.exit(0)