print dir()

import os
#print os.environ


dirname = os.path.dirname(__file__)
print os.listdir(dirname)

filen = os.path.join(dirname, 'new.txt')

f = open(filen, 'wt')
try:
    f.write('example file')
finally:
    f.close()

print os.listdir(dirname)