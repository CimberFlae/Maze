import unittest
import sys
import os
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import solvers.RightWallFollowerSolver as RightWallFollowerSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class RightWallFollowerSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        super(RightWallFollowerSolverTest, self).setUp()
        self.log = logging.getLogger(__name__)
        self.solver = RightWallFollowerSolver.RightWallFollowerSolver()

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RightWallFollowerSolverTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
