import logging
import logging.config

class LoggingConfiguration(logging.Filter):
    pass

LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'maze.log',
            'mode': 'w',
            'formatter': 'detailed'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    },
}