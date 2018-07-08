import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import generators.RecursiveDivisionGenerator as RecursiveDivisionGenerator
import generatorstest.AbstractBaseGeneratorTest as AbstractBaseGeneratorTest

class RecursiveDivisionGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest,  unittest.TestCase):
    
    def setUp(self):
        self.size = 5
        seed = 5
        generator = RecursiveDivisionGenerator.RecursiveDivisionGenerator()
        self.maze = generator.generateRandomMaze(self.size, seed = seed)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RecursiveDivisionGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
