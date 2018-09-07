import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import generators.RecursiveDivisionGenerator as RecursiveDivisionGenerator
import generatorstest.AbstractBaseGeneratorTest as AbstractBaseGeneratorTest
import logging

class RecursiveDivisionGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest,  unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.size = 5
        seed = 5
        generator = RecursiveDivisionGenerator.RecursiveDivisionGenerator()
        self.maze = generator.generateRandomMaze(self.size, seed = seed)

    def test_invalidSize(self):
        generator = RecursiveDivisionGenerator.RecursiveDivisionGenerator()
        with self.assertRaises(Exception):
            self.maze = generator.generateRandomMaze(1)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RecursiveDivisionGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
