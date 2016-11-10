from spacy.en import English
import numpy as np
import random
import os
import sys
import glob
import textacy
import re
import pandas as pd
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from colors import red_color, blue_color
import cPickle





def clean_speeches(speeches):
    '''
    INPUT: List of original speeches
    OUTPUT: List of cleaned speeches
    '''

    clean_speeches = []
    for speech in speeches:
        speech = speech.lower().replace("clinton:", " ").replace("trump:", " ")
        clean_speeches.append(textacy.preprocess.preprocess_text(speech, fix_unicode=True,
                            lowercase=True, transliterate=True, no_urls=True, no_emails=True,
                            no_phone_numbers=True, no_numbers=True, no_currency_symbols=True,
                            no_punct=True, no_contractions=True, no_accents=True))

    return clean_speeches



def get_topics(speeches, path_to_save, n_topics=10, n_words=10):
    '''
    INPUT: List of cleaned speeches
    OUTPUT: Top n_words for n_topics
    '''
    corpus = textacy.Corpus(('en').decode('ascii', 'ignore'), texts=speeches)

    doc_term_matrix, id2term = textacy.vsm.doc_term_matrix((doc.to_terms_list(ngrams=1,
                                named_entities=False, as_strings=True) for doc in corpus),
                                weighting='tfidf', normalize=True, smooth_idf=True, min_df=2,
                                max_df=0.95)

    model = textacy.tm.TopicModel('nmf', n_topics=n_topics)
    model.fit(doc_term_matrix)
    doc_topic_matrix = model.transform(doc_term_matrix)
    doc_topic_matrix.shape
    topic_dic = {}
    for topic_idx, top_terms in model.top_topic_terms(id2term, top_n=n_words):
        topic_dic['Topic' + ' ' + str(topic_idx)] = top_terms


    model.termite_plot(doc_term_matrix, id2term, topics=-1,  n_terms=25, highlight_topics = [2, 3, 4, 5, 8, 9],
                        sort_terms_by='seriation', save=path_to_save)


    return topic_dic



def get_stats(speeches):
    '''
    INPUT: List of uncleaned speeches
    OUTPUT: Dataframe of readability statistics
    '''

    corpus = textacy.Corpus(('en').decode('utf-8'), texts=speeches)
    speech_stats = []
    for text in corpus:
        speech_stats.append(textacy.text_stats.readability_stats(text))

    return speech_stats



def get_wordcloud(speeches, stopwords, color_func, path_to_save):
    '''
    INPUT: List of cleaned speeches, stopwords and plot color
    OUTPUT: Map of US with most common words used by candidate
    '''

    all_text = ' '.join(speeches)

    mask = imread('../code_part2/us_map.png', flatten=True)

    wordcloud = WordCloud(stopwords=stopwords,  background_color='white',
                          width=1800,
                          height=1400,
                          mask=mask,
                          ranks_only=True).generate(all_text)
    plt.figure(figsize = (10,10))
    plt.imshow(wordcloud.recolor(color_func=color_func, random_state=3))
    plt.axis("off")
    plt.savefig(path_to_save)   # save the figure to file
    plt.close()



def analyze_speeches(filepath, path_to_save):
    '''
    INPUT: Filepath to folder that contains speeches
    OUTPUT: Analytical data
    '''

    loaded_speeches = cPickle.load(open(filepath, 'rb'))
    cleaned_speeches = clean_speeches(loaded_speeches)

    topic_dic = get_topics(cleaned_speeches, path_to_save,10, 10)

    topic_df = pd.DataFrame(topic_dic)

    df_stats = get_stats(loaded_speeches)

    return topic_df, df_stats, cleaned_speeches




if __name__ == "__main__":
    filepath = '/Users/MarissaWiseman/Desktop/galvanize/project/data/trump_speeches.p'
    stopwords= STOPWORDS | set(['will', 'want'])
    topic_df, df_stats, cleaned_speeches = analyze_speeches(filepath, '../code_part2/trump_termite.png')
    #print topic_df
    get_wordcloud(cleaned_speeches, stopwords, red_color, '../code_part2/trump_map.png')
