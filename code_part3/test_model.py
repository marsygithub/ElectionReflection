import textacy
import spacy.en
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle
from sklearn.metrics.pairwise import linear_kernel
from congress_dict import people, party
import numpy as np

paragraph = 'immigration reform close borders too many mexicans'



def get_keywords(vectorizer, paragraph):
    '''
    INPUT: strings of words, in any style
    OUTPUT: string of keywords
    '''
    doc = textacy.doc.Doc(paragraph.decode('utf-8'), metadata=None, lang=None)
    string = (' '.join(list(doc.to_terms_list(ngrams=(1, 2, 3), lemmatize=True, lowercase=True,
                            as_strings=True, filter_punct=True, include_pos =['noun', 'adj', 'verb'])))).decode('utf-8')

    keywords = vectorizer.transform([string])
    return keywords




def predict_party(model, keywords):
    '''
    INPUT: keywords
    OUTPUT: probability of being a particular party
    '''
    party_predictions = model.predict(keywords)
    probs_party = model.predict_proba(keywords)

    for prob in probs_party:
        top_3_people = np.argsort(prob)[-3:]
        top_3_prob = prob[top_3_people]
        sum_prob = sum(top_3_prob)
        string = str('{0}% {1}, {2}% {3} and {4}% {5}'.format(round(top_3_prob[2]*100/sum_prob,2), party[top_3_people[2]],
                                         round(top_3_prob[1]*100/sum_prob,1), party[top_3_people[1]],
                                         round(top_3_prob[0]*100/sum_prob,1), party[top_3_people[0]]))
        return string

def predict_person(model, keywords):
    '''
    INPUT: keywords
    OUTPUT: probability of being a particular congressman
    '''
    person_predictions = model.predict(keywords)
    probs_person = model.predict_proba(keywords)

    for prob in probs_person:
        top_3_people = np.argsort(prob)[-3:]
        top_3_prob = prob[top_3_people]
        sum_prob = sum(top_3_prob)
        string = str('{0}% {1}, {2}% {3} and {4}% {5}'.format(round(top_3_prob[2]*100/sum_prob,2), people[top_3_people[2]],
                                         round(top_3_prob[1]*100/sum_prob,1), people[top_3_people[1]],
                                         round(top_3_prob[0]*100/sum_prob,1), people[top_3_people[0]]))

        return string

if __name__ == '__main__':
    vectorizer = pickle.load(open('vectorizer.p', 'rb'))
    speeches = pd.read_pickle('org_speeches')
    matrix = pickle.load(open('term_matrix.pkl', 'rb'))

    with open("model_person.pkl") as f_person:
        model_person = pickle.load(f_person)

    with open("model_party.pkl") as f_party:
        model_party = pickle.load(f_party)

    paragraph = 'immigration reform close borders too many mexicans'

    keywords = get_keywords(vectorizer, paragraph)
    print predict_party(model_party, keywords)
    print predict_person(model_person, keywords)
