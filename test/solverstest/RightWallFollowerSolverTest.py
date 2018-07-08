import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import solvers.RightWallFollowerSolver as RightWallFollowerSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class RightWallFollowerSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        super(RightWallFollowerSolverTest, self).setUp()
        self.solver = RightWallFollowerSolver.RightWallFollowerSolver()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RightWallFollowerSolverTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
