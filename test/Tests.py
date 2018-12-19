import os
import sys
import unittest
import LoggingConfiguration
import logging.config

logging.config.dictConfig(LoggingConfiguration.LOGGING)

suite = unittest.TestLoader().discover(os.path.dirname(os.path.abspath(__file__)), pattern='*Test.py')
result = not unittest.TextTestRunner().run(suite).wasSuccessful()
sys.exit(result)
