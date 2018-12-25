from generators.AbstractGenerator import AbstractGenerator
from model.Mesh import Mesh
import logging


class RecursiveDivisionGenerator(AbstractGenerator):

    def __init__(self):
        AbstractGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    def __generate_maze__(self, size):
        AbstractGenerator.__generate_maze__(self, size)
        """implement Recursive Division Algorithm"""
        mesh = Mesh(size, True)
        for i in range(0, size):  # create boundary walls
            mesh.get_cell(i, 0).create_left()
            mesh.get_cell(i, size - 1).create_right()
            mesh.get_cell(0, i).create_top()
            mesh.get_cell(size - 1, i).create_bottom()
        self.__divideAndGenerate__(mesh, 0, size - 1, 0, size - 1)
        return mesh

    def __divideAndGenerate__(self, mesh, left_border, right_border, top_border, bottom_border):
        if (left_border != right_border) & (top_border != bottom_border):
            row = self.random.randint(left_border + 1, right_border)
            column = self.random.randint(top_border + 1, bottom_border)
            for i in range(left_border, right_border + 1):
                mesh.get_cell(column, i).create_top()
            for i in range(top_border, bottom_border + 1):
                mesh.get_cell(i, row).create_left()
            k = self.random.randint(0, 3)
            left_hole = self.random.randint(left_border, row - 1)
            right_hole = self.random.randint(row, right_border)
            top_hole = self.random.randint(top_border, column - 1)
            bottom_hole = self.random.randint(column, bottom_border)
            if k == 0:
                mesh.get_cell(column, left_hole).remove_top()
                mesh.get_cell(column, right_hole).remove_top()
                mesh.get_cell(top_hole, row).remove_left()
            elif k == 1:
                mesh.get_cell(column, left_hole).remove_top()
                mesh.get_cell(column, right_hole).remove_top()
                mesh.get_cell(bottom_hole, row).remove_left()
            elif k == 2:
                mesh.get_cell(column, left_hole).remove_top()
                mesh.get_cell(top_hole, row).remove_left()
                mesh.get_cell(bottom_hole, row).remove_left()
            elif k == 3:
                mesh.get_cell(column, right_hole).remove_top()
                mesh.get_cell(top_hole, row).remove_left()
                mesh.get_cell(bottom_hole, row).remove_left()
            else:
                self.log.error('Invalid random number')
                raise Exception('Invalid random number')
            self.__divideAndGenerate__(mesh, left_border, row - 1, top_border, column - 1)
            self.__divideAndGenerate__(mesh, row, right_border, top_border, column - 1)
            self.__divideAndGenerate__(mesh, left_border, row - 1, column, bottom_border)
            self.__divideAndGenerate__(mesh, row, right_border, column, bottom_border)
