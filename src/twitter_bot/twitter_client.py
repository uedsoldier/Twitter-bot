import tweepy


class TwitterClient:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
    
    def get_me(self):
        try:
            user = self.client.get_me()
            return user.data
        except Exception as e:
            return {"error": str(e)}

    def publish_tweet(self, texto):
        try:
            return self.client.create_tweet(text=texto)
        except Exception as e:
            return {"error": str(e)}
