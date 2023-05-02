"""
Problem: Our "The Beatles" mp3 files are not named consistently.

Goal: Name our "The Beatles" mp3s consistently.

Steps:
    1. Identify inconsistently named "The Beatles" mp3s with regexes.
    2. Replace the inconsistent naming with consistent naming.
    3. Actually change the filenames (we won't do this).

Step 1 requires regular expressions, so lets focus on that.
    1. Find common patterns in the broadest sample you could.
    2. What are the broad strokes in "the beatles" --> 'the beatles', 'beatles', 'the'


"""

# Make a list of sample alternate spellings.
filenames_from_mydirectory = ["Oasis", "the beatles", "The Beatles", "Beatles, The", "the-beatles", "Tje beatjes"]

import re

# This is our regular expression string.
our_regular_exp = r'.*(beat.es).*'

# This is our regular expression object (re)
myregexp = re.compile(our_regular_exp, re.IGNORECASE)


for filename in filenames_from_mydirectory:
    filename_match = myregexp.match(filename)
    if filename_match:
        print filename_match.group()






