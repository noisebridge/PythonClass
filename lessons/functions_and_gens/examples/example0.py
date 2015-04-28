#Return the absolute value of the number x. Floats as well as ints are accepted values.
abs(-100)
abs(-77.312304986)
abs(10)

#Return True if any element of the iterable is true. If the iterable is empty, return False.
any([0,1,2,3])
any([0, False, "", {}, []])

#enumerate() returns an iterator which yields a tuple that keeps count of the elements in the sequence passed. 
#Since the return value is an iterator, directly accessing it isn't particularly useful. 
from string import ascii_letters as ltrs
for index, letter in enumerate(ltrs):
    print index, letter

print enumerate(ltrs)
print list(enumerate(ltrs))