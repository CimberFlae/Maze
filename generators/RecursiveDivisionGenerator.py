import generators.Generator as Generator
import model.Mesh as Mesh
import random

class RecursiveDivisionGenerator(Generator.Generator):

    def __init__(self):
        Generator.Generator.__init__(self)

    def __generateMaze__(self,size, entry = True, exit = True):
        """implement Recursive Division Algorithm"""
        mesh = Mesh.Mesh(size,True)
        for i in range(0,size):#create boundary walls
            mesh.createLeft(mesh.getCell(i,0))
            mesh.createRight(mesh.getCell(i,size-1))
            mesh.createTop(mesh.getCell(0,i))
            mesh.createBottom(mesh.getCell(size-1,i))
        self.divideAndGenerate(mesh,0, size-1, 0, size-1)
        return mesh

    def divideAndGenerate(self,mesh,leftBorder,rightBorder,topBorder,bottomBorder):
        if ((leftBorder != rightBorder) & (topBorder != bottomBorder)):
            row = random.randint(leftBorder+1,rightBorder)
            column = random.randint(topBorder+1,bottomBorder)
            for i in range(leftBorder,rightBorder+1):
                mesh.createTop(mesh.getCell(column,i))
            for i in range(topBorder,bottomBorder+1):
                mesh.createLeft(mesh.getCell(i,row))
            k = random.randint(0,3)
            leftHole = random.randint(leftBorder,row-1)
            rightHole = random.randint(row,rightBorder)
            topHole = random.randint(topBorder,column-1)
            bottomHole = random.randint(column,bottomBorder)
            if (k == 0):
                mesh.removeTop(mesh.getCell(column,leftHole))
                mesh.removeTop(mesh.getCell(column,rightHole))
                mesh.removeLeft(mesh.getCell(topHole,row))
            elif (k == 1):
                mesh.removeTop(mesh.getCell(column,leftHole))
                mesh.removeTop(mesh.getCell(column,rightHole))
                mesh.removeLeft(mesh.getCell(bottomHole,row))
            elif (k == 2):
                mesh.removeTop(mesh.getCell(column,leftHole))
                mesh.removeLeft(mesh.getCell(topHole,row))
                mesh.removeLeft(mesh.getCell(bottomHole,row))
            elif (k == 3):
                mesh.removeTop(mesh.getCell(column,rightHole))
                mesh.removeLeft(mesh.getCell(topHole,row))
                mesh.removeLeft(mesh.getCell(bottomHole,row))
            self.divideAndGenerate(mesh,leftBorder, row-1, topBorder, column-1)
            self.divideAndGenerate(mesh,row, rightBorder, topBorder, column-1)
            self.divideAndGenerate(mesh,leftBorder, row-1, column, bottomBorder)
            self.divideAndGenerate(mesh,row, rightBorder, column, bottomBorder)
