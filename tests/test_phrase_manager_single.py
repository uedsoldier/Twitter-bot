import sys
import os

# Agrega la carpeta raíz del proyecto al path
ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, ruta_src)
from twitter_bot.phrase_manager import PhraseManager
import redis
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST  = os.getenv('REDIS_HOST','localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT','6379'))
REDIS_USER = os.getenv('REDIS_USER', 'default')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, username=REDIS_USER,password=REDIS_PASSWORD,decode_responses=True)

pm = PhraseManager(redis_store=r)

dias = 10  # Example number of days

phrase = pm.generate(dias)
print(phrase)