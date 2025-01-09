class Board:
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