import redis
from twitter_bot.config import REDIS_HOST, REDIS_PORT, REDIS_USER, REDIS_PASSWORD

class RedisStore:
    def __init__(self):
        self.r = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            username=REDIS_USER,
            password=REDIS_PASSWORD,
            decode_responses=True
        )
    
    def get(self, key):
        return self.r.get(key)
    
    def set(self, key, value):
        self.r.set(key, value)

    def delete(self, key):
        self.r.delete(key)

    def sadd(self, key, value):
        self.r.sadd(key, value)
    
    def sismember(self, key, value):
        return self.r.sismember(key, value)
    
    def scard(self, key):
        return self.r.scard(key)
    
    def incr(self, key):
        return self.r.incr(key)
    
    def smembers(self, key):
        return self.r.smembers(key)
    
    def ping(self):
        return self.r.ping()