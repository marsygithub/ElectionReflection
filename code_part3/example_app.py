from flask import Flask, request, render_template
import cPickle as pickle
import pandas as pd
import numpy as np
from test_model import get_keywords, predict_party, predict_person



app = Flask(__name__)

PORT = 5000


@app.route('/')
def index():
    paragraph = request.args.get('paragraph')

    if paragraph != None:
        keywords = get_keywords(vectorizer, paragraph)
        party = predict_party(model_party, keywords)
        people = predict_person(model_person, keywords)
    else:
        party = ""
        people = ""
        paragraph = ""



    return render_template("index.html", party=party, people=people, query=paragraph)


    #return '{0}\n\n{1}'.format(line1, line2), 200, {'Content-Type': 'text/css; charset=utf-8'}
    #return render_template('index.html', title = 'Flask - Bootstrap')



if __name__ == '__main__':
    vectorizer = pickle.load(open('vectorizer.p', 'rb'))
    print 'vectorizer loaded'
    speeches = pd.read_pickle('org_speeches')
    print 'speeches loaded'
    matrix = pickle.load(open('term_matrix.pkl', 'rb'))
    print 'matrix loaded'
    with open("model_person.pkl") as f_person:
        model_person = pickle.load(f_person)
    print 'person model loaded'
    with open("model_party.pkl") as f_party:
        model_party = pickle.load(f_party)
    print 'party model loaded'

    app.run(host='0.0.0.0', port=PORT, debug=True)




    # Start Flask app
