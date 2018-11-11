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

    def test_small_maze(self):
        generator = PrimGenerator.PrimGenerator()
        maze = generator.generate_random_maze(3, 23)
        self.drawer.draw_maze(maze, 'test_small_maze.txt')
        tc.assertTrue(filecmp.cmp('test_small_maze.txt', 'test_small_maze_expected.txt'))

    def test_medium_maze(self):
        generator = BinaryTreeGenerator.BinaryTreeGenerator()
        maze = generator.generate_random_maze(5, 23)
        self.drawer.draw_maze(maze, 'test_medium_maze.txt')
        tc.assertTrue(filecmp.cmp('test_medium_maze.txt', 'test_medium_maze_expected.txt'))

    def test_big_maze(self):
        generator = KruskalGenerator.KruskalGenerator()
        maze = generator.generate_random_maze(10, 23)
        self.drawer.draw_maze(maze, 'test_big_maze.txt')
        tc.assertTrue(filecmp.cmp('test_big_maze.txt', 'test_big_maze_expected.txt'))

    def test_path(self):
        generator = DepthFirstSearchGenerator.DepthFirstSearchGenerator()
        maze = generator.generate_random_maze(10, 23)
        solver = TremauxSolver.TremauxSolver()
        path = solver.solve_maze(maze)
        self.drawer.draw_path(maze, path, 'test_path.txt')
        tc.assertTrue(filecmp.cmp('test_path.txt', 'test_path_expected.txt'))