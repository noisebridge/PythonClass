"""
    Converts a CSV file of ascii code values (integers)
    into a format readable by hackerrank question.

    hackerrank requires the first line to be N, where N equals
    the number of ascii characters, followed by all ascii codes
    space separated.

"""
import csv
inFilename = 'test_data.csv'
outFilename = 'test_data.txt'

length = 0
outData = ''
with open(inFilename, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        outData += ' '.join(row)
        length += len(row)

with open(outFilename, 'w') as file:
    file.write(str(length) + '\n')
    file.write(outData)
