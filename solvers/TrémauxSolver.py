import solvers.Solver as Solver
import random

class RandomMouseSolver(Solver.Solver):

    def __init__(self):
        Solver.Solver.__init__(self)

    def solveMaze(self,maze):
        """implement TrŽmaux's algorithm"""
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
            self.tryBottom(maze,previous,current)
        elif ((x != 0) & (y == 0)):
            current = self.tryRight(maze,current)
        elif ((x == y == 0) & maze.getTop(current).isRemoved()):
            current = self.tryBottom(maze,current)
        elif ((x == y == 0) & maze.getLeft(current).isRemoved()):
            current = self.tryRight(maze,current)
        while (current != maze.getExit()):
            current = self.tryRandom(maze,current)
        self.cleanPath()
        return self.path

    def tryBottom(self,maze,previous,current):
        if (current != maze.getExit()):
            if (current.wallCount() < 2):#junction
                self.walls.apppend(maze.getTop(current))
                if (not current in self.junctions):
                    self.junctions.append(current)
                    if (current.wallCount() == 0):
                        self.tryRandomFromTop(maze,previous,current)
                    else:#wallCount == 1
                        if (maze.getLeft(current).isRemoved()):
                            self.chooseDirection(self.tryRight,self.tryBottom)
                        elif (maze.getBottom(current).isRemoved()):
                            self.chooseDirection(self.tryLeft,self.tryRight)
                        else:
                            self.chooseDirection(self.tryLeft,self.tryBottom)
                elif (self.walls.count(maze.getTop(current)) == 1):
                    current = maze.getTopNeighbour(current)
                    self.path.append(current)
                    self.tryTop(maze,previous,current)
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
                self.tryBottom(maze,previous,current)
            else:
                previous = current
                if (current.wallCount() == 2):#normal path with curve
                    if (not maze.getRight(current).isRemoved()):
                        current = maze.getRightNeighbour(current)
                        self.path.append(current)
                        self.tryRight(maze,previous,current)
                    else:
                        current = maze.getLeftNeighbour(current)
                        self.path.append(current)
                        self.tryLeft(maze,previous,current)
                else:#dead end
                    current = maze.getTopNeighbour(current)
                    self.path.append(current)
                    self.tryTop(maze,previous,current)

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

    def tryRandomFromTop(self,maze,previous,current):
        list = [self.tryBottom,self.tryLeft,self.tryRight]
        n = random.randint(0,2)
        return list[n](maze,previous,current)

    def tryRandomFromBottom(self,maze,previous,current):
        list = [self.tryTop,self.tryLeft,self.tryRight]
        n = random.randint(0,2)
        return list[n](maze,previous,current)

    def tryRandomFromLeft(self,maze,previous,current):
        list = [self.tryBottom,self.tryTop,self.tryRight]
        n = random.randint(0,2)
        return list[n](maze,previous,current)

    def tryRandomFromRight(self,maze,previous,current):
        list = [self.tryBottom,self.tryLeft,self.tryTop]
        n = random.randint(0,2)
        return list[n](maze,previous,current)

    def chooseDirection(self,foo1,foo2,maze,previous,current):
        n = random.randint(1)
        if (n == 0):
            foo1(maze,previous,current)
        else:
            foo2(maze,previous,current)
