import unittest
import sys
import os
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import solvers.RandomMouseSolver as RandomMouseSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class RandomMouseSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        super(RandomMouseSolverTest, self).setUp()
        self.log = logging.getLogger(__name__)
        self.solver = RandomMouseSolver.RandomMouseSolver()

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RandomMouseSolverTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
