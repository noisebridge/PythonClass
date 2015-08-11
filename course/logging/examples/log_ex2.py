"""
This slight modification of example 1 introduces logging to a file.
"""

import logging

# Eventually move to a configuration file with SafeConfigParser
LOG_FILENAME = 'ex1.log'
LOG_LEVEL = 'ERROR'

logging.basicConfig(filename=LOG_FILENAME, level=LOG_LEVEL)

logging.debug("This is a string that we want to log.")
logging.info("info: this string is cool.")


"""
# Now we just read the file back to ourselves to confirm it worked.
with open('ex1.log', 'r') as f:
    print f.read()
"""
