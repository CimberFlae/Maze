import solvers.Solver as Solver
import random

class RandomMouseSolver(Solver.Solver):

    def __init__(self):
        Solver.Solver.__init__(self)

    def solveMaze(self,maze):
        """implement random mouse algorithm"""
        """this means: always try going straight and if  that's not possible, try a direction at random"""
        """caution: this algorithms only terminates in acceptable amount of time for very small paths (often seen in very small mazes)"""
        if (maze.getEntrance() == None):
            maze.setStandardEntrance()
        if (maze.getExit() == None):
            maze.setStandardExit()
        cell = maze.getEntrance()
        self.path.append(cell)
        x = maze.getX(cell)
        y = maze.getY(cell)
        if ((x == 0) & (y != 0)):
            cell = self.tryBottom(maze,cell)
        elif ((x != 0) & (y == 0)):
            cell = self.tryRight(maze,cell)
        elif ((x == y == 0) & maze.getTop(cell).isRemoved()):
            cell = self.tryBottom(maze,cell)
        elif ((x == y == 0) & maze.getLeft(cell).isRemoved()):
            cell = self.tryRight(maze,cell)
        while (cell != maze.getExit()):
            cell = self.tryRandom(maze,cell)
        self.cleanPath()
        return self.path

    def tryBottom(self,maze,cell):
        if (cell != maze.getExit()):
            size = maze.getSize()
            bottom = maze.getBottom(cell)
            if (bottom.isRemoved() & (not cell.isBorder(bottom,size))):
                cell = maze.getBottomNeighbour(cell)
                self.path.append(cell)
                return self.tryBottom(maze,cell)
            else:
                return cell
        else:
            return cell

    def tryLeft(self,maze,cell):
        if (cell != maze.getExit()):
            size = maze.getSize()
            left = maze.getLeft(cell)
            if (left.isRemoved() & (not cell.isBorder(left,size))):
                cell = maze.getLeftNeighbour(cell)
                self.path.append(cell)
                return self.tryLeft(maze,cell)
            else:
                return cell
        else:
            return cell

    def tryTop(self,maze,cell):
        if (cell != maze.getExit()):
            size = maze.getSize()
            top = maze.getTop(cell)
            if (top.isRemoved() & (not cell.isBorder(top,size))):
                cell = maze.getTopNeighbour(cell)
                self.path.append(cell)
                return self.tryTop(maze,cell)
            else:
                return cell
        else:
            return cell

    def tryRight(self,maze,cell):
        if (cell != maze.getExit()):
            size = maze.getSize()
            right = maze.getRight(cell)
            if (right.isRemoved() & (not cell.isBorder(right,size))):
                cell = maze.getRightNeighbour(cell)
                self.path.append(cell)
                return self.tryRight(maze,cell)
            else:
                return cell
        else:
            return cell

    def tryRandom(self,maze,cell):
        list = [self.tryBottom,self.tryLeft,self.tryTop,self.tryRight]
        n = random.randint(0,3)
        return list[n](maze,cell)
