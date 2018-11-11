from solvers.AbstractSolver import AbstractSolver
import logging


class RightWallFollowerSolver(AbstractSolver):

    def __init__(self):
        AbstractSolver.__init__(self)
        self.log = logging.getLogger(__name__)

    def solve_maze(self, maze):
        """implement right wall following"""
        """this means: always try going in directions in the following order: right, forward, left, backward"""
        self.maze = maze
        if maze.get_entrance() is None or maze.get_exit() is None:
            self.log.error('Entrance or Exit is missing')
            raise Exception('Entrance or Exit is missing')
        cell = maze.get_entrance()
        self.path.append(cell)
        x = cell.get_x()
        y = cell.get_y()
        if (x == 0) & (y != 0):
            self.__try_left__(cell)
        elif (x != 0) & (y == 0):
            self.__try_bottom__(cell)
        elif (x == y == 0) & cell.get_top().is_removed():
            self.__try_left__(cell)
        elif (x == y == 0) & cell.get_left().is_removed():
            self.__try_bottom__(cell)
        else:
            self.log.error('Invalid starting cell')
            raise Exception('Invalid starting cell')
        self.__clean_path__()
        return self.path

    def __try_bottom__(self, cell):
        if cell != self.maze.get_exit():
            if cell.get_bottom().is_removed():
                cell = self.maze.get_bottom_neighbour(cell)
                self.path.append(cell)
                self.__try_left__(cell)
            else:
                self.__try_right__(cell)

    def __try_left__(self, cell):
        if cell != self.maze.get_exit():
            if cell.get_left().is_removed():
                cell = self.maze.get_left_neighbour(cell)
                self.path.append(cell)
                self.__try_top__(cell)
            else:
                self.__try_bottom__(cell)

    def __try_top__(self, cell):
        if cell != self.maze.get_exit():
            if cell.get_top().is_removed():
                cell = self.maze.get_top_neighbour(cell)
                self.path.append(cell)
                self.__try_right__(cell)
            else:
                self.__try_left__(cell)

    def __try_right__(self, cell):
        if cell != self.maze.get_exit():
            if cell.get_right().is_removed():
                cell = self.maze.get_right_neighbour(cell)
                self.path.append(cell)
                self.__try_bottom__(cell)
            else:
                self.__try_top__(cell)
