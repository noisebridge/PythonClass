
import re
import pickle

pickle_filename = 'ngsl.pickle'
mode = 'r'

with open(pickle_filename, mode) as f:
    ngsl_words = pickle.load(f)

partially_decoded = 'mmenc-partial.txt'
with open(partially_decoded, mode) as f:
    contents = f.read()

# pluck alphanumeric+underscore, separate by a space, and split into a list on the space character
partially_decoded_wordlist = re.sub("[^\w]", " ", contents).split()

"""
We want to know our confidence that the nonmatching letters really fit.

For a given part word, multiple source words could fit.

We want to enumerate all the possible source words' permutations but weigh them based
on their confidence interval.

Confidence interval should have a range 0,n where 0 is perfect, and n is 
no confidence. The max confidence value is also the length of the word.

Each part word will generate a bunch of hits like this, so we want a standard data structure.

I think I will use a list of lists. Then the nth element of the outside list is the confidence
interval, and the inside list stores each instance of a pair.

The list of lists will need to be reduced.  Pairs like 'nm' and 'mn' are equivalent.
The reduced form of the list will be a dictionary with 'nm' key and number of occurrences as a value.

Since we know the reduced form why can't se skip the nonreduced form.
"""

# iterate over all source words for each part word
for part_word in partially_decoded_wordlist:
    for source_word in ngsl_words:
        # only take action if the lengths match, this is an easy optimization place for later
        if len(part_word) == len(source_word):
            confidence = 0
            nonmatching_pairs = []
            # step throuch each position in both and check matching
            for i in range(len(source_word)):
                if part_word[i] == source_word[i]:
                    # either increase the confidence of the match
                    confidence += 1
                else:
                    # or add a new nonmatching pair
                    nonmatching_pairs.append(part_word[i] + source_word[i])


