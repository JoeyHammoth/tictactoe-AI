class Board:
    """
    3X3 Board class for tic-tac-toe game. Contains all the relevent methods for retrieving information from and manipulating the game board.

    Methods:
        
    """

    board_list = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
    
    def __init__(self):
        pass

    def is_valid_move(self, x, y):
        if (self.board_list[y][x] != 0):
            return False
        return True
        
    def flip(self, red, x, y):
        if (red == True):
            self.board_list[y][x] = 1
        else:
            self.board_list[y][x] = 2

    def undo(self, x, y):
        self.board_list[y][x] = 0
    
    def print_board(self):
        for y in self.board_list:
            print(y)
        print('\n')
    
    def check_board(self):
        l = self.board_list
        if (l[0] == [1,1,1] or
            l[1] == [1,1,1] or 
            l[2] == [1,1,1] or 
            [l[0][0], l[1][0], l[2][0]] == [1,1,1] or
            [l[0][1], l[1][1], l[2][1]] == [1,1,1] or
            [l[0][2], l[1][2], l[2][2]] == [1,1,1] or
            [l[0][0], l[1][1], l[2][2]] == [1,1,1] or 
            [l[0][2], l[1][1], l[2][0]] == [1,1,1]):
            return 1
        elif (l[0] == [2,2,2] or
            l[1] == [2,2,2] or 
            l[2] == [2,2,2] or 
            [l[0][0], l[1][0], l[2][0]] == [2,2,2] or
            [l[0][1], l[1][1], l[2][1]] == [2,2,2] or
            [l[0][2], l[1][2], l[2][2]] == [2,2,2] or
            [l[0][0], l[1][1], l[2][2]] == [2,2,2] or 
            [l[0][2], l[1][1], l[2][0]] == [2,2,2]):
            return 2
        else:
            for y in l:
                for x in y:
                    if (x == 0):
                        return 0
            return 3
    
    def check_twos(self):
        l = self.board_list
        vert_1 = [l[0][0], l[1][0], l[2][0]]
        vert_2 = [l[0][1], l[1][1], l[2][1]]
        vert_3 = [l[0][2], l[1][2], l[2][2]]
        diag_1 = [l[0][0], l[1][1], l[2][2]]
        diag_2 = [l[0][2], l[1][1], l[2][0]]
        
        if (l[0].count(1) == 2 or
            l[1].count(1) == 2 or
            l[2].count(1) == 2 or
            vert_1.count(1) == 2 or
            vert_2.count(1) == 2 or
            vert_3.count(1) == 2 or
            diag_1.count(1) == 2 or
            diag_2.count(1) == 2):
            return 1
        elif (l[0].count(2) == 2 or
            l[1].count(2) == 2 or
            l[2].count(2) == 2 or
            vert_1.count(2) == 2 or
            vert_2.count(2) == 2 or
            vert_3.count(2) == 2 or
            diag_1.count(2) == 2 or
            diag_2.count(2) == 2):
            return 2
        else:
            return 0
    
    def clear(self):
        self.board_list = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
     
    def get_valid_moves(self):
        valid_moves = []
        l = self.board_list
        for y in range(len(l)):
            for x in range(len(l[y])):
                if (l[y][x] == 0):
                    valid_moves.append((x, y))
        
        return valid_moves
    
    def check_defence(self):
        l = self.board_list
        vert_1 = [l[0][0], l[1][0], l[2][0]]
        vert_2 = [l[0][1], l[1][1], l[2][1]]
        vert_3 = [l[0][2], l[1][2], l[2][2]]
        diag_1 = [l[0][0], l[1][1], l[2][2]]
        diag_2 = [l[0][2], l[1][1], l[2][0]]
        
        if ((l[0].count(2) == 2 and l[0].count(1) == 1) or
            (l[1].count(2) == 2 and l[1].count(1) == 1) or
            (l[2].count(2) == 2 and l[2].count(1) == 1) or
            (vert_1.count(2) == 2 and vert_1.count(1) == 1) or
            (vert_2.count(2) == 2 and vert_2.count(1) == 1) or
            (vert_3.count(2) == 2 and vert_3.count(1) == 1) or
            (diag_1.count(2) == 2 and diag_1.count(1) == 1) or
            (diag_2.count(2) == 2 and diag_2.count(1) == 1)):
            return 1
        elif ((l[0].count(1) == 2 and l[0].count(2) == 1) or
            (l[1].count(1) == 2 and l[1].count(2) == 1) or
            (l[2].count(1) == 2 and l[2].count(2) == 1) or
            (vert_1.count(1) == 2 and vert_1.count(2) == 1) or
            (vert_2.count(1) == 2 and vert_2.count(2) == 1) or
            (vert_3.count(1) == 2 and vert_3.count(2) == 1) or
            (diag_1.count(1) == 2 and diag_1.count(2) == 1) or
            (diag_2.count(1) == 2 and diag_2.count(2) == 1)):
            return 2
        else:
            return 0