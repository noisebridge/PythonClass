
import pickle
import csv

mode = 'r'
filename = 'ngsl1.01.csv'

wordslist = []
with open(filename, mode) as f:
    words = csv.reader(f)

    print words
    for row in words:
        wordslist = row

print wordslist

filename = 'ngsl.pickle'
mode = 'wb'
with open(filename, mode) as f:
    pickle.dump(wordslist, f)

