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
                if (wall == cell.getLeft()):
                    neighbour = mesh.getLeftNeighbour(cell)
                    if (neighbour.getSet() != cell.getSet()):
                        cell.removeLeft()
                        mesh.moveCell(neighbour.getSet(), cell.getSet())
                        stack.append(cell)
                        cell = neighbour
                elif (wall == cell.getRight()):
                    neighbour = mesh.getRightNeighbour(cell)
                    if (neighbour.getSet() != cell.getSet()):
                        cell.removeRight()
                        mesh.moveCell(neighbour.getSet(), cell.getSet())
                        stack.append(cell)
                        cell = neighbour
                elif (wall == cell.getTop()):
                    neighbour = mesh.getTopNeighbour(cell)
                    if (neighbour.getSet() != cell.getSet()):
                        cell.removeTop()
                        mesh.moveCell(neighbour.getSet(), cell.getSet())
                        stack.append(cell)
                        cell = neighbour
                elif (wall == cell.getBottom()):
                    neighbour = mesh.getBottomNeighbour(cell)
                    if (neighbour.getSet() != cell.getSet()):
                        cell.removeBottom()
                        mesh.moveCell(neighbour.getSet(), cell.getSet())
                        stack.append(cell)
                        cell = neighbour
                else:
                    raise Exception('Invalid wall')
            else:
                cell = stack.pop()
        return mesh
