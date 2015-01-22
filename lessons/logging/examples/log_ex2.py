"""
This slight modification of example 1 introduces logging to a file.
"""

import logging

logging.basicConfig(filename='ex1.log', level='DEBUG')

logging.debug("This is a string that we want to log.")
logging.info("info: this string is cool.")


# Now we just read the file back to ourselves to confirm it worked.
with open('ex1.log', 'r') as f:
    print f.read()

