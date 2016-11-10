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
from create_tweet import collect_hashtags, construct_tweet, get_keywords
from debate import debate
import pandas as pd



if __name__ == '__main__':
    #tokens removed
    tokens = [access_token, access_token_secret, consumer_key, consumer_secret]

    with open('../data/trump_followers', 'r') as f:
        followers = f.readlines()

    debate(tokens, '.@KillaryHilton_ ', followers, '../data/trump_dictionary', '../data/trump_tweets', "sqlite:///totrump_tweets.db")
