
import json

poss_permutations = list()

input_filename = "testdata.json"

requested_key = "responsible_agency"
output_filename = "responsible_agency.json"


with open(input_filename, "r") as f:

    for line in f:
        record = json.loads(line)
        poss_permutations.append(record[requested_key])


unique_perms = list(set(poss_permutations))


with open(output_filename, "w") as f:

    json.dump(poss_permutations, f)


perm_freq_dict = {}

for perm in poss_permutations:
    count = perm_freq_dict.get(perm, 0)
    count += 1
    perm_freq_dict[perm] = count

print perm_freq_dict
    
    
