import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
import solvers.RandomMouseSolver as RandomMouseSolver
import solverstest.AbstractBaseSolverTest as AbstractBaseSolverTest

class RandomMouseSolverTest(AbstractBaseSolverTest.AbstractBaseSolverTest, unittest.TestCase):
    
    def setUp(self):
        self.solver = RandomMouseSolver.RandomMouseSolver()
    
    def test_cleanPathLevel1(self):
        super(RandomMouseSolverTest, self).test_cleanPathLevel1()

    def test_cleanPathLevel2(self):
        super(RandomMouseSolverTest, self).test_cleanPathLevel2()

    def test_cleanPathLevel3(self):
        super(RandomMouseSolverTest, self).test_cleanPathLevel3()

    def test_solveMaze(self):
        super(RandomMouseSolverTest, self).test_solveMaze()
    
suite = unittest.TestLoader().loadTestsFromTestCase(RandomMouseSolverTest)
unittest.TextTestRunner(verbosity=2).run(suite)
