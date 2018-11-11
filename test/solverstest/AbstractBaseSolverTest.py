import unittest
import sys
import os
from abc import ABC, abstractmethod
from model.Mesh import Mesh
from model.Cell import Cell
from generators.KruskalGenerator import KruskalGenerator
from drawers.ASCIIDrawer import ASCIIDrawer
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
tc = unittest.TestCase('__init__')


class AbstractBaseSolverTest(ABC):
    
    @abstractmethod
    def setUp(self):
        self.cell1 = Cell(1, 1, 1)
        self.cell2 = Cell(2, 2, 2)
        self.cell3 = Cell(3, 3, 3)
        self.cell4 = Cell(4, 4, 4)
        self.cell5 = Cell(5, 5, 5)
        self.cell6 = Cell(6, 6, 6)
        self.cell7 = Cell(7, 7, 7)
        self.cell8 = Cell(8, 8, 8)
        self.cell9 = Cell(9, 9, 9)
        pass
    
    # check correctness and completeness of __clean_path__
    def test_clean_path_level1(self):
        self.log.debug("test_clean_path_level1")
        self.solver.path = [self.cell1, self.cell2, self.cell1]
        self.solver.__clean_path__()
        tc.assertEqual(len(self.solver.path), 1)
        self.solver.path = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell3,
                            self.cell5, self.cell6]
        self.solver.__clean_path__()
        tc.assertEqual(len(self.solver.path), 5)
        tc.assertEqual(self.solver.path, [self.cell1, self.cell2, self.cell3, self.cell5,
                                          self.cell6])

    def test_clean_path_level2(self):
        self.log.debug("test_clean_path_level2")
        self.solver.path = [self.cell1, self.cell2, self.cell3, self.cell2, self.cell1]
        self.solver.__clean_path__()
        tc.assertEqual(len(self.solver.path), 1)
        self.solver.path = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5,
                            self.cell6, self.cell5, self.cell4, self.cell7, self.cell8]
        self.solver.__clean_path__()
        tc.assertEqual(len(self.solver.path), 6)
        tc.assertEqual(self.solver.path, [self.cell1, self.cell2, self.cell3, self.cell4,
                                          self.cell7, self.cell8])

    def test_clean_path_level3(self):
        self.log.debug("test_clean_path_level3")
        self.solver.path = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell3,
                            self.cell2, self.cell1]
        self.solver.__clean_path__()
        tc.assertEqual(len(self.solver.path), 1)
        self.solver.path = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5,
                            self.cell6, self.cell7, self.cell6, self.cell5, self.cell4, self.cell8, self.cell9]
        self.solver.__clean_path__()
        tc.assertEqual(len(self.solver.path), 6)
        tc.assertEqual(self.solver.path,  [self.cell1, self.cell2, self.cell3, self.cell4,
                                           self.cell8, self.cell9])

    def test_no_entrance(self):
        self.log.debug("test_no_entrance")
        mesh = Mesh(5)
        mesh.exit = mesh.matrix[1][1]
        with self.assertRaises(Exception):
            self.solver.solve_maze(mesh)

    def test_no_exit(self):
        self.log.debug("test_no_exit")
        mesh = Mesh(5)
        mesh.entrance = mesh.matrix[0][0]
        with self.assertRaises(Exception):
            self.solver.solve_maze(mesh)

    def test_solve_easy_maze(self):
        self.log.debug("test_solve_easy_maze")
        mesh = Mesh(2)
        # Openings
        mesh.matrix[0][0].topWall.removed = True
        mesh.matrix[1][1].rightWall.removed = True
        mesh.entrance = mesh.matrix[0][0]
        mesh.exit = mesh.matrix[1][1]
        # Maze
        mesh.matrix[0][0].rightWall.removed = True
        mesh.matrix[0][1].bottomWall.removed = True
        expected_path = [mesh.matrix[0][0], mesh.matrix[0][1], mesh.matrix[1][1]]
        actual_path = self.solver.solve_maze(mesh)
        tc.assertEqual(actual_path, expected_path)

    def test_solve_medium_maze(self):
        self.log.debug("test_solve_medium_maze")
        mesh = Mesh(3)
        # Openings
        mesh.matrix[0][0].topWall.removed = True
        mesh.matrix[2][2].rightWall.removed = True
        mesh.entrance = mesh.matrix[0][0]
        mesh.exit = mesh.matrix[2][2]
        # Maze
        mesh.matrix[0][0].bottomWall.removed = True
        mesh.matrix[0][1].bottomWall.removed = True
        mesh.matrix[0][2].bottomWall.removed = True
        mesh.matrix[1][0].rightWall.removed = True
        mesh.matrix[1][1].rightWall.removed = True
        mesh.matrix[1][1].bottomWall.removed = True
        mesh.matrix[2][0].rightWall.removed = True
        mesh.matrix[2][1].rightWall.removed = True
        expected_path = [mesh.matrix[0][0], mesh.matrix[1][0], mesh.matrix[1][1], mesh.matrix[2][1],
                         mesh.matrix[2][2]]
        actual_path = self.solver.solve_maze(mesh)
        tc.assertEqual(actual_path, expected_path)

    def test_solve_hard_maze(self):
        self.log.debug("test_solve_hard_maze")
        mesh = Mesh(4)
        # Openings
        mesh.matrix[0][2].topWall.removed = True
        mesh.matrix[1][3].rightWall.removed = True
        mesh.entrance = mesh.matrix[0][2]
        mesh.exit = mesh.matrix[1][3]
        # Maze
        mesh.matrix[0][0].rightWall.removed = True
        mesh.matrix[0][1].bottomWall.removed = True
        mesh.matrix[0][1].rightWall.removed = True
        mesh.matrix[0][3].bottomWall.removed = True
        mesh.matrix[1][0].bottomWall.removed = True
        mesh.matrix[1][0].rightWall.removed = True
        mesh.matrix[1][2].bottomWall.removed = True
        mesh.matrix[1][2].rightWall.removed = True
        mesh.matrix[2][0].rightWall.removed = True
        mesh.matrix[2][1].bottomWall.removed = True
        mesh.matrix[2][2].rightWall.removed = True
        mesh.matrix[2][3].bottomWall.removed = True
        mesh.matrix[3][0].rightWall.removed = True
        mesh.matrix[3][1].rightWall.removed = True
        mesh.matrix[3][2].rightWall.removed = True
        expected_path = [mesh.matrix[0][2], mesh.matrix[0][1], mesh.matrix[1][1],
                         mesh.matrix[1][0], mesh.matrix[2][0], mesh.matrix[2][1], mesh.matrix[3][1],
                         mesh.matrix[3][2], mesh.matrix[3][3], mesh.matrix[2][3], mesh.matrix[2][2],
                         mesh.matrix[1][2], mesh.matrix[1][3]]
        actual_path = self.solver.solve_maze(mesh)
        tc.assertEqual(actual_path, expected_path)

    def test_path(self):
        self.log.debug("test_path")
        generator = KruskalGenerator()
        maze = generator.generate_random_maze(10, 23)
        drawer = ASCIIDrawer()
        drawer.draw_maze(maze)
        path = self.solver.solve_maze(maze)
        # Check if first cell is entry
        tc.assertEqual(path[0], maze.get_entrance())
        # Check if last cell is exit
        tc.assertEqual(path[-1], maze.get_exit())
        # Check if every cell transition is allowed (not through a wall)
        for i in range(0, len(path)-1):
            cell1 = path[i]
            x1 = cell1.get_x()
            y1 = cell1.get_y()
            cell2 = path[i+1]
            x2 = cell2.get_x()
            y2 = cell2.get_y()
            if x1 < x2:
                tc.assertTrue(cell1.get_bottom().is_removed())
                tc.assertTrue(cell2.get_top().is_removed())
            if x1 > x2:
                tc.assertTrue(cell1.get_top().is_removed())
                tc.assertTrue(cell2.get_bottom().is_removed())
            if y1 < y2:
                tc.assertTrue(cell1.get_right().is_removed())
                tc.assertTrue(cell2.get_left().is_removed())
            if y1 > y2:
                tc.assertTrue(cell1.get_left().is_removed())
                tc.assertTrue(cell2.get_right().is_removed())
