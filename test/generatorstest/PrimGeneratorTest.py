import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import generators.PrimGenerator as PrimGenerator
import generatorstest.AbstractBaseGeneratorTest as AbstractBaseGeneratorTest

class PrimGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest,  unittest.TestCase):
    
    def setUp(self):
        self.size = 5
        seed = 4
        generator = PrimGenerator.PrimGenerator()
        self.maze = generator.generateRandomMaze(self.size, seed = seed)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PrimGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
