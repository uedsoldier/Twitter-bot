import redis
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
REDIS_HOST  = os.getenv('REDIS_HOST','localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT','6379'))
REDIS_USER = os.getenv('REDIS_USER', 'default')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, username=REDIS_USER,password=REDIS_PASSWORD,decode_responses=True)

initial_date_str = str(r.get('initial_date'))
initial_date = datetime.strptime(initial_date_str, '%Y-%m-%d')

today = datetime.today()
days_since_begin = (today - initial_date).days

print(f"Han pasado {days_since_begin} días desde que comenzó el conteo.")