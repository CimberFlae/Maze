import os
import sys
from generators.KruskalGenerator import KruskalGenerator
from generators.withloops.KruskalWithLoopsGenerator import KruskalWithLoopsGenerator
from generators.DepthFirstSearchGenerator import DepthFirstSearchGenerator
from generators.withloops.DepthFirstSearchWithLoopsGenerator import DepthFirstSearchWithLoopsGenerator
from generators.PrimGenerator import PrimGenerator
from generators.RecursiveDivisionGenerator import RecursiveDivisionGenerator
from generators.withloops.BinaryTreeWithLoopsGenerator import BinaryTreeWithLoopsGenerator
from generators.BinaryTreeGenerator import BinaryTreeGenerator
from drawers.ASCIIDrawer import ASCIIDrawer
from drawers.TkInterDrawer import TkInterDrawer
from solvers.RightWallFollowerSolver import RightWallFollowerSolver
from solvers.LeftWallFollowerSolver import LeftWallFollowerSolver
from solvers.RandomMouseSolver import RandomMouseSolver
from solvers.TremauxSolver import TremauxSolver
import random
import LoggingConfiguration
import logging.config
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


class Demo:
    logging.config.dictConfig(LoggingConfiguration.LOGGING)
    seed = random.randint(1, 100)

    size = 10
    drawer = ASCIIDrawer()
    print("Showcasing the KruskalGenerator and RightWallFollowerSolver")
    generator = KruskalGenerator()
    solver = RightWallFollowerSolver(seed)
    maze = generator.generate_random_maze(size, seed)
    drawer.draw_maze(maze)
    path = solver.solve_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcase finished")

    print("Showcasing the DepthFirstSearchGenerator and LeftWallFollowerSolver")
    generator = DepthFirstSearchGenerator()
    solver = LeftWallFollowerSolver(seed)
    maze = generator.generate_random_maze(size, seed)
    drawer.draw_maze(maze)
    path = solver.solve_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcase finished")

    print("Showcasing the PrimGenerator and RandomMouseSolver")
    generator = PrimGenerator()
    solver = RandomMouseSolver(seed)
    maze = generator.generate_random_maze(size, seed)
    drawer.draw_maze(maze)
    path = solver.solve_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcase finished")

    print("Showcasing the RecursiveDivisionGenerator and TremauxSolver")
    generator = RecursiveDivisionGenerator()
    solver = TremauxSolver(seed)
    maze = generator.generate_random_maze(size, seed)
    drawer.draw_maze(maze)
    path = solver.solve_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcasing finished")

    print("Showcasing the DepthFirstSearchWithLoopsGenerator and RightWallFollowerSolver")
    generator = DepthFirstSearchWithLoopsGenerator()
    solver = RightWallFollowerSolver(seed)
    maze = generator.generate_random_maze(size, seed)
    drawer.draw_maze(maze)
    path = solver.solve_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcasing finished")

    print("Showcasing the BinaryTreeWithLoopsGenerator and LeftWallFollowerSolver")
    generator = BinaryTreeWithLoopsGenerator()
    solver = LeftWallFollowerSolver(seed)
    maze = generator.generate_random_maze(size, seed)
    drawer.draw_maze(maze)
    path = solver.solve_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcasing finished")

    print("Showcasing the KruskalWithLoopsGenerator and RandomMouseSolver")
    generator = KruskalWithLoopsGenerator()
    solver = RandomMouseSolver(seed)
    maze = generator.generate_random_maze(size, seed)
    drawer.draw_maze(maze)
    path = solver.solve_maze(maze)
    drawer.draw_path(maze, path)
    print("Showcasing finished")

    print("Showcasing the BinaryTreeGenerator and TkInter Drawer")
    drawer = TkInterDrawer()
    generator = BinaryTreeGenerator()
    maze = generator.generate_random_maze(size, seed)
    path = solver.solve_maze(maze)
    drawer.draw_maze(maze, path)
    print("All Showcases finished")

