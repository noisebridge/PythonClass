
import re
import pickle

pickle_filename = 'ngsl.pickle'
mode = 'r'

with open(pickle_filename, mode) as f:
    ngsl_words = pickle.load(f)

partially_decoded = 'mmenc-partial.txt'
with open(partially_decoded, mode) as f:
    contents = f.read()

print contents

partially_decoded_wordlist = re.sub("[^\w]", " ", contents).split()

print partially_decoded_wordlist

