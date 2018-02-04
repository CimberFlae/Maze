import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
import generators.DepthFirstSearchGenerator as DepthFirstSearchGenerator
import generatorstest.AbstractBaseGeneratorTest as AbstractBaseGeneratorTest

class DepthFirstSearchGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest,  unittest.TestCase):
    
    def setUp(self):
        self.size = 5
        generator = DepthFirstSearchGenerator.DepthFirstSearchGenerator()
        self.maze = generator.generateRandomMaze(self.size)
    
    def test_validEntry(self):
        super(DepthFirstSearchGeneratorTest, self).test_validEntry()
        
    def test_oneEntry(self):
        super(DepthFirstSearchGeneratorTest, self).test_oneEntry()
        
    def test_validExit(self):
        super(DepthFirstSearchGeneratorTest, self).test_validExit()
        
    def test_oneExit(self):
        super(DepthFirstSearchGeneratorTest, self).test_oneExit()

suite = unittest.TestLoader().loadTestsFromTestCase(DepthFirstSearchGeneratorTest)
unittest.TextTestRunner(verbosity=2).run(suite)
