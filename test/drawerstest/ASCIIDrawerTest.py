import unittest
import sys
import os
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import drawers.ASCIIDrawer as ASCIIDrawer
import test.drawerstest.AbstractBaseDrawerTest as AbstractBaseDrawerTest

class ASCIIDrawerTest(AbstractBaseDrawerTest.AbstractBaseDrawerTest, unittest.TestCase):

    def setUp(self):
        super(ASCIIDrawerTest, self).setUp()
        self.log = logging.getLogger(__name__)
        self.drawer = ASCIIDrawer.ASCIIDrawer()

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ASCIIDrawerTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
