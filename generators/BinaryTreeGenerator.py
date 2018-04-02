import generators.Generator as Generator
import model.Mesh as Mesh
import random

class BinaryTreeGenerator(Generator.Generator):

    def __init__(self):
        Generator.Generator.__init__(self)

    def __generateMaze__(self, size, top = True, bottom = True, entry = True, exit = True, seed = 0):
        if seed != 0:
            random.seed(seed)
        """implement Binary Tree Algorithm"""
        mesh = Mesh.Mesh(size)
        for i in range(1, size):
            mesh.removeLeft(mesh.getCell(0, i))
            mesh.removeTop(mesh.getCell(i, 0))
        for i in range(1, size):
            for j in range(1, size):
                if (random.random() > 0.5):
                    mesh.removeLeft(mesh.getCell(i, j))
                else:
                    mesh.removeTop(mesh.getCell(i, j))
        return mesh
