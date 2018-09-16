import solvers.AbstractSolver as AbstractSolver
import logging

class TremauxSolver(AbstractSolver.AbstractSolver):

    def __init__(self):
        AbstractSolver.AbstractSolver.__init__(self)
        self.log = logging.getLogger(__name__)

    def solveMaze(self, maze):
        self.path = []
        self.maze = maze;
        """implement Tremaux's algorithm"""
        if (maze.getEntrance() == None or maze.getExit() == None):
            self.log.error('Entrance or Exit is missing')
            raise Exception('Entrance or Exit is missing')
        self.walls = {}
        self.junctions = []
        self.path.append(maze.getEntrance())
        self.__tryBottom__() # arbitrary choice to start with
        # arbitrary order of directions
        self.__tryBottom__()
        if (self.__notFinished__()):
            self.__tryLeft__()
        if (self.__notFinished__()):
            self.__tryRight__()
        if (self.__notFinished__()):
            self.__tryTop__()
        self.__cleanPath__()
        return self.path

    def __tryBottom__(self):
        current = self.path[-1]
        if (current.getBottom().isRemoved() and self.maze.getBottomNeighbour(current) != None):
            self.__mark__(current, current.getBottom())
            current = self.maze.getBottomNeighbour(current)
            self.path.append(current)
            self.__decideNext__()

    def __tryLeft__(self):
        current = self.path[-1]
        if (current.getLeft().isRemoved() and self.maze.getLeftNeighbour(current) != None):
            self.__mark__(current, current.getLeft())
            current = self.maze.getLeftNeighbour(current)
            self.path.append(current)
            self.__decideNext__()

    def __tryTop__(self):
        current = self.path[-1]
        if (current.getTop().isRemoved() and self.maze.getTopNeighbour(current) != None):
            self.__mark__(current, current.getTop())
            current = self.maze.getTopNeighbour(current)
            self.path.append(current)
            self.__decideNext__()

    def __tryRight__(self):
        current = self.path[-1]
        if (current.getRight().isRemoved() and self.maze.getRightNeighbour(current) != None):
            self.__mark__(current, current.getRight())
            current = self.maze.getRightNeighbour(current)
            self.path.append(current)
            self.__decideNext__()

    # @Override
    def __handleJunction__(self):
        current = self.path[-1]
        if (not current in self.junctions): # new junction
            self.junctions.append(current)
            if (self.__cameFromTop__()):
                self.__mark__(current, current.getTop())
                while (self.__notFinished__()):
                    # arbitrary order
                    self.__tryBottom__()
                    if (self.__notFinished__()):
                        self.__tryLeft__()
                    if (self.__notFinished__()):
                        self.__tryRight__()
            elif (self.__cameFromBottom__()):
                self.__mark__(self.path[-1], self.path[-1].getBottom())
                while (self.__notFinished__()):
                    # arbitrary order
                    self.__tryLeft__()
                    if (self.__notFinished__()):
                        self.__tryRight__()
                    if (self.__notFinished__()):
                        self.__tryTop__()
            elif (self.__cameFromLeft__()):
                self.__mark__(self.path[-1], self.path[-1].getLeft())
                while (self.__notFinished__()):
                    # arbitrary order
                    self.__tryBottom__()
                    if (self.__notFinished__()):
                        self.__tryRight__()
                    if (self.__notFinished__()):
                        self.__tryTop__()
            elif (self.__cameFromRight__()):
                self.__mark__(self.path[-1], self.path[-1].getRight())
                while (self.__notFinished__()):
                    # arbitrary order
                    self.__tryBottom__()
                    if (self.__notFinished__()):
                        self.__tryLeft__()
                    if (self.__notFinished__()):
                        self.__tryTop__()
            else:
                self.log.error('Came from nowhere')
                raise Exception('Came from nowhere')
        else: # have been here before
            key = self.__getKey__(current)
            if (self.__cameFromTop__()):
                if (self.walls[key].count(current.getTop()) > 0): # this way has been taken
                    self.__mark__(current, current.getTop())
                    while (self.__notFinished__() and self.__hasNVisitedPath__(0)):
                        self.__chooseNVisitedPath__(0)
                    while (self.__notFinished__() and self.__hasNVisitedPath__(1)):
                        self.__chooseNVisitedPath__(1)
            elif (self.__cameFromBottom__()):
                if (self.walls[key].count(current.getBottom()) > 0):
                    self.__mark__(current, current.getBottom())
                    while (self.__notFinished__() and self.__hasNVisitedPath__(0)):
                        self.__chooseNVisitedPath__(0)
                    while (self.__notFinished__() and self.__hasNVisitedPath__(1)):
                        self.__chooseNVisitedPath__(1)
            elif (self.__cameFromLeft__()):
                if (self.walls[key].count(current.getLeft()) > 0):
                    self.__mark__(current, current.getLeft())
                    while (self.__notFinished__() and self.__hasNVisitedPath__(0)):
                        self.__chooseNVisitedPath__(0)
                    while (self.__notFinished__() and self.__hasNVisitedPath__(1)):
                        self.__chooseNVisitedPath__(1)
            elif (self.__cameFromRight__()):
                if (self.walls[key].count(current.getRight()) > 0):
                    self.__mark__(current, current.getRight())
                    while (self.__notFinished__() and self.__hasNVisitedPath__(0)):
                        self.__chooseNVisitedPath__(0)
                    while (self.__notFinished__() and self.__hasNVisitedPath__(1)):
                        self.__chooseNVisitedPath__(1)
            else:
                self.log.error('Came from nowhere')
                raise Exception('Came from nowhere')

    def __notFinished__(self):
        current = self.path[-1]
        return current != self.maze.getExit()

    def __hasNVisitedPath__(self, n):
        current = self.path[-1]
        key = self.__getKey__(current)
        return self.walls[key].count(current.getLeft()) == n or self.walls[key].count(current.getRight()) == n or self.walls[key].count(current.getTop()) == n or self.walls[key].count(current.getBottom()) == n

    def __chooseNVisitedPath__(self, n):
        current = self.path[-1]
        key = self.__getKey__(current)
        if (self.__cameFromBottom__()):
            if (self.walls[key].count(current.getLeft()) == n):
                self.__mark__(current, current.getLeft())
                self.__tryLeft__()
            elif (self.walls[key].count(current.getRight()) == n):
                self.__mark__(current, current.getRight())
                self.__tryRight__()
            elif (self.walls[key].count(current.getTop()) == n):
                self.__mark__(current, current.getTop())
                self.__tryTop__()
            else:
                self.log.error('Every path from here already visited ' + n + ' times')
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.__cameFromLeft__()):
            if (self.walls[key].count(current.getBottom()) == n):
                self.__mark__(current, current.getBottom())
                self.__tryBottom__()
            elif (self.walls[key].count(current.getRight()) == n):
                self.__mark__(current, current.getRight())
                self.__tryRight__()
            elif (self.walls[key].count(current.getTop()) == n):
                self.__mark__(current, current.getTop())
                self.__tryTop__()
            else:
                self.log.error('Every path from here already visited ' + n + ' times')
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.__cameFromRight__()):
            if (self.walls[key].count(current.getBottom()) == n):
                self.__mark__(current, current.getBottom())
                self.__tryBottom__()
            elif (self.walls[key].count(current.getLeft()) == n):
                self.__mark__(current, current.getLeft())
                self.__tryLeft__()
            elif (self.walls[key].count(current.getTop()) == n):
                self.__mark__(current, current.getTop())
                self.__tryTop__()
            else:
                self.log.error('Every path from here already visited ' + n + ' times')
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.__cameFromTop__()):
            if (self.walls[key].count(current.getBottom()) == n):
                self.__mark__(current, current.getBottom())
                self.__tryBottom__()
            elif (self.walls[key].count(current.getLeft()) == n):
                self.__mark__(current, current.getLeft())
                self.__tryLeft__()
            elif (self.walls[key].count(current.getRight()) == n):
                self.__mark__(current, current.getRight())
                self.__tryRight__()
            else:
                self.log.error('Every path from here already visited ' + n + ' times')
                raise Exception('Every path from here already visited ' + n + ' times')
        else:
            self.log.error('Came from nowhere')
            raise Exception('Came from nowhere')

    def __getKey__(self, cell):
        return str(cell.getX()) + str(cell.getY())

    def __mark__(self, cell, wall):
        key = self.__getKey__(cell)
        if (not key in self.walls):
            self.walls[key] = []
        self.walls[key].append(wall)
