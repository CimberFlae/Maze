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
        self.mesh = Mesh(size, True)
        for i in range(0, size):  # create boundary walls
            self.mesh.get_cell(i, 0).create_left()
            self.mesh.get_cell(i, size - 1).create_right()
            self.mesh.get_cell(0, i).create_top()
            self.mesh.get_cell(size - 1, i).create_bottom()
        self.__divideAndGenerate__(0, size - 1, 0, size - 1)
        return self.mesh

    def __divideAndGenerate__(self, left_border, right_border, top_border, bottom_border):
        if (left_border != right_border) and (top_border != bottom_border):
            column = self.random.randint(left_border + 1, right_border)
            row = self.random.randint(top_border + 1, bottom_border)
            for i in range(left_border, right_border + 1):
                self.mesh.get_cell(row, i).create_top()
            for i in range(top_border, bottom_border + 1):
                self.mesh.get_cell(i, column).create_left()
            left_hole = self.random.randint(left_border, column - 1)
            right_hole = self.random.randint(column, right_border)
            top_hole = self.random.randint(top_border, row - 1)
            bottom_hole = self.random.randint(row, bottom_border)
            make_hole_list = [self.__get_make_horizontal_hole__(row, left_hole),
                              self.__get_make_horizontal_hole__(row, right_hole),
                              self.__get_make_vertical_hole__(top_hole, column),
                              self.__get_make_vertical_hole__(bottom_hole, column)]
            for i in range(0, 3):
                choice = self.random.randint(0, len(make_hole_list)-1)
                make_hole_list[choice]()
                make_hole_list.remove(make_hole_list[choice])
            self.__create_loops__(make_hole_list)
            self.__divideAndGenerate__(left_border, column - 1, top_border, row - 1)
            self.__divideAndGenerate__(column, right_border, top_border, row - 1)
            self.__divideAndGenerate__(left_border, column - 1, row, bottom_border)
            self.__divideAndGenerate__(column, right_border, row, bottom_border)

    def __get_make_vertical_hole__(self, column, row):
        return self.mesh.get_cell(column, row).remove_left

    def __get_make_horizontal_hole__(self, column, row):
        return self.mesh.get_cell(column, row).remove_top

    def __create_loops__(self, function_list):
        pass
