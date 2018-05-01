import unittest
import sys
import os
from abc import ABC, abstractmethod
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
tc = unittest.TestCase('__init__')

class AbstractBaseGeneratorTest(ABC):
    
    @abstractmethod
    def setUp(self):
        pass
    
    # check wether the maze has a valid entry point
    def test_validEntry(self):
        entry = self.maze.getEntrance()
        tc.assertIsNotNone(entry, 'Entry is None.')
        tc.assertTrue(entry.getX() == 0 or entry.getY() == 0, 'Entry is neither on the left nor on top side of the Maze')
        
    # check wether the maze has only one entry point
    def test_oneEntry(self):
        entries = 0
        for i in range(self.size):
            cell = self.maze.getCell(i, 0)
            if cell.getLeft().isRemoved():
               entries += 1
            cell = self.maze.getCell(0, i)
            if cell.getTop().isRemoved():
                entries += 1
        tc.assertEqual(entries, 1, 'There are more than one entry')
    
    # check wether the maze has a valid exit point
    def test_validExit(self):
        exit = self.maze.getExit()
        tc.assertIsNotNone(exit, 'Exit is None.')
        tc.assertTrue(exit.getX() == self.size-1 or exit.getY() == self.size-1, 'Exit is neither on the right nor on the bottom side of the Maze')
    
    # check wether the maze has only one exit point
    def test_oneExit(self):
        exits = 0
        for i in range(self.size):
            cell = self.maze.getCell(i, self.size-1)
            if cell.getRight().isRemoved():
               exits += 1
            cell = self.maze.getCell(self.size-1, i)
            if cell.getBottom().isRemoved():
                exits += 1
        tc.assertEqual(exits, 1, 'There are more than one exit')
