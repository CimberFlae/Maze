import generators.Generator as Generator
import model.Mesh as Mesh

class KruskalGenerator(Generator.Generator):

    def __init__(self):
        Generator.Generator.__init__(self)

    def __generateMaze__(self, size, top = True, bottom = True, entry = True, exit = True, seed = 0):
        """ Kruskal's Algorithm"""
        mesh = Mesh.Mesh(size)
        while (mesh.hasMultipleSets()):
            cell = mesh.chooseCell()
            wall = mesh.chooseWall(cell)
            if (wall == mesh.getLeft(cell)):
                neighbour = mesh.getLeftNeighbour(cell)
                if (mesh.getSet(neighbour) != mesh.getSet(cell)):
                    mesh.removeLeft(cell)
                    mesh.moveCell(neighbour.getSet(),cell.getSet())
            elif (wall == mesh.getRight(cell)):
                neighbour = mesh.getRightNeighbour(cell)
                if (mesh.getSet(neighbour) != mesh.getSet(cell)):
                    mesh.removeRight(cell)
                    mesh.moveCell(neighbour.getSet(),cell.getSet())
            elif (wall == mesh.getTop(cell)):
                neighbour = mesh.getTopNeighbour(cell)
                if (mesh.getSet(neighbour) != mesh.getSet(cell)):
                    mesh.removeTop(cell)
                    mesh.moveCell(neighbour.getSet(),cell.getSet())
            elif (wall == mesh.getBottom(cell)):
                neighbour = mesh.getBottomNeighbour(cell)
                if (mesh.getSet(neighbour) != mesh.getSet(cell)):
                    mesh.removeBottom(cell)
                    mesh.moveCell(neighbour.getSet(),cell.getSet())
        return mesh
