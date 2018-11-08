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
        self.log.debug("test_validEntry")
        entry = self.maze.getEntrance()
        tc.assertIsNotNone(entry, 'Entry is None.')
        tc.assertTrue(entry.get_x() == 0 or entry.get_y() == 0, 'Entry is neither on the left nor on top side of the Maze')
        
    # check wether the maze has only one entry point
    def test_oneEntry(self):
        self.log.debug("test_oneEntry")
        entries = 0
        for i in range(self.size):
            cell = self.maze.get_cell(i, 0)
            if cell.get_left().isRemoved():
               entries += 1
            cell = self.maze.get_cell(0, i)
            if cell.get_top().isRemoved():
                entries += 1
        tc.assertEqual(entries, 1, 'There are more than one entry')
    
    # check wether the maze has a valid exit point
    def test_validExit(self):
        self.log.debug("test_validExit")
        exit = self.maze.getExit()
        tc.assertIsNotNone(exit, 'Exit is None.')
        tc.assertTrue(exit.get_x() == self.size - 1 or exit.get_y() == self.size - 1, 'Exit is neither on the right nor on the bottom side of the Maze')
    
    # check wether the maze has only one exit point
    def test_oneExit(self):
        self.log.debug("test_oneExit")
        exits = 0
        for i in range(self.size):
            cell = self.maze.get_cell(i, self.size - 1)
            if cell.get_right().isRemoved():
               exits += 1
            cell = self.maze.get_cell(self.size - 1, i)
            if cell.get_bottom().isRemoved():
                exits += 1
        tc.assertEqual(exits, 1, 'There are more than one exit')
