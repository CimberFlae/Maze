class Wall:
    def __init__(self, removed=False):
        self.removed = removed

    def remove(self):
        self.removed = True

    def create(self):
        self.removed = False

    def isRemoved(self):
        return self.removed