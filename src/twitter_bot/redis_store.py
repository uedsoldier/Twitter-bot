import redis
from twitter_bot.config import REDIS_HOST, REDIS_PORT, REDIS_USER, REDIS_PASSWORD
from redis.exceptions import RedisError, ConnectionError, AuthenticationError, TimeoutError

class RedisStore:
    def __init__(self):
        try:
            self.r = redis.Redis(
                host=REDIS_HOST,
                port=REDIS_PORT,
                username=REDIS_USER,
                password=REDIS_PASSWORD,
                decode_responses=True
            )
        except RedisError as e:
            self.r = None
    
    def get(self, key):
        try:
            return self.r.get(key)
        except RedisError as e:
            return None
            
    
    def set(self, key, value) -> bool:
        try:
            self.r.set(key, value)
            return True
        except RedisError as e:
            return False
            

    def delete(self, key) -> bool:
        try:
            self.r.delete(key)
            return True
        except RedisError as e:
            return False

    def sadd(self, key, value) -> bool:
        try:
            self.r.sadd(key, value)
            return True
        except RedisError as e:
            return False
    
    def sismember(self, key, value):
        try:
            return self.r.sismember(key, value)
        except RedisError as e:
            return None
    
    def scard(self, key):
        try:
            return self.r.scard(key)
        except RedisError as e:
            return None
    
    def incr(self, key):
        try:
            return self.r.incr(key)
        except RedisError as e:
            return None
    
    def smembers(self, key):
        try:
            return self.r.smembers(key)
        except RedisError as e:
            return None
    
    def ping(self):
        try:
            return self.r.ping()
        except RedisError as e:
            return None