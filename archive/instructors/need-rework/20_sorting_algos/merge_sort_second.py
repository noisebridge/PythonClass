"""
Coded this quickly during the lecture describing it.

Divide and conquer algorithm.

Merge sort improves over: selection, insertion, bubble sort, three other sorting algorithms.


Note: I've used a lot of iterator logic that is not pythonic. 
This algorithm was implemented with the intention of being as 
close to the reference algorithm as possible.

The test at the bottom devised is to measure the algorithm against 
the python reference function, list.sort()
"""
import random

# Lets generate an input for now.... array of n numbers:
n = [] 
input_length = 9
input_range = input_length
lowest_input_permitted = 1
for i in range(input_length):
    # Note that the merge step must handle collisions, which are defined as equal values
    n.append( random.randint(lowest_input_permitted ,input_range) )
 
print("list is: \n", n)   

def merge_and_sort(first_half, second_half):
    """
    This will merge two sorted subarrays.
    
    The subarrays are sorted from lowest to highest.

    This must handle when both merged elements are equal!! ***
    """


    j = 0 # this is a counter assigned to first_half
    k = 0 # this is a counter assigned to second_half

    merged = [] # this is the output, append to this progressively during the merge

    while j < len(first_half) and k < len(second_half):
        #print("first_half", "second_half")
        print(first_half, second_half)
        if first_half[j] < second_half[k]:
            merged.append(first_half[j])
            j+=1
        else:
            merged.append(second_half[k]) # handled the equal case in this else
            k+=1

    # Handle merging any remainders after one array is exhausted in the while statement.
    if j < len(first_half):
        merged.extend(first_half[j:len(first_half)])
    if k < len(second_half):
        merged.extend(second_half[k:len(second_half)])

    return merged


def divide_and_recurse(n):
    """
    Recurse over the input, dividing or referring to the base case if 'fully divided'.
    
    In various places, lists must be specified as python will just return an int.
    """


    # return immediately on the base case
    if len(n) < 2:
        return n

    else:
        first_half = []
        second_half = []
        if len(n) == 2: # special case, correctly manages list indexes with rounding
            first_half.append(n[0])
            second_half.append(n[1])
        else: # general case manages list indeces for len(n)=3 or higher.
            first_half.extend(n[0:(len(n)/2)]), 
            second_half.extend(n[(len(n)/2):len(n)])
        return merge_and_sort(divide_and_recurse(first_half), divide_and_recurse(second_half))



result =  divide_and_recurse(n)
n.sort()
if result == n: # Test merge sort against python reference implementation of list.sort()
    print "Sorted: Passed"
else:
    print "Sorted: Failed"

n.reverse() # now unsort (sort is defined as lowest to highest) the reference values, n
if result == n:
    print "Test Validated: NO"
if result != n:
    print "Test Validated: YES"
