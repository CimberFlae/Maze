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

    # TODO: Has previous as an argument because TremauxSolver's method does...has to be uniformed and united
    def chooseDirection(self, directions, maze, previous, current):
        n = random.randint(0, len(directions)-1)
        directions[n](maze, current)
