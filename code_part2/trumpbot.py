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
access_token = '793227945355587584-wrdgMbe7Wps758L1x3Ym41HFgJVOXhs'
access_token_secret = 'P9pkDlOPT8A33DCsEiIHDOfVSLBPDuivPRfEcIo95jJ0Y'
consumer_key = 'zEPxrGbqTgqu6VPkTkAiTCElE'
consumer_secret = 'ubTpeuCxYKpExvFf7fKjz05BXRfyRYlEuG7iwdYnKqQ1nDpIxC'



class StdOutListener(StreamListener):


    def on_data(self, data):
        for user in json.loads(data)['entities']['user_mentions']:
            if user['screen_name'] == 'TonaldDrump___':
                table = db["tweets"]
                table.insert(dict(
                    text=json.loads(data)['text'],
                    tweetid=json.loads(data)['id']
                ))


    def on_error(self, status):
        print status





if __name__ == '__main__':


    db = dataset.connect("sqlite:///totrump_tweets.db")


    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    api = tweepy.API(auth)
    user = api.get_user(screen_name = 'KillaryHilton_')
    stream.filter(follow = [str(user.id)])
