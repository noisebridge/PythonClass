"""

The goal of this module is to inspect an int and a str and see what attributes they share, and what attributes they do not share.

"""

import inspect
import pprint

i = 5
s = "meow"

def function_test():
    pass

f = function_test # now f is defined as function_test. function_test can be called as f()

ins_i = inspect.getmembers(i)
ins_s = inspect.getmembers(s)

attr_i = []
for each in ins_i:
    attr_i.append(each[0])    
attr_s = []
for each in ins_s:
    attr_s.append(each[0])

str_only = []
int_only = []
int_and_str = []
# strip these two lists of attributes down to see what is where
for each in attr_i:
    if each in attr_s:
        int_and_str.append(each)
        attr_s.remove(each)
    else:
        int_only.append(each)
str_only.extend(attr_s)

pprint.pprint( ("IN INTEGERS, NOT IN STRINGS", int_only ) )
pprint.pprint( ("IN STRINGS, NOT IN INTEGERS", str_only ) )
pprint.pprint( ("IN INTEGERS AND STRINGS", int_and_str ) )


