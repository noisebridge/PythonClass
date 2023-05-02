"""
Example 2 is from:  https://docs.python.org/2.6/library/logging.html#simple-examples
                    https://docs.python.org/2.6/library/logging.html#rotatingfilehandler
                    
I finally got this example working by explicitly calling this function 'ex2' and explicitly calling
the submodule app.sample2 logger ex2.sample

Note that I can make the submodule 'sample' simply have the same name as the parent logger and that
will also allow logging. In that case, they are undifferentiable in the logs.

The basis of this problem with using __name__ as the logger name is running the application in
the main python namespace.  If you try run it in the main python namespace, you will find that
the child logger can't find the parent logger since the parent logger will have changed from the
module name to '__main__'

"""

import logging
import logging.handlers

import app.sample2 as sample

logfile = 'logs/example.log'
log_lv = logging.DEBUG

app_logger = logging.getLogger('ex2')
app_logger.setLevel(log_lv)
# app_logger.propagate = 1 # this is the default

#formatter = logging.Formatter('%(asctime)s\t\t%(name)s\t\t%(levelname)s\t\t%(module)s\t\t%(message)s')
formatter = logging.Formatter('%(asctime)s\t\t%(name)s\t\t%(levelname)s\t\t%(module)s:%(lineno)d\t\t%(message)s')

#logging.basicConfig(level=log_lv)

app_handler = logging.handlers.RotatingFileHandler(     logfile, 
                                                        maxBytes=4000000, 
                                                        backupCount=5  )

app_handler.setFormatter(formatter)
app_logger.addHandler(app_handler)

app_logger.debug('---Logging is live!---')
app_logger.warning('Watch out for trans fats!')
app_logger.info('Lets call a module:')

sample.main()

for i in range(5):
    app_logger.debug('range: %s' % i)



