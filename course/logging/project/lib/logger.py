"""
A logger library for add.py
"""
import logging, logging.config
import json

LOGCONFIG_FILENAME = 'logconfig.json'

add_logger = logging.getLogger(__name__)

with open(LOGCONFIG_FILENAME, 'r') as fp:
    logconfig = json.load(fp)

logging.config.dictConfig(logconfig)


# lets create a string to use as a filter
filtered_logs = __name__ + '.add_some_numbers'
# now lets add a filter
add_filter = logging.Filter(filtered_logs)
add_logger.addFilter(add_filter)
