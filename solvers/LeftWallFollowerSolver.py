import solvers.AbstractSolver as AbstractSolver

class LeftWallFollowerSolver(AbstractSolver.AbstractSolver):

    def __init__(self):
        AbstractSolver.AbstractSolver.__init__(self)

    def solveMaze(self, maze):
        """implement left wall following"""
        """this means: always try going in directions in the following order: left, forward, right, backward"""
        self.maze = maze
        if (maze.getEntrance() == None):
            maze.setCustomOpening(0, 0)
        if (maze.getExit() == None):
            maze.setCustomOpening(maze.getSize() - 1, maze.getSize() - 1)
        cell = maze.getEntrance()
        self.path.append(cell)
        x = cell.getX()
        y = cell.getY()
        if ((x == 0) & (y != 0)):
            self.tryRight(cell)
        elif ((x != 0) & (y == 0)):
            self.tryTop(cell)
        elif ((x == y == 0) & cell.getTop().isRemoved()):
            self.tryRight(cell)
        elif ((x == y == 0) & cell.getLeft().isRemoved()):
            self.tryTop(cell)
        else:
            raise Exception('Invalid starting cell')
        self.cleanPath()
        return self.path

    def tryBottom(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.getBottom().isRemoved()):
                cell = self.maze.getBottomNeighbour(cell)
                self.path.append(cell)
                self.tryRight(cell)
            else:
                self.tryLeft(cell)

    def tryLeft(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.getLeft().isRemoved()):
                cell = self.maze.getLeftNeighbour(cell)
                self.path.append(cell)
                self.tryBottom(cell)
            else:
                self.tryTop(cell)

    def tryTop(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.getTop().isRemoved()):
                cell = self.maze.getTopNeighbour(cell)
                self.path.append(cell)
                self.tryLeft(cell)
            else:
                self.tryRight(cell)

    def tryRight(self, cell):
        if (cell != self.maze.getExit()):
            if (cell.getRight().isRemoved()):
                cell = self.maze.getRightNeighbour(cell)
                self.path.append(cell)
                self.tryTop(cell)
            else:
                self.tryBottom(cell)
