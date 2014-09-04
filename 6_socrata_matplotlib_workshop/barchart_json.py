"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
import json


filename = "responsible_agency.json"

with open(filename, "r") as f:    
    poss_permutations = json.load(f)

#unique_perms = list(set(poss_permutations))

perm_freq_dict = {}

for perm in poss_permutations:
    count = perm_freq_dict.get(perm, 0)
    count += 1
    perm_freq_dict[perm] = count


unique_perms = []
unique_perms_count = []
for k,v in perm_freq_dict.iteritems():
    unique_perms.append(str(k))
    unique_perms_count.append(int(v))

# truncate agency names to 20 chars:
for i in range(len(unique_perms)):
    unique_perms[i] = unique_perms[i][0:20]

# Don't allow values greater than ymax
ymax = 200
for i in range(len(unique_perms_count)):
    if unique_perms_count[i] > ymax:
        unique_perms_count[i] = ymax


print unique_perms
print unique_perms_count

unique_perms = tuple(unique_perms)

fig, ax = plt.subplots()

n_groups = len(unique_perms)
index = np.arange(n_groups)

bar_width = 0.35

opacity = 0.4

error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, unique_perms_count, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='Agency')

plt.xlabel('responsible agency')
plt.ylabel('tally')
plt.title('Tally for each responsible agency')
plt.xticks(index + bar_width, unique_perms, rotation='vertical')
plt.legend()

plt.tight_layout()
plt.show()
