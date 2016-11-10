#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.api import API
import tweepy
import os
import time
import cPickle
import textacy
import random
import json
import dataset

#Variables that contains the user credentials to access Twitter API
access_token = '793227266549362688-mIGiqzQjRT5XAwxnOOVCzfyCFBEsCvD'
access_token_secret = '4r45rRpu9wlIcInVx10LDYFJ1wMYQta14zJM0nSODod89'
consumer_key = 'fCgmoqVXMRnM8ljU9Q9V4x9dO'
consumer_secret = 'J3Tawcw89Fhadg8wvMPBubjZEM4jgoCBPuHpxhmcjTAIcR3I9a'


class StdOutListener(StreamListener):


    def on_data(self, data):
        print json.loads(data)['text']
        for user in json.loads(data)['entities']['user_mentions']:
            if user['screen_name'] == 'KillaryHilton_':
                table = db["tweets"]
                table.insert(dict(
                    text=json.loads(data)['text'],
                    tweetid=json.loads(data)['id']
                ))


    def on_error(self, status):
        print status





if __name__ == '__main__':


    db = dataset.connect("sqlite:///toclinton_tweets.db")


    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    api = tweepy.API(auth)
    user = api.get_user(screen_name = 'TonaldDrump___')
    stream.filter(follow = [str(user.id)])
