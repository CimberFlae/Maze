from generators.AbstractGenerator import AbstractGenerator
from model.Mesh import Mesh
import random


class BinaryTreeGenerator(AbstractGenerator):

    def __init__(self):
        AbstractGenerator.__init__(self)

    def __generate_maze__(self, size, seed=0):
        AbstractGenerator.__generate_maze__(self, size)
        if seed != 0:
            random.seed(seed)
        """implement Binary Tree Algorithm"""
        mesh = Mesh(size)
        for i in range(1, size):
            mesh.get_cell(0, i).remove_left()
            mesh.get_cell(i, 0).remove_top()
        for i in range(1, size):
            for j in range(1, size):
                if random.random() > 0.5:
                    mesh.get_cell(i, j).remove_left()
                else:
                    mesh.get_cell(i, j).remove_top()
        return mesh
