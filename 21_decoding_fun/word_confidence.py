
import re
import pickle

# Two variables can be used to fine-tune the output.
# A better solution is do weigh shorter words more lightly and longer more heavily.
confidence_requirement = 3
word_length_requirement = 6


alphabet = 'abcdefghijklmnopqrstuvwxyz'

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

vetted_nonmatching_pairs = dict()

# iterate over all source words for each part word
for part_word in partially_decoded_wordlist:
    part_word = part_word.lower()
    for source_word in ngsl_words:
        source_word = source_word.lower()
        # only take action if the lengths match, this is an easy optimization place for later
        # Also use a min length stopgap to avoid high frequency short words from impacting our stats.
        if len(part_word) >= word_length_requirement and len(part_word) == len(source_word):
            confidence = len(part_word)
            nonmatching_pairs = dict()
            # step throuch each position in both and check matching
            for i in range(len(source_word)):
                if part_word[i] == source_word[i]:
                    # either increase the confidence of the match
                    confidence -= 1
                else:
                    # test that we aren't introducing numbers.
                    if part_word[i] in alphabet and source_word[i] in alphabet:
                        # or add a new nonmatching pair
                        pair = part_word[i] + source_word[i]
                        if pair in nonmatching_pairs.keys():
                            nonmatching_pairs[pair] += 1
                        elif pair[::-1] in nonmatching_pairs.keys():
                            nonmatching_pairs[pair[::-1]] += 1
                        else:
                            nonmatching_pairs[pair] = 1
            # Temporary: use a static confidence to vet pairs
            if confidence <= confidence_requirement:
                # Increment the vetted pairs accordingly.
                for pair, count in nonmatching_pairs.iteritems():
                    if pair in vetted_nonmatching_pairs.keys():
                        vetted_nonmatching_pairs[pair] += count
                    elif pair[::-1] in vetted_nonmatching_pairs.keys():
                        vetted_nonmatching_pairs[pair[::-1]] += count
                    else:
                        vetted_nonmatching_pairs[pair] = count
                        print "New pair:", pair

# Final list of each potential pair. Lets manually test this.
print vetted_nonmatching_pairs

vetted_nonm_list = list()
for ltr, frq in vetted_nonmatching_pairs.iteritems():
    vetted_nonm_list.append((frq, ltr))
vetted_nonm_list.sort()
vetted_nonm_list = vetted_nonm_list[::-1]

print vetted_nonm_list
