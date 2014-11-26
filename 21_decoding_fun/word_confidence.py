
import pickle

filename = 'ngsl.pickle'
mode = 'r'

with open(filename, mode) as f:
    ngsl_words = pickle.load(f)

    print ngsl_words

