class Node:
    """A* Pathfinding Node"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    # Define equals
    def __eq__(self, other):
        return self.position == other.position

    # Define representation
    def __repr__(self):
        return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # Define less than
    def __lt__(self, other):
        return self.f < other.f

    # Define greater than
    def __gt__(self, other):
        return self.f > other.f
