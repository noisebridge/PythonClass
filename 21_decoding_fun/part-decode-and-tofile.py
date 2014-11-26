"""
1. lets auto-assign based on our frequency dict.

2. output the auto-assigned values

Then lets accept human input on a loop.

The loop will swap the two values given.

e.g. I give am, the values of a and m are swapped on the comparison dict.

"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'

encoded_source_file = 'mm.txt'
sample_file = 'cc.txt'
mode = 'r'

with open(encoded_source_file, mode) as f:
    encoded_source = f.read()

with open(sample_file, mode) as f:
    sample = f.read()


def letter_freq_counter(source):
    """ Count up frequency of letters using only lower case. Count based on the alphabet set.
    """

    letter_freq_dict = dict()

    for letter in source:
        letter = letter.lower()
        if letter in alphabet:
            letter_freq_dict[letter] = letter_freq_dict.get(letter, 0) + 1

    return letter_freq_dict


def frq_only_match(encoded_source, source_letter_freq_dict, sample_letter_freq_dict):
    """ Use only frequency to spit out an approximate match.
    """

    # lets have a peek
    source_freq_list = list()
    for ltr, frq in source_letter_freq_dict.iteritems():
        source_freq_list.append((frq, ltr))
    source_freq_list.sort()
    sample_freq_list = list()
    for ltr, frq in sample_letter_freq_dict.iteritems():
        sample_freq_list.append((frq, ltr))
    sample_freq_list.sort()

    print "Source:", source_freq_list
    print "Sample:", sample_freq_list

    # The key is the source(encoded) letter, the value is the sample prediction.
    frq_only_match_dict = dict(zip(*[zip(*source_freq_list)[1], zip(*sample_freq_list)[1]]))

    # Translate one letter at a time
    decoded_source_freq_only = ""
    for letter in encoded_source:
        letter = letter.lower()
        if letter in frq_only_match_dict.keys():
            decoded_source_freq_only += frq_only_match_dict[letter]
        else:
            decoded_source_freq_only += letter
            
    return decoded_source_freq_only



sample_ltr_frq = letter_freq_counter(sample)
source_ltr_frq = letter_freq_counter(encoded_source)

part_decoded_source = frq_only_match(encoded_source, source_ltr_frq, sample_ltr_frq) 


# Give the user something to work with
print part_decoded_source

output_file = 'mmenc-partial.txt'
mode = 'w'
with open(output_file, mode) as f:
    f.write(part_decoded_source)
    

