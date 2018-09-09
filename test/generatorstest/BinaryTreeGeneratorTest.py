import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import generators.BinaryTreeGenerator as BinaryTreeGenerator
import generatorstest.AbstractBaseGeneratorTest as AbstractBaseGeneratorTest
import logging

class BinaryTreeGeneratorTest(AbstractBaseGeneratorTest.AbstractBaseGeneratorTest, unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.size = 5
        seed = 1
        generator = BinaryTreeGenerator.BinaryTreeGenerator()
        self.maze = generator.generateRandomMaze(self.size, seed = seed)

    def test_invalidSize(self):
        self.log.debug("test_invalidSize")
        generator = BinaryTreeGenerator.BinaryTreeGenerator()
        with self.assertRaises(Exception):
            self.maze = generator.generateRandomMaze(1)

    # check wether every cell in the maze has at least one of the left or top wall removed (except the top left cell)
    def test_cells(self):
        self.log.debug("test_cells")
        for i in range(self.size):
            for j in range(self.size):
                if i == j == 0:
                    continue
                cell = self.maze.getCell(i, j)
                self.assertFalse(not cell.getLeft().isRemoved() and not cell.getTop().isRemoved(), 'Cell still has both left and top Wall.')

    # check wether the top row has all left walls removed (except entry cell)
    def test_topRow(self):
        self.log.debug("test_topRow")
        for i in range(1, self.size):
            self.assertTrue(self.maze.getCell(0, i).getLeft().isRemoved(), 'Cell in top row still has left Wall.')

    # check wether the left row has all top walls removed (except entry cell)
    def test_leftRow(self):
        self.log.debug("test_leftRow")
        for i in range(1, self.size):
            self.assertTrue(self.maze.getCell(i, 0).getTop().isRemoved(), 'Cell in left row still has top Wall.')

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BinaryTreeGeneratorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
