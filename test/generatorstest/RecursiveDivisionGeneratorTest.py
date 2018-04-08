import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
import generators.RecursiveDivisionGenerator as RecursiveDivisionGenerator
import generatorstest.AbstractBaseGeneratorTest as AbstractBaseGeneratorTest

class RecursiveDivisionGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest,  unittest.TestCase):
    
    def setUp(self):
        self.size = 5
        seed = 5
        generator = RecursiveDivisionGenerator.RecursiveDivisionGenerator()
        self.maze = generator.generateRandomMaze(self.size, seed = seed)
    
    def test_validEntry(self):
        super(RecursiveDivisionGeneratorTest, self).test_validEntry()
        
    def test_oneEntry(self):
        super(RecursiveDivisionGeneratorTest, self).test_oneEntry()
        
    def test_validExit(self):
        super(RecursiveDivisionGeneratorTest, self).test_validExit()
        
    def test_oneExit(self):
        super(RecursiveDivisionGeneratorTest, self).test_oneExit()

suite = unittest.TestLoader().loadTestsFromTestCase(RecursiveDivisionGeneratorTest)
unittest.TextTestRunner(verbosity=2).run(suite)
