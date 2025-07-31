from datetime import datetime
from twitter_bot.redis_store import RedisStore

class EventTracker:
    def __init__(self, redis_store: RedisStore, key_fecha='fecha_inicio_conteo_banos', key_dias='dias_sin_dignidad'):
        self.store = redis_store
        self.key_fecha = key_fecha
        self.key_dias = key_dias
    
    def register_today_event(self):
        today = datetime.today().strftime('%Y-%m-%d')
        self.store.set(self.key_fecha, today)
        self.store.set(self.key_dias, '0')

    def compute_days(self):
        last = self.store.get(self.key_fecha)
        if not last:
            return 0
        last_date = datetime.strptime(last, '%Y-%m-%d')
        return (datetime.today() - last_date).days
    
    def increment_days_if_no_event(self):
        days = self.compute_days()
        if days > 0:
            self.store.incr(self.key_dias)
        return int(self.store.get(self.key_dias) or 0)