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
        if (maze.get_entrance() == None or maze.get_exit() == None):
            self.log.error('Entrance or Exit is missing')
            raise Exception('Entrance or Exit is missing')
        self.walls = {}
        self.junctions = []
        self.path.append(maze.get_entrance())
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
        if (current.get_bottom().isRemoved() and self.maze.get_bottom_neighbour(current) != None):
            self.__mark__(current, current.get_bottom())
            current = self.maze.get_bottom_neighbour(current)
            self.path.append(current)
            self.__decideNext__()

    def __tryLeft__(self):
        current = self.path[-1]
        if (current.get_left().isRemoved() and self.maze.get_left_neighbour(current) != None):
            self.__mark__(current, current.get_left())
            current = self.maze.get_left_neighbour(current)
            self.path.append(current)
            self.__decideNext__()

    def __tryTop__(self):
        current = self.path[-1]
        if (current.get_top().isRemoved() and self.maze.get_top_neighbour(current) != None):
            self.__mark__(current, current.get_top())
            current = self.maze.get_top_neighbour(current)
            self.path.append(current)
            self.__decideNext__()

    def __tryRight__(self):
        current = self.path[-1]
        if (current.get_right().isRemoved() and self.maze.get_right_neighbour(current) != None):
            self.__mark__(current, current.get_right())
            current = self.maze.get_right_neighbour(current)
            self.path.append(current)
            self.__decideNext__()

    # @Override
    def __handleJunction__(self):
        current = self.path[-1]
        if (not current in self.junctions): # new junction
            self.junctions.append(current)
            if (self.__cameFromTop__()):
                self.__mark__(current, current.get_top())
                while (self.__notFinished__()):
                    # arbitrary order
                    self.__tryBottom__()
                    if (self.__notFinished__()):
                        self.__tryLeft__()
                    if (self.__notFinished__()):
                        self.__tryRight__()
            elif (self.__cameFromBottom__()):
                self.__mark__(self.path[-1], self.path[-1].get_bottom())
                while (self.__notFinished__()):
                    # arbitrary order
                    self.__tryLeft__()
                    if (self.__notFinished__()):
                        self.__tryRight__()
                    if (self.__notFinished__()):
                        self.__tryTop__()
            elif (self.__cameFromLeft__()):
                self.__mark__(self.path[-1], self.path[-1].get_left())
                while (self.__notFinished__()):
                    # arbitrary order
                    self.__tryBottom__()
                    if (self.__notFinished__()):
                        self.__tryRight__()
                    if (self.__notFinished__()):
                        self.__tryTop__()
            elif (self.__cameFromRight__()):
                self.__mark__(self.path[-1], self.path[-1].get_right())
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
                if (self.walls[key].count(current.get_top()) > 0): # this way has been taken
                    self.__mark__(current, current.get_top())
                    while (self.__notFinished__() and self.__hasNVisitedPath__(0)):
                        self.__chooseNVisitedPath__(0)
                    while (self.__notFinished__() and self.__hasNVisitedPath__(1)):
                        self.__chooseNVisitedPath__(1)
            elif (self.__cameFromBottom__()):
                if (self.walls[key].count(current.get_bottom()) > 0):
                    self.__mark__(current, current.get_bottom())
                    while (self.__notFinished__() and self.__hasNVisitedPath__(0)):
                        self.__chooseNVisitedPath__(0)
                    while (self.__notFinished__() and self.__hasNVisitedPath__(1)):
                        self.__chooseNVisitedPath__(1)
            elif (self.__cameFromLeft__()):
                if (self.walls[key].count(current.get_left()) > 0):
                    self.__mark__(current, current.get_left())
                    while (self.__notFinished__() and self.__hasNVisitedPath__(0)):
                        self.__chooseNVisitedPath__(0)
                    while (self.__notFinished__() and self.__hasNVisitedPath__(1)):
                        self.__chooseNVisitedPath__(1)
            elif (self.__cameFromRight__()):
                if (self.walls[key].count(current.get_right()) > 0):
                    self.__mark__(current, current.get_right())
                    while (self.__notFinished__() and self.__hasNVisitedPath__(0)):
                        self.__chooseNVisitedPath__(0)
                    while (self.__notFinished__() and self.__hasNVisitedPath__(1)):
                        self.__chooseNVisitedPath__(1)
            else:
                self.log.error('Came from nowhere')
                raise Exception('Came from nowhere')

    def __notFinished__(self):
        current = self.path[-1]
        return current != self.maze.get_exit()

    def __hasNVisitedPath__(self, n):
        current = self.path[-1]
        key = self.__getKey__(current)
        return self.walls[key].count(current.get_left()) == n or self.walls[key].count(current.get_right()) == n or self.walls[key].count(current.get_top()) == n or self.walls[key].count(current.get_bottom()) == n

    def __chooseNVisitedPath__(self, n):
        current = self.path[-1]
        key = self.__getKey__(current)
        if (self.__cameFromBottom__()):
            if (self.walls[key].count(current.get_left()) == n):
                self.__mark__(current, current.get_left())
                self.__tryLeft__()
            elif (self.walls[key].count(current.get_right()) == n):
                self.__mark__(current, current.get_right())
                self.__tryRight__()
            elif (self.walls[key].count(current.get_top()) == n):
                self.__mark__(current, current.get_top())
                self.__tryTop__()
            else:
                self.log.error('Every path from here already visited ' + n + ' times')
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.__cameFromLeft__()):
            if (self.walls[key].count(current.get_bottom()) == n):
                self.__mark__(current, current.get_bottom())
                self.__tryBottom__()
            elif (self.walls[key].count(current.get_right()) == n):
                self.__mark__(current, current.get_right())
                self.__tryRight__()
            elif (self.walls[key].count(current.get_top()) == n):
                self.__mark__(current, current.get_top())
                self.__tryTop__()
            else:
                self.log.error('Every path from here already visited ' + n + ' times')
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.__cameFromRight__()):
            if (self.walls[key].count(current.get_bottom()) == n):
                self.__mark__(current, current.get_bottom())
                self.__tryBottom__()
            elif (self.walls[key].count(current.get_left()) == n):
                self.__mark__(current, current.get_left())
                self.__tryLeft__()
            elif (self.walls[key].count(current.get_top()) == n):
                self.__mark__(current, current.get_top())
                self.__tryTop__()
            else:
                self.log.error('Every path from here already visited ' + n + ' times')
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.__cameFromTop__()):
            if (self.walls[key].count(current.get_bottom()) == n):
                self.__mark__(current, current.get_bottom())
                self.__tryBottom__()
            elif (self.walls[key].count(current.get_left()) == n):
                self.__mark__(current, current.get_left())
                self.__tryLeft__()
            elif (self.walls[key].count(current.get_right()) == n):
                self.__mark__(current, current.get_right())
                self.__tryRight__()
            else:
                self.log.error('Every path from here already visited ' + n + ' times')
                raise Exception('Every path from here already visited ' + n + ' times')
        else:
            self.log.error('Came from nowhere')
            raise Exception('Came from nowhere')

    def __getKey__(self, cell):
        return str(cell.get_x()) + str(cell.get_y())

    def __mark__(self, cell, wall):
        key = self.__getKey__(cell)
        if (not key in self.walls):
            self.walls[key] = []
        self.walls[key].append(wall)
