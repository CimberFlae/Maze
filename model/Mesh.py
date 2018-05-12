import model.Cell as Cell
import random

class Mesh:
    def __init__(self, size, wallsRemoved = False):
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
        return ((cell.x == 0) & (wall == cell.topWall)) | ((cell.x == self.size-1) & (wall == cell.bottomWall)) | \
                ((cell.y == 0) & (wall == cell.leftWall)) | ((cell.y == self.size-1) & (wall == cell.rightWall))

    def hasNeighbourInDifferentSet(self, cell):#checks if cell has a neighbour which is not in the same set
        x = cell.getX()
        y = cell.getY()
        set = cell.getSet()
        set1 = self.tryGetCell(x+1,y,cell).getSet()
        set2 = self.tryGetCell(x-1,y,cell).getSet()
        set3 = self.tryGetCell(x,y+1,cell).getSet()
        set4 = self.tryGetCell(x,y-1,cell).getSet()
        return not (set == set1 == set2 == set3 == set4)
    
    # TODO: get rid of this function
    def tryGetCell(self,x,y,default): # return the cell if index in range, returns default otherwise
        if (0 <= x < self.size) & (0 <= y < self.size):
            return self.matrix[x][y]
        else:
            return default
            
    def setCustomOpening(self, x, y, vertical = True):
        if x >= self.size or y >= self.size:
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
            else:
                cell.removeTop()
                self.entrance = cell
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
        elif y == 0:
            cell.removeLeft()
            self.entrance = cell
        else:
            cell.removeRight()
            self.exit = cell

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

    def clearExit(self): # clear exit to get sure a maze only has one exit
        if (self.exit != None):
            if (self.exit.getX() == self.size-1):
                self.exit.createBottom()
            if (self.exit.getY() == self.size-1):
                self.exit.createRight()

    def getEntrance(self):
        return self.entrance

    def getExit(self):
        return self.exit

    # delegate methods

    def chooseWall(self, cell): # returns None if there is no non-border wall that is not removed
        if len([wall for wall in cell.getWallList() if not (self.isBorder(cell, wall) or wall.isRemoved())]) > 0:
            while(True):
                wall = cell.chooseWall()
                if not self.isBorder(cell, wall):
                    return wall
        return None

    # TODO: replace uses of this function by cell.getLeft()
    def getLeft(self, cell):
        return cell.getLeft()
    
    # TODO: replace uses of this function by cell.getRight()
    def getRight(self, cell):
        return cell.getRight()

    # TODO: replace uses of this function by cell.getTop()
    def getTop(self, cell):
        return cell.getTop()

    # TODO: replace uses of this function by cell.getBottom()
    def getBottom(self, cell):
        return cell.getBottom()

    # TODO: replace uses of this function by cell.getSet()
    def getSet(self, cell):
        return cell.getSet()

    # TODO: replace uses of this function by cell.removeLeft()
    def removeLeft(self, cell):
        cell.removeLeft()

    # TODO: replace uses of this function by cell.createLeft()
    def createLeft(self, cell):
        cell.createLeft()

    # TODO: replace uses of this function by cell.removeRight()
    def removeRight(self, cell):
        cell.removeRight()

    # TODO: replace uses of this function by cell.createRight()
    def createRight(self, cell):
        cell.createRight()

    # TODO: replace uses of this function by cell.removeTop()
    def removeTop(self, cell):
        cell.removeTop()

    # TODO: replace uses of this function by cell.createTop()
    def createTop(self, cell):
        cell.createTop()

    # TODO: replace uses of this function by cell.removeBottom()
    def removeBottom(self, cell):
        cell.removeBottom()

    # TODO: replace uses of this function by cell.createBottom()
    def createBottom(self, cell):
        cell.createBottom()

    # TODO: replace uses of this function by cell.getX()
    def getX(self, cell):
        return cell.getX()

    # TODO: replace uses of this function by cell.getY()
    def getY(self, cell):
        return cell.getY()
