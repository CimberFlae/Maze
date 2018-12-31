from generators.AbstractGenerator import AbstractGenerator
from model.Mesh import Mesh
import logging


class DepthFirstSearchGenerator(AbstractGenerator):

    def __init__(self):
        AbstractGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    def __generate_maze__(self, size):
        AbstractGenerator.__generate_maze__(self, size)
        """implement Depth-first Search Algorithm"""
        self.mesh = Mesh(size)
        cell = self.mesh.choose_cell(self.random)
        self.stack = []
        while self.mesh.has_multiple_sets():
            if self.mesh.has_neighbour_in_different_set(cell):
                wall = self.mesh.choose_wall(cell, self.random)
                if wall == cell.get_left():
                    neighbour = self.mesh.get_left_neighbour(cell)
                    if neighbour.get_set() != cell.get_set():
                        cell.remove_left()
                        self.mesh.move_cell(neighbour.get_set(), cell.get_set())
                        self.stack.append(cell)
                        cell = neighbour
                elif wall == cell.get_right():
                    neighbour = self.mesh.get_right_neighbour(cell)
                    if neighbour.get_set() != cell.get_set():
                        cell.remove_right()
                        self.mesh.move_cell(neighbour.get_set(), cell.get_set())
                        self.stack.append(cell)
                        cell = neighbour
                elif wall == cell.get_top():
                    neighbour = self.mesh.get_top_neighbour(cell)
                    if neighbour.get_set() != cell.get_set():
                        cell.remove_top()
                        self.mesh.move_cell(neighbour.get_set(), cell.get_set())
                        self.stack.append(cell)
                        cell = neighbour
                elif wall == cell.get_bottom():
                    neighbour = self.mesh.get_bottom_neighbour(cell)
                    if neighbour.get_set() != cell.get_set():
                        cell.remove_bottom()
                        self.mesh.move_cell(neighbour.get_set(), cell.get_set())
                        self.stack.append(cell)
                        cell = neighbour
                else:
                    self.log.error('Invalid wall')
                    raise Exception('Invalid wall')
            else:
                cell = self.__handleDeadEnd__(cell)
        return self.mesh

    def __handleDeadEnd__(self, cell):
        return self.stack.pop()
