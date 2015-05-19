
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def letter_freq_counter(source):
    """ Count up frequency of letters using only lower case. Count based on the alphabet set.
    """

    letter_freq_dict = dict()

    for letter in source:
        letter = letter.lower()
        if letter in alphabet:
            letter_freq_dict[letter] = letter_freq_dict.get(letter, 0) + 1

    return letter_freq_dict


source_file = 'mm.txt'
mode = 'r'
with open(source_file, mode) as f:
    source = f.read()

# run our function
letter_freq_dict = letter_freq_counter(source)

# lets have a peek
letter_freq_list = list()
for ltr, frq in letter_freq_dict.iteritems():
    letter_freq_list.append((frq, ltr))

letter_freq_list.sort()
print letter_freq_list    

