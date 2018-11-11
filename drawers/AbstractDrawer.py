import logging
import sys
import contextlib


class AbstractDrawer:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("generating a drawer")

    def draw_maze(self, maze, filepath):
        """implement a drawing algorithm for the maze"""

    def draw_path(self, maze, path, filepath):
        """implement a drawing algorithm for the path"""

    @contextlib.contextmanager
    def open_writer(self, file_path=None):
        if file_path:
            out = open(file_path, 'w')
        else:
            out = sys.stdout
        try:
            yield out
        finally:
            if out != sys.stdout:
                out.close()
