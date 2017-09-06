import drawers.Drawer as Drawer
import sys

class ASCIIDrawer(Drawer.Drawer):

    def __init__(self):
        Drawer.Drawer.__init__(self)

    def drawMaze(self,maze):
        """implement a drawing algorithm"""
        size = maze.getSize()
        sys.stdout.write(" ")
        for i in range (0,size):
            if not maze.getTop(maze.getCell(0,i)).isRemoved():
                sys.stdout.write("_ ")
            else:
                sys.stdout.write("  ")
        print("")
        for j in range (0,size):
            if not maze.getLeft(maze.getCell(j,0)).isRemoved():
                sys.stdout.write("|")
            else:
                sys.stdout.write(" ")
            for i in range (0,size):
                if not maze.getBottom(maze.getCell(j,i)).isRemoved():
                    sys.stdout.write("_")
                else:
                    sys.stdout.write(" ")
                if not maze.getRight(maze.getCell(j,i)).isRemoved():
                    sys.stdout.write("|")
                else:
                    sys.stdout.write(" ")
            print("")

    def drawPath(self,maze,path):
        """print path with ASCII signs"""
        for i in range (0,len(path)):
            sys.stdout.write("("+maze.getX(path[i]).__str__()+","+maze.getY(path[i]).__str__()+")  ")
            #print (maze.getX(path[i]),maze.getY(path[i]))
        print("")
        sys.stdout.write("( ")
        for i in range (0,len(path)-1):
            x1 = maze.getX(path[i])
            x2 = maze.getX(path[i+1])
            y1 = maze.getY(path[i])
            y2 = maze.getY(path[i+1])
            if (x1 < x2):
                sys.stdout.write("v ")
            elif (x1 > x2):
                sys.stdout.write("^ ")
            elif (y1 < y2):
                sys.stdout.write("-> ")
            else:
                sys.stdout.write("<- ")
        sys.stdout.write(")")
        print("")
