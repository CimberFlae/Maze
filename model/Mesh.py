import model.Cell as Cell
import random
import logging

class Mesh:

    def __init__(self, size, wallsRemoved = False):
        self.log = logging.getLogger(__name__)
        self.size = size
        self.matrix = []
        self.sets = []
        k = 0
        for i in range (0, size):
            matrixrow = []
            for j in range (0, size):
                setrow = []
                cell = Cell.Cell(i, j, k, wallsRemoved)
                setrow.append(cell)
                self.sets.append(setrow)
                k += 1
                matrixrow.append(cell)
            self.matrix.append(matrixrow)
        self.synchronizeWalls()
        self.entrance = None
        self.exit = None

    def synchronizeWalls(self):
        for i in range (0, self.size-1): # synchronize all horizontal walls
            for j in range (0, self.size):
                self.matrix[i][j].setBottom(self.matrix[i+1][j].getTop())
        for i in range (0, self.size): # synchronize all vertical walls
            for j in range (0, self.size-1):
                self.matrix[i][j].setRight(self.matrix[i][j+1].getLeft())

    def getSize(self):
        return self.size

    def getCell(self, x, y):
        return self.matrix[x][y]

    def getLeftNeighbour(self, cell):
        if (cell.getY()-1 < 0):
            return None
        return self.matrix[cell.getX()][cell.getY()-1]

    def getRightNeighbour(self, cell):
        if (cell.getY()+1 >= self.size):
            return None
        return self.matrix[cell.getX()][cell.getY()+1]

    def getTopNeighbour(self, cell):
        if (cell.getX()-1 < 0):
            return None
        return self.matrix[cell.getX()-1][cell.getY()]

    def getBottomNeighbour(self, cell):
        if (cell.getX()+1 >= self.size):
            return None
        return self.matrix[cell.getX()+1][cell.getY()]

    def moveCell(self, fromSet, toSet):
        if fromSet == toSet:
            return
        for i in range (0, len(self.sets[fromSet])):
            self.sets[toSet].append(self.sets[fromSet][i])
            self.sets[fromSet][i].setSet(toSet)
        self.sets[fromSet][:] = []

    def hasMultipleSets(self): # returns True if Maze has more than one set
        for i in range (len(self.sets)):
            if (len(self.sets[i]) == self.size*self.size):
                return False
        return True

    def chooseCell(self): # returns cell with an existing not-border wall, returns None if there is none
        hasResult = False
        for i in range(self.size):
            for j in range(self.size):
                if self.hasNeighbourInDifferentSet(self.matrix[i][j]):
                    hasResult = True
        while (hasResult):
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            cell = self.matrix[x][y]
            if (self.hasNeighbourInDifferentSet(cell)):
                return cell
        return None

    def isBorder(self, cell, wall):
        return ((cell.x == 0) and (wall == cell.topWall)) or ((cell.x == self.size-1) and (wall == cell.bottomWall)) or\
                ((cell.y == 0) and (wall == cell.leftWall)) or ((cell.y == self.size-1) and (wall == cell.rightWall))

    def hasNeighbourInDifferentSet(self, cell):#checks if cell has a neighbour which is not in the same set
        set = cell.getSet()

        top = self.getTopNeighbour(cell)
        setTop = top == None or top.getSet() == set

        bottom = self.getBottomNeighbour(cell)
        setBottom = bottom == None or bottom.getSet() == set

        right = self.getRightNeighbour(cell)
        setRight = right == None or right.getSet() == set

        left = self.getLeftNeighbour(cell)
        setLeft = left == None or left.getSet() == set

        return not (setTop and setBottom and setRight and setLeft)
    
    def setCustomOpening(self, x, y, vertical = True):
        if x >= self.size or y >= self.size:
            self.log.error('Opening cell has to part of the maze - check your indexes')
            raise IndexError('Opening cell has to part of the maze - check your indexes')
        cell = self.matrix[x][y]
        if x == 0:
            if y == 0:
                if vertical:
                    cell.removeTop()
                else:
                    cell.removeLeft()
                self.entrance = cell
            elif y == self.size - 1:
                if vertical:
                    cell.removeTop()
                    self.entrance = cell
                else:
                    cell.removeRight()
                    self.exit = cell
            elif y > 0 and y < self.size - 1:
                cell.removeTop()
                self.entrance = cell
            else:
                self.log.error('Invalid y-coordinate')
                raise Exception('Invalid y-coordinate')
        elif x == self.size - 1:
            if y == self.size - 1:
                if vertical:
                    cell.removeBottom()
                else:
                    cell.removeRight()
                self.exit = cell
            elif y == 0:
                if vertical:
                    cell.removeBottom()
                    self.exit = cell
                else:
                    cell.removeLeft()
                    self.entrance = cell
            else:
                cell.removeBottom()
                self.exit = cell
        elif x > 0 and x < self.size - 1 and y == 0:
            cell.removeLeft()
            self.entrance = cell
        elif x > 0 and x < self.size - 1 and y == self.size - 1:
            cell.removeRight()
            self.exit = cell
        else:
            self.log.error('Invalid coordinates')
            raise Exception('Invalid coordinates')

    def setRandomTopEntrance(self):
        self.clearEntrance()
        n = random.randint(0, self.size-1)
        self.setCustomOpening(0, n, True)

    def setRandomLeftEntrance(self):
        self.clearEntrance()
        n = random.randint(0, self.size-1)
        self.setCustomOpening(n, 0, False)

    def setRandomBottomExit(self):
        self.clearExit()
        n = random.randint(0, self.size-1)
        self.setCustomOpening(self.size-1, n, True)

    def setRandomRightExit(self):
        self.clearExit()
        n = random.randint(0, self.size-1)
        self.setCustomOpening(n, self.size-1, False)

    def clearEntrance(self): # clear entrance to get sure a maze only has one entrance
        if (self.entrance != None):
            if (self.entrance.getX() == 0):
                self.entrance.createTop()
            if (self.entrance.getY() == 0):
                self.entrance.createLeft()
            self.entrance = None

    def clearExit(self): # clear exit to get sure a maze only has one exit
        if (self.exit != None):
            if (self.exit.getX() == self.size-1):
                self.exit.createBottom()
            if (self.exit.getY() == self.size-1):
                self.exit.createRight()
            self.exit = None

    def getEntrance(self):
        return self.entrance

    def getExit(self):
        return self.exit

    def chooseWall(self, cell): # returns None if there is no non-border wall that is not removed
        if len([wall for wall in cell.getWallList() if not (self.isBorder(cell, wall) or wall.isRemoved())]) > 0:
            while(True):
                wall = cell.chooseWall()
                if not self.isBorder(cell, wall):
                    return wall
        return None
