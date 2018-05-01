import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import model.Cell as Cell
import model.Wall as Wall

class CellTest(unittest.TestCase):
    
    def setUp(self):
        self.cell = Cell.Cell(1, 2, 3)
    
    def test_CellInit(self):
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
        self.cell.setSet(2)
        self.assertEqual(self.cell.set, 2, 'Cell has wrong Set.')
    
    def test_getSet(self):
        self.assertEqual(self.cell.set, self.cell.getSet(), 'getSet returned wrong value.')
    
    def test_getX(self):
        self.assertEqual(self.cell.x, self.cell.getX(), 'getX returned wrong value.')
    
    def test_getY(self):
        self.assertEqual(self.cell.y, self.cell.getY(), 'getY returned wrong value.')
    
    def test_getLeft(self):
        self.assertEqual(self.cell.leftWall, self.cell.getLeft(), 'getLeft returned wrong value.')
    
    def test_setLeft(self):
        wall = Wall.Wall()
        self.cell.setLeft(wall)
        self.assertEqual(self.cell.leftWall, wall, 'Left wall is set incorrectly.')
    
    def test_getRight(self):
        self.assertEqual(self.cell.rightWall, self.cell.getRight(), 'getRight returned wrong value.')
    
    def test_setRight(self):
        wall = Wall.Wall()
        self.cell.setRight(wall)
        self.assertEqual(self.cell.rightWall, wall, 'Right wall is set incorrectly.')
    
    def test_getTop(self):
        self.assertEqual(self.cell.topWall, self.cell.getTop(), 'getTop returned wrong value.')
    
    def test_setTop(self):
        wall = Wall.Wall()
        self.cell.setTop(wall)
        self.assertEqual(self.cell.topWall, wall, 'Top wall is set incorrectly.')
    
    def test_getBottom(self):
        self.assertEqual(self.cell.bottomWall, self.cell.getBottom(), 'getBottom returned wrong value.')
    
    def test_setBottom(self):
        wall = Wall.Wall()
        self.cell.setBottom(wall)
        self.assertEqual(self.cell.bottomWall, wall, 'Bottom wall is set incorrectly.')
    
    def test_removeLeft(self):
        self.cell.removeLeft()
        self.assertTrue(self.cell.leftWall.isRemoved(), 'Left wall is not removed.')
    
    def test_createLeft(self):
        self.cell.createLeft()
        self.assertFalse(self.cell.leftWall.isRemoved(), 'Left wall is removed.')
    
    def test_removeRight(self):
        self.cell.removeRight()
        self.assertTrue(self.cell.rightWall.isRemoved(), 'Right wall is not removed.')
    
    def test_createRight(self):
        self.cell.createRight()
        self.assertFalse(self.cell.rightWall.isRemoved(), 'Right wall is removed.')
    
    def test_removeTop(self):
        self.cell.removeTop()
        self.assertTrue(self.cell.topWall.isRemoved(), 'Top wall is not removed.')
    
    def test_createTop(self):
        self.cell.createTop()
        self.assertFalse(self.cell.topWall.isRemoved(), 'Top wall is removed.')
    
    def test_removeBottom(self):
        self.cell.removeBottom()
        self.assertTrue(self.cell.bottomWall.isRemoved(), 'Bottom wall is not removed.')
    
    def test_createBottom(self):
        self.cell.createBottom()
        self.assertFalse(self.cell.bottomWall.isRemoved(), 'Bottom wall is removed.')
    
    def test_hasWall(self):
        self.assertTrue(self.cell.hasWall())
        self.cell.removeLeft()
        self.cell.removeRight()
        self.cell.removeTop()
        self.cell.removeBottom()
        self.assertFalse(self.cell.hasWall(), 'Cell still has walls.')
    
    def test_wallCount(self):
        self.assertEqual(self.cell.wallCount(), 4, 'Cell does not have correct number of walls.')
        self.cell.removeLeft()
        self.assertEqual(self.cell.wallCount(), 3, 'Cell does not have correct number of walls.')
        self.cell.removeRight()
        self.assertEqual(self.cell.wallCount(), 2, 'Cell does not have correct number of walls.')
        self.cell.removeTop()
        self.assertEqual(self.cell.wallCount(), 1, 'Cell does not have correct number of walls.')
        self.cell.removeBottom()
        self.assertEqual(self.cell.wallCount(), 0, 'Cell does not have correct number of walls.')
    
    def test_chooseWallSuccess(self):
        wall = self.cell.chooseWall()
        self.assertFalse(wall.isRemoved(), 'Removed wall has been chosen.')
        
    def test_chooseWallFail(self):
        self.cell.removeLeft()
        self.cell.removeRight()
        self.cell.removeTop()
        self.cell.removeBottom()
        wall = self.cell.chooseWall()
        self.assertIsNone(wall, 'A wall could be chosen.')

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CellTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
