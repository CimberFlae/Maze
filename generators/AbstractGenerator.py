import random

class AbstractGenerator:

    def __init__(self):
        print ("generating a " + self.__class__.__name__)

    def __generateMaze__(self, size, seed = 0):
        """Generate a Maze using a specific algorithm"""
        if (size < 2):
            raise Exception('Invalid maze size!')

    def generateRandomMaze(self, size, seed = 0):
        if (seed != 0):
            random.seed(seed)
        maze = self.__generateMaze__(size, seed = seed)
        if random.getrandbits(1) == 0:
            maze.setRandomTopEntrance()
        else:
            maze.setRandomLeftEntrance()
        if random.getrandbits(1) == 0:
            maze.setRandomBottomExit()
        else:
            maze.setRandomRightExit()
        return maze
    
    def generateCustomMaze(self, size, x1, y1, x2, y2, seed = 0):
        maze = self.__generateMaze__(size, seed = seed)
        maze.setCustomOpening(x1, y1, True)
        maze.setCustomOpening(x2, y2, True)
        return maze
