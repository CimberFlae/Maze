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
        self.maze = generator.generateMaze(self.size)
    
    # check wether the maze has a valid entry point
    def test_entry(self):
        super(BinaryTreeGeneratorTest, self).test_entry()
        
    # check wether the maze has a valid exit point
    def test_exit(self):
        super(BinaryTreeGeneratorTest, self).test_exit()
        
    # check wether every cell in the maze has either the left wall or the top wall removed
    def test_cells(self):
        super(BinaryTreeGeneratorTest, self).test_cells()
                
    # check wether the top row has all left walls removed (except entry cell)
    def test_topRow(self):
        super(BinaryTreeGeneratorTest, self).test_topRow()
        
    # check wether the left row has all top walls removed (except entry cell)
    def test_leftRow(self):
        super(BinaryTreeGeneratorTest, self).test_leftRow()
        
if __name__ == '__main__':
    unittest.main()
