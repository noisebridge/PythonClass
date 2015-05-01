"""
Example 1

There is a bug below that should be KEPT, it is to illustrate a point.
"""
import re

# Lets make a few strings to test:
test_string_1 = "This is a test string."

# Now lets define our regular expression as a python raw string
regex_example_string = r'.*test.*'

# Compile Regular Expression Objects with the string.
my_compiled_re = re.compile(regex_example_string)

print "Test String 1", test_string_1

print "Regular Expression String =", regex_example_string
print

print my_compiled_re

print "String 1:"
print "expression: my_compiled_re =", my_compiled_re.match(test_string_1)
print "expression: my_compiled_re =", my_compiled_re.match(test_string_1).group()

