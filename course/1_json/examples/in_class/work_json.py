'''objectives: 
1. open the existing file 'abcde.json' 
2. convert all data in file to a python type
3. perform a simple python operation such as adding 10 to each value 
4. convert that object back to json and write it to a new file 
5. repeat :)
'''

import json  

with open('abcde.json', 'r') as fp:
    abc_json = json.load(fp) 

#print to show data before changing it in python
print 'before {}'.format(abc_json)

#idiom to iterate over both key and value in dictionary type
for key, value in abc_json.iteritems():
    abc_json[key] += 10
    #line above actually adds 10 to the value

    #the abc_json[key] simply accesses the value, and then we add 10
    print "value: {0}, abc_json[key]: {1}".format(value, abc_json[key])

abc_str = json.dumps(abc_json)

#look at abc_str object to verify completion
print json.loads(abc_str)

#verify type of dumps function of json module
print type( json.dumps(abc_str) )

