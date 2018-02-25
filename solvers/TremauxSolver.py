import solvers.Solver as Solver
import random

class TremauxSolver(Solver.Solver):

    def __init__(self):
        Solver.Solver.__init__(self)

    def solveMaze(self, maze):
        """implement Tremaux's algorithm"""
        if (maze.getEntrance() == None):
            maze.setStandardEntrance()
        if (maze.getExit() == None):
            maze.setStandardExit()
        current = maze.getEntrance()
        previous = None
        self.walls = {}
        self.junctions = []
        self.path.append(current)
        x = maze.getX(current)
        y = maze.getY(current)
        if ((x == 0) & (y != 0)):
            self.tryRandomFromTop(maze, previous, current)
        elif ((x != 0) & (y == 0)):
            self.tryRandomFromLeft(maze, previous, current)
        elif ((x == y == 0) & maze.getTop(current).isRemoved()):
            self.chooseDirection([self.tryBottom, self.tryRight], maze, previous, current)
        while (self.path[-1] != maze.getExit()):    
            self.chooseDirection([self.tryBottom, self.tryLeft, self.tryRight, self.tryTop], maze, previous, current)
        self.cleanPath()
        return self.path

    def tryBottom(self, maze, previous, current):
        if (current.getBottom().isRemoved() and maze.getBottomNeighbour(current) != None):
            self.mark(current, current.getBottom())
            previous = current
            current = maze.getBottomNeighbour(current)
            self.path.append(current)
            self.decideNext(maze, previous, current)

    def tryLeft(self, maze, previous, current):
        if (current.getLeft().isRemoved() and maze.getLeftNeighbour(current) != None):
            self.mark(current, current.getLeft())
            previous = current
            current = maze.getLeftNeighbour(current)
            self.path.append(current)
            self.decideNext(maze, previous, current)

    def tryTop(self, maze, previous, current):
        if (current.getTop().isRemoved() and maze.getTopNeighbour(current) != None):
            self.mark(current, current.getTop())
            previous = current
            current = maze.getTopNeighbour(current)
            self.path.append(current)
            self.decideNext(maze, previous, current)

    def tryRight(self, maze, previous, current):
        if (current.getRight().isRemoved() and maze.getRightNeighbour(current) != None):
            self.mark(current, current.getRight())
            previous = current
            current = maze.getRightNeighbour(current)
            self.path.append(current)
            self.decideNext(maze, previous, current)

    def tryRandomFromTop(self, maze, previous, current):
        list = [self.tryBottom, self.tryLeft, self.tryRight]
        self.chooseDirection(list, maze, previous, current)

    def tryRandomFromBottom(self, maze, previous, current):
        list = [self.tryTop, self.tryLeft, self.tryRight]
        self.chooseDirection(list, maze, previous, current)

    def tryRandomFromLeft(self, maze, previous, current):
        list = [self.tryBottom, self.tryTop, self.tryRight]
        self.chooseDirection(list, maze, previous, current)

    def tryRandomFromRight(self, maze, previous, current):
        list = [self.tryBottom, self.tryLeft, self.tryTop]
        self.chooseDirection(list, maze, previous, current)

    def chooseDirection(self, directions, maze, previous, current):
        n = random.randint(0, len(directions)-1)
        directions[n](maze, previous, current)

    def decideNext(self, maze, previous, current):
        if (current != maze.getExit()):
            if (current.wallCount() < 2): # junction
                if (not current in self.junctions): # new junction
                    self.junctions.append(current)
                    if (self.cameFromTop(maze, previous, current)):
                        self.mark(current, current.getTop())
                        while (self.path[-1] == current and self.path[-1] != maze.getExit()):
                            self.tryRandomFromTop(maze, previous, current)
                    elif (self.cameFromBottom(maze, previous, current)):
                        self.mark(current, current.getBottom())
                        while (self.path[-1] == current and self.path[-1] != maze.getExit()):
                            self.tryRandomFromBottom(maze, previous, current)
                    elif (self.cameFromLeft(maze, previous, current)):
                        self.mark(current, current.getLeft())
                        while (self.path[-1] == current and self.path[-1] != maze.getExit()):
                            self.tryRandomFromLeft(maze, previous, current)
                    else:
                        self.mark(current, current.getRight())
                        while (self.path[-1] == current and self.path[-1] != maze.getExit()):
                            self.tryRandomFromRight(maze, previous, current)
                else: # have been here before
                    key = self.getKey(current)
                    if (self.cameFromTop(maze, previous, current)):
                        if (self.walls[key].count(current.getTop()) > 0): # this way has been taken
                            self.mark(current, current.getTop())
                            while (self.hasNVisitedPath(maze, previous, current, 0) and self.path[-1] != maze.getExit()):
                                self.chooseNVisitedPath(maze, previous, current, 0)
                            while (self.hasNVisitedPath(maze, previous, current, 1) and self.path[-1] != maze.getExit()):
                                self.chooseNVisitedPath(maze, previous, current, 1)
                    elif (self.cameFromBottom(maze, previous, current)):
                        if (self.walls[key].count(current.getBottom()) > 0):
                            self.mark(current, current.getBottom())
                            while (self.hasNVisitedPath(maze, previous, current, 0) and self.path[-1] != maze.getExit()):
                                self.chooseNVisitedPath(maze, previous, current, 0)
                            while (self.hasNVisitedPath(maze, previous, current, 1) and self.path[-1] != maze.getExit()):
                                self.chooseNVisitedPath(maze, previous, current, 1)
                    elif (self.cameFromLeft(maze, previous, current)):
                        if (self.walls[key].count(current.getLeft()) > 0):
                            self.mark(current, current.getLeft())
                            while (self.hasNVisitedPath(maze, previous, current, 0) and self.path[-1] != maze.getExit()):
                                self.chooseNVisitedPath(maze, previous, current, 0)
                            while (self.hasNVisitedPath(maze, previous, current, 1) and self.path[-1] != maze.getExit()):
                                self.chooseNVisitedPath(maze, previous, current, 1)
                    else:
                        if (self.walls[key].count(current.getRight()) > 0):
                            self.mark(current, current.getRight())
                            while (self.hasNVisitedPath(maze, previous, current, 0) and self.path[-1] != maze.getExit()):
                                self.chooseNVisitedPath(maze, previous, current, 0)
                            while (self.hasNVisitedPath(maze, previous, current, 1) and self.path[-1] != maze.getExit()):
                                self.chooseNVisitedPath(maze, previous, current, 1)
            elif (current.wallCount() == 2): # normal path
                self.findNext(maze, previous, current)
            else: # dead end; do nothing and go back
                if (self.cameFromTop(maze, previous, current)):
                    self.tryTop(maze, previous, current)
                elif (self.cameFromBottom(maze, previous, current)):
                    self.tryBottom(maze, previous, current)
                elif (self.cameFromLeft(maze, previous, current)):
                    self.tryLeft(maze, previous, current)
                else:
                    self.tryRight(maze, previous, current)

    # Cannot (currently) use method of abstract class due to different prototype
    def findNext(self, maze, previous, current): # if there is only one way to go
        if (self.cameFromBottom(maze, previous, current)): # came from bottom
            if (current.getLeft().isRemoved()):
                self.tryLeft(maze, previous, current)
            elif (current.getRight().isRemoved()):
                self.tryRight(maze, previous, current)
            else:
                self.tryTop(maze, previous, current)
        elif (self.cameFromLeft(maze, previous, current)): # came from left
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze, previous, current)
            elif (current.getRight().isRemoved()):
                self.tryRight(maze, previous, current)
            else:
                self.tryTop(maze, previous, current)
        elif (self.cameFromRight(maze, previous, current)): # came from right
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze, previous, current)
            elif (current.getLeft().isRemoved()):
                self.tryLeft(maze, previous, current)
            else:
                self.tryTop(maze, previous, current)
        else: # came from top
            if (current.getBottom().isRemoved()):
                self.tryBottom(maze, previous, current)
            elif (current.getLeft().isRemoved()):
                self.tryLeft(maze, previous, current)
            else:
                self.tryRight(maze, previous, current)

    def cameFromTop(self, maze, previous, current):
        return maze.getTopNeighbour(current) == previous

    def cameFromRight(self, maze, previous, current):
        return maze.getRightNeighbour(current) == previous

    def cameFromBottom(self, maze, previous, current):
        return maze.getBottomNeighbour(current) == previous

    def cameFromLeft(self, maze, previous, current):
        return maze.getLeftNeighbour(current) == previous

    def hasNVisitedPath(self, maze, previous, current, n):
        key = self.getKey(current)
        return self.walls[key].count(current.getLeft()) == n or self.walls[key].count(current.getRight()) == n or self.walls[key].count(current.getTop()) == n or self.walls[key].count(current.getBottom()) == n

    def chooseNVisitedPath(self, maze, previous, current, n):
        key = self.getKey(current)
        if (self.cameFromBottom(maze, previous, current)):
            if (self.walls[key].count(current.getLeft()) == n):
                self.mark(current, current.getLeft())
                self.tryLeft(maze, previous, current)
            elif (self.walls[key].count(current.getRight()) == n):
                self.mark(current, current.getRight())
                self.tryRight(maze, previous, current)
            else:
                self.mark(current, current.getTop())
                self.tryTop(maze, previous, current)
        elif (self.cameFromLeft(maze, previous, current)):
            if (self.walls[key].count(current.getBottom()) == n):
                self.mark(current, current.getBottom())
                self.tryBottom(maze, previous, current)
            elif (self.walls[key].count(current.getRight()) == n):
                self.mark(current, current.getRight())
                self.tryRight(maze, previous, current)
            else:
                self.mark(current, current.getTop())
                self.tryTop(maze, previous, current)
        elif (self.cameFromRight(maze, previous, current)):
            if (self.walls[key].count(current.getLeft()) == n):
                self.mark(current, current.getLeft())
                self.tryLeft(maze, previous, current)
            elif (self.walls[key].count(current.getBottom()) == n):
                self.mark(current, current.getBottom())
                self.tryBottom(maze, previous, current)
            else:
                self.mark(current, current.getTop())
                self.tryTop(maze, previous, current)
        else:
            if (self.walls[key].count(current.getLeft()) == n):
                self.mark(current, current.getLeft())
                self.tryLeft(maze, previous, current)
            elif (self.walls[key].count(current.getRight()) == n):
                self.mark(current, current.getRight())
                self.tryRight(maze, previous, current)
            else:
                self.mark(current, current.getBottom())
                self.tryBottom(maze, previous, current)

    def getKey(self, cell):
        return str(cell.getX()) + str(cell.getY())

    def mark(self, cell, wall):
        key = self.getKey(cell)
        if (not key in self.walls):
            self.walls[key] = []
        self.walls[key].append(wall)
