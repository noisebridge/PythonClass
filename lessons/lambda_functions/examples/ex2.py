"""

Examples of using filter, map and reduce functions with lambda expressions.
These are simple ways to work with lists.

"""

words = 'Python supports the creation of anonymous functions at runtime, \
          using a construct called "lambda".'.split()

# ----------------------------------------------------------
# filter function
words_with_on = filter(lambda w: 'on' in w, words)
print '(lambda)   words containing "on":', words_with_on

# The same solution as above, but using a function with a loop
def find_words_containing(words, search_str):
    words_containing = list()
    for word in words:
        if search_str in word:
            words_containing.append(word)
    return words_containing

print '(for loop) words containing "on":', find_words_containing(words, 'on')

# TBD: can we use list comprehension to do the same thing?

# ----------------------------------------------------------
# map function
# Convert a sentence to a list of the lengths of each word.
# Which length occurs most frequently?
word_lens = map(lambda i: len(i), words)
print 'length of each word: ', word_lens

# TBD: Another idea would be to map a list of integers to a string
#      representing either 'even' or 'odd'. How would that work?

# map two lists together
names = ['jake', 'sue', 'bob', 'larry']
greetings = ['hello', 'hi', 'hola', 'howdy']
print map(lambda x, y: x + ' ' + y + '!', greetings, names)

# what about mapping three lists?
# For example, lets use true/false values and solve the following:
# ans = a AND ( b OR c )
# where a, b and c are lists of booleans
a = [True, True, True, False]
b = [False, True, False, True]
c = [True, False, False, True]
ans = map(lambda x, y, z: x and (y or z), a, b, c)
print ans

#TBD: How would we compute this with for loops or list comprehension?

# ----------------------------------------------------------
# reduce function
# The function reduce(func, seq) continually applies the function func()
# to the sequence seq. It returns a single value.
values = [47, 11, 42, 13]
sum1 = reduce(lambda x, y: x + y, values)
sum2 = sum(values)
assert(sum1 == sum2)

# Finding the maximum of a list with using reduce:
# (notice the odd expression below and try evaluating it in the interpreter)
largest = lambda a, b: a if (a > b) else b
largest_val = reduce(largest, values)
print 'largest number is: ', largest_val

# Ideas to try: search some JSON data (via filter function)
# and then modify the results (via map function)


# ----------------------------------------------------------
# sort function
#
# A common task is to sort a list, a simple JSON dictionary or an
# object by a specific attribute/field.  Using lambda gives flexibility.

scores = {'bob': 75, 'sue': 50, 'jack': 100}
scores_sorted = sorted(scores.items(), key=lambda x: x[1])
print 'sorted scores are:', scores_sorted
print 'sorted scores converted back to a dict:', dict(scores_sorted)

# an alternative solution without lambdas:
import operator
scores_sorted2 = sorted(scores.items(), key=operator.itemgetter(0))

# TBD: What if we wanted to sort the following object?
# objects can be sorted as well. An example of sorting a list of 
# users by their scores:  
# my_list.sort(key = lambda x: x.score)
