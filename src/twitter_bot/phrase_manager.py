import random
import redis


class PhraseManager:

    def __init__(self, redis_store: redis.Redis, key_phrases: str = 'phrases_database', key_used: str = 'used_phrases'):
        self.store = redis_store
        self.key_phrases = key_phrases
        self.key_used = key_used
        self.hashtag = ' #FueraBaños  #ChingaTuMadreBaños'

    def generate(self, dias):

        phrases = self.store.smembers(self.key_phrases)
        used_phrases = self.store.smembers(self.key_used)
        available_phrases = list(phrases - used_phrases)

        if not available_phrases:
            self.store.delete(self.key_used)
            available_phrases = phrases
        
        phrase = random.choice(available_phrases)
        self.store.sadd(self.key_used, phrase)
        return phrase.format(dias=dias) + self.hashtag

    def load_phrases(self, phrases: list):
        if self.store.scard(self.key_phrases) == 0:
            for phrase in phrases:
                self.store.sadd(self.key_phrases, phrase)
            print(f'Phrases loaded into Redis: {len(phrases)}')
        else:
            print('Phrases already loaded into Redis, skipping.')
