class Generator:

    def __init__(self):
        print ("generating a Generator")

    def generateMaze(self, size, top = True, bottom = True, entry = True, exit = True):
        """Generate a Maze using a specific algorithm"""

    def setStandardEntrance(self, maze, top):
        maze.clearEntrance()
        if top:
            maze.setCustomOpening(0, 0, True)
        else:
            maze.setCustomOpening(0, 0, False)
        return maze

    def setStandardExit(self, maze, bottom):
        maze.clearExit()
        if bottom:
            maze.setCustomOpening(maze.getSize()-1, maze.getSize()-1, None, True)
        else:
            maze.setCustomOpening(maze.getSize()-1, maze.getSize()-1, None, False)
        return maze
    
    def setStandardEntryExit(self, maze, entry, exit, top, bottom):
        if entry:
            maze = self.setStandardEntrance(maze, top)
        if exit:
            maze = self.setStandardExit(maze, bottom)
        return maze

    def setRandomTopEntrance(self,maze):
        maze.setRandomTopEntrance()
        return maze

    def setRandomLeftEntrance(self,maze):
        maze.setRandomLeftEntrance()
        return maze

    def setRandomBottomExit(self,maze):
        maze.setRandomBottomExit()
        return maze

    def setRandomRightExit(self,maze):
        maze.setRandomRightExit()
        return maze
