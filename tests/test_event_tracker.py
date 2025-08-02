import sys, os
from dotenv import load_dotenv
from pathlib import Path

ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if ruta_src not in sys.path:
    sys.path.insert(0, ruta_src)

from twitter_bot.redis_store import RedisStore
from twitter_bot.event_tracker import EventTracker

# Ruta absoluta al .env (asumiendo que está un nivel arriba de tests/)
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv()

r = RedisStore()
event_tracker = EventTracker(r)

print('Test Event Tracker')

print('Days since start:', event_tracker.compute_days_since_start())


