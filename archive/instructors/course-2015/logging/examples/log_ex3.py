"""
Now lets go for broke. 

This isn't our final version but it will expose you to the settings we will be configuring there.

Steps:
    1. Set up logger's 'name'.
    2. Specify a handler (FileHandler)
    3. Specify a formatter and attach it to the handler.
    4. Add the handler to the logger 'name'.
    5. Use the logger.

"""

import logging

myloglv = logging.DEBUG

logger_name = "MY_CUSTOM_ROOT_NAME"

MY_EXAMPLE_LOGFILE_NAME = 'example.log'

mylogger = logging.getLogger(logger_name)

mylogger.setLevel(myloglv)

logger_handler = logging.FileHandler(MY_EXAMPLE_LOGFILE_NAME)

myformatter = logging.Formatter('%(asctime)s\t\t%(name)s\t\t%(levelname)s\t\t%(module)s:%(lineno)d\t\t%(message)s\t\t%(exc_info)s')
logger_handler.setFormatter(myformatter)

mylogger.addHandler(logger_handler)

try:
    potato
except Exception as myexc:
    mylogger.error("No Potato.", myexc)


