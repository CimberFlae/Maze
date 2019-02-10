import unittest
import sys
import os
from generators.DepthFirstSearchGenerator import DepthFirstSearchGenerator
from test.generatorstest.AbstractBaseGeneratorTest import AbstractBaseGeneratorTest
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


class DepthFirstSearchGeneratorTest(AbstractBaseGeneratorTest, unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.size = 5
        self.seed = 2
        self.generator = DepthFirstSearchGenerator()
        self.maze = self.generator.generate_random_maze(self.size, seed=self.seed)

    def test_invalid_size(self):
        self.log.debug("test_invalid_size")
        generator = DepthFirstSearchGenerator()
        with self.assertRaises(Exception):
            self.maze = generator.generate_random_maze(1)


# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DepthFirstSearchGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
