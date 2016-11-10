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


def get_keywords(text):
    '''
    INPUT: text from a received tweet
    OUTPUT: tuple of 3 key words always including policy
    '''

    #doc = textacy.doc.Doc(text, metadata=None, lang=('en').decode('ascii', 'ignore'))
    #keywords = textacy.keyterms.textrank(doc, n_keyterms=2)

    keywords = text.split()
    choose = []
    for keyword in keywords:
        if len(keyword) >= 5:
                if keyword.startswith('@') or keyword.startswith('#'):
                        continue
                else:
                        choose.append(keyword)
    new_input = (random.choice(choose), random.choice(choose), 'policy')

    return new_input



def collect_hashtags(df):
    '''
    INPUT: dataframe of historical tweets
    OUTPUT: list of unique hashtags used by
    '''

    hashtags = []
    for hashtag in df['hashtags']:
        for one in hashtag:
            hashtags.append(one)
    hashtags =  list(set(hashtags))
    return hashtags



def construct_tweet(tuple_keywords, d, hashtags, user_mentions):
    '''
    INPUT: tuple of keywords, dictionary of words, list of hashtags, and user to mention
    OUTPUT: a new tweet
    '''

    num_words = 3
    consider = []
    for key, value in d.iteritems():
        common = set(tuple_keywords) & set(key)
        if common != set([]):
            consider.append(key)

    sentence = list(consider[random.randint(0, len(consider) -1)])

    for i in range(0, random.randint(10, 15)):
        if tuple(sentence[-num_words:]) in d.keys():
            new_word = random.choice(d[tuple(sentence[-num_words:])])
            sentence.append(new_word)

    sentence[0] = sentence[0].capitalize()
    sentence = ' '.join(sentence)


    #for user in user_mentions:
        #sentence = user + sentence

    hashes = random.sample(hashtags,random.choice([1, 2]))

    for hashtag in hashes:
        sentence = sentence + (' #').decode('utf-8', 'ignore') + hashtag

    return sentence
