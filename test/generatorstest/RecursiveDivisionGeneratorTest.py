import unittest
import sys
import os
from generators.RecursiveDivisionGenerator import RecursiveDivisionGenerator
from test.generatorstest.AbstractBaseGeneratorTest import AbstractBaseGeneratorTest
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


class RecursiveDivisionGeneratorTest(AbstractBaseGeneratorTest, unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.size = 5
        self.seed = 5
        self.generator = RecursiveDivisionGenerator()
        self.maze = self.generator.generate_random_maze(self.size, seed=self.seed)

    def test_invalid_size(self):
        self.log.debug("test_invalid_size")
        generator = RecursiveDivisionGenerator()
        with self.assertRaises(Exception):
            self.maze = generator.generate_random_maze(1)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RecursiveDivisionGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
