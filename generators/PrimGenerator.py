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
        self.mesh = Mesh(size)
        cell = self.mesh.choose_cell(self.random)
        self.queue = [cell]
        while len(self.queue) > 0:
            n = self.random.randint(0, len(self.queue)-1)
            cell = self.queue[n]
            self.log.debug('looking at ' + str(cell))
            wall = self.mesh.choose_wall(cell, self.random)
            if wall == cell.get_left():
                neighbour = self.mesh.get_left_neighbour(cell)
            elif wall == cell.get_right():
                neighbour = self.mesh.get_right_neighbour(cell)
            elif wall == cell.get_top():
                neighbour = self.mesh.get_top_neighbour(cell)
            elif wall == cell.get_bottom():
                neighbour = self.mesh.get_bottom_neighbour(cell)
            else:
                self.log.error('Invalid wall: ' + str(wall))
                raise Exception('Invalid wall: ' + str(wall))
            if cell.get_set() != neighbour.get_set():
                self.log.debug('removing wall to ' + str(neighbour))
                wall.remove()
                self.mesh.move_cell(neighbour.get_set(), cell.get_set())
                self.queue.append(neighbour)
            else:
                self.__create_loops__(cell, neighbour, wall)
            if not self.mesh.has_neighbour_in_different_set(cell):
                self.log.debug('removing cell from queue')
                self.queue.remove(cell)
        return self.mesh

    def __create_loops__(self, cell, neighbour, wall):
        pass