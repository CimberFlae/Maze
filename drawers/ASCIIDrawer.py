import drawers.AbstractDrawer as AbstractDrawer
import logging


class ASCIIDrawer(AbstractDrawer.AbstractDrawer):

    def __init__(self):
        AbstractDrawer.AbstractDrawer.__init__(self)
        self.log = logging.getLogger(__name__)

    def draw_maze(self, maze, file_path=None):
        """implement a drawing algorithm"""
        with self.open_writer(file_path) as out:
            size = maze.get_size()
            out.write("\n ")
            for i in range (0, size):
                if not maze.get_cell(0, i).get_top().isRemoved():
                    out.write("_ ")
                else:
                    out.write("  ")
            out.write("\n")
            for j in range (0, size):
                if not maze.get_cell(j, 0).get_left().isRemoved():
                    out.write("|")
                else:
                    out.write(" ")
                for i in range (0,size):
                    if not maze.get_cell(j, i).get_bottom().isRemoved():
                        out.write("_")
                    else:
                        out.write(" ")
                    if not maze.get_cell(j, i).get_right().isRemoved():
                        out.write("|")
                    else:
                        out.write(" ")
                out.write("\n")

    def draw_path(self, maze, path, file_path=None):
        """print path with ASCII signs"""
        with self.open_writer(file_path) as out:
            for i in range (0, len(path)):
                out.write("(" + path[i].get_x().__str__() + "," + path[i].get_y().__str__() + ") ")
            out.write("\n( ")
            # Draw entrance
            entrance = maze.get_entrance()
            if entrance.get_left().isRemoved() and maze.get_left_neighbour(entrance) is None:
                out.write("-> ")
            else:
                out.write("v ")
            for i in range (0, len(path)-1):
                x1 = path[i].get_x()
                x2 = path[i+1].get_x()
                y1 = path[i].get_y()
                y2 = path[i+1].get_y()
                if x1 < x2:
                    out.write("v ")
                elif x1 > x2:
                    out.write("^ ")
                elif y1 < y2:
                    out.write("-> ")
                elif y1 > y2:
                    out.write("<- ")
                else:
                    self.log.error('Invalid cell transition')
                    raise Exception('Invalid cell transition')
            # Draw exit
            maze_exit = maze.get_exit()
            if maze_exit.get_right().isRemoved() and maze.get_right_neighbour(maze_exit) is None:
                out.write("-> ")
            else:
                out.write("v ")
            out.write(")\n")
