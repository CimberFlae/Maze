import solvers.AbstractSolver as AbstractSolver
import logging

class LeftWallFollowerSolver(AbstractSolver.AbstractSolver):

    def __init__(self):
        AbstractSolver.AbstractSolver.__init__(self)
        self.log = logging.getLogger(__name__)

    def solveMaze(self, maze):
        """implement left wall following"""
        """this means: always try going in directions in the following order: left, forward, right, backward"""
        self.maze = maze
        if (maze.getEntrance() == None or maze.getExit() == None):
            self.log.error('Entrance or Exit is missing')
            raise Exception('Entrance or Exit is missing')
        cell = maze.getEntrance()
        self.path.append(cell)
        x = cell.get_x()
        y = cell.get_y()
        if ((x == 0) & (y != 0)):
            self.__tryRight__(cell)
        elif ((x != 0) & (y == 0)):
            self.__tryTop__(cell)
        elif ((x == y == 0) & cell.get_top().isRemoved()):
            self.__tryRight__(cell)
        elif ((x == y == 0) & cell.get_left().isRemoved()):
            self.__tryTop__(cell)
        else:
            self.log.error('Invalid starting cell')
            raise Exception('Invalid starting cell')
        self.__cleanPath__()
        return self.path

    def __tryBottom__(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.get_bottom().isRemoved()):
                cell = self.maze.get_bottom_neighbour(cell)
                self.path.append(cell)
                self.__tryRight__(cell)
            else:
                self.__tryLeft__(cell)

    def __tryLeft__(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.get_left().isRemoved()):
                cell = self.maze.get_left_neighbour(cell)
                self.path.append(cell)
                self.__tryBottom__(cell)
            else:
                self.__tryTop__(cell)

    def __tryTop__(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.get_top().isRemoved()):
                cell = self.maze.get_top_neighbour(cell)
                self.path.append(cell)
                self.__tryLeft__(cell)
            else:
                self.__tryRight__(cell)

    def __tryRight__(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.get_right().isRemoved()):
                cell = self.maze.get_right_neighbour(cell)
                self.path.append(cell)
                self.__tryTop__(cell)
            else:
                self.__tryBottom__(cell)
