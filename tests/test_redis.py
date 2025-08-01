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

fecha_inicio_conteo_banos_str = str(r.get('fecha_inicio_conteo_banos'))
fecha_inicio_conteo_banos = datetime.strptime(fecha_inicio_conteo_banos_str, '%Y-%m-%d')

hoy = datetime.today()
dias = (hoy - fecha_inicio_conteo_banos).days

print(f"Han pasado {dias} días desde que comenzó el conteo de Santiago Baños.")