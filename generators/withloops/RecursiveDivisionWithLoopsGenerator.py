from generators.RecursiveDivisionGenerator import RecursiveDivisionGenerator
import logging


class RecursiveDivisionWithLoopsGenerator(RecursiveDivisionGenerator):

    def __init__(self):
        RecursiveDivisionGenerator.__init__(self)
        self.log = logging.getLogger(__name__)
        self.foo = lambda: self.random.random() <= 1/self.mesh.get_size()

    # @Override
    def __create_loops__(self, function_list):
        if self.foo():
            self.log.debug('creating loop')
            function_list[0]()

    def set_probability_function(self, foo):
        self.foo = foo
