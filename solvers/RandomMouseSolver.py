import solvers.AbstractSolver as AbstractSolver
import random
import logging

class RandomMouseSolver(AbstractSolver.AbstractSolver):

    def __init__(self):
        AbstractSolver.AbstractSolver.__init__(self)
        self.log = logging.getLogger(__name__)

    def solveMaze(self, maze, seed = 0):
        if (seed != 0):
            random.seed(seed)
        self.maze = maze
        """implement random mouse algorithm"""
        """this means: always follow a given path to a junction and from there try a direction at random"""
        """caution: this algorithms may take longer than anticipated (since it is random)"""
        if (maze.getEntrance() == None or maze.getExit() == None):
            self.log.error('Entrance or Exit is missing')
            raise Exception('Entrance or Exit is missing')
        cell = maze.getEntrance()
        self.path.append(cell)
        while (self.path[-1] != maze.getExit()):
            self.decideNext()
        self.cleanPath()
        return self.path

    def tryBottom(self):
        cell = self.path[-1]
        if (cell != self.maze.getExit()):
            bottom = cell.getBottom()
            if (bottom.isRemoved() & (not self.maze.isBorder(cell, bottom))):
                cell = self.maze.getBottomNeighbour(cell)
                self.path.append(cell)

    def tryLeft(self):
        cell = self.path[-1]
        if (cell != self.maze.getExit()):
            left = cell.getLeft()
            if (left.isRemoved() & (not self.maze.isBorder(cell, left))):
                cell = self.maze.getLeftNeighbour(cell)
                self.path.append(cell)

    def tryTop(self):
        cell = self.path[-1]
        if (cell != self.maze.getExit()):
            top = cell.getTop()
            if (top.isRemoved() & (not self.maze.isBorder(cell, top))):
                cell = self.maze.getTopNeighbour(cell)
                self.path.append(cell)

    def tryRight(self):
        cell = self.path[-1]
        if (cell != self.maze.getExit()):
            right = cell.getRight()
            if (right.isRemoved() & (not self.maze.isBorder(cell, right))):
                cell = self.maze.getRightNeighbour(cell)
                self.path.append(cell)
