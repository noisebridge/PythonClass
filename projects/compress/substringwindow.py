"""
Illustrate a comparison window for a substring
"""
import math


mystring = 'cacacacacaca'

# Initialize this as half, rounded down.
window_size = int(math.floor(len(mystring)/2)) # half the string length

# decrement the window size from L/2 to 1 and find matches.
# where L = length of initial string
while window_size > 0:

    # window lower bound starts right after the window we are checking against
    window_lower_bound = window_size
    target_substring = mystring[0:window_size]

    # while loop (while the second value is less than the total)
    while (window_lower_bound + window_size) <= len(mystring):

        current_substring_to_check = mystring[window_lower_bound:(window_size+window_lower_bound)] 
        window_lower_bound += 1

        print target_substring, current_substring_to_check, target_substring == current_substring_to_check

    window_size -= 1

