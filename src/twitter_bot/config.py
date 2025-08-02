import os 

REDIS_HOST = os.getenv('REDIS_HOST','localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT','6379'))
REDIS_USER = os.getenv('REDIS_USER', 'default')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)

CONSUMER_KEY= os.getenv('CONSUMER_KEY') 
CONSUMER_SECRET= os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN= os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET= os.getenv('ACCESS_TOKEN_SECRET')
