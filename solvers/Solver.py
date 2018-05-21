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

    def cameFromTop(self, maze):
        previous = self.getPrevious()
        return maze.getTopNeighbour(self.path[-1]) == previous

    def cameFromRight(self, maze):
        previous = self.getPrevious()
        return maze.getRightNeighbour(self.path[-1]) == previous

    def cameFromBottom(self, maze):
        previous = self.getPrevious()
        return maze.getBottomNeighbour(self.path[-1]) == previous

    def cameFromLeft(self, maze):
        previous = self.getPrevious()
        return maze.getLeftNeighbour(self.path[-1]) == previous

    def getPrevious(self):
        return self.path[-2] if len(self.path) > 1 else None

    def findNext(self, maze): # if there is only one way to go
        current = self.path[-1]
        if (self.cameFromBottom(maze)): # came from bottom
            if (current.getLeft().isRemoved()):
                self.tryLeft(maze)
            elif (current.getRight().isRemoved()):
                self.tryRight(maze)
            else:
                self.tryTop(maze)
        elif (self.cameFromLeft(maze)): # came from left
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze)
            elif (current.getRight().isRemoved()):
                self.tryRight(maze)
            else:
                self.tryTop(maze)
        elif (self.cameFromRight(maze)): # came from right
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze)
            elif (current.getLeft().isRemoved()):
                self.tryLeft(maze)
            else:
                self.tryTop(maze)
        else: # came from top
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze)
            elif (current.getLeft().isRemoved()):
                self.tryLeft(maze)
            else:
                self.tryRight(maze)

    def chooseDirection(self, directions, maze):
        n = random.randint(0, len(directions)-1)
        directions[n](maze)

    def decideNext(self, maze):
        current = self.path[-1]
        if self.isJunction(current):
            self.handleJunction(maze)
        elif self.isPath(current):
            self.handlePath(maze)
        else: # dead end; do nothing and go back
            self.handleDeadEnd(maze)

    def handleJunction(self, maze):
        current = self.path[-1]
        directions = [];
        if (self.cameFromTop(maze)):
            directions = [self.tryBottom, self.tryRight, self.tryLeft]
        elif (self.cameFromBottom(maze)):
            directions = [self.tryTop, self.tryRight, self.tryLeft]
        elif (self.cameFromLeft(maze)):
            directions = [self.tryBottom, self.tryRight, self.tryTop]
        else:
            directions = [self.tryBottom, self.tryTop, self.tryLeft]
        while (current == self.path[-1] and current != maze.getExit()):
            self.chooseDirection(directions, maze)

    def handlePath(self, maze):
        self.findNext(maze)

    def handleDeadEnd(self, maze):
        if (self.cameFromTop(maze)):
            self.tryTop(maze)
        elif (self.cameFromBottom(maze)):
            self.tryBottom(maze)
        elif (self.cameFromLeft(maze)):
            self.tryLeft(maze)
        else:
            self.tryRight(maze)
