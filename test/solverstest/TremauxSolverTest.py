import unittest
import sys
import os
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
print(sys.path)
import solvers.TremauxSolver as TremauxSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class TremauxSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        super(TremauxSolverTest, self).setUp()
        self.log = logging.getLogger(__name__)
        self.solver = TremauxSolver.TremauxSolver()

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TremauxSolverTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
