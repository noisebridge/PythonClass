# -*- coding: utf-8 -*-

#above is used to set the encoding for this module, (unfortunately didn't help that much)

#used for seeing our data in nicest string format possible
import pprint

#again idiom for reading in a file, relative path given
with open('../pres_on_trade.txt', 'r') as fp: 
    all_text = fp.read()

#str.split() will split groups of characters on any white space, easy... nice
#sorted built-in function will only sort alphbetically here  
all_words = sorted(all_text.split())

#begin preparation of words for a reasonable word frequency count

#we need to change our words from str to unicode
#unicode_words = [unicode(word) for word in all_words if unicode(word)]
#list comprehensions won't work because we get errors, 
#let's do a try: except: block
unicode_words = []
for word in all_words:
    try:
        unicode_words.append(unicode(word))
    except UnicodeDecodeError:
        pass 

#awesome list comprehension, they take iterables and return lists
#this will clean our words of unwanted punctuation and change to all lowercase
all_words = [word.strip("?.\'-,().").lower() for word in unicode_words]

#print all_words
#help(''.strip)
 

#reminder on dictionary syntax - setting the key and value 
#dict_name[key] = value 
#word_freq_dc['word'] = 18 

#using dict.get method to check for existence and build word_freq dictionary
word_freq_dc = {}

for word in all_words:
    times = word_freq_dc.get(word, 0)
    times += 1
    word_freq_dc[word] = times 


#the easy way :) if you knew about it or where to look
from collections import Counter
#help(Counter)

counter = Counter(all_words)

#can use slice method on a sequence, this gets first 40 of type list
#that is: Counter.most_common() returns a list, a list is considerd one kind of sequence
print(counter.most_common()[:40])

#end line character for clarity when printing 
print '\n'

#to be sure
counter_for_dc = Counter(word_freq_dc)
counter_from_before = Counter(all_words)

print counter_for_dc == counter_from_before


#going further with a generator expression
non_small_words = (word for word in all_words 
                   if len(word) > 4 and 
                   word is not 'usa' and 
                   word not in 
                   ['applause', 'laughter', 'there', 'these', 'those'])

recounter = Counter(non_small_words)
print(recounter.most_common()[:40])


#below is work we did to figure out the proper procedure to
#count words using a dictionary

#pprint.pprint(word_freq_dc)

#for k, v in word_freq_dc.iteritems():
#   tupled_word_freq.append((k, v))

#tupled_word_freq = zip(word_freq_dc.itervalues(), word_freq_dc.iterkeys())

#print(tupled_word_freq)
#print sorted(tupled_word_freq)

#help(word_freq_dc.get)
