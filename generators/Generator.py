import random

class Generator:

    def __init__(self):
        print ("generating a " + self.__class__.__name__)

    def __generateMaze__(self, size, seed = 0):
        """Generate a Maze using a specific algorithm"""

    def generateRandomMaze(self, size, seed = 0):
        if (seed != 0):
            random.seed(seed)
        maze = self.__generateMaze__(size, seed = seed)
        if random.getrandbits(1) == 0:
            self.setRandomTopEntrance(maze)
        else:
            self.setRandomLeftEntrance(maze)
        if random.getrandbits(1) == 0:
            self.setRandomBottomExit(maze)
        else:
            self.setRandomRightExit(maze)
        return maze
    
    def generateCustomMaze(self, size, x1, y1, x2, y2, seed = 0):
        maze = self.__generateMaze__(size, seed = seed)
        maze.setCustomOpening(x1, y1, True)
        maze.setCustomOpening(x2, y2, True)
        return maze

    def setStandardEntrance(self, maze, top):
        maze.clearEntrance()
        if top:
            maze.setCustomOpening(0, 0, True)
        else:
            maze.setCustomOpening(0, 0, False)

    def setStandardExit(self, maze, bottom):
        maze.clearExit()
        if bottom:
            maze.setCustomOpening(maze.getSize()-1, maze.getSize()-1, True)
        else:
            maze.setCustomOpening(maze.getSize()-1, maze.getSize()-1, False)
    
    def setStandardEntryExit(self, maze, entry, exit, top, bottom):
        if entry:
            maze = self.setStandardEntrance(maze, top)
        if exit:
            maze = self.setStandardExit(maze, bottom)

    #TODO: replace uses of these functions by the direct call? if it doesn't create more calls!
    def setRandomTopEntrance(self, maze):
        maze.setRandomTopEntrance()

    def setRandomLeftEntrance(self, maze):
        maze.setRandomLeftEntrance()

    def setRandomBottomExit(self, maze):
        maze.setRandomBottomExit()

    def setRandomRightExit(self, maze):
        maze.setRandomRightExit()
