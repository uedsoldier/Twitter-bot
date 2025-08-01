import sys
import os

# Agrega la carpeta raíz del proyecto al path
ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, ruta_src)
from twitter_bot.phrase_manager import PhraseManager
import redis
from dotenv import load_dotenv

pm = PhraseManager()

load_dotenv()
REDIS_HOST  = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

dias = 10  # Example number of days

phrase = pm.generate(dias, redis_store=r)
print(phrase)