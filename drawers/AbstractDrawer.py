import logging
import sys
import contextlib


class AbstractDrawer:
    """Base class for all maze/path drawers. Every drawer implements its own algorithm to draw a maze or a path."""

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("generating a drawer")

    def draw_maze(self, maze, file_path):
        """Draw a maze. The drawing algorithm is decided by the instantiating class.
        This method has to be implemented by the concrete subclassing drawer."""

    def draw_path(self, maze, path, file_path):
        """Draw a path. The drawing algorithm is decided by the instantiating class.
        This method has to be implemented by the concrete subclassing drawer."""

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
