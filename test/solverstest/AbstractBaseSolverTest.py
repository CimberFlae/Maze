import unittest
import sys
import os
from abc import ABC, abstractmethod
import model.Mesh as Mesh
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
tc = unittest.TestCase('__init__')

class AbstractBaseSolverTest(ABC):
    
    @abstractmethod
    def setUp(self):
        pass
    
    # check correctness and completeness of cleanPath
    def test_cleanPathLevel1(self):
        self.solver.path = ['->', '<-']
        self.solver.cleanPath()
        tc.assertEmpty(self.solver.path)
        self.solver.path = ['^', '<-', 'v', '^', '^', '->']
        self.solver.cleanPath()
        tc.assertEquals(len(self.solver.path), 4)
        tc.assertEquals(self.solver.path, ['^', '<-', '^', '->'])

    def test_cleanPathLevel2(self):
        self.solver.path = ['<-', 'v', '^', '->']
        self.solver.cleanPath()
        tc.assertEmpty(self.solver.path)
        self.solver.path = ['v', '->', '^', '->', '^', 'v', '<-', '^', '^']
        tc.assertEquals(len(self.solver.path), 5)
        tc.assertEquals(self.solver.path,  ['v', '->', '^', '^', '^'])

    def test_cleanPathLevel3(self):
        self.solver.path = ['<-', '<-', 'v', '^', '->', '->']
        self.solver.cleanPath()
        tc.assertEmpty(self.solver.path)
        self.solver.path = ['v', '->', '^', '->', '^', '<-', '->', 'v', '<-', '^', '^']
        tc.assertEquals(len(self.solver.path), 5)
        tc.assertEquals(self.solver.path,  ['v', '->', '^', '^', '^'])

    def test_solveMaze(self):
        mesh = Mesh.Mesh(4)
        # Openings
        mesh.matrix[0][2].topWall.removed = True
        mesh.matrix[1][3].rightWall.removed = True
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
        expectedPath = ['v', '<-', 'v', '<-', 'v', '->', 'v', '->', '->', '^', '<-', '^', '->', '->']
        actualPath = self.solver.solveMaze(mesh)
        tc.assertEquals(actualPath, expectedPath)
