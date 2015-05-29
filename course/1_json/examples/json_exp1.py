import json
import os

with open("abcde.json") as f:
    abcde_dict = json.load(f)


print abcde_dict


with open("robotlovecats.json", 'w') as fx:
    json.dump(abcde_dict, fx)

with open('robotlovecats.json', 'a') as fx:
    fx.write(os.linesep + json.dumps(abcde_dict)) 

