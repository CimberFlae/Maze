import random

class Solver:

    def __init__(self):
        self.path = []
        print("generating a solver")

    def solveMaze(self, maze):
        """implement a solving algorithm"""

    # cleans the path of redundant moves
    def cleanPath(self):
        i = 2
        while (i < len(self.path)):
            if (self.path[i-2] == self.path[i]):
                self.cleanup(i-2, i)
                i = 2
            else:
                i += 1

    def cleanup(self, i, j):
        if (i > 0 and j < len(self.path)-1 and self.path[i-1] == self.path[j+1]):
            self.cleanup(i-1, j+1)
        else:
            del self.path[(i+1):(j+1)]

    def isJunction(self, cell):
        return cell.wallCount() < 2

    def isPath(self, cell):
        return cell.wallCount() == 2

    def cameFromTop(self, maze, previous, current):
        return maze.getTopNeighbour(current) == previous

    def cameFromRight(self, maze, previous, current):
        return maze.getRightNeighbour(current) == previous

    def cameFromBottom(self, maze, previous, current):
        return maze.getBottomNeighbour(current) == previous

    def cameFromLeft(self, maze, previous, current):
        return maze.getLeftNeighbour(current) == previous

    def findNext(self, maze, previous, current): # if there is only one way to go
        if (self.cameFromBottom(maze, previous, current)): # came from bottom
            if (current.getLeft().isRemoved()):
                self.tryLeft(maze, current)
            elif (current.getRight().isRemoved()):
                self.tryRight(maze, current)
            else:
                self.tryTop(maze, current)
        elif (self.cameFromLeft(maze, previous, current)): # came from left
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze, current)
            elif (current.getRight().isRemoved()):
                self.tryRight(maze, current)
            else:
                self.tryTop(maze, current)
        elif (self.cameFromRight(maze, previous, current)): # came from right
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze, current)
            elif (current.getLeft().isRemoved()):
                self.tryLeft(maze, current)
            else:
                self.tryTop(maze, current)
        else: # came from top
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze, current)
            elif (current.getLeft().isRemoved()):
                self.tryLeft(maze, current)
            else:
                self.tryRight(maze, current)

    def chooseDirection(self, directions, maze, current):
        n = random.randint(0, len(directions)-1)
        directions[n](maze, current)

    def decideNext(self, maze, previous, cell):
        if self.isJunction(cell):
            self.handleJunction(maze, previous, cell)
        elif self.isPath(cell):
            self.handlePath(maze, previous, cell)
        else: # dead end; do nothing and go back
            self.handleDeadEnd(maze, previous, cell)

    def handleJunction(self, maze, previous, cell):
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
            self.chooseDirection(directions, maze, cell)

    def handlePath(self, maze, previous, cell):
        self.findNext(maze, previous, cell)

    def handleDeadEnd(self, maze, previous, cell):
        if (self.cameFromTop(maze, previous, cell)):
            self.tryTop(maze, cell)
        elif (self.cameFromBottom(maze, previous, cell)):
            self.tryBottom(maze, cell)
        elif (self.cameFromLeft(maze, previous, cell)):
            self.tryLeft(maze, cell)
        else:
            self.tryRight(maze, cell)
