import solvers.Solver as Solver

class TremauxSolver(Solver.Solver):

    def __init__(self):
        Solver.Solver.__init__(self)

    def solveMaze(self, maze):
        self.path = []
        """implement Tremaux's algorithm"""
        if (maze.getEntrance() == None):
            maze.setCustomOpening(0, 0)
        if (maze.getExit() == None):
            maze.setCustomOpening(maze.getSize() - 1, maze.getSize() - 1)
        self.walls = {}
        self.junctions = []
        self.path.append(maze.getEntrance())
        self.tryBottom(maze) # arbitrary choice to start with
        # arbitrary order of directions
        self.tryBottom(maze)
        if (self.notFinished(maze)):
            self.tryLeft(maze)
        if (self.notFinished(maze)):
            self.tryRight(maze)
        if (self.notFinished(maze)):
            self.tryTop(maze)
        self.cleanPath()
        return self.path

    def tryBottom(self, maze):
        current = self.path[-1]
        if (current.getBottom().isRemoved() and maze.getBottomNeighbour(current) != None):
            self.mark(current, current.getBottom())
            current = maze.getBottomNeighbour(current)
            self.path.append(current)
            self.decideNext(maze)

    def tryLeft(self, maze):
        current = self.path[-1]
        if (current.getLeft().isRemoved() and maze.getLeftNeighbour(current) != None):
            self.mark(current, current.getLeft())
            current = maze.getLeftNeighbour(current)
            self.path.append(current)
            self.decideNext(maze)

    def tryTop(self, maze):
        current = self.path[-1]
        if (current.getTop().isRemoved() and maze.getTopNeighbour(current) != None):
            self.mark(current, current.getTop())
            current = maze.getTopNeighbour(current)
            self.path.append(current)
            self.decideNext(maze)

    def tryRight(self, maze):
        current = self.path[-1]
        if (current.getRight().isRemoved() and maze.getRightNeighbour(current) != None):
            self.mark(current, current.getRight())
            current = maze.getRightNeighbour(current)
            self.path.append(current)
            self.decideNext(maze)

    # @Override
    def handleJunction(self, maze):
        current = self.path[-1]
        if (not current in self.junctions): # new junction
            self.junctions.append(current)
            if (self.cameFromTop(maze)):
                self.mark(current, current.getTop())
                while (self.notFinished(maze)):
                    # arbitrary order
                    self.tryBottom(maze)
                    if (self.notFinished(maze)):
                        self.tryLeft(maze)
                    if (self.notFinished(maze)):
                        self.tryRight(maze)
            elif (self.cameFromBottom(maze)):
                self.mark(self.path[-1], self.path[-1].getBottom())
                while (self.notFinished(maze)):
                    # arbitrary order
                    self.tryTop(maze)
                    if (self.notFinished(maze)):
                        self.tryLeft(maze)
                    if (self.notFinished(maze)):
                        self.tryRight(maze)
            elif (self.cameFromLeft(maze)):
                self.mark(self.path[-1], self.path[-1].getLeft())
                while (self.notFinished(maze)):
                    # arbitrary order
                    self.tryBottom(maze)
                    if (self.notFinished(maze)):
                        self.tryTop(maze)
                    if (self.notFinished(maze)):
                        self.tryRight(maze)
            elif (self.cameFromRight(maze)):
                self.mark(self.path[-1], self.path[-1].getRight())
                while (self.notFinished(maze)):
                    # arbitrary order
                    self.tryBottom(maze)
                    if (self.notFinished(maze)):
                        self.tryLeft(maze)
                    if (self.notFinished(maze)):
                        self.tryTop(maze)
            else:
                raise Exception('Came from nowhere')
        else: # have been here before
            key = self.getKey(current)
            if (self.cameFromTop(maze)):
                if (self.walls[key].count(current.getTop()) > 0): # this way has been taken
                    self.mark(current, current.getTop())
                    while (self.notFinished(maze) and self.hasNVisitedPath(maze, 0)):
                        self.chooseNVisitedPath(maze, 0)
                    while (self.notFinished(maze) and self.hasNVisitedPath(maze, 1)):
                        self.chooseNVisitedPath(maze, 1)
            elif (self.cameFromBottom(maze)):
                if (self.walls[key].count(current.getBottom()) > 0):
                    self.mark(current, current.getBottom())
                    while (self.notFinished(maze) and self.hasNVisitedPath(maze, 0)):
                        self.chooseNVisitedPath(maze, 0)
                    while (self.notFinished(maze) and self.hasNVisitedPath(maze, 1)):
                        self.chooseNVisitedPath(maze, 1)
            elif (self.cameFromLeft(maze)):
                if (self.walls[key].count(current.getLeft()) > 0):
                    self.mark(current, current.getLeft())
                    while (self.notFinished(maze) and self.hasNVisitedPath(maze, 0)):
                        self.chooseNVisitedPath(maze, 0)
                    while (self.notFinished(maze) and self.hasNVisitedPath(maze, 1)):
                        self.chooseNVisitedPath(maze, 1)
            elif (self.cameFromRight(maze)):
                if (self.walls[key].count(current.getRight()) > 0):
                    self.mark(current, current.getRight())
                    while (self.notFinished(maze) and self.hasNVisitedPath(maze, 0)):
                        self.chooseNVisitedPath(maze, 0)
                    while (self.notFinished(maze) and self.hasNVisitedPath(maze, 1)):
                        self.chooseNVisitedPath(maze, 1)
            else:
                raise Exception('Came from nowhere')

    def notFinished(self, maze):
        current = self.path[-1]
        return current != maze.getExit()

    def hasNVisitedPath(self, maze, n):
        current = self.path[-1]
        key = self.getKey(current)
        return self.walls[key].count(current.getLeft()) == n or self.walls[key].count(current.getRight()) == n or self.walls[key].count(current.getTop()) == n or self.walls[key].count(current.getBottom()) == n

    def chooseNVisitedPath(self, maze, n):
        current = self.path[-1]
        key = self.getKey(current)
        if (self.cameFromBottom(maze)):
            if (self.walls[key].count(current.getLeft()) == n):
                self.mark(current, current.getLeft())
                self.tryLeft(maze)
            elif (self.walls[key].count(current.getRight()) == n):
                self.mark(current, current.getRight())
                self.tryRight(maze)
            elif (self.walls[key].count(current.getTop()) == n):
                self.mark(current, current.getTop())
                self.tryTop(maze)
            else:
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.cameFromLeft(maze)):
            if (self.walls[key].count(current.getBottom()) == n):
                self.mark(current, current.getBottom())
                self.tryBottom(maze)
            elif (self.walls[key].count(current.getRight()) == n):
                self.mark(current, current.getRight())
                self.tryRight(maze)
            elif (self.walls[key].count(current.getTop()) == n):
                self.mark(current, current.getTop())
                self.tryTop(maze)
            else:
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.cameFromRight(maze)):
            if (self.walls[key].count(current.getLeft()) == n):
                self.mark(current, current.getLeft())
                self.tryLeft(maze)
            elif (self.walls[key].count(current.getBottom()) == n):
                self.mark(current, current.getBottom())
                self.tryBottom(maze)
            elif (self.walls[key].count(current.getTop()) == n):
                self.mark(current, current.getTop())
                self.tryTop(maze)
            else:
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.cameFromTop(maze)):
            if (self.walls[key].count(current.getLeft()) == n):
                self.mark(current, current.getLeft())
                self.tryLeft(maze)
            elif (self.walls[key].count(current.getRight()) == n):
                self.mark(current, current.getRight())
                self.tryRight(maze)
            elif (self.walls[key].count(current.getBottom()) == n):
                self.mark(current, current.getBottom())
                self.tryBottom(maze)
            else:
                raise Exception('Every path from here already visited ' + n + ' times')
        else:
            raise Exception('Came from nowhere')

    def getKey(self, cell):
        return str(cell.getX()) + str(cell.getY())

    def mark(self, cell, wall):
        key = self.getKey(cell)
        if (not key in self.walls):
            self.walls[key] = []
        self.walls[key].append(wall)
