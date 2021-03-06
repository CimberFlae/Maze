from generators.BinaryTreeGenerator import BinaryTreeGenerator
import logging


class BinaryTreeWithLoopsGenerator(BinaryTreeGenerator):

    def __init__(self):
        BinaryTreeGenerator.__init__(self)
        self.log = logging.getLogger(__name__)
        self.foo = lambda: self.random.random() <= 1/(2*self.size)

    # @Override
    def __create_loops__(self, cell, size):
        # Don't want too many loops, so we set the probability for a cell to remove both walls to 1/(2*size)
        if self.foo():
            cell.remove_left()
            cell.remove_top()

    def set_probability_function(self, foo):
        self.foo = foo
