import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import model.Wall as Wall
import logging

class WallTest(unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.wall = Wall.Wall()
        
    def test_removedInit(self):
        self.log.debug("test_removedInit")
        self.assertFalse(self.wall.removed, 'Wall is removed.')
        
    def test_remove(self):
        self.log.debug("test_remove")
        self.wall.remove()
        self.assertTrue(self.wall.removed, 'Wall is not removed.')
        
    def test_create(self):
        self.log.debug("test_create")
        self.wall.create()
        self.assertFalse(self.wall.removed, 'Wall is removed.')
        
    def test_isRemoved(self):
        self.log.debug("test_isRemoved")
        self.assertEqual(self.wall.isRemoved(), self.wall.removed, 'isRemoved returns wrong value.')

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(WallTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
