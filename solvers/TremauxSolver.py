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
        self.walls = []
        self.junctions = []
        self.path.append(current)
        x = maze.getX(current)
        y = maze.getY(current)
        if ((x == 0) & (y != 0)):
            self.tryBottom(maze, previous, current)
        elif ((x != 0) & (y == 0)):
            self.tryRight(maze, current)
        elif ((x == y == 0) & maze.getTop(current).isRemoved()):
            self.tryBottom(maze, current)
        elif ((x == y == 0) & maze.getLeft(current).isRemoved()):
            self.tryRight(maze, current)
        while (self.path[-1] != maze.getExit()):# tryRandom does not exist...
            self.tryRandom(maze, current)
        self.cleanPath()
        return self.path

    def tryBottom(self, maze, previous, current):
        if (current != maze.getExit()):
            if (current.wallCount() < 2):#junction
                self.walls.apppend(maze.getTop(current))
                if (not current in self.junctions):
                    self.junctions.append(current)
                    if (current.wallCount() == 0):
                        self.tryRandomFromTop(maze, previous, current)
                    else:#wallCount == 1
                        if (maze.getLeft(current).isRemoved()):
                            self.chooseDirection(self.tryRight, self.tryBottom)
                        elif (maze.getBottom(current).isRemoved()):
                            self.chooseDirection(self.tryLeft, self.tryRight)
                        else:
                            self.chooseDirection(self.tryLeft, self.tryBottom)
                elif (self.walls.count(maze.getTop(current)) == 1):
                    current = maze.getTopNeighbour(current)
                    self.path.append(current)
                    self.tryTop(maze, previous, current)
                else:#walls.count == 2 --> #choose direction with least walls.count
                    if (current.wallCount() == 0):
                        pass
                        #3 possible ways
                    else:
                        pass
                        #2 possible ways
            elif (maze.getBottom(current).isRemoved()):#normal straight path
                previous = current
                current = maze.getBottomNeighbour(current)
                self.path.append(current)
                self.tryBottom(maze, previous, current)
            else:
                previous = current
                if (current.wallCount() == 2):#normal path with curve
                    if (not maze.getRight(current).isRemoved()):# This smells: why go to right if right wall is NOT removed
                        current = maze.getRightNeighbour(current)
                        self.path.append(current)
                        self.tryRight(maze, previous, current)
                    else:
                        current = maze.getLeftNeighbour(current)
                        self.path.append(current)
                        self.tryLeft(maze, previous, current)
                else:#dead end
                    current = maze.getTopNeighbour(current)
                    self.path.append(current)
                    self.tryTop(maze, previous, current)

    def tryLeft(self, maze, previous, cell):
        if (cell != maze.getExit()):
            left = maze.getLeft(cell)
            if (left.isRemoved() & (not maze.isBorder(cell, left))):
                previous = cell
                cell = maze.getLeftNeighbour(cell)
                self.path.append(cell)
                self.tryLeft(maze, previous, cell)
#                return self.tryLeft(maze, cell)
#            else:
#                return cell
#        else:
#            return cell

    def tryTop(self, maze, previous, cell):
        if (cell != maze.getExit()):
            top = maze.getTop(cell)
            if (top.isRemoved() & (not maze.isBorder(cell, top))):
                previous = cell
                cell = maze.getTopNeighbour(cell)
                self.path.append(cell)
                self.tryTop(maze, previous, cell)
#                return self.tryTop(maze, cell)
#            else:
#                return cell
#        else:
#            return cell

    def tryRight(self, maze, previous, cell):
        if (cell != maze.getExit()):
            right = maze.getRight(cell)
            if (right.isRemoved() & (not maze.isBorder(cell, right))):
                previous = cell
                cell = maze.getRightNeighbour(cell)
                self.path.append(cell)
                self.tryRight(maze, previous, cell)
#                return self.tryRight(maze, cell)
#            else:
#                return cell
#        else:
#            return cell

    def tryRandomFromTop(self, maze, previous, current):
        list = [self.tryBottom, self.tryLeft, self.tryRight]
        n = random.randint(0, 2)
        return list[n](maze, previous, current)

    def tryRandomFromBottom(self, maze, previous, current):
        list = [self.tryTop, self.tryLeft, self.tryRight]
        n = random.randint(0, 2)
        return list[n](maze, previous, current)

    def tryRandomFromLeft(self, maze, previous, current):
        list = [self.tryBottom, self.tryTop, self.tryRight]
        n = random.randint(0, 2)
        return list[n](maze, previous, current)

    def tryRandomFromRight(self, maze, previous, current):
        list = [self.tryBottom, self.tryLeft, self.tryTop]
        n = random.randint(0, 2)
        return list[n](maze, previous, current)

    def chooseDirection(self, foo1, foo2, maze, previous, current):
        n = random.randint(1)
        if (n == 0):
            foo1(maze, previous, current)
        else:
            foo2(maze, previous, current)
