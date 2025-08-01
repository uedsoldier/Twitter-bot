import redis
from dotenv import load_dotenv
import os

load_dotenv()
REDIS_HOST  = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))

def main():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    frases = [
        'Van {dias} días con Baños ahí sentado...',
        'Baños no hace nada útil desde hace {dias} días.',
        'Ya son {dias} días de desastre con Baños.',
    ]

    # Simulamos días para formatear frases
    dias = 10

    for frase_tpl in frases:
        frase = frase_tpl.format(dias=dias)
        if r.sismember('used_phrases', frase):
            print(f'Frase ya usada: "{frase}"')
        else:
            print(f'Frase nueva, agregando: "{frase}"')
            r.sadd('used_phrases', frase)

    # Mostrar todas las frases usadas
    usadas = r.smembers('used_phrases')
    print('\nFrases almacenadas en Redis:')
    for f in usadas:
        print(f'- {f}')

if __name__ == '__main__':
    main()
