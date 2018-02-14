import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
import solvers.TremauxSolver as TremauxSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class TremauxSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        self.solver = TremauxSolver.TremauxSolver()
    
    def test_cleanPathLevel1(self):
        super(TremauxSolverTest, self).test_cleanPathLevel1()

    def test_cleanPathLevel2(self):
        super(TremauxSolverTest, self).test_cleanPathLevel2()

    def test_cleanPathLevel3(self):
        super(TremauxSolverTest, self).test_cleanPathLevel3()

    def test_solveMaze(self):
        super(TremauxSolverTest, self).test_solveMaze()
    
suite = unittest.TestLoader().loadTestsFromTestCase(TremauxSolverTest)
unittest.TextTestRunner(verbosity=2).run(suite)
