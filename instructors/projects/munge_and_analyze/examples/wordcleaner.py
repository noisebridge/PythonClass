"""
Discard words with letters that are not in the accepted list
"""


import pickle

pickle_file = "ngsl.pickle"
output_pickle_file = "ngsl_clean.pickle"

accepted_alphabet = 'abcdefghijklmnopqrstuvwxyz'

with open(pickle_file, 'r') as f:
    source_word_list = pickle.load(f)

clean_word_list = []
for word in source_word_list:
    word = word.lower()
    for letter in word:
        if letter not in accepted_alphabet:
            print word
            break
    clean_word_list.append(word)

with open(output_pickle_file, 'w') as f:
    pickle.dump(clean_word_list, f)
