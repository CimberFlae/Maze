import solvers.Solver as Solver

class TremauxSolver(Solver.Solver):

    def __init__(self):
        Solver.Solver.__init__(self)

    def solveMaze(self, maze):
        self.path = []
        self.maze = maze;
        """implement Tremaux's algorithm"""
        if (maze.getEntrance() == None):
            maze.setCustomOpening(0, 0)
        if (maze.getExit() == None):
            maze.setCustomOpening(maze.getSize() - 1, maze.getSize() - 1)
        self.walls = {}
        self.junctions = []
        self.path.append(maze.getEntrance())
        self.tryBottom() # arbitrary choice to start with
        # arbitrary order of directions
        self.tryBottom()
        if (self.notFinished()):
            self.tryLeft()
        if (self.notFinished()):
            self.tryRight()
        if (self.notFinished()):
            self.tryTop()
        self.cleanPath()
        return self.path

    def tryBottom(self):
        current = self.path[-1]
        if (current.getBottom().isRemoved() and self.maze.getBottomNeighbour(current) != None):
            self.mark(current, current.getBottom())
            current = self.maze.getBottomNeighbour(current)
            self.path.append(current)
            self.decideNext()

    def tryLeft(self):
        current = self.path[-1]
        if (current.getLeft().isRemoved() and self.maze.getLeftNeighbour(current) != None):
            self.mark(current, current.getLeft())
            current = self.maze.getLeftNeighbour(current)
            self.path.append(current)
            self.decideNext()

    def tryTop(self):
        current = self.path[-1]
        if (current.getTop().isRemoved() and self.maze.getTopNeighbour(current) != None):
            self.mark(current, current.getTop())
            current = self.maze.getTopNeighbour(current)
            self.path.append(current)
            self.decideNext()

    def tryRight(self):
        current = self.path[-1]
        if (current.getRight().isRemoved() and self.maze.getRightNeighbour(current) != None):
            self.mark(current, current.getRight())
            current = self.maze.getRightNeighbour(current)
            self.path.append(current)
            self.decideNext()

    # @Override
    def handleJunction(self):
        current = self.path[-1]
        if (not current in self.junctions): # new junction
            self.junctions.append(current)
            if (self.cameFromTop()):
                self.mark(current, current.getTop())
                while (self.notFinished()):
                    # arbitrary order
                    self.tryBottom()
                    if (self.notFinished()):
                        self.tryLeft()
                    if (self.notFinished()):
                        self.tryRight()
            elif (self.cameFromBottom()):
                self.mark(self.path[-1], self.path[-1].getBottom())
                while (self.notFinished()):
                    # arbitrary order
                    self.tryLeft()
                    if (self.notFinished()):
                        self.tryRight()
                    if (self.notFinished()):
                        self.tryTop()
            elif (self.cameFromLeft()):
                self.mark(self.path[-1], self.path[-1].getLeft())
                while (self.notFinished()):
                    # arbitrary order
                    self.tryBottom()
                    if (self.notFinished()):
                        self.tryRight()
                    if (self.notFinished()):
                        self.tryTop()
            elif (self.cameFromRight()):
                self.mark(self.path[-1], self.path[-1].getRight())
                while (self.notFinished()):
                    # arbitrary order
                    self.tryBottom()
                    if (self.notFinished()):
                        self.tryLeft()
                    if (self.notFinished()):
                        self.tryTop()
            else:
                raise Exception('Came from nowhere')
        else: # have been here before
            key = self.getKey(current)
            if (self.cameFromTop()):
                if (self.walls[key].count(current.getTop()) > 0): # this way has been taken
                    self.mark(current, current.getTop())
                    while (self.notFinished() and self.hasNVisitedPath(0)):
                        self.chooseNVisitedPath(0)
                    while (self.notFinished() and self.hasNVisitedPath(1)):
                        self.chooseNVisitedPath(1)
            elif (self.cameFromBottom()):
                if (self.walls[key].count(current.getBottom()) > 0):
                    self.mark(current, current.getBottom())
                    while (self.notFinished() and self.hasNVisitedPath(0)):
                        self.chooseNVisitedPath(0)
                    while (self.notFinished() and self.hasNVisitedPath(1)):
                        self.chooseNVisitedPath(1)
            elif (self.cameFromLeft()):
                if (self.walls[key].count(current.getLeft()) > 0):
                    self.mark(current, current.getLeft())
                    while (self.notFinished() and self.hasNVisitedPath(0)):
                        self.chooseNVisitedPath(0)
                    while (self.notFinished() and self.hasNVisitedPath(1)):
                        self.chooseNVisitedPath(1)
            elif (self.cameFromRight()):
                if (self.walls[key].count(current.getRight()) > 0):
                    self.mark(current, current.getRight())
                    while (self.notFinished() and self.hasNVisitedPath(0)):
                        self.chooseNVisitedPath(0)
                    while (self.notFinished() and self.hasNVisitedPath(1)):
                        self.chooseNVisitedPath(1)
            else:
                raise Exception('Came from nowhere')

    def notFinished(self):
        current = self.path[-1]
        return current != self.maze.getExit()

    def hasNVisitedPath(self, n):
        current = self.path[-1]
        key = self.getKey(current)
        return self.walls[key].count(current.getLeft()) == n or self.walls[key].count(current.getRight()) == n or self.walls[key].count(current.getTop()) == n or self.walls[key].count(current.getBottom()) == n

    def chooseNVisitedPath(self, n):
        current = self.path[-1]
        key = self.getKey(current)
        if (self.cameFromBottom()):
            if (self.walls[key].count(current.getLeft()) == n):
                self.mark(current, current.getLeft())
                self.tryLeft()
            elif (self.walls[key].count(current.getRight()) == n):
                self.mark(current, current.getRight())
                self.tryRight()
            elif (self.walls[key].count(current.getTop()) == n):
                self.mark(current, current.getTop())
                self.tryTop()
            else:
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.cameFromLeft()):
            if (self.walls[key].count(current.getBottom()) == n):
                self.mark(current, current.getBottom())
                self.tryBottom()
            elif (self.walls[key].count(current.getRight()) == n):
                self.mark(current, current.getRight())
                self.tryRight()
            elif (self.walls[key].count(current.getTop()) == n):
                self.mark(current, current.getTop())
                self.tryTop()
            else:
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.cameFromRight()):
            if (self.walls[key].count(current.getBottom()) == n):
                self.mark(current, current.getBottom())
                self.tryBottom()
            elif (self.walls[key].count(current.getLeft()) == n):
                self.mark(current, current.getLeft())
                self.tryLeft()
            elif (self.walls[key].count(current.getTop()) == n):
                self.mark(current, current.getTop())
                self.tryTop()
            else:
                raise Exception('Every path from here already visited ' + n + ' times')
        elif (self.cameFromTop()):
            if (self.walls[key].count(current.getBottom()) == n):
                self.mark(current, current.getBottom())
                self.tryBottom()
            elif (self.walls[key].count(current.getLeft()) == n):
                self.mark(current, current.getLeft())
                self.tryLeft()
            elif (self.walls[key].count(current.getRight()) == n):
                self.mark(current, current.getRight())
                self.tryRight()
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
