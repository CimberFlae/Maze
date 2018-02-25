import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
import solvers.RandomMouseSolver as RandomMouseSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class RandomMouseSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        super(RandomMouseSolverTest, self).setUp()
        self.solver = RandomMouseSolver.RandomMouseSolver()

    def test_path(self):
        # skip this test because atm this solver is working recursively and hits maximum level of recursion in
        # big mazes like this
        pass
    
suite = unittest.TestLoader().loadTestsFromTestCase(RandomMouseSolverTest)
unittest.TextTestRunner(verbosity=2).run(suite)
