import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import model.Cell as Cell
import model.Wall as Wall

class CellTest(unittest.TestCase):
    
    def setUp(self):
        self.cell = Cell.Cell(1, 2, 3)
    
    def test_CellInit(self):
        wallList = self.cell.wallList
        self.assertEqual(len(wallList), 4)
        for i in range(4):
            self.assertFalse(wallList[i].isRemoved())
        self.assertEqual(self.cell.leftWall, wallList[0])
        self.assertEqual(self.cell.rightWall, wallList[1])
        self.assertEqual(self.cell.topWall, wallList[2])
        self.assertEqual(self.cell.bottomWall, wallList[3])
        self.assertEqual(self.cell.x, 1)
        self.assertEqual(self.cell.y, 2)
        self.assertEqual(self.cell.set, 3)
    
    def test_setSet(self):
        self.cell.setSet(2)
        self.assertEqual(self.cell.set, 2)
    
    def test_getSet(self):
        self.assertEqual(self.cell.set, self.cell.getSet())
    
    def test_getX(self):
        self.assertEqual(self.cell.x, self.cell.getX())
    
    def test_getY(self):
        self.assertEqual(self.cell.y, self.cell.getY())
    
    def test_getLeft(self):
        self.assertEqual(self.cell.leftWall, self.cell.getLeft())
    
    def test_setLeft(self):
        wall = Wall.Wall()
        self.cell.setLeft(wall)
        self.assertEqual(self.cell.leftWall, wall)
    
    def test_getRight(self):
        self.assertEqual(self.cell.rightWall, self.cell.getRight())
    
    def test_setRight(self):
        wall = Wall.Wall()
        self.cell.setRight(wall)
        self.assertEqual(self.cell.rightWall, wall)
    
    def test_getTop(self):
        self.assertEqual(self.cell.topWall, self.cell.getTop())
    
    def test_setTop(self):
        wall = Wall.Wall()
        self.cell.setTop(wall)
        self.assertEqual(self.cell.topWall, wall)
    
    def test_getBottom(self):
        self.assertEqual(self.cell.bottomWall, self.cell.getBottom())
    
    def test_setBottom(self):
        wall = Wall.Wall()
        self.cell.setBottom(wall)
        self.assertEqual(self.cell.bottomWall, wall)
    
    def test_removeLeft(self):
        self.cell.removeLeft()
        self.assertTrue(self.cell.leftWall.isRemoved())
    
    def test_createLeft(self):
        self.cell.createLeft()
        self.assertFalse(self.cell.leftWall.isRemoved())
    
    def test_removeRight(self):
        self.cell.removeRight()
        self.assertTrue(self.cell.rightWall.isRemoved())
    
    def test_createRight(self):
        self.cell.createRight()
        self.assertFalse(self.cell.rightWall.isRemoved())
    
    def test_removeTop(self):
        self.cell.removeTop()
        self.assertTrue(self.cell.topWall.isRemoved())
    
    def test_createTop(self):
        self.cell.createTop()
        self.assertFalse(self.cell.topWall.isRemoved())
    
    def test_removeBottom(self):
        self.cell.removeBottom()
        self.assertTrue(self.cell.bottomWall.isRemoved())
    
    def test_createBottom(self):
        self.cell.createBottom()
        self.assertFalse(self.cell.bottomWall.isRemoved())
    
    def test_hasWall(self):
        self.assertTrue(self.cell.hasWall())
        self.cell.removeLeft()
        self.cell.removeRight()
        self.cell.removeTop()
        self.cell.removeBottom()
        self.assertFalse(self.cell.hasWall())
    
    def test_wallCount(self):
        self.assertEqual(self.cell.wallCount(), 4)
        self.cell.removeLeft()
        self.assertEqual(self.cell.wallCount(), 3)
        self.cell.removeRight()
        self.assertEqual(self.cell.wallCount(), 2)
        self.cell.removeTop()
        self.assertEqual(self.cell.wallCount(), 1)
        self.cell.removeBottom()
        self.assertEqual(self.cell.wallCount(), 0)
    
    def test_chooseWallSuccess(self):
        wall = self.cell.chooseWall()
        self.assertFalse(wall.isRemoved())
        
    def test_chooseWallFail(self):
        self.cell.removeLeft()
        self.cell.removeRight()
        self.cell.removeTop()
        self.cell.removeBottom()
        wall = self.cell.chooseWall()
        self.assertIsNone(wall)
    
if __name__ == '__main__':
    unittest.main()
