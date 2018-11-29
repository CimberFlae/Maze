import unittest
import sys
import os
import logging
import LoggingConfiguration
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
tc = unittest.TestCase('__init__')


class LoggingTest(unittest.TestCase):

    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("Testing logging functionality")
    
    # check if log file exists and is not empty
    def test_log(self):
        tc.assertTrue(os.path.isfile('maze.log'), 'The file "maze.log" cannot be found!')
        tc.assertNotEqual(os.stat("maze.log").st_size, 0, 'The file "maze.log" is empty!')


# This is needed for the individual execution of this test class
if __name__ == "__main__":
    logging.config.dictConfig(LoggingConfiguration.LOGGING)
    suite = unittest.TestLoader().loadTestsFromTestCase(LoggingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)