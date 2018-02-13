import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
import solvers.LeftWallFollowerSolver as LeftWallFollowerSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class LeftWallFollowerSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        self.solver = LeftWallFollowerSolver.LeftWallFollowerSolver()
    
    def test_cleanPathLevel1(self):
        super(LeftWallFollowerSolverTest, self).test_cleanPathLevel1()

    def test_cleanPathLevel2(self):
        super(LeftWallFollowerSolverTest, self).test_cleanPathLevel2()

    def test_cleanPathLevel3(self):
        super(LeftWallFollowerSolverTest, self).test_cleanPathLevel3()

    def test_solveMaze(self):
        super(LeftWallFollowerSolverTest, self).test_solveMaze()
    
suite = unittest.TestLoader().loadTestsFromTestCase(LeftWallFollowerSolverTest)
unittest.TextTestRunner(verbosity=2).run(suite)
