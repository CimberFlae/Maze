import unittest
import sys
import os
from abc import ABC, abstractmethod
import generators.KruskalGenerator as KruskalGenerator
import generators.BinaryTreeGenerator as BinaryTreeGenerator
import generators.DepthFirstSearchGenerator as DepthFirstSearchGenerator
import generators.PrimGenerator as PrimGenerator
import solvers.TremauxSolver as TremauxSolver
import filecmp
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
tc = unittest.TestCase('__init__')

class AbstractBaseDrawerTest(ABC):

    @abstractmethod
    def setUp(self):
        pass

    def test_smallMaze(self):
        generator = PrimGenerator.PrimGenerator()
        maze = generator.generateRandomMaze(3, 23)
        self.drawer.drawMaze(maze, 'test_smallMaze.txt')
        tc.assertTrue(filecmp.cmp('test_smallMaze.txt', 'test_smallMaze_expected.txt'))

    def test_mediumMaze(self):
        generator = BinaryTreeGenerator.BinaryTreeGenerator()
        maze = generator.generateRandomMaze(5, 23)
        self.drawer.drawMaze(maze, 'test_mediumMaze.txt')
        tc.assertTrue(filecmp.cmp('test_mediumMaze.txt', 'test_mediumMaze_expected.txt'))

    def test_bigMaze(self):
        generator = KruskalGenerator.KruskalGenerator()
        maze = generator.generateRandomMaze(10, 23)
        self.drawer.drawMaze(maze, 'test_bigMaze.txt')
        tc.assertTrue(filecmp.cmp('test_bigMaze.txt', 'test_bigMaze_expected.txt'))

    def test_path(self):
        generator = DepthFirstSearchGenerator.DepthFirstSearchGenerator()
        maze = generator.generateRandomMaze(10, 23)
        solver = TremauxSolver.TremauxSolver()
        path = solver.solveMaze(maze)
        self.drawer.drawPath(maze, path, 'test_path.txt')
        tc.assertTrue(filecmp.cmp('test_path.txt', 'test_path_expected.txt'))