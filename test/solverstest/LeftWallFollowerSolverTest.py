import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import solvers.LeftWallFollowerSolver as LeftWallFollowerSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class LeftWallFollowerSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        super(LeftWallFollowerSolverTest, self).setUp()
        self.solver = LeftWallFollowerSolver.LeftWallFollowerSolver()

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LeftWallFollowerSolverTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
