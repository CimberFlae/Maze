from drawers.AbstractDrawer import AbstractDrawer
import logging
from tkinter import *


class TkInterDrawer(AbstractDrawer):

    def __init__(self):
        AbstractDrawer.__init__(self)
        self.log = logging.getLogger(__name__)

    def __get_resolution(self, size):
        z = 5
        self.resolution = 47.5
        while z <= size:
            self.resolution = (z * z * self.resolution + 268.46) / ((z + 1) * (z + 1))
            z += 1

    # TkInter can only display the path inside the maze (not separately)
    def draw_maze(self, matrix, path):
        self.__get_resolution(matrix.get_size())
        root = Tk()
        root.title("Maze")
        canvas = Canvas(root)
        root.geometry('280x280+100+100')
        self.__draw(matrix, canvas)
        self.__draw_path__(path, canvas)
        canvas.pack(side=LEFT, fill='both')
        root.mainloop()

    def __draw(self, matrix, canvas):  # draw the maze
        sys.stdout.write(" ")
        for i in range(0, matrix.get_size()):
            if not matrix.get_cell(0, i).get_top().is_removed():
                "draw upper horizontal line"
                canvas.create_line((i+1) * self.resolution, self.resolution, (i + 2) * self.resolution, self.resolution)
        for j in range(0, matrix.get_size()):
            print("")
            if not matrix.get_cell(j, 0).get_left().is_removed():
                "draw left vertical line"
                canvas.create_line(self.resolution, (j + 1) * self.resolution, self.resolution,
                                   (j + 2) * self.resolution)

            for i in range(0, matrix.get_size()):
                cell = matrix.get_cell(j, i)
                if not cell.get_bottom().is_removed():
                    "draw lower horizontal line"
                    canvas.create_line((i+1) * self.resolution, (j + 2) * self.resolution, (i + 2) * self.resolution,
                                       (j + 2) * self.resolution)
                if not cell.get_right().is_removed():
                    "draw right vertical line"
                    canvas.create_line((i+2) * self.resolution, (j + 1) * self.resolution, (i + 2) * self.resolution,
                                       (j + 2) * self.resolution)
        print("")

    def __draw_path__(self, path, canvas):  # draws the path
        entrance = path[0]
        i = entrance.get_y()
        j = entrance.get_x()
        if entrance.get_left().is_removed():
            canvas.create_line((i + 1.5) * self.resolution, j * self.resolution, (i + 1.5) * self.resolution,
                               (j + 1.5) * self.resolution, fill="red")
        elif entrance.get_top().is_removed():
            canvas.create_line(i * self.resolution, (j + 1.5) * self.resolution, (i + 1.5) * self.resolution,
                               (j + 1.5) * self.resolution, fill="red")
        else:
            self.log.error('No entrance?')
            raise Exception('No entrance?')
        i += 1.5
        j += 1.5
        for k in range(0, len(path) - 1):
            x1 = path[k].get_x()
            x2 = path[k + 1].get_x()
            y1 = path[k].get_y()
            y2 = path[k + 1].get_y()
            if x1 < x2:
                canvas.create_line(i * self.resolution, j * self.resolution, i * self.resolution,
                                   (j + 1) * self.resolution, fill="red")
                j += 1
            elif x1 > x2:
                canvas.create_line(i * self.resolution, j * self.resolution, i * self.resolution,
                                   (j - 1) * self.resolution, fill="red")
                j -= 1
            elif y1 < y2:
                canvas.create_line(i * self.resolution, j * self.resolution, (i + 1) * self.resolution,
                                   j * self.resolution, fill="red")
                i += 1
            elif y1 > y2:
                canvas.create_line(i * self.resolution, j * self.resolution, (i - 1) * self.resolution,
                                   j * self.resolution, fill="red")
                i -= 1
            else:
                self.log.error('Invalid cell transition')
                raise Exception('Invalid cell transition')
        if path[-1].get_right().is_removed():
            canvas.create_line(i * self.resolution, j * self.resolution, (i + 1.5) * self.resolution,
                               j * self.resolution, fill="red")
        elif path[-1].get_bottom().is_removed():
            canvas.create_line(i * self.resolution, j * self.resolution, i * self.resolution,
                               (j + 1.5) * self.resolution, fill="red")
        else:
            self.log.error('No entrance?')
            raise Exception('No entrance?')
