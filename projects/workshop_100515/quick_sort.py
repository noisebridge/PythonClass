""" Quick Sort

Implement a simple quick sort in Python.

"""
# we'll use a random pivot.
import random

def my_sorter(mylist):
    """ The atomic component of recursive quick sort

    """

    # we are missing a base case

    if len(mylist) == 1:
        return mylist
    # do we need this?
    if len(mylist) == 0:
        return mylist

    pivot_index = random.choice(range(len(mylist)))
    pivot = mylist[pivot_index]

    left_side = mylist[0:pivot_index]
    right_side = mylist[pivot_index+1:]

    #print left_side, pivot, right_side

    # can swap left and right once we find one in each, then append 
    # once we run out on one side.
    right_side_2 = list()
    left_side_2 = list()

    for item in left_side+right_side:
        if item > pivot:
            right_side_2.append(item)
        if item <= pivot:
            left_side_2.append(item)

    print "l:", left_side_2
    print "p:", pivot
    print "l+p:", left_side_2 + [pivot]
    print "r:", right_side_2
    return my_sorter(left_side_2) + [pivot] + my_sorter(right_side_2)

mylist = [4,6,5,9,2,3,1,8]
print mylist
print my_sorter(mylist)

