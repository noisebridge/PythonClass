
import pickle

with open('ngsl_clean.pickle', 'rb') as f:

    # print pickle.load(f)
    word_list = pickle.load(f)

letter_freq_dict = dict()

for word in word_list:
    for letter in word:
        letter_freq_dict[letter] = letter_freq_dict.get(letter, 0) + 1

#print letter_freq_dict

letter_freq_list = list()
for key in letter_freq_dict.keys():
    letter_freq_list.append([letter_freq_dict[key], key])

letter_freq_list.sort()

print letter_freq_list
