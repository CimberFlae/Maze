import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import generators.KruskalGenerator as KruskalGenerator
import generatorstest.AbstractBaseGeneratorTest as AbstractBaseGeneratorTest
import logging

class KruskalGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest,  unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.size = 5
        seed = 3
        generator = KruskalGenerator.KruskalGenerator()
        self.maze = generator.generateRandomMaze(self.size, seed = seed)

    def test_invalidSize(self):
        self.log.debug("test_invalidSize")
        generator = KruskalGenerator.KruskalGenerator()
        with self.assertRaises(Exception):
            self.maze = generator.generateRandomMaze(1)

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(KruskalGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
