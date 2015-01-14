"""
Example 1 is from https://docs.python.org/2/howto/logging.html#logging-to-a-file
"""

import logging

logfile = 'example.log'
log_lv = logging.DEBUG

log_to_file = False

if log_to_file is True:
    logging.basicConfig(filename=logfile, level=log_lv)
else:
    logging.basicConfig(level=log_lv)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

if log_to_file is True:
    with open(logfile, 'r') as f:
        print f.read()

