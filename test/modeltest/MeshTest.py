import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import model.Mesh as Mesh
import logging

class MeshTest(unittest.TestCase):
    
    def setUp(self):
        self.log = logging.getLogger(__name__)
        self.mesh = Mesh.Mesh(10)
    
    def test_MeshInit(self):
        self.log.debug("test_MeshInit")
        mesh = self.mesh
        self.assertEqual(mesh.size, 10, 'Size is wrong.')
        self.assertEqual(len(mesh.matrix), mesh.size, 'Length of matrix does not match size.')
        self.assertEqual(len(mesh.sets), 100, 'Wrong number of Sets found.')
        self.assertEqual(sum(len(cellSet) for cellSet in mesh.sets), len(set().union(*(set(cellSet) for cellSet in mesh.sets))), 'Not all Sets are distinct.')
        for i in range (0, mesh.size-1):
            for j in range (0, mesh.size):
                self.assertEqual(mesh.matrix[i][j].getBottom(), mesh.matrix[i+1][j].getTop(),
                'Adjacent cells [' + str(i) + ',' + str(j) + '] and [' + str(i+1) + ',' + str(j) + '] do not share a horizontal wall.')
        for i in range (0, mesh.size):
            for j in range (0, mesh.size-1):
                self.assertEqual(mesh.matrix[i][j].getRight(),  mesh.matrix[i][j+1].getLeft(),
                'Adjacent cells [' + str(i) + ',' + str(j) + '] and [' + str(i) + ',' + str(j+1) + '] do not share a vertical wall.')
        for i in range (0, mesh.size):
            self.assertFalse(mesh.matrix[0][i].getTop().isRemoved(), 'Mesh has an entry.')
            self.assertFalse(mesh.matrix[mesh.size - 1][i].getBottom().isRemoved(), 'Mesh has an entry.')
            self.assertFalse(mesh.matrix[i][0].getLeft().isRemoved(), 'Mesh has an entry.')
            self.assertFalse(mesh.matrix[i][mesh.size - 1].getRight().isRemoved(), 'Mesh has an entry.')
    
    def test_getSize(self):
        self.log.debug("test_getSize")
        self.assertEqual(self.mesh.getSize(), self.mesh.size, 'getSize returns wrong value.')
    
    def test_getCell(self):
        self.log.debug("test_getCell")
        self.assertEqual(self.mesh.getCell(3, 7), self.mesh.matrix[3][7], 'getCell returns wrong value.')
    
    def test_getLeftNeighbour(self):
        self.log.debug("test_getLeftNeighbour")
        cell = self.mesh.matrix[3][7]
        self.assertEqual(self.mesh.getLeftNeighbour(cell), self.mesh.matrix[cell.getX()][cell.getY()-1], 'getLeftNeighbour returns wrong value.')
    
    def test_getRightNeighbour(self):
        self.log.debug("test_getRightNeighbour")
        cell = self.mesh.matrix[3][7]
        self.assertEqual(self.mesh.getRightNeighbour(cell), self.mesh.matrix[cell.getX()][cell.getY()+1], 'getRightNeighbour returns wrong value.')
    
    def test_getTopNeighbour(self):
        self.log.debug("test_getTopNeighbour")
        cell = self.mesh.matrix[3][7]
        self.assertEqual(self.mesh.getTopNeighbour(cell), self.mesh.matrix[cell.getX()-1][cell.getY()], 'getTopNeighbour returns wrong value.')
    
    def test_getBottomNeighbour(self):
        self.log.debug("test_getBottomNeighbour")
        cell = self.mesh.matrix[3][7]
        self.assertEqual(self.mesh.getBottomNeighbour(cell), self.mesh.matrix[cell.getX()+1][cell.getY()], 'getBottomNeighbour returns wrong value.')
    
    def test_moveCell(self):
        self.log.debug("test_moveCell")
        cell1 = self.mesh.matrix[3][7]
        set1 = cell1.set
        cell2 = self.mesh.matrix[7][3]
        set2 = cell2.set
        self.assertNotEqual(set1, set2, 'Cells have same Set.')
        self.mesh.moveCell(set1, set2)
        self.assertEqual(cell1.set, cell2.set, 'Cells do not have same Set.')
        self.assertEqual(cell1.set, set2, 'Cells were moved into wrong Set.')
        self.assertIn(cell1, self.mesh.sets[set2], 'Set does not contain Cell.')
        self.assertIn(cell2, self.mesh.sets[set2], 'Set does not contain Cell.')
        self.assertNotIn(cell1, self.mesh.sets[set1], 'Set does contain Cell.')
        self.assertNotIn(cell2, self.mesh.sets[set1], 'Set does contain Cell.')
        self.assertEqual(len(self.mesh.sets[set1]), 0, 'Set still contains Cells.')
    
    def test_checkSets(self):
        self.log.debug("test_checkSets")
        self.assertTrue(self.mesh.hasMultipleSets(), 'Mesh has only one non-empty Set.')
        for i in range(self.mesh.size**2):
            self.mesh.moveCell(i, 0)
        self.assertFalse(self.mesh.hasMultipleSets(), 'Not all Cells are in the same Set.')
    
    def test_chooseCellSuccess(self):
        self.log.debug("test_chooseCellSuccess")
        cell = self.mesh.chooseCell()
        self.assertTrue(self.mesh.hasNeighbourInDifferentSet(cell), 'Cell without Wall to a neighbour has been chosen.')
    
    def test_chooseCellFail(self):
        self.log.debug("test_chooseCellFail")
        for i in range(100):
            self.mesh.moveCell(i, 0)
        cell = self.mesh.chooseCell()
        self.assertIsNone(cell, 'A Cell could be chosen.')
    
    def test_isBorder(self):
        self.log.debug("test_isBorder")
        cell37 = self.mesh.matrix[3][7]
        self.assertFalse(self.mesh.isBorder(cell37,  cell37.topWall), 'Cell is border.')
        self.assertFalse(self.mesh.isBorder(cell37,  cell37.leftWall), 'Cell is border.')
        self.assertFalse(self.mesh.isBorder(cell37,  cell37.bottomWall), 'Cell is border.')
        self.assertFalse(self.mesh.isBorder(cell37,  cell37.rightWall), 'Cell is border.')
        cell39 = self.mesh.matrix[3][9]
        self.assertTrue(self.mesh.isBorder(cell39, cell39.rightWall), 'Cell is not border.')
        cell30 = self.mesh.matrix[3][0]
        self.assertTrue(self.mesh.isBorder(cell30, cell30.leftWall), 'Cell is not border.')
        cell07 = self.mesh.matrix[0][7]
        self.assertTrue(self.mesh.isBorder(cell07, cell07.topWall), 'Cell is not border.')
        cell97 = self.mesh.matrix[9][7]
        self.assertTrue(self.mesh.isBorder(cell97, cell97.bottomWall), 'Cell is not border.')
    
    def test_isLegitNeighbour(self):
        self.log.debug("test_isLegitNeighbour")
        self.assertTrue(self.mesh.hasNeighbourInDifferentSet(self.mesh.matrix[3][7]), 'Cell has no neighbour in different Set.')
        self.mesh.moveCell(0, 1)
        self.mesh.moveCell(10, 1)
        self.assertFalse(self.mesh.hasNeighbourInDifferentSet(self.mesh.matrix[0][0]), 'Cells has neighbour in different Set.')
    
    def test_setCustomOpening(self):
        self.log.debug("test_setCustomOpening")
        self.assertRaises(IndexError, self.mesh.setCustomOpening, 10, 9)
        self.mesh.setCustomOpening(0, 0, True)
        self.assertTrue(self.mesh.matrix[0][0].getTop().isRemoved(), 'Cell (0,0) is not removed.')

    def test_setRandomTopEntrance(self):
        self.log.debug("test_setRandomTopEntrance")
        self.mesh.setRandomTopEntrance()
        found = False
        for i in range(0, 10):
            if self.mesh.matrix[0][i].getTop().isRemoved():
                found = True
        if not found:
            self.assertTrue(False, 'No top entrance found')

    def test_setRandomLeftEntrance(self):
        self.log.debug("test_setRandomLeftEntrance")
        self.mesh.setRandomLeftEntrance()
        found = False
        for i in range(0, 10):
            if self.mesh.matrix[i][0].getLeft().isRemoved():
                found = True
        if not found:
            self.assertTrue(False, 'No left entrance found')

    def test_setRandomBottomExit(self):
        self.log.debug("test_setRandomBottomExit")
        self.mesh.setRandomBottomExit()
        found = False
        for i in range(0, 10):
            if self.mesh.matrix[9][i].getBottom().isRemoved():
                found = True
        if not found:
            self.assertTrue(False, 'No bottom exit found')

    def test_setRandomRightExit(self):
        self.log.debug("test_setRandomRightExit")
        self.mesh.setRandomRightExit()
        found = False
        for i in range(0, 10):
            if self.mesh.matrix[i][9].getRight().isRemoved():
                found = True
        if not found:
            self.assertTrue(False, 'No right exit found')

    def test_clearEntrance(self):
        self.log.debug("test_clearEntrance")
        self.mesh.setCustomOpening(0, 0)
        self.mesh.clearEntrance()
        self.assertFalse(self.mesh.matrix[0][0].getTop().isRemoved(), 'Entrance was not cleared')
        self.assertFalse(self.mesh.matrix[0][0].getLeft().isRemoved(), 'Entrance was not cleared')

    def test_clearExit(self):
        self.log.debug("test_clearExit")
        self.mesh.setCustomOpening(9, 9)
        self.mesh.clearExit()
        self.assertFalse(self.mesh.matrix[9][9].getBottom().isRemoved(), 'Exit was not cleared')
        self.assertFalse(self.mesh.matrix[9][9].getRight().isRemoved(), 'Exit was not cleared')

    def test_getEntrance(self):
        self.log.debug("test_getEntrance")
        self.mesh.setCustomOpening(0, 0)
        self.assertEqual(self.mesh.getEntrance(), self.mesh.matrix[0][0], 'getEntrance returned wrong value')

    def test_getExit(self):
        self.log.debug("test_getExit")
        self.mesh.setCustomOpening(9, 9)
        self.assertEqual(self.mesh.getExit(), self.mesh.matrix[9][9], 'getExit returned wrong value')

    def test_chooseWall(self):
        self.log.debug("test_chooseWall")
        cell = self.mesh.matrix[0][5]
        cell.removeLeft()
        wall = self.mesh.chooseWall(cell)
        self.assertIsNotNone(wall, 'No wall was chosen')
        self.assertNotEqual(wall, cell.getLeft(), 'A removed wall was chosen')
        self.assertNotEqual(wall, cell.getTop, 'A border wall was chosen')
        cell.removeRight()
        cell.removeBottom()
        wall = self.mesh.chooseWall(cell)
        self.assertIsNone(wall, 'A (removed or border) wall was chosen')

# This is needed for the individual execution of this test class
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MeshTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
