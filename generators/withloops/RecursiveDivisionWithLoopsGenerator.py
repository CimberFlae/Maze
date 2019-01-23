from generators.RecursiveDivisionGenerator import RecursiveDivisionGenerator
import logging


class RecursiveDivisionWithLoopsGenerator(RecursiveDivisionGenerator):

    def __init__(self):
        RecursiveDivisionGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    # @Override
    def __create_loops__(self, function_list):
        if self.random.random() <= 1/self.mesh.get_size():
            self.log.debug('creating loop')
            function_list[0]()
