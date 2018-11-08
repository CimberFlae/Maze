import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import model.Cell as Cell
import model.Wall as Wall
import logging

class CellTest(unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.cell = Cell.Cell(1, 2, 3)
    
    def test_CellInit(self):
        self.log.debug("test_CellInit")
        wallList = self.cell.wallList
        self.assertEqual(len(wallList), 4, 'Did not find 4 walls.')
        for i in range(4):
            self.assertFalse(wallList[i].isRemoved())
        self.assertEqual(self.cell.leftWall, wallList[0], 'Left wall was not in first place in list.')
        self.assertEqual(self.cell.rightWall, wallList[1], 'Right wall was not in second place in list.')
        self.assertEqual(self.cell.topWall, wallList[2], 'Top wall was not in third place in list.')
        self.assertEqual(self.cell.bottomWall, wallList[3], 'Bottom wall was not in fourth place in list.')
        self.assertEqual(self.cell.x, 1, 'X-coordinate is wrong.')
        self.assertEqual(self.cell.y, 2, 'y-coordinate is wrong.')
        self.assertEqual(self.cell.set, 3, 'Set is wrong.')
    
    def test_setSet(self):
        self.log.debug("test_setSet")
        self.cell.set_set(2)
        self.assertEqual(self.cell.set, 2, 'Cell has wrong Set.')
    
    def test_getSet(self):
        self.log.debug("test_getSet")
        self.assertEqual(self.cell.set, self.cell.get_set(), 'get_set returned wrong value.')
    
    def test_getX(self):
        self.log.debug("test_getX")
        self.assertEqual(self.cell.x, self.cell.get_x(), 'get_x returned wrong value.')
    
    def test_getY(self):
        self.log.debug("test_getY")
        self.assertEqual(self.cell.y, self.cell.get_y(), 'get_y returned wrong value.')
    
    def test_getLeft(self):
        self.log.debug("test_getLeft")
        self.assertEqual(self.cell.leftWall, self.cell.get_left(), 'get_left returned wrong value.')
    
    def test_setLeft(self):
        self.log.debug("test_setLeft")
        wall = Wall.Wall()
        self.cell.set_left(wall)
        self.assertEqual(self.cell.leftWall, wall, 'Left wall is set incorrectly.')
    
    def test_getRight(self):
        self.log.debug("test_getRight")
        self.assertEqual(self.cell.rightWall, self.cell.get_right(), 'get_right returned wrong value.')
    
    def test_setRight(self):
        self.log.debug("test_setRight")
        wall = Wall.Wall()
        self.cell.set_right(wall)
        self.assertEqual(self.cell.rightWall, wall, 'Right wall is set incorrectly.')
    
    def test_getTop(self):
        self.log.debug("test_getTop")
        self.assertEqual(self.cell.topWall, self.cell.get_top(), 'get_top returned wrong value.')
    
    def test_setTop(self):
        self.log.debug("test_setTop")
        wall = Wall.Wall()
        self.cell.set_top(wall)
        self.assertEqual(self.cell.topWall, wall, 'Top wall is set incorrectly.')
    
    def test_getBottom(self):
        self.log.debug("test_getBottom")
        self.assertEqual(self.cell.bottomWall, self.cell.get_bottom(), 'get_bottom returned wrong value.')
    
    def test_setBottom(self):
        self.log.debug("test_setBottom")
        wall = Wall.Wall()
        self.cell.set_bottom(wall)
        self.assertEqual(self.cell.bottomWall, wall, 'Bottom wall is set incorrectly.')
    
    def test_removeLeft(self):
        self.log.debug("test_removeLeft")
        self.cell.remove_left()
        self.assertTrue(self.cell.leftWall.isRemoved(), 'Left wall is not removed.')
    
    def test_createLeft(self):
        self.log.debug("test_createLeft")
        self.cell.create_left()
        self.assertFalse(self.cell.leftWall.isRemoved(), 'Left wall is removed.')
    
    def test_removeRight(self):
        self.log.debug("test_removeRight")
        self.cell.remove_right()
        self.assertTrue(self.cell.rightWall.isRemoved(), 'Right wall is not removed.')
    
    def test_createRight(self):
        self.log.debug("test_createRight")
        self.cell.create_right()
        self.assertFalse(self.cell.rightWall.isRemoved(), 'Right wall is removed.')
    
    def test_removeTop(self):
        self.log.debug("test_removeTop")
        self.cell.remove_top()
        self.assertTrue(self.cell.topWall.isRemoved(), 'Top wall is not removed.')
    
    def test_createTop(self):
        self.log.debug("test_createTop")
        self.cell.create_top()
        self.assertFalse(self.cell.topWall.isRemoved(), 'Top wall is removed.')
    
    def test_removeBottom(self):
        self.log.debug("test_removeBottom")
        self.cell.remove_bottom()
        self.assertTrue(self.cell.bottomWall.isRemoved(), 'Bottom wall is not removed.')
    
    def test_createBottom(self):
        self.log.debug("test_createBottom")
        self.cell.create_bottom()
        self.assertFalse(self.cell.bottomWall.isRemoved(), 'Bottom wall is removed.')
    
    def test_hasWall(self):
        self.log.debug("test_hasWall")
        self.assertTrue(self.cell.has_wall())
        self.cell.remove_left()
        self.cell.remove_right()
        self.cell.remove_top()
        self.cell.remove_bottom()
        self.assertFalse(self.cell.has_wall(), 'Cell still has walls.')
    
    def test_wallCount(self):
        self.log.debug("test_wallCount")
        self.assertEqual(self.cell.wall_count(), 4, 'Cell does not have correct number of walls.')
        self.cell.remove_left()
        self.assertEqual(self.cell.wall_count(), 3, 'Cell does not have correct number of walls.')
        self.cell.remove_right()
        self.assertEqual(self.cell.wall_count(), 2, 'Cell does not have correct number of walls.')
        self.cell.remove_top()
        self.assertEqual(self.cell.wall_count(), 1, 'Cell does not have correct number of walls.')
        self.cell.remove_bottom()
        self.assertEqual(self.cell.wall_count(), 0, 'Cell does not have correct number of walls.')
    
    def test_chooseWallSuccess(self):
        self.log.debug("test_chooseWallSuccess")
        wall = self.cell.choose_wall()
        self.assertFalse(wall.isRemoved(), 'Removed wall has been chosen.')
        
    def test_chooseWallFail(self):
        self.log.debug("test_chooseWallFail")
        self.cell.remove_left()
        self.cell.remove_right()
        self.cell.remove_top()
        self.cell.remove_bottom()
        wall = self.cell.choose_wall()
        self.assertIsNone(wall, 'A wall could be chosen.')

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CellTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
