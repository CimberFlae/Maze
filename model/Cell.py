from model.Wall import Wall
import random
import logging


class Cell:
    def __init__(self, x, y, set_id, walls_removed=False):
        self.log = logging.getLogger(__name__)
        self.leftWall = Wall(walls_removed)
        self.rightWall = Wall(walls_removed)
        self.topWall = Wall(walls_removed)
        self.bottomWall = Wall(walls_removed)
        self.wallList = [self.leftWall, self.rightWall, self.topWall, self.bottomWall]
        self.x = x
        self.y = y
        self.set = set_id

    # only for debugging
    def check_invariant(self):
        if (self.wallList[0] == self.leftWall) & (self.wallList[1] == self.rightWall) & \
                (self.wallList[2] == self.topWall) & (self.wallList[3] == self.bottomWall):
            self.log.debug("Everything correct")
        else:
            self.log.debug("BUG")

    def set_set(self, set_id):
        self.set = set_id

    def get_set(self):
        return self.set

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_left(self):
        return self.leftWall

    def set_left(self, wall):
        self.leftWall = wall
        self.wallList[0] = wall

    def get_right(self):
        return self.rightWall

    def set_right(self, wall):
        self.rightWall = wall
        self.wallList[1] = wall

    def get_top(self):
        return self.topWall

    def set_top(self, wall):
        self.topWall = wall
        self.wallList[2] = wall

    def get_bottom(self):
        return self.bottomWall

    def set_bottom(self, wall):
        self.bottomWall = wall
        self.wallList[3] = wall
    
    def get_wall_list(self):
        return self.wallList

    def remove_left(self):
        self.leftWall.remove()

    def create_left(self):
        self.leftWall.create()

    def remove_right(self):
        self.rightWall.remove()

    def create_right(self):
        self.rightWall.create()

    def remove_top(self):
        self.topWall.remove()

    def create_top(self):
        self.topWall.create()

    def remove_bottom(self):
        self.bottomWall.remove()

    def create_bottom(self):
        self.bottomWall.create()

    def has_wall(self):
        return (not self.leftWall.is_removed()) | (not self.rightWall.is_removed()) | \
               (not self.topWall.is_removed()) | (not self.bottomWall.is_removed())

    def wall_count(self):
        return (not self.leftWall.is_removed()) + (not self.rightWall.is_removed()) + \
               (not self.topWall.is_removed()) + (not self.bottomWall.is_removed())

    # returns a random wall that is nor removed nor a border.
    # returns None if there is no such wall
    def choose_wall(self, custom_random=random):
        available = [wall for wall in self.wallList if not wall.is_removed()]
        nof_walls = len(available)
        if nof_walls > 0:
            n = custom_random.randint(0, nof_walls-1)
            wall = available[n]
            return wall
        return None

    def __repr__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"
