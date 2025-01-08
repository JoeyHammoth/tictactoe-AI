import Coord

class Board:
    def __init__(self):
        zero_zero = Coord(0, 0)
        one_zero = Coord(1, 0)
        two_zero = Coord(2, 0)
        zero_one = Coord(0, 1)
        one_one = Coord(1, 1)
        two_one = Coord(2, 1)
        zero_two = Coord(0, 2)
        one_two = Coord(1, 2)
        two_two = Coord(2, 2)
        list = [zero_zero, one_zero, two_zero, zero_one, one_one, two_one, zero_two, one_two, two_two]
    
    def circleFlip(self, x, y):
        for crd in list:
            if (crd.x == x and crd.y == y):
                crd.content = 1
    
    def squareFlip(self, x, y):
        for crd in list:
            if (crd.x == x and crd.y == y):
                crd.content = 2

    def clearBoard(self):
        for crd in list:
            crd.content = 0
