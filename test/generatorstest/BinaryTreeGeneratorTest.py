import unittest
import sys
import os
from generators.BinaryTreeGenerator import BinaryTreeGenerator
from test.generatorstest.AbstractBaseGeneratorTest import AbstractBaseGeneratorTest
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


class BinaryTreeGeneratorTest(AbstractBaseGeneratorTest, unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.size = 5
        self.seed = 1
        self.generator = BinaryTreeGenerator()
        self.maze = self.generator.generate_random_maze(self.size, seed=self.seed)

    def test_invalid_size(self):
        self.log.debug("test_invalid_size")
        generator = BinaryTreeGenerator()
        with self.assertRaises(Exception):
            self.maze = generator.generate_random_maze(1)

    # check whether every cell in the maze has at least one of the left or top wall removed (except the top left cell)
    def test_cells(self):
        self.log.debug("test_cells")
        for i in range(self.size):
            for j in range(self.size):
                if i == j == 0:
                    continue
                cell = self.maze.get_cell(i, j)
                self.assertFalse(not cell.get_left().is_removed() and not cell.get_top().is_removed(),
                                 'Cell still has both left and top Wall.')

    # check whether the top row has all left walls removed (except entry cell)
    def test_top_row(self):
        self.log.debug("test_top_row")
        for i in range(1, self.size):
            self.assertTrue(self.maze.get_cell(0, i).get_left().is_removed(), 'Cell in top row still has left Wall.')

    # check whether the left row has all top walls removed (except entry cell)
    def test_left_row(self):
        self.log.debug("test_left_row")
        for i in range(1, self.size):
            self.assertTrue(self.maze.get_cell(i, 0).get_top().is_removed(), 'Cell in left row still has top Wall.')


# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BinaryTreeGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
