import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import generators.KruskalGenerator as KruskalGenerator
import generators.DepthFirstSearchGenerator as DepthFirstSearchGenerator
import generators.PrimGenerator as PrimGenerator
import generators.RecursiveDivisionGenerator as RecursiveDivisionGenerator
import generators.BinaryTreeGenerator as BinaryTreeGenerator
import drawers.ASCIIDrawer as ASCIIDrawer
import solvers.RightWallFollowerSolver as RightWallFollowerSolver
import solvers.LeftWallFollowerSolver as LeftWallFollowerSolver
import solvers.RandomMouseSolver as RandomMouseSolver
import solvers.TremauxSolver as TremauxSolver

class Demo:

    size = 10
    drawer = ASCIIDrawer.ASCIIDrawer()
    print("Showcasing the KruskalGenerator and RightWallFollowerSolver")
    generator = KruskalGenerator.KruskalGenerator()
    solver = RightWallFollowerSolver.RightWallFollowerSolver()
    maze = generator.generate_random_maze(size)
    path = solver.solveMaze(maze)
    drawer.draw_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcase finished")

    print("Showcasing the DepthFirstSearchGenerator and LeftWallFollowerSolver")
    generator = DepthFirstSearchGenerator.DepthFirstSearchGenerator()
    solver = LeftWallFollowerSolver.LeftWallFollowerSolver()
    maze = generator.generate_random_maze(size)
    path = solver.solveMaze(maze)
    drawer.draw_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcase finished")

    print("Showcasing the PrimGenerator and RandomMouseSolver")
    generator = PrimGenerator.PrimGenerator()
    solver = RandomMouseSolver.RandomMouseSolver()
    maze = generator.generate_random_maze(size)
    path = solver.solveMaze(maze)
    drawer.draw_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcase finished")

    print("Showcasing the RecursiveDivisionGenerator and TremauxSolver")
    generator = RecursiveDivisionGenerator.RecursiveDivisionGenerator()
    solver = TremauxSolver.TremauxSolver()
    maze = generator.generate_random_maze(size)
    path = solver.solveMaze(maze)
    drawer.draw_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcasine finished")

    print("Showcasing the BinaryTreeGenerator")
    generator = BinaryTreeGenerator.BinaryTreeGenerator()
    maze = generator.generate_random_maze(size)
    drawer.draw_maze(maze)
    print("All Showcases finished")
