import solvers.Solver as Solver
import random

class RandomMouseSolver(Solver.Solver):

    def __init__(self):
        Solver.Solver.__init__(self)

    def solveMaze(self, maze, seed = 0):
        if (seed != 0):
            random.seed(seed)
        """implement random mouse algorithm"""
        """this means: always follow a given path to a junction and from there try a direction at random"""
        """caution: this algorithms may take longer than anticipated (since it is random)"""
        if (maze.getEntrance() == None):
            maze.setCustomOpening(0, 0)
        if (maze.getExit() == None):
            maze.setCustomOpening(maze.getSize() - 1, maze.getSize() - 1)
        cell = maze.getEntrance()
        self.path.append(cell)
        while (self.path[-1] != maze.getExit()):
            self.decideNext(maze)
        self.cleanPath()
        return self.path

    def tryBottom(self, maze):
        cell = self.path[-1]
        if (cell != maze.getExit()):
            bottom = cell.getBottom()
            if (bottom.isRemoved() & (not maze.isBorder(cell, bottom))):
                cell = maze.getBottomNeighbour(cell)
                self.path.append(cell)

    def tryLeft(self, maze):
        cell = self.path[-1]
        if (cell != maze.getExit()):
            left = cell.getLeft()
            if (left.isRemoved() & (not maze.isBorder(cell, left))):
                cell = maze.getLeftNeighbour(cell)
                self.path.append(cell)

    def tryTop(self, maze):
        cell = self.path[-1]
        if (cell != maze.getExit()):
            top = cell.getTop()
            if (top.isRemoved() & (not maze.isBorder(cell, top))):
                cell = maze.getTopNeighbour(cell)
                self.path.append(cell)

    def tryRight(self, maze):
        cell = self.path[-1]
        if (cell != maze.getExit()):
            right = cell.getRight()
            if (right.isRemoved() & (not maze.isBorder(cell, right))):
                cell = maze.getRightNeighbour(cell)
                self.path.append(cell)

    def tryRandom(self, maze, cell):
        list = [self.tryBottom, self.tryLeft, self.tryTop, self.tryRight]
        n = random.randint(0, 3)
        return list[n](maze, cell)
