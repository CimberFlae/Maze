import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import generators.PrimGenerator as PrimGenerator
import generatorstest.AbstractBaseGeneratorTest as AbstractBaseGeneratorTest
import logging

class PrimGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest,  unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.size = 5
        seed = 4
        generator = PrimGenerator.PrimGenerator()
        self.maze = generator.generateRandomMaze(self.size, seed = seed)

    def test_invalidSize(self):
        self.log.debug("test_invalidSize")
        generator = PrimGenerator.PrimGenerator()
        with self.assertRaises(Exception):
            generator.generateRandomMaze(1)

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PrimGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
