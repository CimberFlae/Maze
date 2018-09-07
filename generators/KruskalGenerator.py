import generators.AbstractGenerator as AbstractGenerator
import model.Mesh as Mesh

class KruskalGenerator(AbstractGenerator.AbstractGenerator):

    def __init__(self):
        AbstractGenerator.AbstractGenerator.__init__(self)

    def __generateMaze__(self, size, seed = 0):
        AbstractGenerator.AbstractGenerator.__generateMaze__(self, size)
        """ Kruskal's Algorithm"""
        mesh = Mesh.Mesh(size)
        while (mesh.hasMultipleSets()):
            cell = mesh.chooseCell()
            wall = mesh.chooseWall(cell)
            if (wall == cell.getLeft()):
                neighbour = mesh.getLeftNeighbour(cell)
                if (neighbour.getSet() != cell.getSet()):
                    cell.removeLeft()
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
            elif (wall == cell.getRight()):
                neighbour = mesh.getRightNeighbour(cell)
                if (neighbour.getSet() != cell.getSet()):
                    cell.removeRight()
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
            elif (wall == cell.getTop()):
                neighbour = mesh.getTopNeighbour(cell)
                if (neighbour.getSet() != cell.getSet()):
                    cell.removeTop()
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
            elif (wall == cell.getBottom()):
                neighbour = mesh.getBottomNeighbour(cell)
                if (neighbour.getSet() != cell.getSet()):
                    cell.removeBottom()
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
            else:
                raise Exception('Invalid wall')
        return mesh
