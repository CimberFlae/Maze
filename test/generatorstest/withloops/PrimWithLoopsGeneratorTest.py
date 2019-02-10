import unittest
import sys
import os
from generators.withloops.PrimWithLoopsGenerator import PrimWithLoopsGenerator
from test.generatorstest.PrimGeneratorTest import PrimGeneratorTest
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


class PrimWithLoopsGeneratorTest(PrimGeneratorTest, unittest.TestCase):

    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.size = 5
        self.seed = 9
        self.generator = PrimWithLoopsGenerator()
        self.maze = self.generator.generate_random_maze(self.size, seed=self.seed)

    def test_invalid_size(self):
        self.log.debug("test_invalid_size")
        generator = PrimWithLoopsGenerator()
        with self.assertRaises(Exception):
            self.maze = generator.generate_random_maze(1)


# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PrimWithLoopsGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
