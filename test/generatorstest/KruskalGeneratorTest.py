import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import generators.KruskalGenerator as KruskalGenerator
import generatorstest.AbstractBaseGeneratorTest as AbstractBaseGeneratorTest

class KruskalGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest,  unittest.TestCase):
    
    def setUp(self):
        self.size = 5
        seed = 3
        generator = KruskalGenerator.KruskalGenerator()
        self.maze = generator.generateRandomMaze(self.size, seed = seed)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(KruskalGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
