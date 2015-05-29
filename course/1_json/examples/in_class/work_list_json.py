'''much like work_json.py but uses a python list data structure
to make the iteration process less complex. python dictionaries take 
a bit of practice to handle with ease.
'''


import json  

with open('abcde.json', 'r') as fp:
    abc_json = json.load(fp) 


json_ls = list(abc_json)

for num in range(42):
    json_ls.append(num)


with open('new_json.json', 'w') as fp:
    json.dump(json_ls, fp) 


with open('new_json.json', 'r') as fp:
    json_again = json.load(fp)

for num in range(10):
    json_again.append(num)


print json_again