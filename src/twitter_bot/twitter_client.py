import tweepy


class TwitterClient:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

    def publish_tweet(self, texto):
        try:
            response = self.client.create_tweet(text=texto)
            print(f'Tweet publicado: https://twitter.com/user/status/{response.data["id"]}')
            return response
        except Exception as e:
            print(f'Error al publicar tweet: {e}')
            return None
