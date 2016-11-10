import pandas as pd
from location import states, location
from createdf import create_dataframe
import tweepy
import os
import numpy as np
import datetime
import tweepy
import random
import sys
from historical_tweets import collect_tweets

#Connect to Twitter via Tweepy
auth = tweepy.OAuthHandler(os.environ.get('TWITTER_CONSUMER_KEY'), os.environ.get('TWITTER_SECRET_CONSUMER_KEY'))
auth.set_access_token(os.environ.get('TWITTER_ACCESS_KEY'), os.environ.get('TWITTER_SECRET_ACCESS_KEY'))

api = tweepy.API(auth)

dfs = []

#Create dataframes from individual daily json files.
for arg in sys.argv[1:-2]:
    print arg
    df = create_dataframe(str(arg))
    dfs.append(df)

df = pd.concat(dfs)

df = df.reset_index(drop=True)


#Change NoneObject to 'Not Specified'
df['user_location']=df['user_location'].apply(lambda x: 'Not Specified' if x is None else x)

#Map location description to a state
for abb, keywords in states.iteritems():
    df['user_location'] = map(lambda x: location(x, abb, keywords), df['user_location'])

#Save file with updated states
df.to_pickle(str(sys.argv[-2]))

screen_names =df['user_screen_name']
screen_names = list(screen_names.unique())
numbers = random.sample(range(len(screen_names)), min(10000, len(screen_names)))
screen_names = [screen_names[i] for i in numbers]

tweet_list = []
endDate =   datetime.datetime(2016, 9, 1, 0, 0, 0)
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

df_previous = pd.DataFrame(tweet_list)
df_previous = df[['created_at', 'screen_name', 'location', 'text', 'hashtags', 'retweets']]

df_previous['location']=df['location'].apply(lambda x: 'Not Specified' if x is None else x)

#Map location description to a state
for abb, keywords in states.iteritems():
    df['location'] = map(lambda x: location(x, abb, keywords), df['location'])

df_previous.to_pickle(str(sys.argv[-1]))
