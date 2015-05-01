

"""
Surprised with the result?  Remember the .* value - this value catches ANYTHING. The result is that the whole string is matched.

How do we extract the information we want??

Grouping! https://docs.python.org/2/howto/regex.html#grouping

Move on to regex2.py. 
"""
import re

test_string_1 = "This is a test string."

regex_extraction_str = r'.*(te(st))(.*)'

pg = re.compile(regex_extraction_str)

matched_group = pg.match(test_string_1)


print
print "The root group (original string):", matched_group.group()
print "Beginning index of the root group:", matched_group.start()
print "End index of the root group:", matched_group.end()
print "Full index of the matched group.", matched_group.span()
print
print "First group: %s" % matched_group.group(1)
print "Beginning index of first group:", matched_group.start(1)
print "End index of group 1:", matched_group.end(1)
print "Full index of group 1:", matched_group.span(1)
print
# side note: groups can be nested
print "Second group: %s" % matched_group.group(2)
print "Beginning index of second group:", matched_group.start(2)
print "End index of group 2:", matched_group.end(2)
print "Full index of group 2:", matched_group.span(2)
print
print "Third group: %s" % matched_group.group(3)
print "Beginning index of third group:", matched_group.start(3)
print "End index of group 3:", matched_group.end(3)
print "Full index of group 3:", matched_group.span(3)



