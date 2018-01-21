import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import generators.DepthFirstSearchGenerator as DepthFirstSearchGenerator
import AbstractBaseGeneratorTest

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
        
    def test_cells(self):
        super(DepthFirstSearchGeneratorTest, self).test_cells()
                
    def test_topRow(self):
        super(DepthFirstSearchGeneratorTest, self).test_topRow()
        
    def test_leftRow(self):
        super(DepthFirstSearchGeneratorTest, self).test_leftRow()

if __name__ == '__main__':
    unittest.main()
