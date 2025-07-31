import redis
from datetime import datetime

r = redis.Redis(host='192.168.1.4', port=6379, decode_responses=True)

test_counter = int(r.get('test_counter'))

print(f'Test counter value: {test_counter}')

test_counter += 1
r.set('test_counter', test_counter)

print(f'Test counter value (after increment): {test_counter}')



