import json 
from pprint import pprint as pp 

#make sure the path is relative to the files on your local drive
with open('../files/customer_form.json') as fp:
    cust_record = json.loads(fp.read())
    pp(cust_record)

    #this block can be inside or outside the with block
    for i in cust_record['phoneNumber']:
        print i['number']
        print i['type']

    #we practiced other types of dictionary access as well
    #eg:
    state_value = cust_record['address']['state']
    #print state_value 

    #reassign age value
    cust_record['age'] = 26  
    print cust_record['age']
    # or add one (this should be 27 now)
    cust_record['age'] += 1
    print cust_record['age']    

#writing just the customer's phone and fax numbers to a .json file
with open('customer_phone_and_fax.json', 'w') as fp:
    json.dump(cust_record['phoneNumber'], fp)   

#appending to that existing file
with open('customer_phone_and_fax.json', 'a') as fp:
    json.dump(cust_record['phoneNumber'], fp) 
    
