import pandas as pd
import re
import cPickle
import string
from collections import defaultdict


def make_dict(speech_filepath, tweets_filepath, to_path, num_words=3):
    '''
    INPUT: filepath to speeches, filepath to tweets, path to save file,
           num of keywords for dictionary
    OUTPUT: pickled dictionary of candidate
    '''
    speeches =  cPickle.load(open(speech_filepath,'rb'))
    df = pd.read_pickle(tweets_filepath)

    clean_speeches = []
    for speech in speeches:
        speech = speech.replace('CLINTON:', ' ').replace('TRUMP:', ' ').replace('Clinton:', ' ').replace('Trump:', ' ')
        clean_speeches.append(speech.replace('\n', ' '))

        d = defaultdict(list)

    for speech in clean_speeches:
        words = speech.split()
        for i in range(num_words, len(words)-1):
            key = tuple(words[i-(num_words):i])
            d[key].append(words[i])

    cPickle.dump(d, open(to_path, 'wb'))

if __name__ == "__main__":
    make_dict('../data/clinton_speeches.p', '../data/hillary_tweets', 'clinton_dict')
