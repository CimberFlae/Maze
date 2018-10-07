import logging
import sys
import contextlib

class AbstractDrawer:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("generating a drawer")

    def drawMaze(self, maze, filepath):
        """implement a drawing algorithm for the maze"""

    def drawPath(self, maze, path, filepath):
        """implement a drawing algorithm for the path"""

    @contextlib.contextmanager
    def openWriter(self, filepath=None):
        if filepath:
            out = open(filepath, 'w')
        else:
            out = sys.stdout
        try:
            yield out
        finally:
            if out != sys.stdout:
                out.close()