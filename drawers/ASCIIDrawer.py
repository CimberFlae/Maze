import drawers.AbstractDrawer as AbstractDrawer
import sys
import logging

class ASCIIDrawer(AbstractDrawer.AbstractDrawer):

    def __init__(self):
        AbstractDrawer.AbstractDrawer.__init__(self)
        self.log = logging.getLogger(__name__)

    def drawMaze(self, maze, filepath=None):
        """implement a drawing algorithm"""
        with self.openWriter(filepath) as out:
            size = maze.getSize()
            out.write("\n ")
            for i in range (0, size):
                if not maze.getCell(0, i).getTop().isRemoved():
                    out.write("_ ")
                else:
                    out.write("  ")
            out.write("\n")
            for j in range (0, size):
                if not maze.getCell(j, 0).getLeft().isRemoved():
                    out.write("|")
                else:
                    out.write(" ")
                for i in range (0,size):
                    if not maze.getCell(j, i).getBottom().isRemoved():
                        out.write("_")
                    else:
                        out.write(" ")
                    if not maze.getCell(j, i).getRight().isRemoved():
                        out.write("|")
                    else:
                        out.write(" ")
                out.write("\n")

    def drawPath(self, maze, path, filepath=None):
        """print path with ASCII signs"""
        with self.openWriter(filepath) as out:
            for i in range (0, len(path)):
                out.write("(" + path[i].getX().__str__() + "," + path[i].getY().__str__() + ") ")
            out.write("\n( ")
            # Draw entrance
            entrance = maze.getEntrance()
            if (entrance.getLeft().isRemoved() and maze.getLeftNeighbour(entrance) == None):
                out.write("-> ")
            else:
                out.write("v ")
            for i in range (0, len(path)-1):
                x1 = path[i].getX()
                x2 = path[i+1].getX()
                y1 = path[i].getY()
                y2 = path[i+1].getY()
                if (x1 < x2):
                    out.write("v ")
                elif (x1 > x2):
                    out.write("^ ")
                elif (y1 < y2):
                    out.write("-> ")
                elif (y1 > y2):
                    out.write("<- ")
                else:
                    self.log.error('Invalid cell transition')
                    raise Exception('Invalid cell transition')
            # Draw exit
            exit = maze.getExit()
            if (exit.getRight().isRemoved() and maze.getRightNeighbour(exit) == None):
                out.write("-> ")
            else:
                out.write(" v")
            out.write(")\n")
