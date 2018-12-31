from generators.DepthFirstSearchGenerator import DepthFirstSearchGenerator
import logging


class DepthFirstSearchWithLoopsGenerator(DepthFirstSearchGenerator):

    def __init__(self):
        DepthFirstSearchGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    # @Override
    def __handleDeadEnd__(self, cell):
        if cell.wall_count() == 3:  # Don't want too many loops
            wall = self.mesh.choose_wall(cell, self.random)
            if wall is not None:
                wall.remove()
        return self.stack.pop()