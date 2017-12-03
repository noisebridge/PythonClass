def lowercase(string):
    return string.lower()


# Concatenate using a loop
def concat_loop(strings):
    result = ','
    for string in strings:
        result += lowercase(string)  # !
    return result


# Concatenate using string.join
def concat_join(strings):
    return ','.join([lowercase(string) for string in strings])  # !


# Read in the system dictionary and produce a comma-separated
# list of lowercase words
strings = open('/usr/share/dict/words').readlines()
concat_loop(strings)
concat_join(strings)
