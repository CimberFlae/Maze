import drawers.Drawer as Drawer
import sys

class ASCIIDrawer(Drawer.Drawer):

    def __init__(self):
        Drawer.Drawer.__init__(self)

    def drawMaze(self, maze):
        """implement a drawing algorithm"""
        size = maze.getSize()
        sys.stdout.write(" ")
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
        for i in range (0,len(path)):
            sys.stdout.write("(" + path[i].getX().__str__() + "," + path[i].getY().__str__() + ")  ")
        print("")
        sys.stdout.write("( ")
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
                raise Exception('Invalid cell transition')
        sys.stdout.write(")")
        print("")
