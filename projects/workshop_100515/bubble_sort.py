""" Bubble Sort 

"""
import random
import time

def compare_two_numbers(a, b):
    """ Return the two numbers as a tuple, smallest to largest.

    """
    if a > b:
        result = (b, a)
    else:
        # this covers <=
        result = (a, b)

    return result

mylist = range(1,21)
random.shuffle(mylist)
print mylist

#mylist = [4,2,3,1]

for j in range(len(mylist)-1):
    # lets iterate over the list length minus one times.
    for i in range(len(mylist)-j-1):
        print mylist
        mylist[i], mylist[i+1] = compare_two_numbers(mylist[i], mylist[i+1])
        time.sleep(.4)

print mylist



