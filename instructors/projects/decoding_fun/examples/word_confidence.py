"""
The words need to all be lowercase and only a-z.
We don't check that here.

"""

import re
import pickle

# Two variables can be used to fine-tune the output.
# A better solution is do weigh shorter words more lightly and longer more heavily.
confidence_requirement = 2
word_length_requirement = 6


alphabet = 'abcdefghijklmnopqrstuvwxyz'

partially_decoded = 'mmenc-partial.txt'

pickle_filename = 'ngsl.pickle'
mode = 'r'

with open(pickle_filename, mode) as f:
    ngsl_words = pickle.load(f)

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

vetted_nonmatching_pairs = dict()

# iterate over all source words for each part word
for part_word in partially_decoded_wordlist:
    for source_word in ngsl_words:
        len_source_word = len(source_word)
        len_part_word = len(part_word)

        # use a min length stopgap to avoid high frequency short words from impacting our stats.
        if len_part_word >= word_length_requirement:
            # only take action if the lengths match, this is an easy optimization place for later
            if len_part_word == len_source_word:
                confidence = len_part_word
                nonmatching_pairs = dict()
                # step throuch each position in both and check matching
                for i in range(len_source_word):
                    if part_word[i] == source_word[i]:
                        # either increase the confidence of the match
                        confidence -= 1
                    else:
                        # or add a new nonmatching pair, in any order. the dict made here needs consolidated
                        # for example, you could have nm and mn in this dict which should be combined.
                        pair = part_word[i] + source_word[i]
                        nonmatching_pairs[pair] = nonmatching_pairs.get(pair, 0) + 1
                # use a static confidence to vet pairs
                if confidence <= confidence_requirement:
                    # Increment the vetted pairs accordingly.
                    for pair, count in nonmatching_pairs.iteritems():
                        if vetted_nonmatching_pairs.get(pair, 0) == 0:
                            print "New pair:", pair
                        vetted_nonmatching_pairs[pair] = vetted_nonmatching_pairs.get(pair, 0) + count

clean_nonmatching_pairs = dict()
# We need to consolidate pairs in vetted_nonmatching_pairs that need combined, such as nm and mn.
for pair, count in vetted_nonmatching_pairs.iteritems():
    if pair[::-1] in clean_nonmatching_pairs:
        clean_nonmatching_pairs[pair[::-1]] += count
    else:
        clean_nonmatching_pairs[pair] = count


# Final list of each potential pair. Lets manually test this.
print clean_nonmatching_pairs

vetted_nonm_list = list()
for ltr, frq in clean_nonmatching_pairs.iteritems():
    vetted_nonm_list.append((frq, ltr))
vetted_nonm_list.sort()
vetted_nonm_list = vetted_nonm_list[::-1]

print vetted_nonm_list
