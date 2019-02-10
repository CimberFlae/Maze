import random
import logging


class AbstractGenerator:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("generating a " + self.__class__.__name__)
        self.random = random

    def __generate_maze__(self, size):
        """Generate a Maze using a specific algorithm"""
        self.size = size
        if size < 2:
            self.log.error('Invalid maze size!')
            raise Exception('Invalid maze size!')

    def generate_random_maze(self, size, seed=0):
        if seed != 0:
            self.random.seed(seed)
            self.log.debug("generating maze with random seed {%s}", str(seed))
        maze = self.__generate_maze__(size)
        if self.random.getrandbits(1) == 0:
            self.log.debug('generating top entrance')
            maze.set_random_top_entrance()
        else:
            self.log.debug('generating left entrance')
            maze.set_random_left_entrance()
        if self.random.getrandbits(1) == 0:
            maze.set_random_bottom_exit()
        else:
            maze.set_random_right_exit()
        return maze
    
    def generate_custom_maze(self, size, x1, y1, x2, y2, seed=0, coordinates=False):
        """Generate a maze with the entry and exit set to the specified location.
        The entry will be placed at [x1,y1], the exit at [x2,y2].
        The random seed can be provided through the parameter 'seed'.
        By default the generator interprets the given coordinates as indices in a matrix,
        i.e. the top left corner is [0,0], the bottom right corner is [size-1,size-1].
        If you want the coordinates to be interpreted as in a coordinate system,
        set the 'coordinates' parameter to 'True'. In that case the bottom left corner would be [0,0]
        and the top right corner would be [size-1,size-1]"""
        if seed != 0:
            self.random.seed(seed)
            self.log.debug("generating maze with random seed {%s}", str(seed))
        maze = self.__generate_maze__(size)
        if coordinates:
            tmp_x1 = x1
            tmp_x2 = x2
            x1 = size - 1 - y1
            x2 = size - 1 - y2
            y1 = tmp_x1
            y2 = tmp_x2
        maze.set_custom_opening(x1, y1, True)
        maze.set_custom_opening(x2, y2, True)
        return maze
