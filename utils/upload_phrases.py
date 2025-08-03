import sys
import os

# Agrega la carpeta raíz del proyecto al path
ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
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

phrases_to_load = [
    'Wendy Guevara le dejó más beneficios al América que Baños resultados... y van {dias} días.',
    'Mayito Bezares volvió a cuadro y aportó más al América que Baños en estos {dias} días.',
    'Abelito todavía ni debuta, y ya se espera que aporte más al América que Baños tras {dias} días.',
    'Con Wendy dando exposición mediática y Baños sumando {dias} días sin fichar bien, ya sabemos quién genera más para el América.',
    'Van {dias} días y Wendy, Mayito y Abelito han sido más útiles al América que Baños con su lista de refuerzos.',
    'Baños lleva {dias} días sin sumar nada en lo deportivo, y la farándula le está aportando más al América que él.',
    'Wendy entretiene, Mayito revive viejas glorias y Abelito genera expectativa... Baños solo acumula {dias} días de intrascendencia.',
    'Wendy y Mayito ya justificaron su valor mediático. Baños sigue sin justificar su puesto después de {dias} días.',
    'En términos de impacto para el América, Wendy y compañía ya golean a Baños tras {dias} días de nula gestión.',
    'La exposición que dan Wendy y Abelito supera lo que Baños ha logrado en {dias} días como director deportivo.',
    'Wendy y Abelito le generan más al América que los fichajes que Baños no ha cerrado... y ya van {dias} días.',
    'Mayito tiene mejor retorno para el América que Baños, y eso que lleva {dias} días sin patear un balón.'
]

pm = PhraseManager(redis_store=r)

pm.load_phrases(phrases_to_load)
