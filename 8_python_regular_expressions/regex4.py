"""
Goal:

    List all problematic permutations of the band name for The Beatles and correct it.

    With a single letter replace, we are missing the transpose failure possibility in the test_set_of_filenames

"""
import re

test_set_of_filenames = ['the beatles', 'The Beatles', 'Beatles, The', 'Da Beatels']

regex_search_str = r'beatles'

# run a string replace on the regex search to allow one in-place letter change.

regex_search_perm_list = []

def dot_replacer(regex_search_str, i):

    string_to_mutate = regex_search_str[0:i] + '.' + regex_search_str[i+1:]
    return string_to_mutate


i=0
while i < len(regex_search_str):

    regex_fuzzy_str = dot_replacer(regex_search_str, i)
    regex_search_perm_list.append(regex_fuzzy_str)
    i+=1

print regex_search_perm_list

match_obj_results = []
for test_filename in test_set_of_filenames:
    for expr_str in regex_search_perm_list:
        
        # Will skip None type which is false. No results in re match object yields None type.
        search_result = re.search(expr_str, test_filename, flags=re.IGNORECASE)
        if search_result:
            match_obj_results.append(search_result)
            break
        
for res in match_obj_results:
    print res
    """
    if res.group != False:
        print( "Result: %s" % res.group )
    """
