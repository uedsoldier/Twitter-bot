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
            print(f'Error getting user: {e}')
            return None

    def publish_tweet(self, texto):
        try:
            response = self.client.create_tweet(text=texto)
            print(f'Published tweet: https://twitter.com/user/status/{response.data["id"]}')
            return response
        except Exception as e:
            print(f'Error publishing tweet: {e}')
            return None
