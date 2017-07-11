''' Docstring: Where you put your notes

Lorem ipsum...

Lorem ipsum...

'''
def bubble_sort(unsorted_list):
    ''' This is a short description of the function

    You can have more info below, this turns into output for the 
    help() builtin function
    '''

    # if we were doing from the right to the left
    # i = len(unsorted_list) - 1   
    # we need to have an index!!
    # start at the leftmost pair
    i = 0

    # run at least once
    # python does not have: do... while
    has_been_swapped = True
    while has_been_swapped:

        # has a swap occurred yet in this loop?
        has_been_swapped = False

        # "get to the end" - if i = len(unsorted_list)-1
        # if we "get to the end" start over
        while i < (len(unsorted_list) - 1):

            # atomic action - everything comes down to the comparison
            # grab two items and compare them
            if unsorted_list[i] > unsorted_list[i+1]:
                has_been_swapped = True
                print(unsorted_list[i], unsorted_list[i+1])
                # "change the order" - swap the left-side and the right-side values
                # "change the order" if the right-side number is smaller than the left-side 
                # more pythonic, but less readable? depends on the reader
                # unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                _temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = _temp

            # move on to the next pair - move to the right one spot
            i += 1

        # "start over" - go back to the top.... set the index to zero again
        i = 0

    # what data type comes out? a list of numbers
    return unsorted_list


if __name__ == "__main__":

    import random # used shuffle method only


    # what data type goes in? a list of numbers
    my_list = [3,2,1]
    print(bubble_sort(my_list))

    # lets do a bigger list
    another_list = range(100)
    random.shuffle(another_list)
    print(another_list)
    print(bubble_sort(another_list))
