import glob
import cPickle
import re

def load_speeches(filepath):
    '''
    INPUT: Filepath to folder that contains speeches
    OUTPUT: Raw data list of speeches
    '''

    file_list = glob.glob(filepath + '/*.txt')

    all_speeches = []
    for file_path in file_list:
        with open(file_path) as f:
            speech = f.read()
            speech = re.sub("[\(\[].*?[\)\]]", " ", speech).decode('utf-8', 'ignore')
        all_speeches.append(speech)

    return all_speeches


if __name__ == "__main__":
    clinton_speeches = load_speeches('/Users/MarissaWiseman/Desktop/galvanize/project/data/clinton_speeches')
    trump_speeches = load_speeches('/Users/MarissaWiseman/Desktop/galvanize/project/data/trump_speeches')
    cPickle.dump(clinton_speeches, open('../data/clinton_speeches.p', 'wb'))
    cPickle.dump(trump_speeches, open('../data/trump_speeches.p', 'wb'))
