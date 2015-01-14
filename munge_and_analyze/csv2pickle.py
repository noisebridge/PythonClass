"""
A simple little snippet that will:
1. import a csv file - the file must be a single row of comma-separated values.
2. import the row to a single dimensional list.
3. pickle the list and dump it to a pickle file.
"""

import pickle
import csv

mode = 'r'
input_filename = 'ngsl1.01.csv'
output_filename = 'ngsl.pickle'

wordslist = []
with open(input_filename, mode) as f:
    words = csv.reader(f)

    print words
    for row in words:
        wordslist = row

print wordslist

mode = 'wb'
with open(output_filename, mode) as f:
    pickle.dump(wordslist, f)

