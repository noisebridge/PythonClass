
"""
Surprised with the result?  Remember the .* value - this value catches ANYTHING. The result is that the whole string is matched.

How do we extract the information we want??

Grouping! https://docs.python.org/2/howto/regex.html#grouping

Move on to regex2.py. 
"""
import re

test_string_1 = "This is a test string."

regex_extraction_str = r'(.*)((t)((e)((s)(t))))(.*)'

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

# side note: strings can be nested

#https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
range_of_group = (0,1,2,3,4,5,6,7,8,9)
print matched_group.group(*range_of_group)
