import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import generators.DepthFirstSearchGenerator as DepthFirstSearchGenerator
import generatorstest.AbstractBaseGeneratorTest as AbstractBaseGeneratorTest

class DepthFirstSearchGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest,  unittest.TestCase):
    
    def setUp(self):
        self.size = 5
        seed = 2
        generator = DepthFirstSearchGenerator.DepthFirstSearchGenerator()
        self.maze = generator.generateRandomMaze(self.size, seed = seed)

    def test_invalidSize(self):
        generator = DepthFirstSearchGenerator.DepthFirstSearchGenerator()
        with self.assertRaises(Exception):
            self.maze = generator.generateRandomMaze(1)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DepthFirstSearchGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
