"""
Initializing two separate root loggers.

"""
import logging

myloglv = logging.DEBUG


mylogger = logging.getLogger('myrootlevel')

splogger = logging.getLogger('spaghettilogger')

mylogger.setLevel(myloglv)

splogger.setLevel(myloglv)

logger_handler = logging.FileHandler('example.log')

myformatter = logging.Formatter('%(asctime)s\t\t%(name)s\t\t%(levelname)s\t\t%(module)s:%(lineno)d\t\t%(message)s')
logger_handler.setFormatter(myformatter)

mylogger.addHandler(logger_handler)
splogger.addHandler(logger_handler)


splogger.debug("Spaghetti time.")

mylogger.debug("This is my first logging statement.")

logging.critical("What root name is this logged to?")


