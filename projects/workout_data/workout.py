
import pprint
import json
import logging

logging.basicConfig(level=logging.DEBUG)

filename = 'workout.json'

out_filename = 'workout_metadata.json'

workout_component_keys = [  'Equipment', 'Force', 'Level', 'Main Muscle Worked', 'Mechanics Type', 'Sport', 'Type', 
                            'guide', 'Your Rating', 'link', 'pic_left', 'pic_right' ]

with open(filename, 'rb') as f:
    workouts = json.load(f)

# Why is this data a list of 873 single key dictionaries?
print len(workouts)
print type(workouts)

# Lets make it into a single dictionary with 873 keys. That will be easier to use.
workouts_dict = dict()
for _wrapper_dict in workouts:
    for _k, _v in _wrapper_dict.iteritems():
        workouts_dict[_k] = _v

dict_of_possible_values = dict()
for data_label in workout_component_keys:
    dict_of_possible_values[data_label] = list()

for workout, components in workouts_dict.iteritems():
    for data_label in workout_component_keys:
        # This will ensure that the list contains only unique values.
        if components[data_label] not in dict_of_possible_values[data_label]:
            dict_of_possible_values[data_label].append(components[data_label])

with open(out_filename, 'wb') as f:
    json.dump(dict_of_possible_values, f)
pprint.pprint(dict_of_possible_values)

# Lets review the data for completeness since there is no schema per se.
for workout, components in workouts_dict.iteritems():

    # Check for missing data and log it.
    for component_key in workout_component_keys:
        if component_key not in components.keys():
            logging.debug(workout + ": " + component_key + "- KeyError")

    # Check for extra data and log it.
    for component_key in components.keys():
        if component_key not in workout_component_keys:
            logging.debug(workout + ": " + component_key + "- Extra Data")





