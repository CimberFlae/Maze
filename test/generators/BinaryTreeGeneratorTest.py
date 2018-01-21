import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import generators.BinaryTreeGenerator as BinaryTreeGenerator
import AbstractBaseGeneratorTest

class BinaryTreeGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest, unittest.TestCase):
    
    def setUp(self):
        self.size = 5
        generator = BinaryTreeGenerator.BinaryTreeGenerator()
        self.maze = generator.generateRandomMaze(self.size)
    
    def test_validEntry(self):
        super(BinaryTreeGeneratorTest, self).test_validEntry()
        
    def test_oneEntry(self):
        super(BinaryTreeGeneratorTest, self).test_oneEntry()
        
    def test_validExit(self):
        super(BinaryTreeGeneratorTest, self).test_validExit()
        
    def test_oneExit(self):
        super(BinaryTreeGeneratorTest, self).test_oneExit()
        
    def test_cells(self):
        super(BinaryTreeGeneratorTest, self).test_cells()
                
    def test_topRow(self):
        super(BinaryTreeGeneratorTest, self).test_topRow()
        
    def test_leftRow(self):
        super(BinaryTreeGeneratorTest, self).test_leftRow()
        
if __name__ == '__main__':
    unittest.main()
