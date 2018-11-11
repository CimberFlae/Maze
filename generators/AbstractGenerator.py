import random
import logging


class AbstractGenerator:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("generating a " + self.__class__.__name__)

    def __generate_maze__(self, size, seed=0):
        """Generate a Maze using a specific algorithm"""
        if size < 2:
            self.log.error('Invalid maze size!')
            raise Exception('Invalid maze size!')

    def generate_random_maze(self, size, seed=0):
        if seed != 0:
            random.seed(seed)
        maze = self.__generate_maze__(size, seed=seed)
        if random.getrandbits(1) == 0:
            maze.set_random_top_entrance()
        else:
            maze.set_random_left_entrance()
        if random.getrandbits(1) == 0:
            maze.set_random_bottom_exit()
        else:
            maze.set_random_right_exit()
        return maze
    
    def generate_custom_maze(self, size, x1, y1, x2, y2, seed=0):
        maze = self.__generate_maze__(size, seed=seed)
        maze.set_custom_opening(x1, y1, True)
        maze.set_custom_opening(x2, y2, True)
        return maze
