"""
Illustrate a comparison window for a substring
"""


mystring = 'cacacacacaca'

"""
Initial window size is 1/2 the total length of the string
BECAUSE you can't match more than half of the string
to less than half of the string, the lengths aren't even right.
"""
init_window_size = 3 # half the string length

substr1 = mystring[0:init_window_size]
substr2 = mystring[init_window_size:]

# print substr1 == substr2

# if it is odd, round up.
#init_window_size = int(len(mystring)/2)

"""
we will calculate the next windowsize by subtracting 1 from
the current window size.

"""

# find the new window size from the initial window size
window_size = init_window_size - 1

# we will check substr1 against all the other substrings.
substr1 = mystring[0:window_size]

substr2 = mystring[window_size:(window_size+window_size)]

# increment by 1 for the next substring to check
# (we can keep incrementing the window position by 1 
# until we hit the top)
substr3 = mystring[window_size+1:(window_size+window_size+1)]

substr4 = mystring[window_size+1+1:(window_size+window_size+1+1)]

# print substr1
# print substr2
# 
# print substr1 == substr2
# print substr1 == substr3
# print substr1 == substr4
# 

# window lower bound starts right after the window we are checking against
window_lower_bound = window_size
target_substring = mystring[0:window_size]

# while loop (while the second value is less than the total)
while (window_lower_bound + window_size) <= len(mystring):

    current_substring_to_check = mystring[window_lower_bound:(window_size+window_lower_bound)] 
    window_lower_bound += 1

    print target_substring == current_substring_to_check


