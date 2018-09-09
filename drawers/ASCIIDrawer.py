import drawers.AbstractDrawer as AbstractDrawer
import sys
import logging

class ASCIIDrawer(AbstractDrawer.AbstractDrawer):

    def __init__(self):
        AbstractDrawer.AbstractDrawer.__init__(self)
        self.log = logging.getLogger(__name__)

    def drawMaze(self, maze):
        """implement a drawing algorithm"""
        size = maze.getSize()
        sys.stdout.write("\n ")
        for i in range (0, size):
            if not maze.getCell(0, i).getTop().isRemoved():
                sys.stdout.write("_ ")
            else:
                sys.stdout.write("  ")
        print("")
        for j in range (0, size):
            if not maze.getCell(j, 0).getLeft().isRemoved():
                sys.stdout.write("|")
            else:
                sys.stdout.write(" ")
            for i in range (0,size):
                if not maze.getCell(j, i).getBottom().isRemoved():
                    sys.stdout.write("_")
                else:
                    sys.stdout.write(" ")
                if not maze.getCell(j, i).getRight().isRemoved():
                    sys.stdout.write("|")
                else:
                    sys.stdout.write(" ")
            print("")

    def drawPath(self, maze, path):
        """print path with ASCII signs"""
        for i in range (0, len(path)):
            sys.stdout.write("(" + path[i].getX().__str__() + "," + path[i].getY().__str__() + ") ")
        print("")
        sys.stdout.write("( ")
        # Draw entrance
        entrance = maze.getEntrance()
        if (entrance.getLeft().isRemoved() and maze.getLeftNeighbour(entrance) == None):
            sys.stdout.write("-> ")
        else:
            sys.stdout.write("v ")
        for i in range (0, len(path)-1):
            x1 = path[i].getX()
            x2 = path[i+1].getX()
            y1 = path[i].getY()
            y2 = path[i+1].getY()
            if (x1 < x2):
                sys.stdout.write("v ")
            elif (x1 > x2):
                sys.stdout.write("^ ")
            elif (y1 < y2):
                sys.stdout.write("-> ")
            elif (y1 > y2):
                sys.stdout.write("<- ")
            else:
                self.log.error('Invalid cell transition')
                raise Exception('Invalid cell transition')
        # Draw exit
        exit = maze.getExit()
        if (exit.getRight().isRemoved() and maze.getRightNeighbour(exit) == None):
            sys.stdout.write("-> ")
        else:
            sys.stdout.write(" v")
        sys.stdout.write(")")
        print("")
