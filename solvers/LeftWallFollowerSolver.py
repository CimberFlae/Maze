import solvers.Solver as Solver

class LeftWallFollowerSolver(Solver.Solver):

    def __init__(self):
        Solver.Solver.__init__(self)

    def solveMaze(self,maze):
        """implement left wall following"""
        """this means: always try going in directions in the following order: left, forward, right, backward"""
        if (maze.getEntrance() == None):
            #maze.setStandardEntrance()
            maze.setCustomOpening(0, 0)
        if (maze.getExit() == None):
            #maze.setStandardExit()
            maze.setCustomOpening(maze.getSize() - 1, maze.getSize() - 1)
        cell = maze.getEntrance()
        self.path.append(cell)
        x = maze.getX(cell)
        y = maze.getY(cell)
        if ((x == 0) & (y != 0)):
            self.tryRight(maze, cell)
        elif ((x != 0) & (y == 0)):
            self.tryTop(maze, cell)
        elif ((x == y == 0) & maze.getTop(cell).isRemoved()):
            self.tryRight(maze, cell)
        elif ((x == y == 0) & maze.getLeft(cell).isRemoved()):
            self.tryTop(maze, cell)
        self.cleanPath()
        return self.path

    def tryBottom(self,maze,cell):
        if (cell != maze.getExit()):
            if (maze.getBottom(cell).isRemoved()):
                cell = maze.getBottomNeighbour(cell)
                self.path.append(cell)
                self.tryRight(maze,cell)
            else:
                self.tryLeft(maze, cell)

    def tryLeft(self,maze,cell):
        if (cell != maze.getExit()):
            if (maze.getLeft(cell).isRemoved()):
                cell = maze.getLeftNeighbour(cell)
                self.path.append(cell)
                self.tryBottom(maze,cell)
            else:
                self.tryTop(maze,cell)

    def tryTop(self,maze,cell):
        if (cell != maze.getExit()):
            if (maze.getTop(cell).isRemoved()):
                cell = maze.getTopNeighbour(cell)
                self.path.append(cell)
                self.tryLeft(maze,cell)
            else:
                self.tryRight(maze, cell)

    def tryRight(self,maze,cell):
        if (cell != maze.getExit()):
            if (maze.getRight(cell).isRemoved()):
                cell = maze.getRightNeighbour(cell)
                self.path.append(cell)
                self.tryTop(maze, cell)
            else:
                self.tryBottom(maze, cell)
