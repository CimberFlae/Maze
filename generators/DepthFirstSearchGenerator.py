import generators.Generator as Generator
import model.Mesh as Mesh

class DepthFirstSearchGenerator(Generator.Generator):

    def __init__(self):
        Generator.Generator.__init__(self)

    def __generateMaze__(self, size, seed = 0):
        """implement Depth-first Search Algorithm"""
        mesh = Mesh.Mesh(size)
        cell = mesh.chooseCell()
        stack = []
        while (mesh.hasMultipleSets()):
            if (mesh.hasNeighbourInDifferentSet(cell)):
                wall = mesh.chooseWall(cell)
                if (wall == mesh.getLeft(cell)):
                    neighbour = mesh.getLeftNeighbour(cell)
                    if (mesh.getSet(neighbour) != mesh.getSet(cell)):
                        mesh.removeLeft(cell)
                        mesh.moveCell(neighbour.getSet(),cell.getSet())
                        stack.append(cell)
                        cell = neighbour
                elif (wall == mesh.getRight(cell)):
                    neighbour = mesh.getRightNeighbour(cell)
                    if (mesh.getSet(neighbour) != mesh.getSet(cell)):
                        mesh.removeRight(cell)
                        mesh.moveCell(neighbour.getSet(),cell.getSet())
                        stack.append(cell)
                        cell = neighbour
                elif (wall == mesh.getTop(cell)):
                    neighbour = mesh.getTopNeighbour(cell)
                    if (mesh.getSet(neighbour) != mesh.getSet(cell)):
                        mesh.removeTop(cell)
                        mesh.moveCell(neighbour.getSet(),cell.getSet())
                        stack.append(cell)
                        cell = neighbour
                elif (wall == mesh.getBottom(cell)):
                    neighbour = mesh.getBottomNeighbour(cell)
                    if (mesh.getSet(neighbour) != mesh.getSet(cell)):
                        mesh.removeBottom(cell)
                        mesh.moveCell(neighbour.getSet(),cell.getSet())
                        stack.append(cell)
                        cell = neighbour
            else:
                cell = stack.pop()
        return mesh
