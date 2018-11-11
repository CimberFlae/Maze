import unittest
import sys
import os
import logging
from solvers.LeftWallFollowerSolver import LeftWallFollowerSolver
from test.solverstest.AbstractBaseSolverTest import AbstractBaseSolverTest
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


class LeftWallFollowerSolverTest(AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        super(LeftWallFollowerSolverTest, self).setUp()
        self.log = logging.getLogger(__name__)
        self.solver = LeftWallFollowerSolver()


# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LeftWallFollowerSolverTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
