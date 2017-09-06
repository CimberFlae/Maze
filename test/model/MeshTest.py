import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import model.Mesh as Mesh

class MeshTest(unittest.TestCase):
    
    def setUp(self):
        self.mesh = Mesh.Mesh(10)
    
    def test_MeshInit(self):
        mesh = self.mesh
        self.assertEqual(mesh.size, 10)
        self.assertEqual(len(mesh), mesh.size)
        self.assertEqual(len(mesh.sets), 100)
        self.assertEqual(len(mesh.sets), len(set(mesh.sets)))
        for i in range (0, mesh.size-1):
            for j in range (0, mesh.size):
                self.assertEqual(mesh.matrix[i][j].getBottom, mesh.matrix[i+1][j].getTop())
        for i in range (0, mesh.size):
            for j in range (0, mesh.size-1):
                self.assertEqual(mesh.matrix[i][j].getRight,  mesh.matrix[i][j+1].getLeft())
        for i in range (0, mesh.size):
            self.assertFalse(mesh.matrix[0][i].getTopWall.isRemoved())
            self.assertFalse(mesh.matrix[mesh.size - 1][i].getBottomWall.isRemoved())
            self.assertFalse(mesh.matrix[i][0].getLeftWall.isRemoved())
            self.assertFalse(mesh.matrix[i][mesh.size - 1].getRightWall.isRemoved())
    
    def test_getSize(self):
        self.assertEqual(self.mesh.getSize(), self.mesh.size)
    
    def test_getCell(self):
        self.assertEqual(self.mesh.getCell(3, 7), self.mesh.matrix[3][7])
    
    def test_getLeftNeighbour(self):
        cell = self.mesh.matrix[3][7]
        self.assertEqual(self.mesh.getLeftNeighbour(cell), self.mesh.matrix[cell.getX()][cell.getY()-1])
    
    def test_getRightNeighbour(self):
        cell = self.mesh.matrix[3][7]
        self.assertEqual(self.mesh.getRightNeighbour(cell), self.mesh.matrix[cell.getX()][cell.getY()+1])
    
    def test_getTopNeighbour(self):
        cell = self.mesh.matrix[3][7]
        self.assertEqual(self.mesh.getTopNeighbour(cell), self.mesh.matrix[cell.getX()-1][cell.getY()])
    
    def test_getBottomNeighbour(self):
        cell = self.mesh.matrix[3][7]
        self.assertEqual(self.mesh.getBottomNeighbour(cell), self.mesh.matrix[cell.getX()+1][cell.getY()])
    
    def test_moveCell(self):
        cell1 = self.mesh[3][7]
        set1 = cell1.set
        cell2 = self.mesh[7][3]
        set2 = cell2.set
        self.assertNotEqual(set1, set2)
        self.mesh.moveCell(set1, set2)
        self.assertEqual(cell1.set, cell2.set)
        self.assertEqual(cell1.set, set2)
        self.assertIn(cell1, self.mesh.sets[set2])
        self.assertIn(cell2, self.mesh.sets[set2])
        self.assertNotIn(cell1, self.mesh.sets[set1])
        self.assertNotIn(cell2, self.mesh.sets[set1])
        self.assertEqual(len(self.mesh.sets[set1]), 0)
    
    def test_checkSets(self):
        self.assertFalse(self.mesh.checkSets())
        for i in range(100):
            self.mesh.moveCell(i, 0)
        self.assertTrue(self.mesh.checkSets())
    
    def test_chooseCellSuccess(self):
        cell = self.mesh.chooseCell()
        self.assertTrue(self.mesh.hasLegitNeighbour(cell))
    
    def test_chooseCellFail(self):
        for i in range(100):
            self.mesh.moveCell(i, 0)
        cell = self.mesh.chooseCell()
        self.assertIsNone(cell)
    
    def test_isBorder(self):
        self.assertFalse(self.mesh.isBorder(self.mesh.matrix[3][7]))
        self.assertTrue(self.mesh.isBorder(self.mesh.matrix[3][9]))
        self.assertTrue(self.mesh.isBorder(self.mesh.matrix[3][0]))
        self.assertTrue(self.mesh.isBorder(self.mesh.matrix[0][7]))
        self.assertTrue(self.mesh.isBorder(self.mesh.matrix[9][7]))
    
    def test_isLegitNeighbour(self):
        self.assertTrue(self.mesh.isLegitNeighbour(self.mesh.matrix[3][7]))
        self.mesh.moveCell(0, 1)
        self.mesh.moveCell(10, 1)
        self.assertFalse(self.mesh.isLegitNeighbour(self.mesh.matrix[0][0]))
    
    def test_setCustomOpening(self):
        self.assertRaises(self.mesh.setCustomOpening(10, 9), 'Opening cell has to part of the maze - check your indexes')
        self.mesh.setCustomOpening(0, 0, True)
        self.assertTrue(self.mesh.matrix[0][0].getTopWall().isRemoved())
        #test more functionality
    
if __name__ == '__main__':
    unittest.main()
