
import json

config_dict = {
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'precise': {
            'format': '%(asctime)s\t\t%(name)s\t\t%(levelname)s\t\t%(module)s:%(lineno)d\t\t%(message)s'
        },
    },
    'handlers': {
        'file': {
            'level':'DEBUG',   
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/example.log',
            'maxBytes': 1000000,
            'backupCount': 5,
            'formatter': 'precise',
            'encoding' : 'UTF-8'
        },  
    },
    'loggers': {
        '': {                  
            'handlers': ['file'], 
            'level': 'DEBUG',
            'propagate': True
        }
    }
} 

with open('logconfig.json', 'w') as f:
    json.dump(config_dict, f)
