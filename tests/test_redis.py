import redis
from datetime import datetime

r = redis.Redis(host='192.168.1.4', port=6379, decode_responses=True)

fecha_inicio_conteo_banos_str = r.get('fecha_inicio_conteo_banos')
fecha_inicio_conteo_banos = datetime.strptime(fecha_inicio_conteo_banos_str, '%Y-%m-%d')

hoy = datetime.today()
dias = (hoy - fecha_inicio_conteo_banos).days

print(f"Han pasado {dias} días desde que comenzó el conteo de Santiago Baños.")