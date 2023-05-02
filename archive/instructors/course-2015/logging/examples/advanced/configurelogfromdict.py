"""
This uses a json file as a config file, which is loaded
as a Python dict().  The result is a fully configured
logger.

Also note that the encoding specified in the config file
is UTF-8. I am not sure if this need to be specified in 
some environments, but I didn't need it on Ubuntu 14.04.
"""

import json
import logging
import logging.config

logger = logging.getLogger('ex4')


log_config_filename = "configs/logconfig.json"

# The JSON object is loaded as a dict
with open(log_config_filename, 'r') as f:
    logconfig = json.load(f)

# Configure using the dict
logging.config.dictConfig(logconfig)

logger.info(u"It works!  Here's some unicode: \xc3\xb4")
