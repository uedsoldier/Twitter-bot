import sys
import os

# Agrega la carpeta raíz del proyecto al path
ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, ruta_src)
from twitter_bot.phrase_manager import PhraseManager
import redis

pm = PhraseManager()

r = redis.Redis(host='192.168.1.4', port=6379, decode_responses=True)

dias = 10  # Example number of days

phrase = pm.generate(dias, redis_store=r)
print(phrase)