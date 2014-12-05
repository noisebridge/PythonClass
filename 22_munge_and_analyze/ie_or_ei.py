"""

Data Analysis Ideas:



    i before e, except after c - not a good rule, let's prove it
    pseudocode:
        1st case: search for *ei - 
                    if cei - tally success case 1
                    else - tally fail case 1
        2nd case: search for *ie
                    if not cie - tally success case 2
                    if cie - tally fail case 2






"""


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

# The sort function works in place to sort the list.
# In this case it sorted on the first value of the inside list.
letter_freq_list.sort()

#print letter_freq_list


rules = """
    i before e, except after c - not a good rule, let's prove it
    pseudocode:
        1st case: search for *ei - 
                    if cei - tally success case 1
                    else - tally fail case 1
        2nd case: search for *ie
                    if not cie - tally success case 2
                    if cie - tally fail case 2

"""

tallies = {     'success_case_1'    : 0,
                'fail_case_1'       : 0,
                'success_case_2'    : 0,
                'fail_case_2'       : 0 }

s1 = []
s2 = []
f1 = []
f2 = []

for word in word_list:

    # what if ei exists more than once?
    ei_index = word.find('ei')
    if ei_index > 0:
        if word[ei_index-1] == 'c':
            tallies['success_case_1'] += 1
            s1.append(word)
        else:
            tallies['fail_case_1'] += 1
            f1.append(word)

    ie_index = word.find('ie')
    if ie_index > 0:
        if word[ie_index-1] != 'c':
            tallies['success_case_2'] += 1
            s2.append(word)
        # Only case left for the else is ie_index == 'c'
        else:
            tallies['fail_case_2'] += 1
            f2.append(word)
    
print
print tallies
print rules
print 's1 =', s1
print 'f2 =', f2
print 'f1 =', f1
print 's2 =', s2


