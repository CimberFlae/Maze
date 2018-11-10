import generators.AbstractGenerator as AbstractGenerator
import model.Mesh as Mesh
import logging


class KruskalGenerator(AbstractGenerator.AbstractGenerator):

    def __init__(self):
        AbstractGenerator.AbstractGenerator.__init__(self)
        self.log = logging.getLogger(__name__)

    def __generate_maze__(self, size, seed=0):
        AbstractGenerator.AbstractGenerator.__generate_maze__(self, size)
        """ Kruskal's Algorithm"""
        mesh = Mesh.Mesh(size)
        while mesh.has_multiple_sets():
            cell = mesh.choose_cell()
            wall = mesh.choose_wall(cell)
            if wall == cell.get_left():
                neighbour = mesh.get_left_neighbour(cell)
                if neighbour.get_set() != cell.get_set():
                    cell.remove_left()
                    mesh.move_cell(neighbour.get_set(), cell.get_set())
            elif wall == cell.get_right():
                neighbour = mesh.get_right_neighbour(cell)
                if neighbour.get_set() != cell.get_set():
                    cell.remove_right()
                    mesh.move_cell(neighbour.get_set(), cell.get_set())
            elif wall == cell.get_top():
                neighbour = mesh.get_top_neighbour(cell)
                if neighbour.get_set() != cell.get_set():
                    cell.remove_top()
                    mesh.move_cell(neighbour.get_set(), cell.get_set())
            elif wall == cell.get_bottom():
                neighbour = mesh.get_bottom_neighbour(cell)
                if neighbour.get_set() != cell.get_set():
                    cell.remove_bottom()
                    mesh.move_cell(neighbour.get_set(), cell.get_set())
            else:
                self.log.error('Invalid wall')
                raise Exception('Invalid wall')
        return mesh
