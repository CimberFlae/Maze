import logging

class AbstractDrawer:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug("generating a drawer")

    def drawMaze(self,maze):
        """implement a drawing algorithm for the maze"""

    def drawPath(self,maze,path):
        """implement a drawing algorithm for the path"""
