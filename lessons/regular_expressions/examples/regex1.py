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
print p

pi = re.compile(regex_example_string, re.IGNORECASE)
print pi

print

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

len(matched.group())

print "The Whole Match:", test_string_1[matched.start():matched.end()]
print "The Whole Match len:", len(test_string_1[matched.start():matched.end()])
print
print pg.groups()
