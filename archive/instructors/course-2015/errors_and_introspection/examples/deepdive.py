in_a_list = dir(list())
in_a_dict = dir(dict())

only_in_a_list = []
for attribute in in_a_list:
    if attribute not in in_a_dict:
        only_in_a_list.append(attribute)
        
only_in_a_dict = []
for attribute in in_a_dict:
    if attribute not in in_a_list:
        only_in_a_dict.append(attribute)

print
print "Things in a list but not a dict: {}".format(only_in_a_list)
print
print "Things in a dict but not a list: {}".format(only_in_a_dict)
print
