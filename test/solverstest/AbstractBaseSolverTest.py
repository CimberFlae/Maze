import unittest
import sys
import os
from abc import ABC, abstractmethod
import model.Mesh as Mesh
import model.Cell as Cell
import generators.KruskalGenerator as KruskalGenerator
import drawers.ASCIIDrawer as ASCIIDrawer
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
tc = unittest.TestCase('__init__')
class AbstractBaseSolverTest(ABC):
    
    @abstractmethod
    def setUp(self):
        self.cell1 = Cell.Cell(1, 1, 1)
        self.cell2 = Cell.Cell(2, 2, 2)
        self.cell3 = Cell.Cell(3, 3, 3)
        self.cell4 = Cell.Cell(4, 4, 4)
        self.cell5 = Cell.Cell(5, 5, 5)
        self.cell6 = Cell.Cell(6, 6, 6)
        self.cell7 = Cell.Cell(7, 7, 7)
        self.cell8 = Cell.Cell(8, 8, 8)
        self.cell9 = Cell.Cell(9, 9, 9)
        pass
    
    # check correctness and completeness of __cleanPath__
    def test_cleanPathLevel1(self):
        self.log.debug("test_cleanPathLevel1")
        self.solver.path = [self.cell1, self.cell2, self.cell1]
        self.solver.__cleanPath__()
        tc.assertEqual(len(self.solver.path), 1)
        self.solver.path = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell3,
            self.cell5, self.cell6]
        self.solver.__cleanPath__()
        tc.assertEqual(len(self.solver.path), 5)
        tc.assertEqual(self.solver.path, [self.cell1, self.cell2, self.cell3, self.cell5,
            self.cell6])

    def test_cleanPathLevel2(self):
        self.log.debug("test_cleanPathLevel2")
        self.solver.path = [self.cell1, self.cell2, self.cell3, self.cell2, self.cell1]
        self.solver.__cleanPath__()
        tc.assertEqual(len(self.solver.path), 1)
        self.solver.path = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5,
            self.cell6, self.cell5, self.cell4, self.cell7, self.cell8]
        self.solver.__cleanPath__()
        tc.assertEqual(len(self.solver.path), 6)
        tc.assertEqual(self.solver.path, [self.cell1, self.cell2, self.cell3, self.cell4,
            self.cell7, self.cell8])

    def test_cleanPathLevel3(self):
        self.log.debug("test_cleanPathLevel3")
        self.solver.path = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell3,
            self.cell2, self.cell1]
        self.solver.__cleanPath__()
        tc.assertEqual(len(self.solver.path), 1)
        self.solver.path = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5,
            self.cell6, self.cell7, self.cell6, self.cell5, self.cell4, self.cell8, self.cell9]
        self.solver.__cleanPath__()
        tc.assertEqual(len(self.solver.path), 6)
        tc.assertEqual(self.solver.path,  [self.cell1, self.cell2, self.cell3, self.cell4,
            self.cell8, self.cell9])

    def test_noEntrance(self):
        self.log.debug("test_noEntrance")
        mesh = Mesh.Mesh(5)
        mesh.exit = mesh.matrix[1][1]
        with self.assertRaises(Exception):
            self.solver.solveMaze(mesh)

    def test_noExit(self):
        self.log.debug("test_noExit")
        mesh = Mesh.Mesh(5)
        mesh.entrance = mesh.matrix[0][0]
        with self.assertRaises(Exception):
            self.solver.solveMaze(mesh)

    def test_solveEasyMaze(self):
        self.log.debug("test_solveEasyMaze")
        mesh = Mesh.Mesh(2)
        # Openings
        mesh.matrix[0][0].topWall.removed = True
        mesh.matrix[1][1].rightWall.removed = True
        mesh.entrance = mesh.matrix[0][0]
        mesh.exit = mesh.matrix[1][1]
        # Maze
        mesh.matrix[0][0].rightWall.removed = True
        mesh.matrix[0][1].bottomWall.removed = True
        expectedPath = [mesh.matrix[0][0], mesh.matrix[0][1], mesh.matrix[1][1]]
        actualPath = self.solver.solveMaze(mesh)
        tc.assertEqual(actualPath, expectedPath)

    def test_solveMediumMaze(self):
        self.log.debug("test_solveMediumMaze")
        mesh = Mesh.Mesh(3)
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
        expectedPath = [mesh.matrix[0][0], mesh.matrix[1][0], mesh.matrix[1][1], mesh.matrix[2][1],
            mesh.matrix[2][2]]
        actualPath = self.solver.solveMaze(mesh)
        tc.assertEqual(actualPath, expectedPath)

    def test_solveHardMaze(self):
        self.log.debug("test_solveHardMaze")
        mesh = Mesh.Mesh(4)
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
        expectedPath = [mesh.matrix[0][2], mesh.matrix[0][1], mesh.matrix[1][1],
            mesh.matrix[1][0], mesh.matrix[2][0], mesh.matrix[2][1], mesh.matrix[3][1],
                mesh.matrix[3][2], mesh.matrix[3][3], mesh.matrix[2][3], mesh.matrix[2][2],
                    mesh.matrix[1][2], mesh.matrix[1][3]]
        actualPath = self.solver.solveMaze(mesh)
        tc.assertEqual(actualPath, expectedPath)

    def test_path(self):
        self.log.debug("test_path")
        generator = KruskalGenerator.KruskalGenerator()
        maze = generator.generate_random_maze(10, 23)
        drawer = ASCIIDrawer.ASCIIDrawer()
        drawer.draw_maze(maze)
        path = self.solver.solveMaze(maze)
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
                tc.assertTrue(cell1.get_bottom().isRemoved())
                tc.assertTrue(cell2.get_top().isRemoved())
            if x1 > x2:
                tc.assertTrue(cell1.get_top().isRemoved())
                tc.assertTrue(cell2.get_bottom().isRemoved())
            if y1 < y2:
                tc.assertTrue(cell1.get_right().isRemoved())
                tc.assertTrue(cell2.get_left().isRemoved())
            if y1 > y2:
                tc.assertTrue(cell1.get_left().isRemoved())
                tc.assertTrue(cell2.get_right().isRemoved())
