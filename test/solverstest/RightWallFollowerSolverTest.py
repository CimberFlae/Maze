import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
import solvers.RightWallFollowerSolver as RightWallFollowerSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class RightWallFollowerSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        super(RightWallFollowerSolverTest, self).setUp()
        self.solver = RightWallFollowerSolver.RightWallFollowerSolver()
    
    def test_cleanPathLevel1(self):
        super(RightWallFollowerSolverTest, self).test_cleanPathLevel1()

    def test_cleanPathLevel2(self):
        super(RightWallFollowerSolverTest, self).test_cleanPathLevel2()

    def test_cleanPathLevel3(self):
        super(RightWallFollowerSolverTest, self).test_cleanPathLevel3()

    def test_solveEasyMaze(self):
        super(RightWallFollowerSolverTest, self).test_solveEasyMaze()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RightWallFollowerSolverTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
