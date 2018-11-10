import random
import logging

class AbstractSolver:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.path = []
        self.log.debug("generating a solver")

    def solveMaze(self, maze):
        """implement a solving algorithm"""

    # cleans the path of redundant moves
    def __cleanPath__(self):
        i = 2
        while (i < len(self.path)):
            if (self.path[i-2] == self.path[i]):
                self.__cleanup__(i - 2, i)
                i = 2
            else:
                i += 1

    def __cleanup__(self, i, j):
        if (i > 0 and j < len(self.path)-1 and self.path[i-1] == self.path[j+1]):
            self.__cleanup__(i - 1, j + 1)
        else:
            del self.path[(i+1):(j+1)]

    def __isJunction__(self, cell):
        return cell.wall_count() < 2

    def __isPath__(self, cell):
        return cell.wall_count() == 2 and cell != self.maze.get_entrance()

    def __isDeadEnd__(self, cell):
        return cell.wall_count() == 3 or cell.wall_count() == 2 and cell == self.maze.get_entrance()

    def __cameFromTop__(self):
        previous = self.__getPrevious__()
        return previous != None and self.maze.get_top_neighbour(self.path[-1]) == previous

    def __cameFromRight__(self):
        previous = self.__getPrevious__()
        return previous != None and self.maze.get_right_neighbour(self.path[-1]) == previous

    def __cameFromBottom__(self):
        previous = self.__getPrevious__()
        return previous != None and self.maze.get_bottom_neighbour(self.path[-1]) == previous

    def __cameFromLeft__(self):
        previous = self.__getPrevious__()
        return previous != None and self.maze.get_left_neighbour(self.path[-1]) == previous

    def __getPrevious__(self):
        return self.path[-2] if len(self.path) > 1 else None

    def __findNext__(self): # if there is only one way to go
        current = self.path[-1]
        if (self.__cameFromBottom__()):
            if (current.get_left().isRemoved()):
                self.__tryLeft__()
            elif (current.get_right().isRemoved()):
                self.__tryRight__()
            elif (current.get_top().isRemoved()):
                self.__tryTop__()
            else:
                self.log.error('No way out')
                raise Exception('No way out')
        elif (self.__cameFromLeft__()):
            if (current.get_bottom().isRemoved()):
                self.__tryBottom__()
            elif (current.get_right().isRemoved()):
                self.__tryRight__()
            elif (current.get_top().isRemoved()):
                self.__tryTop__()
            else:
                self.log.error('No way out')
                raise Exception('No way out')
        elif (self.__cameFromRight__()):
            if (current.get_bottom().isRemoved()):
                self.__tryBottom__()
            elif (current.get_left().isRemoved()):
                self.__tryLeft__()
            elif (current.get_top().isRemoved()):
                self.__tryTop__()
            else:
                self.log.error('No way out')
                raise Exception('No way out')
        elif (self.__cameFromTop__()):
            if (current.get_bottom().isRemoved()):
                self.__tryBottom__()
            elif (current.get_left().isRemoved()):
                self.__tryLeft__()
            elif (current.get_right().isRemoved()):
                self.__tryRight__()
            else:
                self.log.error('No way out')
                raise Exception('No way out')
        elif (self.path[-1] == self.maze.get_entrance()): # We're at the entrance
            self.__handleJunction__()
        else:
            self.log.error('Came from nowhere')
            raise Exception('Came from nowhere')

    def __chooseDirection__(self, directions):
        n = random.randint(0, len(directions)-1)
        directions[n]()

    def __decideNext__(self):
        current = self.path[-1]
        if self.__isJunction__(current):
            self.__handleJunction__()
        elif self.__isPath__(current):
            self.__handlePath__()
        elif self.__isDeadEnd__(current): # do nothing and go back
            self.__handleDeadEnd__()
        else:
            self.log.error('Invalid wall count')
            raise Exception('Invalid wall count')

    def __handleJunction__(self):
        current = self.path[-1]
        if (self.__cameFromTop__()):
            directions = [self.__tryBottom__, self.__tryLeft__, self.__tryRight__]
        elif (self.__cameFromBottom__()):
            directions = [self.__tryLeft__, self.__tryRight__, self.__tryTop__]
        elif (self.__cameFromLeft__()):
            directions = [self.__tryBottom__, self.__tryRight__, self.__tryTop__]
        elif (self.__cameFromRight__()):
            directions = [self.__tryBottom__, self.__tryLeft__, self.__tryTop__]
        elif (self.path[-1] == self.maze.get_entrance()): # We're at the entrance
            directions = [self.__tryBottom__, self.__tryLeft__, self.__tryRight__, self.__tryTop__]
        else:
            self.log.error('Came from nowhere')
            raise Exception('Came from nowhere')
        while (current == self.path[-1] and current != self.maze.get_exit()):
            self.__chooseDirection__(directions)

    def __handlePath__(self):
        self.__findNext__()

    def __handleDeadEnd__(self):
        if (self.__cameFromTop__()):
            self.__tryTop__()
        elif (self.__cameFromBottom__()):
            self.__tryBottom__()
        elif (self.__cameFromLeft__()):
            self.__tryLeft__()
        elif (self.__cameFromRight__()):
            self.__tryRight__()
        elif (self.path[-1] == self.maze.get_entrance()): # We're at the entrance
            self.__handleJunction__()
        else:
            self.log.error('Came from nowhere')
            raise Exception('Came from nowhere')

    def __tryBottom__(self):
        pass # to be implemented in subclass

    def __tryLeft__(self):
        pass  # to be implemented in subclass

    def __tryRight__(self):
        pass  # to be implemented in subclass

    def __tryTop__(self):
        pass  # to be implemented in subclass