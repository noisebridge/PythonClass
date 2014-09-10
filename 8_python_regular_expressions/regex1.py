"""
Example 1

Modified from: https://docs.python.org/2/howto/regex.html#regex-howto
"""
import re

###
### Define our regex string
###

regex_example_string = r'.*test.*'

print
print "RE =", regex_example_string
print

###
### Compile Regular Expression Objects with the string.
###

p = re.compile(regex_example_string)
p

pi = re.compile(regex_example_string, re.IGNORECASE)
pi

###
### Test Cases
###
test_string_1 = "This is a test string."

# Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
# https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange
test_string_2 = test_string_1.title()

print "Test String 1", test_string_1
print "Test String 2", test_string_2
print

###
### Tests
###
"""
Performing Matches: https://docs.python.org/2/howto/regex.html#performing-matches

match() / search() / findall() / finditer()
Mostly, match is what you want.

The other three are nice shortcuts.

match & search - return "Match Objects"
find & findall - return list and iterator objects containing strings respectively
"""


print "Test 1, RE: p =", p.match(test_string_1)
print "Test 1, RE: pi =", pi.match(test_string_1)
print
print "Test 2, RE: p =", p.match(test_string_2)
print "Test 2, RE: pi =", pi.match(test_string_2)
print

###
### Results
###
"""
Lets see what we get!
"""

#Lets stick to the following:
matched = p.match(test_string_1)

print matched.group()
print matched.start()
print matched.end()
print matched.span()

print "The Whole Match:", test_string_1[matched.start():matched.end()]
print

"""
Surprised with the result?  Remember the .* value - this value catches ANYTHING. The result is that the whole string is matched.

How do we extract the information we want??

Grouping! https://docs.python.org/2/howto/regex.html#grouping

Move on to regex2.py. 
"""

test_string_1 = "This is a test string."

regex_extraction_str = r'.*(test).*'

pg = re.compile(regex_extraction_str)

# still using test_string_1

matched_group = pg.match(test_string_1)
print matched_group.group()
print matched_group.start()
print matched_group.end()
print matched_group.span()

print "Still the whole match: %s" % test_string_1[matched_group.start(): matched_group.end()]
print

print "Now the whole group: %s" % matched_group.group()
print "The whole group once more: %s" % matched_group.group(0)
print "And our first group: %s" % matched_group.group(1)





