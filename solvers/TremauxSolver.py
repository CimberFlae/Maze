from solvers.AbstractSolver import AbstractSolver
import logging
import traceback


class TremauxSolver(AbstractSolver):

    def __init__(self, seed=0):
        AbstractSolver.__init__(self, seed)
        self.log = logging.getLogger(__name__)

    def solve_maze(self, maze):
        self.path = []
        self.maze = maze
        """implement Tremaux's algorithm"""
        if maze.get_entrance() is None or maze.get_exit() is None:
            self.log.error('Entrance or Exit is missing')
            raise Exception('Entrance or Exit is missing')
        self.walls = {}
        self.junctions = []
        self.path.append(maze.get_entrance())
        self.log.debug("Entrance: " + str(maze.get_entrance()))
        self.__decide_next__()
        self.__clean_path__()
        return self.path

    def __try_bottom__(self):
        current = self.path[-1]
        self.log.debug("try bottom in " + str(current))
        if current.get_bottom().is_removed() and self.maze.get_bottom_neighbour(current) is not None:
            self.__mark__(current, current.get_bottom())
            current = self.maze.get_bottom_neighbour(current)
            self.path.append(current)
            self.__decide_next__()
            self.log.debug('finished deciding next in after trying bottom')

    def __try_left__(self):
        current = self.path[-1]
        if current.get_left().is_removed() and self.maze.get_left_neighbour(current) is not None:
            self.__mark__(current, current.get_left())
            current = self.maze.get_left_neighbour(current)
            self.path.append(current)
            self.__decide_next__()
            self.log.debug('finished deciding next in after trying left')

    def __try_top__(self):
        current = self.path[-1]
        if current.get_top().is_removed() and self.maze.get_top_neighbour(current) is not None:
            self.__mark__(current, current.get_top())
            current = self.maze.get_top_neighbour(current)
            self.path.append(current)
            self.__decide_next__()
            self.log.debug('finished deciding next in after trying top')

    def __try_right__(self):
        current = self.path[-1]
        if current.get_right().is_removed() and self.maze.get_right_neighbour(current) is not None:
            self.__mark__(current, current.get_right())
            current = self.maze.get_right_neighbour(current)
            self.path.append(current)
            self.__decide_next__()
            self.log.debug('finished deciding next in after trying right')

    # @Override
    def __handle_junction__(self):
        self.log.debug('handling junction...')
        current = self.path[-1]
        if current not in self.junctions:  # new junction
            self.junctions.append(current)
            if self.__cameFromTop__():
                self.log.debug('came from top...')
                self.__mark__(current, current.get_top())
                while self.__not_finished__():
                    # arbitrary order
                    self.__try_bottom__()
                    if self.__not_finished__():
                        self.__try_left__()
                    if self.__not_finished__():
                        self.__try_right__()
            elif self.__cameFromBottom__():
                self.log.debug('came from bottom...')
                self.__mark__(self.path[-1], self.path[-1].get_bottom())
                while self.__not_finished__():
                    # arbitrary order
                    self.__try_left__()
                    if self.__not_finished__():
                        self.__try_right__()
                    if self.__not_finished__():
                        self.__try_top__()
            elif self.__cameFromLeft__():
                self.log.debug('came from left...')
                self.__mark__(self.path[-1], self.path[-1].get_left())
                while self.__not_finished__():
                    # arbitrary order
                    self.__try_bottom__()
                    if self.__not_finished__():
                        self.__try_right__()
                    if self.__not_finished__():
                        self.__try_top__()
            elif self.__cameFromRight__():
                self.log.debug('came from right...')
                self.__mark__(self.path[-1], self.path[-1].get_right())
                while self.__not_finished__():
                    # arbitrary order
                    self.__try_bottom__()
                    if self.__not_finished__():
                        self.__try_left__()
                    if self.__not_finished__():
                        self.__try_top__()
            else:
                self.log.error('Came from nowhere')
                raise Exception('Came from nowhere')
        else:  # have been here before
            key = self.__get_key__(current)
            if self.__cameFromTop__():
                self.__mark__(current, current.get_top())
                if self.walls[key].count(current.get_top()) == 1:  # we just came through here, we go right back
                    self.__try_top__()
                else:  # we try the least marked path
                    while self.__not_finished__() and self.__has_n_visited_path__(0):
                        self.__choose_n_visited_path__(0)
                    while self.__not_finished__() and self.__has_n_visited_path__(1):
                        self.__choose_n_visited_path__(1)
            elif self.__cameFromBottom__():
                self.__mark__(current, current.get_bottom())
                if self.walls[key].count(current.get_bottom()) == 1:
                    self.__try_bottom__()
                else:
                    while self.__not_finished__() and self.__has_n_visited_path__(0):
                        self.__choose_n_visited_path__(0)
                    while self.__not_finished__() and self.__has_n_visited_path__(1):
                        self.__choose_n_visited_path__(1)
            elif self.__cameFromLeft__():
                self.__mark__(current, current.get_left())
                if self.walls[key].count(current.get_left()) == 1:
                    self.__try_left__()
                else:
                    while self.__not_finished__() and self.__has_n_visited_path__(0):
                        self.__choose_n_visited_path__(0)
                    while self.__not_finished__() and self.__has_n_visited_path__(1):
                        self.__choose_n_visited_path__(1)
            elif self.__cameFromRight__():
                self.__mark__(current, current.get_right())
                if self.walls[key].count(current.get_right()) == 1:
                    self.__try_right__()
                else:
                    while self.__not_finished__() and self.__has_n_visited_path__(0):
                        self.__choose_n_visited_path__(0)
                    while self.__not_finished__() and self.__has_n_visited_path__(1):
                        self.__choose_n_visited_path__(1)
            else:
                self.log.error('Came from nowhere')
                raise Exception('Came from nowhere')

    def __not_finished__(self):
        current = self.path[-1]
        return current != self.maze.get_exit()

    def __has_n_visited_path__(self, n):
        current = self.path[-1]
        key = self.__get_key__(current)
        return self.walls[key].count(current.get_left()) == n or self.walls[key].count(current.get_right()) == n or \
            self.walls[key].count(current.get_top()) == n or self.walls[key].count(current.get_bottom()) == n

    def __choose_n_visited_path__(self, n):
        current = self.path[-1]
        key = self.__get_key__(current)
        if self.__cameFromBottom__():
            if self.walls[key].count(current.get_left()) == n:
                self.__mark__(current, current.get_left())
                self.__try_left__()
            elif self.walls[key].count(current.get_right()) == n:
                self.__mark__(current, current.get_right())
                self.__try_right__()
            elif self.walls[key].count(current.get_top()) == n:
                self.__mark__(current, current.get_top())
                self.__try_top__()
            else:
                self.log.error('Every path from here already visited ' + str(n) + ' times')
                raise Exception('Every path from here already visited ' + str(n) + ' times')
        elif self.__cameFromLeft__():
            if self.walls[key].count(current.get_bottom()) == n:
                self.__mark__(current, current.get_bottom())
                self.__try_bottom__()
            elif self.walls[key].count(current.get_right()) == n:
                self.__mark__(current, current.get_right())
                self.__try_right__()
            elif self.walls[key].count(current.get_top()) == n:
                self.__mark__(current, current.get_top())
                self.__try_top__()
            else:
                self.log.error('Every path from here already visited ' + str(n) + ' times')
                raise Exception('Every path from here already visited ' + str(n) + ' times')
        elif self.__cameFromRight__():
            if self.walls[key].count(current.get_bottom()) == n:
                self.__mark__(current, current.get_bottom())
                self.__try_bottom__()
            elif self.walls[key].count(current.get_left()) == n:
                self.__mark__(current, current.get_left())
                self.__try_left__()
            elif self.walls[key].count(current.get_top()) == n:
                self.__mark__(current, current.get_top())
                self.__try_top__()
            else:
                self.log.error('Every path from here already visited ' + str(n) + ' times')
                raise Exception('Every path from here already visited ' + str(n) + ' times')
        elif self.__cameFromTop__():
            if self.walls[key].count(current.get_bottom()) == n:
                self.__mark__(current, current.get_bottom())
                self.__try_bottom__()
            elif self.walls[key].count(current.get_left()) == n:
                self.__mark__(current, current.get_left())
                self.__try_left__()
            elif self.walls[key].count(current.get_right()) == n:
                self.__mark__(current, current.get_right())
                self.__try_right__()
            else:
                self.log.error('Every path from here already visited ' + str(n) + ' times')
                raise Exception('Every path from here already visited ' + str(n) + ' times')
        else:
            self.log.error('Came from nowhere')
            raise Exception('Came from nowhere')

    def __get_key__(self, cell):
        return str(cell.get_x()) + str(cell.get_y())

    def __mark__(self, cell, wall):
        key = self.__get_key__(cell)
        if key not in self.walls:
            self.walls[key] = []
        self.walls[key].append(wall)
