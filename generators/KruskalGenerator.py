import generators.Generator as Generator
import model.Mesh as Mesh

class KruskalGenerator(Generator.Generator):

    def __init__(self):
        Generator.Generator.__init__(self)

    def __generateMaze__(self, size, seed = 0):
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
        return mesh
