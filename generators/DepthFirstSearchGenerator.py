from generators.AbstractGenerator import AbstractGenerator
from model.Mesh import Mesh
import logging


class DepthFirstSearchGenerator(AbstractGenerator):

    def __init__(self):
        AbstractGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    def __generate_maze__(self, size, seed=0):
        AbstractGenerator.__generate_maze__(self, size)
        """implement Depth-first Search Algorithm"""
        mesh = Mesh(size)
        cell = mesh.choose_cell()
        stack = []
        while mesh.has_multiple_sets():
            if mesh.has_neighbour_in_different_set(cell):
                wall = mesh.choose_wall(cell)
                if wall == cell.get_left():
                    neighbour = mesh.get_left_neighbour(cell)
                    if neighbour.get_set() != cell.get_set():
                        cell.remove_left()
                        mesh.move_cell(neighbour.get_set(), cell.get_set())
                        stack.append(cell)
                        cell = neighbour
                elif wall == cell.get_right():
                    neighbour = mesh.get_right_neighbour(cell)
                    if neighbour.get_set() != cell.get_set():
                        cell.remove_right()
                        mesh.move_cell(neighbour.get_set(), cell.get_set())
                        stack.append(cell)
                        cell = neighbour
                elif wall == cell.get_top():
                    neighbour = mesh.get_top_neighbour(cell)
                    if neighbour.get_set() != cell.get_set():
                        cell.remove_top()
                        mesh.move_cell(neighbour.get_set(), cell.get_set())
                        stack.append(cell)
                        cell = neighbour
                elif wall == cell.get_bottom():
                    neighbour = mesh.get_bottom_neighbour(cell)
                    if neighbour.get_set() != cell.get_set():
                        cell.remove_bottom()
                        mesh.move_cell(neighbour.get_set(), cell.get_set())
                        stack.append(cell)
                        cell = neighbour
                else:
                    self.log.error('Invalid wall')
                    raise Exception('Invalid wall')
            else:
                cell = stack.pop()
        return mesh
