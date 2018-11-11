import unittest
import sys
import os
from generators.KruskalGenerator import KruskalGenerator
from test.generatorstest.AbstractBaseGeneratorTest import AbstractBaseGeneratorTest
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


class KruskalGeneratorTest(AbstractBaseGeneratorTest, unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.size = 5
        seed = 3
        generator = KruskalGenerator()
        self.maze = generator.generate_random_maze(self.size, seed=seed)

    def test_invalid_size(self):
        self.log.debug("test_invalid_size")
        generator = KruskalGenerator()
        with self.assertRaises(Exception):
            self.maze = generator.generate_random_maze(1)


# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(KruskalGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
