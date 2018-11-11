from solvers.AbstractSolver import AbstractSolver
import random
import logging


class RandomMouseSolver(AbstractSolver):

    def __init__(self):
        AbstractSolver.__init__(self)
        self.log = logging.getLogger(__name__)

    def solve_maze(self, maze, seed = 0):
        if seed != 0:
            random.seed(seed)
        self.maze = maze
        """implement random mouse algorithm"""
        """this means: always follow a given path to a junction and from there try a direction at random"""
        """caution: this algorithms may take longer than anticipated (since it is random)"""
        if maze.get_entrance() is None or maze.get_exit() is None:
            self.log.error('Entrance or Exit is missing')
            raise Exception('Entrance or Exit is missing')
        cell = maze.get_entrance()
        self.path.append(cell)
        while self.path[-1] != maze.get_exit():
            self.__decide_next__()
        self.__clean_path__()
        return self.path

    def __try_bottom__(self):
        cell = self.path[-1]
        if cell != self.maze.get_exit():
            bottom = cell.get_bottom()
            if bottom.is_removed() & (not self.maze.is_border(cell, bottom)):
                cell = self.maze.get_bottom_neighbour(cell)
                self.path.append(cell)

    def __try_left__(self):
        cell = self.path[-1]
        if cell != self.maze.get_exit():
            left = cell.get_left()
            if left.is_removed() & (not self.maze.is_border(cell, left)):
                cell = self.maze.get_left_neighbour(cell)
                self.path.append(cell)

    def __try_top__(self):
        cell = self.path[-1]
        if cell != self.maze.get_exit():
            top = cell.get_top()
            if top.is_removed() & (not self.maze.is_border(cell, top)):
                cell = self.maze.get_top_neighbour(cell)
                self.path.append(cell)

    def __try_right__(self):
        cell = self.path[-1]
        if cell != self.maze.get_exit():
            right = cell.get_right()
            if right.is_removed() & (not self.maze.is_border(cell, right)):
                cell = self.maze.get_right_neighbour(cell)
                self.path.append(cell)
