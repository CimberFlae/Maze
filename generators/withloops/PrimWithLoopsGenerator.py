from generators.PrimGenerator import PrimGenerator
import logging


class PrimWithLoopsGenerator(PrimGenerator):

    def __init__(self):
        PrimGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    # @Override
    def __create_loops__(self, cell, neighbour, wall):
        if cell.wall_count() == 3 and neighbour.wall_count() == 3:
            self.log.debug('removing wall to ' + str(neighbour) + ' to create a loop')
            wall.remove()
            if len([wall for wall in neighbour.get_walls() if not (self.mesh.is_border(neighbour, wall) or wall.is_removed())]) == 0:
                self.queue.remove(neighbour)
