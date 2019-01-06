from generators.AbstractGenerator import AbstractGenerator
from model.Mesh import Mesh
import logging


class KruskalGenerator(AbstractGenerator):

    def __init__(self):
        AbstractGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    def __generate_maze__(self, size):
        AbstractGenerator.__generate_maze__(self, size)
        """ Kruskal's Algorithm"""
        mesh = Mesh(size)
        while mesh.has_multiple_sets():
            cell = mesh.choose_cell(self.random)
            wall = mesh.choose_wall(cell, self.random)
            if wall == cell.get_left():
                neighbour = mesh.get_left_neighbour(cell)
            elif wall == cell.get_right():
                neighbour = mesh.get_right_neighbour(cell)
            elif wall == cell.get_top():
                neighbour = mesh.get_top_neighbour(cell)
            elif wall == cell.get_bottom():
                neighbour = mesh.get_bottom_neighbour(cell)
            else:
                self.log.error('Invalid wall')
                raise Exception('Invalid wall')
            if neighbour.get_set() != cell.get_set():
                wall.remove()
                mesh.move_cell(neighbour.get_set(), cell.get_set())
            else:
                self.__create_loops__(wall, size)
        return mesh

    # To be overridden by subclass
    def __create_loops__(self, wall, size):
        pass
