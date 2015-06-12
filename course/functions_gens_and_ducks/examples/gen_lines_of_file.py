"""utility functions to read in and parse a file efficiently
"""

def gen_file_line(text):
    with open(text) as fp:
        for line in fp:
            yield line