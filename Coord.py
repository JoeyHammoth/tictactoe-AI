import math

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        content = 0
    
    def distance(self, x, y):
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)