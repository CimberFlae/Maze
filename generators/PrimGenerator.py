from generators.AbstractGenerator import AbstractGenerator
from model.Mesh import Mesh
import logging


class PrimGenerator(AbstractGenerator):

    def __init__(self):
        AbstractGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    def __generate_maze__(self, size):
        AbstractGenerator.__generate_maze__(self, size)
        """implement Prim's Algorithm"""
        mesh = Mesh(size)
        cell = mesh.choose_cell(self.random)
        queue = [cell]
        while len(queue) > 0:
            n = self.random.randint(0, len(queue)-1)
            cell = queue[n]
            wall = mesh.choose_wall(cell, self.random)
            if wall == cell.get_left():
                neighbour = mesh.get_left_neighbour(cell)
                if cell.get_set() != neighbour.get_set():
                    cell.remove_left()
                    mesh.move_cell(neighbour.get_set(), cell.get_set())
                    queue.append(neighbour)
            elif wall == cell.get_right():
                neighbour = mesh.get_right_neighbour(cell)
                if cell.get_set() != neighbour.get_set():
                    cell.remove_right()
                    mesh.move_cell(neighbour.get_set(), cell.get_set())
                    queue.append(neighbour)
            elif wall == cell.get_top():
                neighbour = mesh.get_top_neighbour(cell)
                if cell.get_set() != neighbour.get_set():
                    cell.remove_top()
                    mesh.move_cell(neighbour.get_set(), cell.get_set())
                    queue.append(neighbour)
            elif wall == cell.get_bottom():
                neighbour = mesh.get_bottom_neighbour(cell)
                if cell.get_set() != neighbour.get_set():
                    cell.remove_bottom()
                    mesh.move_cell(neighbour.get_set(), cell.get_set())
                    queue.append(neighbour)
            else:
                self.log.error('Invalid wall')
                raise Exception('Invalid wall')
            if not mesh.has_neighbour_in_different_set(cell):
                queue.remove(cell)
        return mesh
