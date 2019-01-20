import unittest
import sys
import os
from abc import ABC, abstractmethod
from drawers.ASCIIDrawer import ASCIIDrawer
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
tc = unittest.TestCase('__init__')


class AbstractBaseGeneratorTest(ABC):
    
    @abstractmethod
    def setUp(self):
        pass
    
    # check whether the maze has a valid entry point
    def test_valid_entry(self):
        self.log.debug("test_valid_entry")
        entry = self.maze.get_entrance()
        tc.assertIsNotNone(entry, 'Entry is None.')
        tc.assertTrue(entry.get_x() == 0 or entry.get_y() == 0,
                      'Entry is neither on the left nor on top side of the Maze')
        
    # check whether the maze has only one entry point
    def test_one_entry(self):
        self.log.debug("test_one_entry")
        entries = 0
        for i in range(self.size):
            cell = self.maze.get_cell(i, 0)
            if cell.get_left().is_removed():
                entries += 1
            cell = self.maze.get_cell(0, i)
            if cell.get_top().is_removed():
                entries += 1
        drawer = ASCIIDrawer()
        drawer.draw_maze(self.maze)
        tc.assertEqual(entries, 1, 'There is more than one entry')
    
    # check whether the maze has a valid exit point
    def test_valid_exit(self):
        self.log.debug("test_valid_exit")
        maze_exit = self.maze.get_exit()
        tc.assertIsNotNone(maze_exit, 'Exit is None.')
        tc.assertTrue(maze_exit.get_x() == self.size - 1 or maze_exit.get_y() == self.size - 1,
                      'Exit is neither on the right nor on the bottom side of the Maze')
    
    # check whether the maze has only one exit point
    def test_one_exit(self):
        self.log.debug("test_one_exit")
        exits = 0
        for i in range(self.size):
            cell = self.maze.get_cell(i, self.size - 1)
            if cell.get_right().is_removed():
                exits += 1
            cell = self.maze.get_cell(self.size - 1, i)
            if cell.get_bottom().is_removed():
                exits += 1
        tc.assertEqual(exits, 1, 'There is more than one exit')
