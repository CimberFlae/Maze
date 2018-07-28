import generators.AbstractGenerator as AbstractGenerator
import model.Mesh as Mesh
import random

class PrimGenerator(AbstractGenerator.AbstractGenerator):

    def __init__(self):
        AbstractGenerator.AbstractGenerator.__init__(self)

    def __generateMaze__(self, size, seed = 0):
        if seed != 0:
            random.seed(seed)
        """implement Prim's Algorithm"""
        mesh = Mesh.Mesh(size)
        cell = mesh.chooseCell()
        queue = [cell]
        while (len(queue) > 0):
            n = random.randint(0, len(queue)-1)
            cell = queue[n]
            wall = mesh.chooseWall(cell)
            if (wall == cell.getLeft()):
                neighbour = mesh.getLeftNeighbour(cell)
                if (cell.getSet() != neighbour.getSet()):
                    cell.removeLeft()
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
                    queue.append(neighbour)
            elif (wall == cell.getRight()):
                neighbour = mesh.getRightNeighbour(cell)
                if (cell.getSet() != neighbour.getSet()):
                    cell.removeRight()
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
                    queue.append(neighbour)
            elif (wall == cell.getTop()):
                neighbour = mesh.getTopNeighbour(cell)
                if (cell.getSet() != neighbour.getSet()):
                    cell.removeTop()
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
                    queue.append(neighbour)
            elif (wall == cell.getBottom()):
                neighbour = mesh.getBottomNeighbour(cell)
                if (cell.getSet() != neighbour.getSet()):
                    cell.removeBottom()
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
                    queue.append(neighbour)
            else:
                raise Exception('Invalid wall')
            if (not mesh.hasNeighbourInDifferentSet(cell)):
                queue.remove(cell)
        return mesh
