import unittest
import sys
import os
from generators.withloops.DepthFirstSearchWithLoopsGenerator import DepthFirstSearchWithLoopsGenerator
from test.generatorstest.DepthFirstSearchGeneratorTest import DepthFirstSearchGeneratorTest
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


class DepthFirstSearchWithLoopsGeneratorTest(DepthFirstSearchGeneratorTest, unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.size = 5
        seed = 2
        generator = DepthFirstSearchWithLoopsGenerator()
        self.maze = generator.generate_random_maze(self.size, seed=seed)

    def test_invalid_size(self):
        self.log.debug("test_invalid_size")
        generator = DepthFirstSearchWithLoopsGenerator()
        with self.assertRaises(Exception):
            self.maze = generator.generate_random_maze(1)


# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DepthFirstSearchWithLoopsGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
