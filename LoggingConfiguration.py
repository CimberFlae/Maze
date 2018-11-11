import logging
import logging.config


class LoggingConfiguration(logging.Filter):
    pass


LOGGING = {
    'version': 1,
    'formatters': {
        'tests': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)s %(levelname)s: %(message)s'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'maze.log',
            'mode': 'w',
            'formatter': 'tests'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    },
}

if __name__ == '__main__':
    logging.config.dictConfig(LOGGING)