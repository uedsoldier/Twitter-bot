import tweepy
from twitter_bot.responses import TweetResponse, UserResponse


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
            response = self.client.get_me()
            return UserResponse(
                success=True,
                user_data=response.data,
            )
        except tweepy.TooManyRequests as e:
            return UserResponse(
                success=False,
                error='Too many requests',
                status_code=429
            )
        except tweepy.Unauthorized as e:
            return UserResponse(
                success=False,
                error='Unauthorized',
                status_code=401
            )
        except Exception as e:
            return UserResponse(
                success=False,
                error=str(e),
                status_code=500
            )

    def publish_tweet(self, tweet):
        try:
            response = self.client.create_tweet(text=tweet)
            url = f'https://twitter.com/user/status/{response.data["id"]}'
            return TweetResponse(
                success=True,
                url=url,
            )
        except tweepy.TooManyRequests as e:
            return TweetResponse(
                success=False,
                error='Too many requests',
                status_code=429
            )
        except tweepy.Unauthorized as e:
            return TweetResponse(
                success=False,
                error='Unauthorized',
                status_code=401
            )
        except Exception as e:
            return TweetResponse(
                success=False,
                error=str(e),
                status_code=500
            )
