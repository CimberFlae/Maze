from generators.KruskalGenerator import KruskalGenerator
import logging


class KruskalWithLoopsGenerator(KruskalGenerator):

    def __init__(self):
        KruskalGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    # @Override
    def __create_loops__(self, wall, size):
        # Don't want too many loops, so we set the probability for a cell to remove both walls to 1/(2*size)
        if self.random.random() <= 1/(2*size):
            wall.remove()