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

    def isDeadEnd(self, cell):
        return cell.wallCount() == 3

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
        if (self.cameFromBottom(maze)):
            if (current.getLeft().isRemoved()):
                self.tryLeft(maze)
            elif (current.getRight().isRemoved()):
                self.tryRight(maze)
            elif (current.getTop().isRemoved()):
                self.tryTop(maze)
            else:
                raise Exception('No way out')
        elif (self.cameFromLeft(maze)):
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze)
            elif (current.getRight().isRemoved()):
                self.tryRight(maze)
            elif (current.getTop().isRemoved()):
                self.tryTop(maze)
            else:
                raise Exception('No way out')
        elif (self.cameFromRight(maze)):
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze)
            elif (current.getLeft().isRemoved()):
                self.tryLeft(maze)
            elif (current.getTop().isRemoved()):
                self.tryTop(maze)
            else:
                raise Exception('No way out')
        elif (self.cameFromTop(maze)):
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze)
            elif (current.getLeft().isRemoved()):
                self.tryLeft(maze)
            elif (current.getRight().isRemoved()):
                self.tryRight(maze)
            else:
                raise Exception('No way out')
        else:
            raise Exception('Came from nowhere')

    def chooseDirection(self, directions, maze):
        n = random.randint(0, len(directions)-1)
        directions[n](maze)

    def decideNext(self, maze):
        current = self.path[-1]
        if self.isJunction(current):
            self.handleJunction(maze)
        elif self.isPath(current):
            self.handlePath(maze)
        elif self.isDeadEnd(current): # do nothing and go back
            self.handleDeadEnd(maze)
        else:
            raise Exception('Invalid wall count')

    def handleJunction(self, maze):
        current = self.path[-1]
        directions = [];
        if (self.cameFromTop(maze)):
            directions = [self.tryBottom, self.tryRight, self.tryLeft]
        elif (self.cameFromBottom(maze)):
            directions = [self.tryTop, self.tryRight, self.tryLeft]
        elif (self.cameFromLeft(maze)):
            directions = [self.tryBottom, self.tryRight, self.tryTop]
        elif (self.cameFromRight(maze)):
            directions = [self.tryBottom, self.tryTop, self.tryLeft]
        else:
            raise Exception('Came from nowhere')
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
        elif (self.cameFromRight(maze)):
            self.tryRight(maze)
        else:
            raise Exception('Came from nowhere')
