import unittest
import sys
import os
from abc import ABC, abstractmethod
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

class AbstractBaseGeneratorTest(ABC, unittest.TestCase):
    
    @abstractmethod
    def setUp(self):
        pass
    
    # check wether the maze has a valid entry point
    def test_entry(self):
        entry = self.maze.getEntrance()
        self.assertIsNotNone(entry, 'Entry is None.')
        self.assertEqual(entry.getX(), 0, 'Entry is not on the left side of the Maze.')
        self.assertEqual(entry.getY(), 0, 'Entry is not on the top side of the Maze.')
        
    # check wether the maze has a valid exit point
    def test_exit(self):
        exit = self.maze.getExit()
        self.assertIsNotNone(exit, 'Exit is None.')
        self.assertEqual(exit.getX(), self.size-1, 'Exit is not on the right side of the Maze.')
        self.assertEqual(exit.getY(), self.size-1, 'Exit is not on the bottom side of the Maze.')
        
    # check wether every cell in the maze has either the left wall or the top wall removed
    def test_cells(self):
        for i in range(self.size):
            for j in range(self.size):
                cell = self.maze.getCell(i, j)
                self.assertNotEqual(cell.getLeft().isRemoved, cell.getTop().isRemoved, 'Cell still has both left and top Wall.')
                
    # check wether the top row has all left walls removed (except entry cell)
    def test_topRow(self):
        for i in range(1, self.size):
            self.assertTrue(self.maze.getCell(0, i).getLeft().isRemoved, 'Cell in top row still has left Wall.')
            
    # check wether the left row has all top walls removed (except entry cell)
    def test_leftRow(self):
        for i in range(1, self.size):
            self.assertTrue(self.maze.getCell(i, 0).getTop().isRemoved, 'Cell in left row still has top Wall.')
