from model.Cell import Cell
import random
import logging


class Mesh:

    def __init__(self, size, walls_removed=False):
        self.log = logging.getLogger(__name__)
        self.size = size
        self.matrix = []
        self.sets = []
        k = 0
        for i in range(0, size):
            matrix_row = []
            for j in range(0, size):
                set_row = []
                cell = Cell(i, j, k, walls_removed)
                set_row.append(cell)
                self.sets.append(set_row)
                k += 1
                matrix_row.append(cell)
            self.matrix.append(matrix_row)
        self.__synchronizeWalls__()
        self.entrance = None
        self.exit = None

    def __synchronizeWalls__(self):
        for i in range(0, self.size-1):  # synchronize all horizontal walls
            for j in range(0, self.size):
                self.matrix[i][j].set_bottom(self.matrix[i + 1][j].get_top())
        for i in range(0, self.size):  # synchronize all vertical walls
            for j in range(0, self.size-1):
                self.matrix[i][j].set_right(self.matrix[i][j + 1].get_left())

    def get_size(self):
        return self.size

    def get_cell(self, x, y):
        return self.matrix[x][y]

    def get_left_neighbour(self, cell):
        if cell.get_y()-1 < 0:
            return None
        return self.matrix[cell.get_x()][cell.get_y() - 1]

    def get_right_neighbour(self, cell):
        if cell.get_y()+1 >= self.size:
            return None
        return self.matrix[cell.get_x()][cell.get_y() + 1]

    def get_top_neighbour(self, cell):
        if cell.get_x()-1 < 0:
            return None
        return self.matrix[cell.get_x() - 1][cell.get_y()]

    def get_bottom_neighbour(self, cell):
        if cell.get_x()+1 >= self.size:
            return None
        return self.matrix[cell.get_x() + 1][cell.get_y()]

    def move_cell(self, from_set, to_set):
        if from_set == to_set:
            return
        for i in range(0, len(self.sets[from_set])):
            self.sets[to_set].append(self.sets[from_set][i])
            self.sets[from_set][i].set_set(to_set)
        self.sets[from_set][:] = []

    def has_multiple_sets(self):  # returns True if Maze has more than one set
        for i in range(len(self.sets)):
            if len(self.sets[i]) == self.size*self.size:
                return False
        return True

    # returns cell with an existing not-border wall, returns None if there is none
    def choose_cell(self, custom_random=random):
        has_result = False
        for i in range(self.size):
            for j in range(self.size):
                if self.has_neighbour_in_different_set(self.matrix[i][j]):
                    has_result = True
        while has_result:
            x = custom_random.randint(0, self.size-1)
            y = custom_random.randint(0, self.size-1)
            cell = self.matrix[x][y]
            if self.has_neighbour_in_different_set(cell):
                return cell
        return None

    def is_border(self, cell, wall):
        return ((cell.x == 0) and (wall == cell.topWall)) or ((cell.x == self.size-1) and (wall == cell.bottomWall)) or\
                ((cell.y == 0) and (wall == cell.leftWall)) or ((cell.y == self.size-1) and (wall == cell.rightWall))

    def has_neighbour_in_different_set(self, cell):  # checks if cell has a neighbour which is not in the same set
        set_id = cell.get_set()

        top = self.get_top_neighbour(cell)
        set_top = top is None or top.get_set() == set_id

        bottom = self.get_bottom_neighbour(cell)
        set_bottom = bottom is None or bottom.get_set() == set_id

        right = self.get_right_neighbour(cell)
        set_right = right is None or right.get_set() == set_id

        left = self.get_left_neighbour(cell)
        set_left = left is None or left.get_set() == set_id

        return not (set_top and set_bottom and set_right and set_left)
    
    def set_custom_opening(self, x, y, vertical=True):
        if x >= self.size or y >= self.size:
            self.log.error('Opening cell has to part of the maze - check your indexes')
            raise IndexError('Opening cell has to part of the maze - check your indexes')
        cell = self.matrix[x][y]
        if x == 0:
            if y == 0:
                if vertical:
                    cell.remove_top()
                else:
                    cell.remove_left()
                self.entrance = cell
            elif y == self.size - 1:
                if vertical:
                    cell.remove_top()
                    self.entrance = cell
                else:
                    cell.remove_right()
                    self.exit = cell
            elif 0 < y < self.size - 1:
                cell.remove_top()
                self.entrance = cell
            else:
                self.log.error('Invalid y-coordinate')
                raise Exception('Invalid y-coordinate')
        elif x == self.size - 1:
            if y == self.size - 1:
                if vertical:
                    cell.remove_bottom()
                else:
                    cell.remove_right()
                self.exit = cell
            elif y == 0:
                if vertical:
                    cell.remove_bottom()
                    self.exit = cell
                else:
                    cell.remove_left()
                    self.entrance = cell
            else:
                cell.remove_bottom()
                self.exit = cell
        elif y == 0 < x < self.size - 1:
            cell.remove_left()
            self.entrance = cell
        elif 0 < x < self.size - 1 and y == self.size - 1:
            cell.remove_right()
            self.exit = cell
        else:
            self.log.error('Invalid coordinates')
            raise Exception('Invalid coordinates')

    def set_random_top_entrance(self):
        self.clear_entrance()
        n = random.randint(0, self.size-1)
        self.set_custom_opening(0, n, True)

    def set_random_left_entrance(self):
        self.clear_entrance()
        n = random.randint(0, self.size-1)
        self.set_custom_opening(n, 0, False)

    def set_random_bottom_exit(self):
        self.clear_exit()
        n = random.randint(0, self.size-1)
        self.set_custom_opening(self.size - 1, n, True)

    def set_random_right_exit(self):
        self.clear_exit()
        n = random.randint(0, self.size-1)
        self.set_custom_opening(n, self.size - 1, False)

    def clear_entrance(self):  # clear entrance to get sure a maze only has one entrance
        if self.entrance is not None:
            if self.entrance.get_x() == 0:
                self.entrance.create_top()
            if self.entrance.get_y() == 0:
                self.entrance.create_left()
            self.entrance = None

    def clear_exit(self):  # clear exit to get sure a maze only has one exit
        if self.exit is not None:
            if self.exit.get_x() == self.size-1:
                self.exit.create_bottom()
            if self.exit.get_y() == self.size-1:
                self.exit.create_right()
            self.exit = None

    def get_entrance(self):
        return self.entrance

    def get_exit(self):
        return self.exit

    # returns None if there is no non-border wall that is not removed
    def choose_wall(self, cell, custom_random=random):
        if len([wall for wall in cell.get_wall_list() if not (self.is_border(cell, wall) or wall.is_removed())]) > 0:
            while True:
                wall = cell.choose_wall(custom_random)
                if not self.is_border(cell, wall):
                    return wall
        return None
