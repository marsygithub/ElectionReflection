#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.api import API
import tweepy
import os
import time
import cPickle
import random
import json
import dataset
from create_tweet import collect_hashtags, construct_tweet, get_keywords
import pandas as pd


def debate(tokens, followers, to_user, dictionary_path, tweet_path, db_path):

    auth = OAuthHandler(tokens[2], tokens[3])
    auth.set_access_token(tokens[0], tokens[1])

    api = tweepy.API(auth)

    d = cPickle.load(open(dictionary_path, 'rb'))
    df = pd.read_pickle(tweet_path)
    hashtags = collect_hashtags(df)

    db = dataset.connect(db_path)
    table = db['tweets']
    last_tweet = list(table)[-1]['text']

    while True:
        if last_tweet == list(table)[-1]['text']:
            time.sleep(60)
            continue
        else:
            time.sleep(10)
            last_tweet = list(table)[-1]['text']
            tweetid = list(table)[-1]['tweetid']

            user = random.choice(followers)
            user_mention = '@' + str(user)

            keywords = get_keywords(last_tweet)
            sentence = construct_tweet(keywords, d, hashtags, [to_user])

            sentence = to_user + user_mention + ' ' + sentence

            try:
                status = api.update_status(status=sentence, in_reply_to_status_id = tweetid)

            except tweepy.TweepError as e:
                #print e.message[0]['code']
                if e.message[0]['code'] == 186:
                    sentence = sentence[0:140]
                    sentence = sentence.split()[:-1]
                    sentence = ' '.join(sentence)
                    status = api.update_status(status=sentence, in_reply_to_status_id = tweetid)
            time.sleep(10)
