import tweepy
import os

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_SECRET_CONSUMER_KEY')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_KEY')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_SECRET_ACCESS_KEY')




auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Testing!"
api.update_status(status=status)
