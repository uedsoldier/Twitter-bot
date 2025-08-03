import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
CONSUMER_KEY= os.getenv('CONSUMER_KEY') 
CONSUMER_SECRET= os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN= os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET= os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

tweet_text = 'Primera publicación automática desde Python usando Tweepy! #Python #Tweepy'
client.create_tweet(text=tweet_text)