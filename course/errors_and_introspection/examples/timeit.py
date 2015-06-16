"""
Lets time two things!

But what should we time? How about pop and ipop.

Lets see if it takes longer to pop from the left of a list than the right.

Looks like we'll have to run our timeit statements at the bottom:
    https://docs.python.org/2/library/timeit.html
"""
import timeit

t1 = timeit.timer

def pop_sample():
    """
    """
    list1 = range(10000)
    list1b = list()
    for item in list1:
        list1b.append(list1.pop())
    return


def ipop_sample():
    """
    """
    list2 = range(10000)
    list2b = list()
    for item in list1:
        list2b.append(list2.pop(0))
    return

    
