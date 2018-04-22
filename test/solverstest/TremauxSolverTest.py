import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
import solvers.TremauxSolver as TremauxSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class TremauxSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        super(TremauxSolverTest, self).setUp()
        self.solver = TremauxSolver.TremauxSolver()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TremauxSolverTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
