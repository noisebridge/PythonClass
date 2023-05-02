"""

Our plan of attack:

1. Make a file with some test data to work with.
2. Import that file into python as a string. String type gives us an index, which we need.
3. Think about substring matching and how to find candidates to try to compress.
4. Implement a substring matching procedure, and store the output.
5. Reverse the process to 'prove' the output doesn't lose any information.


Summary:
    We are making a non-lossy (lossless) compression program/algorithm/script.

"""

filename = "sampledata.txt"

with open(filename, 'r') as f:
    contents = f.read()

for v in range(len(contents)):
    print v, contents[v]

