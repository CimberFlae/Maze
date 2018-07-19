import solvers.Solver as Solver
import random

class RandomMouseSolver(Solver.Solver):

    def __init__(self):
        Solver.Solver.__init__(self)

    def solveMaze(self, maze, seed = 0):
        if (seed != 0):
            random.seed(seed)
        self.maze = maze
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

    def tryRandom(self, cell):
        list = [self.tryBottom, self.tryLeft, self.tryTop, self.tryRight]
        n = random.randint(0, 3)
        return list[n](cell)
