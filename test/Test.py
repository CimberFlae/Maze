import os
os.chdir(os.path.join(os.path.curdir,  '..'))
import generators.KruskalGenerator as KruskalGenerator
import generators.DepthFirstSearchGenerator as DepthFirstSearchGenerator
import generators.PrimGenerator as PrimGenerator
import generators.RecursiveDivisionGenerator as RecursiveDivisionGenerator
import generators.BinaryTreeGenerator as BinaryTreeGenerator
import drawers.ASCIIDrawer as ASCIIDrawer
import solvers.RightWallFollowerSolver as RightWallFollowerSolver
import solvers.LeftWallFollowerSolver as LeftWallFollowerSolver
import solvers.RandomMouseSolver as RandomMouseSolver

class Test:

    size = 5
    drawer = ASCIIDrawer.ASCIIDrawer()
    print("testing the KruskalGenerator and RightWallFollowerSolver")
    generator = KruskalGenerator.KruskalGenerator()
    solver = RightWallFollowerSolver.RightWallFollowerSolver()
    maze = generator.generateMaze(size)
    path = solver.solveMaze(maze)
    drawer.drawMaze(maze)
    drawer.drawPath(maze, path)
    print("Test finished")

    print("testing the DepthFirstSearchGenerator and LeftWallFollowerSolver")
    generator = DepthFirstSearchGenerator.DepthFirstSearchGenerator()
    solver = LeftWallFollowerSolver.LeftWallFollowerSolver()
    maze = generator.generateMaze(size)
    path = solver.solveMaze(maze)
    drawer.drawMaze(maze)
    drawer.drawPath(maze,path)
    print("Test finished")

    print("testing the PrimGenerator and RandomMouseSolver")
    generator = PrimGenerator.PrimGenerator()
    solver = RandomMouseSolver.RandomMouseSolver()
    maze = generator.generateMaze(size)
    #path = solver.solveMaze(maze)
    drawer.drawMaze(maze)
    #drawer.drawPath(maze, path)
    print("Test finished")

    """testing the RecursiveDivisionGenerator"""
    print("testing the RecursiveDivisionGenerator")
    generator = RecursiveDivisionGenerator.RecursiveDivisionGenerator()
    maze = generator.generateMaze(size)
    drawer.drawMaze(maze)
    print("RecursiveDivisionTest finished")

    """testing the BinaryTreeGenerator"""
    print("testing the BinaryTreeGenerator")
    generator = BinaryTreeGenerator.BinaryTreeGenerator()
    maze = generator.generateMaze(size)
    drawer.drawMaze(maze)
    print("All tests finished")
    print(True+True)
