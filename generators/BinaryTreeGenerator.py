import generators.AbstractGenerator as AbstractGenerator
import model.Mesh as Mesh
import random

class BinaryTreeGenerator(AbstractGenerator.AbstractGenerator):

    def __init__(self):
        AbstractGenerator.AbstractGenerator.__init__(self)

    def __generateMaze__(self, size, seed = 0):
        if seed != 0:
            random.seed(seed)
        """implement Binary Tree Algorithm"""
        mesh = Mesh.Mesh(size)
        for i in range(1, size):
            mesh.getCell(0, i).removeLeft()
            mesh.getCell(i, 0).removeTop()
        for i in range(1, size):
            for j in range(1, size):
                if (random.random() > 0.5):
                    mesh.getCell(i, j).removeLeft()
                else:
                    mesh.getCell(i, j).removeTop()
        return mesh
