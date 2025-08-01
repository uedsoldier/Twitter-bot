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
    "Van {dias} días con Baños ahí sentado rascándose los huevos mientras el América se arrastra.",
    "{dias} días lleva Baños sin hacer nada útil, y aún así le siguen pagando. Qué chingón ser inútil con credencial.",
    "{dias} días seguidos llevamos aguantando a este imbécil al frente del América. ¿Qué hicimos para merecer esto?",
    "Ya son {dias} días viendo cómo Baños destruye lo que generaciones construyeron con sangre y garra.",
    "Con {dias} días de inoperancia, Baños está haciendo historia… pero como el peor directivo que ha pasado por Coapa.",
    "Cada uno de estos {dias} días ha sido un escupitajo a la afición gracias a Baños y su eterna mediocridad.",
    '{dias} días acumulando excusas, petardos y ridículos. Santiago Baños, el rey del "ya merito".',
    "Van {dias} días de este cáncer en el palco. Y nadie tiene los huevos de extirparlo.",
    "Cada uno de estos {dias} días ha sido una bofetada al americanismo, cortesía del estorbo llamado Santiago Baños.",
    "{dias} días con Baños y el América parece sketch de comedia. Pero sin risas.",
    "Ya van {dias} días sin dignidad en la directiva. Y Baños cada vez más cómodo destruyendo desde adentro.",
    "Son {dias} días de pura vergüenza institucional con Baños al mando. ¿Hasta cuándo, carajo?",
    "¿Sabías que van {dias} días sin que Baños haga algo que valga la pena? Ya es marca personal.",
    "{dias} días viendo cómo Baños hunde el barco y nadie lo saca del timón.",
    "El América grande. Baños pequeño. Y llevamos {dias} días soportando esa contradicción.",
    "Ya pasaron {dias} días de sabotaje disfrazado de gestión. Baños debería pagar por daños emocionales.",
    "Con {dias} días seguidos de desastre, Baños ya debería tener una estatua... hecha por los antis.",
    "{dias} días han pasado desde la última vez que Baños no la cagó. Ah, espera... eso nunca pasó.",
    "Van {dias} días y ni una puta renuncia. Ojalá tuviera tanta resistencia el medio campo.",
    "{dias} días con el destructor en jefe al frente. Ni Cuauhtémoc con la zurda arregla esta mierda.",
    "{dias} días y Baños sigue ahí, como un pinche mueble roto que nadie se atreve a tirar.",
    "{dias} días tragándose el sueldo sin rendir cuentas. Baños no es directivo, es parásito con gafete.",
    "Ya son {dias} días de que Baños hace lo mismo que siempre: nada... pero peor.",
    "A estas alturas ({dias} días), Baños ya debería tener prohibido pisar Coapa sin pedir perdón de rodillas.",
    "Van {dias} días viendo cómo Baños convierte al América en un circo sin gracia. Y él es el payaso jefe.",
    "Van {dias} días desde que Baños sigue creyendo que esto es la Liga Balón de Oro.",
    "Emilio, despierta: {dias} días de tortura con Santiago Baños a cargo.",
    "{dias} días sin dignidad deportiva. Gracias, Baños.",
    "Con {dias} días de Baños, Jardine ya merece indemnización por daños psicológicos.",
    "Azcárraga lleva {dias} días creyendo que Baños es competente. Eso es lealtad.",
    "Desde hace {dias} días, Baños administra al América como si fuera su Fantasy.",
    "{dias} días y Baños sigue. ¿Lo están clonando o qué chingados?",
    "Que alguien le diga a Baños que el América no es su pasantía eterna. Van {dias} días.",
    "¿Quién tiene más vidas, un gato o Baños en el América? Van {dias} días.",
    "{dias} días sin que Baños pida perdón. Candidato al Guinness de cinismo.",
    "Ya son {dias} días. Si Baños fuera jugador, ya lo habrían mandado a la Sub-20.",
    "Santiago Baños, {dias} días sin aportar algo útil. Nuevo récord continental.",
    "Con {dias} días de Baños, el América ya debería considerarse equipo resiliente.",
    "Hay rehenes que han durado menos cautivos que lo que Baños lleva en Coapa: {dias} días.",
    "Van {dias} días y Baños no se va. ¿Es esto una prueba divina?",
    "La dignidad del americanismo lleva {dias} días secuestrada por Baños.",
    "Que alguien avise a Iñárritu: {dias} días con Baños, y el club ya parece shitBas.",
]

pm = PhraseManager(redis_store=r)

pm.load_phrases(phrases_to_load)

print(pm.generate(666))