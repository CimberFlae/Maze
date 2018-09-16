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
        x = cell.getX()
        y = cell.getY()
        if ((x == 0) & (y != 0)):
            self.__tryRight__(cell)
        elif ((x != 0) & (y == 0)):
            self.__tryTop__(cell)
        elif ((x == y == 0) & cell.getTop().isRemoved()):
            self.__tryRight__(cell)
        elif ((x == y == 0) & cell.getLeft().isRemoved()):
            self.__tryTop__(cell)
        else:
            self.log.error('Invalid starting cell')
            raise Exception('Invalid starting cell')
        self.__cleanPath__()
        return self.path

    def __tryBottom__(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.getBottom().isRemoved()):
                cell = self.maze.getBottomNeighbour(cell)
                self.path.append(cell)
                self.__tryRight__(cell)
            else:
                self.__tryLeft__(cell)

    def __tryLeft__(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.getLeft().isRemoved()):
                cell = self.maze.getLeftNeighbour(cell)
                self.path.append(cell)
                self.__tryBottom__(cell)
            else:
                self.__tryTop__(cell)

    def __tryTop__(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.getTop().isRemoved()):
                cell = self.maze.getTopNeighbour(cell)
                self.path.append(cell)
                self.__tryLeft__(cell)
            else:
                self.__tryRight__(cell)

    def __tryRight__(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.getRight().isRemoved()):
                cell = self.maze.getRightNeighbour(cell)
                self.path.append(cell)
                self.__tryTop__(cell)
            else:
                self.__tryBottom__(cell)
