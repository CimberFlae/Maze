import random
import logging


class AbstractSolver:
    """Base class for all maze solvers. Every solver implements its own algorithm to solve a maze by using
    or overriding the base class methods."""

    def __init__(self, seed=0):
        self.log = logging.getLogger(__name__)
        self.path = []
        self.log.debug("generating a " + self.__class__.__name__)
        self.random = random
        if seed != 0:
            self.random.seed(seed)

    def solve_maze(self, maze):
        """Solve a maze. The solving algorithm is decided by the instantiating class.
        This method has to be implemented by the concrete subclassing solver."""

    # cleans the path of redundant moves
    def __clean_path__(self):
        i = 2
        while i < len(self.path):
            if self.path[i - 2] == self.path[i]:
                self.__cleanup__(i - 2, i)
                i = 2
            else:
                i += 1

    def __cleanup__(self, i, j):
        if i > 0 and j < len(self.path) - 1 and self.path[i - 1] == self.path[j + 1]:
            self.__cleanup__(i - 1, j + 1)
        else:
            del self.path[(i + 1):(j + 1)]

    def __is_junction__(self, cell):
        self.log.debug("current cell: " + str(cell) + " is junction: " + str(cell.wall_count() < 2))
        return cell.wall_count() < 2

    def __isPath__(self, cell):
        return cell.wall_count() == 2 and cell != self.maze.get_entrance()

    def __isDeadEnd__(self, cell):
        return cell.wall_count() == 3 or cell.wall_count() == 2 and cell == self.maze.get_entrance()

    def __cameFromTop__(self):
        previous = self.__getPrevious__()
        current = self.path[-1]
        return previous is not None and self.maze.get_top_neighbour(current) == previous \
               or previous is None and self.maze.get_top_neighbour(current) is None \
               and current.get_top().is_removed()

    def __cameFromRight__(self):
        previous = self.__getPrevious__()
        return previous is not None and self.maze.get_right_neighbour(self.path[-1]) == previous

    def __cameFromBottom__(self):
        previous = self.__getPrevious__()
        return previous is not None and self.maze.get_bottom_neighbour(self.path[-1]) == previous

    def __cameFromLeft__(self):
        previous = self.__getPrevious__()
        current = self.path[-1]
        return previous is not None and self.maze.get_left_neighbour(current) == previous \
               or previous is None and self.maze.get_left_neighbour(current) is None \
               and current.get_left().is_removed()

    def __getPrevious__(self):
        return self.path[-2] if len(self.path) > 1 else None

    def __findNext__(self):  # if there is only one way to go
        current = self.path[-1]
        if self.__cameFromBottom__():
            if current.get_left().is_removed() and self.maze.get_left_neighbour(current) is not None:
                self.__try_left__()
            elif current.get_right().is_removed() and self.maze.get_right_neighbour(current) is not None:
                self.__try_right__()
            elif current.get_top().is_removed() and self.maze.get_top_neighbour(current) is not None:
                self.__try_top__()
            else:
                self.log.error('No way out')
                raise Exception('No way out')
        elif self.__cameFromLeft__():
            if current.get_bottom().is_removed() and self.maze.get_bottom_neighbour(current) is not None:
                self.__try_bottom__()
            elif current.get_right().is_removed() and self.maze.get_right_neighbour(current) is not None:
                self.__try_right__()
            elif current.get_top().is_removed() and self.maze.get_top_neighbour(current) is not None:
                self.__try_top__()
            else:
                self.log.error('No way out')
                raise Exception('No way out')
        elif self.__cameFromRight__():
            if current.get_bottom().is_removed() and self.maze.get_bottom_neighbour(current) is not None:
                self.__try_bottom__()
            elif current.get_left().is_removed() and self.maze.get_left_neighbour(current) is not None:
                self.__try_left__()
            elif current.get_top().is_removed() and self.maze.get_top_neighbour(current) is not None:
                self.__try_top__()
            else:
                self.log.error('No way out')
                raise Exception('No way out')
        elif self.__cameFromTop__():
            if current.get_bottom().is_removed() and self.maze.get_bottom_neighbour(current) is not None:
                self.__try_bottom__()
            elif current.get_left().is_removed() and self.maze.get_left_neighbour(current) is not None:
                self.__try_left__()
            elif current.get_right().is_removed() and self.maze.get_right_neighbour(current) is not None:
                self.__try_right__()
            else:
                self.log.error('No way out')
                raise Exception('No way out')
        elif self.path[-1] == self.maze.get_entrance():  # We're at the entrance
            self.__handle_junction__()
        else:
            self.log.error('Came from nowhere')
            raise Exception('Came from nowhere')

    def __choose_direction__(self, directions):
        n = self.random.randint(0, len(directions) - 1)
        directions[n]()

    def __decide_next__(self):
        current = self.path[-1]
        if current == self.maze.get_exit():
            return
        self.log.debug("deciding next in: " + str(current))
        if self.__is_junction__(current):
            self.__handle_junction__()
            self.log.debug('finished handling junction')
        elif self.__isPath__(current):
            self.__handle_path__()
        elif self.__isDeadEnd__(current):  # do nothing and go back
            self.__handle_dead_end__()
        else:
            self.log.error('Invalid wall count')
            raise Exception('Invalid wall count')

    def __handle_junction__(self):
        self.log.debug('handling junction...')
        current = self.path[-1]
        if self.__cameFromTop__():
            self.log.debug('came from top...')
            directions = [self.__try_bottom__, self.__try_left__, self.__try_right__]
        elif self.__cameFromBottom__():
            self.log.debug('came from bottom...')
            directions = [self.__try_left__, self.__try_right__, self.__try_top__]
        elif self.__cameFromLeft__():
            self.log.debug('came from left...')
            directions = [self.__try_bottom__, self.__try_right__, self.__try_top__]
        elif self.__cameFromRight__():
            self.log.debug('came from right...')
            directions = [self.__try_bottom__, self.__try_left__, self.__try_top__]
        elif self.path[-1] == self.maze.get_entrance():  # We're at the entrance
            self.log.debug('we are at the entrance...')
            directions = [self.__try_bottom__, self.__try_left__, self.__try_right__, self.__try_top__]
        else:
            self.log.error('Came from nowhere')
            raise Exception('Came from nowhere')
        while current == self.path[-1] and current != self.maze.get_exit():
            self.__choose_direction__(directions)

    def __handle_path__(self):
        self.__findNext__()

    def __handle_dead_end__(self):
        current = self.path[-1]
        [pathway] = list(filter(lambda wall: wall.is_removed() and self.maze.get_neighbour(current, wall) is not None,
                         current.get_walls()))
        self.log.debug(self.maze.get_neighbour(current, pathway))
        if pathway == current.get_top():
            self.__try_top__()
        elif pathway == current.get_bottom():
            self.__try_bottom__()
        elif pathway == current.get_left():
            self.__try_left__()
        elif pathway == current.get_right():
            self.__try_right__()
        else:
            self.log.error('Came from nowhere')
            raise Exception('Came from nowhere')

    def __try_bottom__(self):
        pass  # to be implemented in subclass

    def __try_left__(self):
        pass  # to be implemented in subclass

    def __try_right__(self):
        pass  # to be implemented in subclass

    def __try_top__(self):
        pass  # to be implemented in subclass
