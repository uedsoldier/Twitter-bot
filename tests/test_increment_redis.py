import redis
import os
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST  = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

test_counter = int(r.get('test_counter'))

print(f'Test counter value: {test_counter}')

test_counter += 1
r.set('test_counter', test_counter)

print(f'Test counter value (after increment): {test_counter}')



