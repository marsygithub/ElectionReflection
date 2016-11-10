import pandas as pd
import os
import numpy as np
import datetime
import tweepy
import random


auth = tweepy.OAuthHandler(os.environ.get('TWITTER_CONSUMER_KEY'), os.environ.get('TWITTER_SECRET_CONSUMER_KEY'))
auth.set_access_token(os.environ.get('TWITTER_ACCESS_KEY'), os.environ.get('TWITTER_SECRET_ACCESS_KEY'))

api = tweepy.API(auth)


def collect_tweets(filename):
    df = pd.read_pickle(filename)

    screen_names =df['user_screen_name']
    screen_names = list(screen_names.unique())
    numbers = random.sample(range(len(screen_names)), 10000)
    screen_names = [screen_names[i] for i in numbers]

    tweet_list = []
    endDate =   datetime.datetime(2016, 3, 1, 0, 0, 0)
    hashtags = []
    for user in screen_names:
        try:
            tweets = api.user_timeline(id = str(user), count=50000)
            for tweet in tweets:
                if tweet.created_at < endDate:
                    if tweet.entities.get('hashtags') != []:
                        hashtags = []
                        for item in tweet.entities.get('hashtags'):
                            hashtags.append(item['text'])

                    tweet_list.append({'text': tweet.text, 'created_at': tweet.created_at, 'screen_name': user,
                                       'hashtags':hashtags, 'retweets': tweet.retweet_count, 'location': tweet.user.location})

        except tweepy.TweepError:
            continue

    df = pd.DataFrame(tweet_list)
    df = df[['created_at', 'screen_name', 'location', 'text', 'hashtags', 'retweets']]

    return df
