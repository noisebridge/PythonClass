import json

json_objects_list = []
filename = "testdata.json"

with open(filename, 'r') as f:
    for line in f:
        json_objects_list.append(json.loads(line))



district_count = {}
for record in json_objects_list:
    times = district_count.get(record['supervisor_district'], 0)
    times += 1
    #district_count.update( { record['supervisor_district'] : times } )
    district_count[record['supervisor_district']] = times

print district_count
