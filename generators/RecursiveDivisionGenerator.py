import generators.AbstractGenerator as AbstractGenerator
import model.Mesh as Mesh
import random
import logging

class RecursiveDivisionGenerator(AbstractGenerator.AbstractGenerator):

    def __init__(self):
        AbstractGenerator.AbstractGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    def __generateMaze__(self, size, seed = 0):
        AbstractGenerator.AbstractGenerator.__generateMaze__(self, size)
        if (seed != 0):
            random.seed(seed)
        """implement Recursive Division Algorithm"""
        mesh = Mesh.Mesh(size, True)
        for i in range(0, size): # create boundary walls
            mesh.getCell(i, 0).createLeft()
            mesh.getCell(i, size-1).createRight()
            mesh.getCell(0, i).createTop()
            mesh.getCell(size-1, i).createBottom()
        self.divideAndGenerate(mesh,0, size-1, 0, size-1)
        return mesh

    def divideAndGenerate(self, mesh, leftBorder, rightBorder, topBorder, bottomBorder):
        if ((leftBorder != rightBorder) & (topBorder != bottomBorder)):
            row = random.randint(leftBorder+1, rightBorder)
            column = random.randint(topBorder+1, bottomBorder)
            for i in range(leftBorder, rightBorder+1):
                mesh.getCell(column, i).createTop()
            for i in range(topBorder, bottomBorder+1):
                mesh.getCell(i, row).createLeft()
            k = random.randint(0, 3)
            leftHole = random.randint(leftBorder, row-1)
            rightHole = random.randint(row, rightBorder)
            topHole = random.randint(topBorder, column-1)
            bottomHole = random.randint(column, bottomBorder)
            if (k == 0):
                mesh.getCell(column, leftHole).removeTop()
                mesh.getCell(column, rightHole).removeTop()
                mesh.getCell(topHole, row).removeLeft()
            elif (k == 1):
                mesh.getCell(column, leftHole).removeTop()
                mesh.getCell(column, rightHole).removeTop()
                mesh.getCell(bottomHole, row).removeLeft()
            elif (k == 2):
                mesh.getCell(column, leftHole).removeTop()
                mesh.getCell(topHole, row).removeLeft()
                mesh.getCell(bottomHole, row).removeLeft()
            elif (k == 3):
                mesh.getCell(column, rightHole).removeTop()
                mesh.getCell(topHole, row).removeLeft()
                mesh.getCell(bottomHole, row).removeLeft()
            else:
                self.log.error('Invalid random number')
                raise Exception('Invalid random number')
            self.divideAndGenerate(mesh,leftBorder, row-1, topBorder, column-1)
            self.divideAndGenerate(mesh,row, rightBorder, topBorder, column-1)
            self.divideAndGenerate(mesh,leftBorder, row-1, column, bottomBorder)
            self.divideAndGenerate(mesh,row, rightBorder, column, bottomBorder)
