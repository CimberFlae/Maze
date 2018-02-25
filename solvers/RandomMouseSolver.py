import solvers.Solver as Solver
import random

class RandomMouseSolver(Solver.Solver):

    def __init__(self):
        Solver.Solver.__init__(self)

    def solveMaze(self, maze):
        """implement random mouse algorithm"""
        """this means: always follow a given path to a junction and from there try a direction at random"""
        """caution: this algorithms only terminates in acceptable amount of time for very small paths (often seen in very small mazes)"""
        if (maze.getEntrance() == None):
            maze.setStandardEntrance()
        if (maze.getExit() == None):
            maze.setStandardExit()
        cell = maze.getEntrance()
        self.path.append(cell)
        x = maze.getX(cell)
        y = maze.getY(cell)
        if ((x == 0) & (y != 0)):
            self.tryBottom(maze, cell)
        elif ((x != 0) & (y == 0)):
            self.tryRight(maze, cell)
        elif ((x == y == 0) & maze.getTop(cell).isRemoved()):
            self.tryBottom(maze, cell)
        elif ((x == y == 0) & maze.getLeft(cell).isRemoved()):
            self.tryRight(maze, cell)
        while (self.path[-1] != maze.getExit()):
            self.tryRandom(maze, cell)
        self.cleanPath()
        return self.path

    def tryBottom(self, maze, cell):
        previous = cell
        if (cell != maze.getExit()):
            bottom = maze.getBottom(cell)
            if (bottom.isRemoved() & (not maze.isBorder(cell, bottom))):
                cell = maze.getBottomNeighbour(cell)
                self.path.append(cell)
                self.decideNext(maze, previous, cell)

    def tryLeft(self, maze, cell):
        previous = cell
        if (cell != maze.getExit()):
            left = maze.getLeft(cell)
            if (left.isRemoved() & (not maze.isBorder(cell, left))):
                cell = maze.getLeftNeighbour(cell)
                self.path.append(cell)
                self.decideNext(maze, previous, cell)

    def tryTop(self, maze, cell):
        previous = cell
        if (cell != maze.getExit()):
            top = maze.getTop(cell)
            if (top.isRemoved() & (not maze.isBorder(cell, top))):
                cell = maze.getTopNeighbour(cell)
                self.path.append(cell)
                self.decideNext(maze, previous, cell)

    def tryRight(self, maze, cell):
        previous = cell
        if (cell != maze.getExit()):
            right = maze.getRight(cell)
            if (right.isRemoved() & (not maze.isBorder(cell, right))):
                cell = maze.getRightNeighbour(cell)
                self.path.append(cell)
                self.decideNext(maze, previous, cell)

    def tryRandom(self, maze, cell):
        list = [self.tryBottom, self.tryLeft, self.tryTop, self.tryRight]
        n = random.randint(0, 3)
        return list[n](maze, cell)

    # TODO: put this function (also partially used in TremauxSolver) to abstract Solver
    # and use functions like 'handleJunction', 'handlePath', handleDeadEnd'...
    def decideNext(self, maze, previous, cell):
        if (super(RandomMouseSolver, self).isJunction(cell)):
            directions = [];
            if (self.cameFromTop(maze, previous, cell)):
                directions = [self.tryBottom,  self.tryRight,  self.tryLeft]
            elif (self.cameFromBottom(maze, previous, cell)):
                directions = [self.tryTop,  self.tryRight,  self.tryLeft]
            elif (self.cameFromLeft(maze, previous, cell)):
                directions = [self.tryBottom,  self.tryRight,  self.tryTop]
            else:
                directions = [self.tryBottom,  self.tryTop,  self.tryLeft]
            while (cell == self.path[-1] and cell != maze.getExit()):
                super(RandomMouseSolver, self).chooseDirection(directions, maze, previous, cell)
        elif (cell.wallCount() == 2): # normal path
            super(RandomMouseSolver, self).findNext(maze, previous, cell)
        else: # dead end; do nothing and go back
                if (self.cameFromTop(maze, previous, cell)):
                    self.tryTop(maze, cell)
                elif (self.cameFromBottom(maze, previous, cell)):
                    self.tryBottom(maze, cell)
                elif (self.cameFromLeft(maze, previous, cell)):
                    self.tryLeft(maze, cell)
                else:
                    self.tryRight(maze, cell)
