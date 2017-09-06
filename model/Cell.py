import model.Wall as Wall
import random

class Cell:
    def __init__(self,x,y,set,wallsRemoved=False):
        self.leftWall = Wall.Wall(wallsRemoved)
        self.rightWall = Wall.Wall(wallsRemoved)
        self.topWall = Wall.Wall(wallsRemoved)
        self.bottomWall = Wall.Wall(wallsRemoved)
        self.wallList = [self.leftWall, self.rightWall, self.topWall, self.bottomWall]
        self.x = x
        self.y = y
        self.set = set

    #only for debugging
    def checkInvariant(self):
        if (self.wallList[0] == self.leftWall) & (self.wallList[1] == self.rightWall) & \
            (self.wallList[2] == self.topWall) & (self.wallList[3] == self.bottomWall):
            print("Everything correct")
        else:
            print("BUG")

    def setSet(self,set):
        self.set = set

    def getSet(self):
        return self.set

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getLeft(self):
        return self.leftWall

    def setLeft(self,wall):
        self.leftWall = wall
        self.wallList[0] = wall

    def getRight(self):
        return self.rightWall

    def setRight(self,wall):
        self.rightWall = wall
        self.wallList[1] = wall

    def getTop(self):
        return self.topWall

    def setTop(self,wall):
        self.topWall = wall
        self.wallList[2] = wall

    def getBottom(self):
        return self.bottomWall

    def setBottom(self,wall):
        self.bottomWall = wall
        self.wallList[3] = wall
    
    def getWallList(self):
        return self.wallList

    def removeLeft(self):
        self.leftWall.remove()

    def createLeft(self):
        self.leftWall.create()

    def removeRight(self):
        self.rightWall.remove()

    def createRight(self):
        self.rightWall.create()

    def removeTop(self):
        self.topWall.remove()

    def createTop(self):
        self.topWall.create()

    def removeBottom(self):
        self.bottomWall.remove()

    def createBottom(self):
        self.bottomWall.create()

    def hasWall(self):
        return (not self.leftWall.isRemoved()) | (not self.rightWall.isRemoved()) | \
                (not self.topWall.isRemoved()) | (not self.bottomWall.isRemoved())

    def wallCount(self):
        return (not self.leftWall.isRemoved()) + (not self.rightWall.isRemoved()) + \
                (not self.topWall.isRemoved()) + (not self.bottomWall.isRemoved())

    def chooseWall(self):#returns a random wall that is nor removed nor a border. returns None if there is no such wall
        available = [wall for wall in self.wallList if not wall.isRemoved()]
        nofWalls = len(available)
        if (nofWalls > 0):
            n = random.randint(0,nofWalls-1)
            wall = available[n]
            return wall
        return None
