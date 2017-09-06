import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import generators.BinaryTreeGenerator as BinaryTreeGenerator

class BinaryTreeGeneratorTest(unittest.TestCase):
    
    def setUp(self):
        self.size = 5
        generator = BinaryTreeGenerator.BinaryTreeGenerator()
        self.maze = generator.generateMaze(self.size)
    
    # check wether the maze has a valid entry point
    def test_entry(self):
        entry = self.maze.getEntrance()
        self.assertIsNotNone(entry)
        self.assertEqual(entry.getX(), 0)
        self.assertEqual(entry.getY(), 0)
        
    # check wether the maze has a valid exit point
    def test_exit(self):
        exit = self.maze.getExit()
        self.assertIsNotNone(exit)
        self.assertEqual(exit.getX(), self.size-1)
        self.assertEqual(exit.getY(), self.size-1)
        
    # check wether every cell in the maze has either the left wall or the top wall removed
    def test_cells(self):
        for i in range(self.size):
            for j in range(self.size):
                cell = self.maze.getCell(i, j)
                self.assertNotEqual(cell.getLeft().isRemoved, cell.getTop().isRemoved)
                
    # check wether the top row has all left walls removed (except entry cell)
    def test_topRow(self):
        for i in range(1, self.size):
            self.assertTrue(self.maze.getCell(0, i).getLeft().isRemoved)
            
    # check wether the left row has all top walls removed (except entry cell)
    def test_leftRow(self):
        for i in range(1, self.size):
            self.assertTrue(self.maze.getCell(i, 0).getTop().isRemoved)
    
if __name__ == '__main__':
    unittest.main()
