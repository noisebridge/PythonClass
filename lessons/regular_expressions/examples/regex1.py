"""
Example 1

Modified from: https://docs.python.org/2/howto/regex.html#regex-howto

There is a bug below that should be KEPT, it is to illustrate a point.
"""
import re

# Lets make a few strings to test:
test_string_1 = "This is a test string."

# Second string will be a titlecased version of the first:
test_string_2 = test_string_1.title()

# Now lets define our regular expression as a python raw string
regex_example_string = r'.*test.*'


# Compile Regular Expression Objects with the string.
my_compiled_re = re.compile(regex_example_string)
my_compiled_re_ignorecase = re.compile(regex_example_string, re.IGNORECASE)


print "Test String 1", test_string_1
print "Test String 2", test_string_2
print


print "Regular Expression String =", regex_example_string
print


print my_compiled_re
print my_compiled_re_ignorecase
print


"""
Now it's time to use the regular expressions.

Performing Matches: https://docs.python.org/2/howto/regex.html#performing-matches

match() / search() / findall() / finditer()
Mostly, match is what you want.

The other three are nice shortcuts.

match & search - return "Match Objects"
find & findall - return list and iterator objects containing strings respectively
"""


print "String 1:"
print "expression: my_compiled_re =", my_compiled_re.match(test_string_1)
print "expression: my_compiled_re =", my_compiled_re.match(test_string_1).group()
print "expression: my_compiled_re_ignorecase =", my_compiled_re_ignorecase.match(test_string_1)
print "expression: my_compiled_re_ignorecase =", my_compiled_re_ignorecase.match(test_string_1).group()
print

print "String 2:"
print "expression: my_compiled_re =", my_compiled_re.match(test_string_2)
print "Why do we get a bug here? We will need to wrap these things in conditionals for regular use. Use the pattern---   if match: \ do_stuff(match)"
print "expression: my_compiled_re =", my_compiled_re.match(test_string_2).group()
print "expression: my_compiled_re_ignorecase =", my_compiled_re_ignorecase.match(test_string_2)
print "expression: my_compiled_re_ignorecase =", my_compiled_re_ignorecase.match(test_string_2).group()
print

print "Why are they the same memory location?"
print "Each object is just running a new match on the same compiled regular expression."


