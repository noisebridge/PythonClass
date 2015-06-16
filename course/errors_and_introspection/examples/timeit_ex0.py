"""
Lets time two things!

But what should we time? How about pop and ipop.

Lets see if it takes longer to pop from the left of a list than the right.

Looks like we'll have to run our timeit statements at the bottom:
    https://docs.python.org/2/library/timeit.html
"""
import timeit

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
    for item in list2:
        list2b.append(list2.pop(0))
    return

if __name__ == '__main__':

    t1 = timeit.timeit("pop_sample()", number=1000, setup="from __main__ import pop_sample")
    t2 = timeit.timeit("ipop_sample()", number=1000, setup="from __main__ import ipop_sample")

    print "pop:", t1
    print "ipop:", t2
