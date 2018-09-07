import random

class AbstractSolver:

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
        return cell.wallCount() == 2 and cell != self.maze.getEntrance()

    def isDeadEnd(self, cell):
        return cell.wallCount() == 3 or cell.wallCount() == 2 and cell == self.maze.getEntrance()

    def cameFromTop(self):
        previous = self.getPrevious()
        return previous != None and self.maze.getTopNeighbour(self.path[-1]) == previous

    def cameFromRight(self):
        previous = self.getPrevious()
        return previous != None and self.maze.getRightNeighbour(self.path[-1]) == previous

    def cameFromBottom(self):
        previous = self.getPrevious()
        return previous != None and self.maze.getBottomNeighbour(self.path[-1]) == previous

    def cameFromLeft(self):
        previous = self.getPrevious()
        return previous != None and self.maze.getLeftNeighbour(self.path[-1]) == previous

    def getPrevious(self):
        return self.path[-2] if len(self.path) > 1 else None

    def findNext(self): # if there is only one way to go
        current = self.path[-1]
        if (self.cameFromBottom()):
            if (current.getLeft().isRemoved()):
                self.tryLeft()
            elif (current.getRight().isRemoved()):
                self.tryRight()
            elif (current.getTop().isRemoved()):
                self.tryTop()
            else:
                raise Exception('No way out')
        elif (self.cameFromLeft()):
            if (current.getBottom().isRemoved()):
                self.tryBottom()
            elif (current.getRight().isRemoved()):
                self.tryRight()
            elif (current.getTop().isRemoved()):
                self.tryTop()
            else:
                raise Exception('No way out')
        elif (self.cameFromRight()):
            if (current.getBottom().isRemoved()):
                self.tryBottom()
            elif (current.getLeft().isRemoved()):
                self.tryLeft()
            elif (current.getTop().isRemoved()):
                self.tryTop()
            else:
                raise Exception('No way out')
        elif (self.cameFromTop()):
            if (current.getBottom().isRemoved()):
                self.tryBottom()
            elif (current.getLeft().isRemoved()):
                self.tryLeft()
            elif (current.getRight().isRemoved()):
                self.tryRight()
            else:
                raise Exception('No way out')
        elif (self.path[-1] == self.maze.getEntrance()): # We're at the entrance
            self.handleJunction()
        else:
            raise Exception('Came from nowhere')

    def chooseDirection(self, directions):
        n = random.randint(0, len(directions)-1)
        directions[n]()

    def decideNext(self):
        current = self.path[-1]
        if self.isJunction(current):
            self.handleJunction()
        elif self.isPath(current):
            self.handlePath()
        elif self.isDeadEnd(current): # do nothing and go back
            self.handleDeadEnd()
        else:
            raise Exception('Invalid wall count')

    def handleJunction(self):
        current = self.path[-1]
        directions = [];
        if (self.cameFromTop()):
            directions = [self.tryBottom, self.tryLeft, self.tryRight]
        elif (self.cameFromBottom()):
            directions = [self.tryLeft, self.tryRight, self.tryTop]
        elif (self.cameFromLeft()):
            directions = [self.tryBottom, self.tryRight, self.tryTop]
        elif (self.cameFromRight()):
            directions = [self.tryBottom, self.tryLeft, self.tryTop]
        elif (self.path[-1] == self.maze.getEntrance()): # We're at the entrance
            directions = [self.tryBottom, self.tryLeft, self.tryRight, self.tryTop]
        else:
            raise Exception('Came from nowhere')
        while (current == self.path[-1] and current != self.maze.getExit()):
            self.chooseDirection(directions)

    def handlePath(self):
        self.findNext()

    def handleDeadEnd(self):
        if (self.cameFromTop()):
            self.tryTop()
        elif (self.cameFromBottom()):
            self.tryBottom()
        elif (self.cameFromLeft()):
            self.tryLeft()
        elif (self.cameFromRight()):
            self.tryRight()
        elif (self.path[-1] == self.maze.getEntrance()): # We're at the entrance
            self.handleJunction()
        else:
            raise Exception('Came from nowhere')
