import redis
from dotenv import load_dotenv
import os

load_dotenv()
REDIS_HOST  = os.getenv('REDIS_HOST','localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT','6379'))
REDIS_USER = os.getenv('REDIS_USER', 'default')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')


def main():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, username=REDIS_USER,password=REDIS_PASSWORD,decode_responses=True)

    frases = [
    ]

    # Simulamos días para formatear frases
    dias = 10

    for frase_tpl in frases:
        frase = frase_tpl.format(dias=dias)
        if r.sismember('used_phrases', frase):
            print(f'Phrase already used: "{frase}"')
        else:
            print(f'New phrase, adding: "{frase}"')
            r.sadd('used_phrases', frase)

    # Mostrar todas las frases usadas
    usadas = r.smembers('used_phrases')
    print('\nPhrases stored in redis:')
    for f in usadas:
        print(f'- {f}')

if __name__ == '__main__':
    main()
