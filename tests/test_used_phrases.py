import redis
from dotenv import load_dotenv
import os

load_dotenv()
REDIS_HOST  = os.getenv('REDIS_HOST','localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT','6379'))
REDIS_USER = os.getenv('REDIS_USER', 'default')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')


def main():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, username=REDIS_USER,password=REDIS_PASSWORD,decode_responses=True)

    phrases = [
    ]


    for phrase in phrases:
        if r.sismember('used_phrases', phrase):
            print(f'Phrase already used: "{phrase}"')
        else:
            print(f'New phrase, adding: "{phrase}"')
            r.sadd('phrases_database', phrase)

if __name__ == '__main__':
    main()
