from solvers.AbstractSolver import AbstractSolver
import logging


class LeftWallFollowerSolver(AbstractSolver):

    def __init__(self, seed=0):
        AbstractSolver.__init__(self, seed)
        self.log = logging.getLogger(__name__)

    def solve_maze(self, maze):
        """implement left wall following"""
        """this means: always try going in directions in the following order: left, forward, right, backward"""
        self.path = []
        self.maze = maze
        if maze.get_entrance() is None or maze.get_exit() is None:
            self.log.error('Entrance or Exit is missing')
            raise Exception('Entrance or Exit is missing')
        cell = maze.get_entrance()
        self.path.append(cell)
        x = cell.get_x()
        y = cell.get_y()
        if (x == 0) & (y != 0):
            self.__try_right__()
        elif (x != 0) & (y == 0):
            self.__try_top__()
        elif (x == y == 0) & cell.get_top().is_removed():
            self.__try_right__()
        elif (x == y == 0) & cell.get_left().is_removed():
            self.__try_top__()
        else:
            self.log.error('Invalid starting cell')
            raise Exception('Invalid starting cell')
        self.__clean_path__()
        return self.path

    def __try_bottom__(self):
        cell = self.path[-1]
        if cell != self.maze.get_exit():
            if cell.get_bottom().is_removed():
                cell = self.maze.get_bottom_neighbour(cell)
                self.path.append(cell)
                self.__try_right__()
            else:
                self.__try_left__()

    def __try_left__(self):
        cell = self.path[-1]
        if cell != self.maze.get_exit():
            if cell.get_left().is_removed():
                cell = self.maze.get_left_neighbour(cell)
                self.path.append(cell)
                self.__try_bottom__()
            else:
                self.__try_top__()

    def __try_top__(self):
        cell = self.path[-1]
        if cell != self.maze.get_exit():
            if cell.get_top().is_removed():
                cell = self.maze.get_top_neighbour(cell)
                self.path.append(cell)
                self.__try_left__()
            else:
                self.__try_right__()

    def __try_right__(self):
        cell = self.path[-1]
        if cell != self.maze.get_exit():
            if cell.get_right().is_removed():
                cell = self.maze.get_right_neighbour(cell)
                self.path.append(cell)
                self.__try_top__()
            else:
                self.__try_bottom__()
