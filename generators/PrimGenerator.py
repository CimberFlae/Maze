import generators.Generator as Generator
import model.Mesh as Mesh
import random

class PrimGenerator(Generator.Generator):

    def __init__(self):
        Generator.Generator.__init__(self)

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
                    mesh.removeLeft(cell)
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
                    queue.append(neighbour)
            elif (wall == cell.getRight()):
                neighbour = mesh.getRightNeighbour(cell)
                if (cell.getSet() != neighbour.getSet()):
                    mesh.removeRight(cell)
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
                    queue.append(neighbour)
            elif (wall == cell.getTop()):
                neighbour = mesh.getTopNeighbour(cell)
                if (cell.getSet() != neighbour.getSet()):
                    mesh.removeTop(cell)
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
                    queue.append(neighbour)
            elif (wall == cell.getBottom()):
                neighbour = mesh.getBottomNeighbour(cell)
                if (cell.getSet() != neighbour.getSet()):
                    mesh.removeBottom(cell)
                    mesh.moveCell(neighbour.getSet(), cell.getSet())
                    queue.append(neighbour)
            if (not mesh.hasNeighbourInDifferentSet(cell)):
                queue.remove(cell)
        return mesh
