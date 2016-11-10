import textacy
import spacy.en
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle


cw = textacy.corpora.CapitolWords()
docs = cw.records(date_range=('1996-01-01', '2016-12-31'))
content_stream, metadata_stream = textacy.fileio.split_record_fields(docs, 'text', 'speaker_name')
corpus = textacy.Corpus(('en').decode('utf-8', 'ignore'), texts=content_stream, metadatas=metadata_stream)

#Dataframe of the speaker and speeches created from the corpus
df = pd.read_pickle('speeches')

drop_words = ['objection', 'american', 'people', 'gentlewoman', 'gentleman', 'minute', 'distinguished', 'yea', 'desk',
             'vote', 'internship', 'unanimous', 'consent', 'quorum', 'previous', 'session', 'amendment', 'read', 'immediate',
             'consideration', 'senator', 'congress', 'house', 'rollcall', 'floor', 'desire', 'nay', 'present', 'ask', 'rescind',
             'order', 'recognize', 'yield', 'question', 'authorize', 'meet', 'proceed', 'motion', 'pending', 'set', 'table', 'lie',
             'president', 'speaker', 'appeal', 'ruling']

democrats = [ u'Joseph Biden', u'Joe Biden', u'Barack Obama', u'Bernie Sanders', u'Hillary Clinton', u'Lincoln Chafee']
republicans = [u'Rand Paul', u'Rick Santorum', u'Lindsey Graham', u'John Kasich', u'Mike Pence', u'Marco Rubio']
independents = [ u'Jim Webb']

#function used to create new column in dataframe that identifies speaker party
def party(person):
    if person in democrats:
        return 'D'
    elif person in republicans:
        return 'R'
    else:
        return 'I'

#Creating string of keywords for each speech
list_keywords = []
short = []
for i, doc in enumerate(corpus):
    string = (' '.join(list(doc.to_terms_list(ngrams=(1, 2, 3), lemmatize=True, lowercase=True,
                        as_strings=True, filter_punct=True, include_pos =['noun', 'adj', 'verb'])))).decode('utf-8')

    resultwords  = [word for word in string.split() if word not in drop_words]
    result = (' '.join(resultwords)).decode('utf-8')

    list_keywords.append(result)
    # Identifying speeches less than 30 words
    if len(doc.text.split()) <= 30:
        short.append(i)

#List of keywords excluding the short speeches
new_list = []
for i, item in enumerate(list_keywords):
    if i not in short:
        new_list.append(item)
len(new_list)


#Creating the "y-values" for teh shortened dataframe that
#excludes the short speeches
party = []
for i, value in enumerate(df['party']):
    if i not in short:
        party.append(value)

person = []
for i, value in enumerate(df['name']):
    if i not in short:
        person.append(value)

#Pickle vectorizer
tfidf = TfidfVectorizer(stop_words='english', ngram_range = (1,3), min_df=2, sublinear_tf=True).fit(new_list)
tfidfed = tfidf.transform(new_list)

pickle.dump(tfidfed, open('term_matrix.pkl', 'wb'))


#Pickle model that identifies person
X_train, X_test, y_train, y_test = train_test_split(tfidfed, person)

clf = MultinomialNB(alpha = .01).fit(X_train, y_train)

pickle.dump(clf, open('model_person.pkl', 'wb'))

#Pickle model that identifies party
X_train, X_test, y_train, y_test = train_test_split(tfidfed, party)

clf = MultinomialNB(alpha = .01).fit(X_train, y_train)

pickle.dump(clf, open('model_party.pkl', 'wb'))

# Pickle Dataframe excluding the short speeches
df_new = df.drop(df.index[short])
df_new =df_new.reset_index(drop=True)
