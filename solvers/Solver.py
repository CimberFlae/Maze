class Solver:

    def __init__(self):
        self.path = []
        print("generating a solver")

    def solveMaze(self,maze):
        """implement a solving algorithm"""

    def cleanPath(self):
        i = 2
        while (i < len(self.path)):
            if (self.path[i-2] == self.path[i]):
                self.cleanup(i-2,i)
                i = 0
            else:
                i += 1

    def cleanup(self,i,j):
        if (self.path[i-1] == self.path[j+1]):
            self.cleanup(i-1,j+1)
        else:
            del self.path[(i+1):(j+1)]
