class Board:
    """
    3X3 Board class for tic-tac-toe game. Contains all the relevent methods for retrieving information from and manipulating the game board.

    Attributes:
    board_list - A 3X3 list representing the game board. 0 represents an empty space, 1 represents a red piece, and 2 represents a blue piece.

    Methods:
    - is_valid_move(x, y) - Returns True if the move is valid, False if not.
    - flip(red, x, y) - Places a piece on the board.
    - undo(x, y) - Removes a piece from the board.
    - print_board() - Prints the current state of the board.
    - check_board() - Returns 1 if red wins, 2 if blue wins, 3 if it's a draw, and 0 if the game is still ongoing.
    - check_twos() - Returns 1 if red has two in a row, 2 if blue has two in a row, and 0 if neither player has two in a row.
    - clear() - Clears the board.
    - get_valid_moves() - Returns a list of valid moves.
    - check_defence() - Returns 1 if red has two in a row and one empty space, 2 if blue has two in a row and one empty space, 
    and 0 if neither player has two in a row.
    - check_line() - Returns 0 if the top row is full, 1 if the middle row is full, 2 if the bottom row is full, 3 if the left 
    column is full, 4 if the middle column is full, 5 if the right column is full, 6 if the left diagonal is full, 7 if the right diagonal 
    is full, and -1 if no line is full.    
    """

    board_list = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
    
    def __init__(self):
        pass

    def is_valid_move(self, x, y):
        """
        Returns True if the move is valid, False if not.
        
        Args:
        - x - The x coordinate of the move.
        - y - The y coordinate of the move.
        
        Returns:
        True if the move is valid, False if not.
        """
        if (self.board_list[y][x] != 0):
            return False
        return True
        
    def flip(self, red, x, y):
        """
        Places a piece on the board.
        
        Args:
        - red - True if the piece is red, False if the piece is blue.
        - x - The x coordinate of the move.
        - y - The y coordinate of the move.
        
        Returns:
        None
        """
        if (red == True):
            self.board_list[y][x] = 1
        else:
            self.board_list[y][x] = 2

    def undo(self, x, y):
        """
        Removes a piece from the board.
        
        Args:
        - x - The x coordinate of the move.
        - y - The y coordinate of the move.
        
        Returns:
        None
        """
        self.board_list[y][x] = 0
    
    def print_board(self):
        """
        Prints the current state of the board.
        
        Args:
        None
        
        Returns:
        None
        """
        for y in self.board_list:
            print(y)
        print('\n')
    
    def check_board(self):
        """
        Returns 1 if red wins, 2 if blue wins, 3 if it's a draw, and 0 if the game is still ongoing.
        
        Args:
        None
        
        Returns:
        1 if red wins, 2 if blue wins, 3 if it's a draw, and 0 if the game is still ongoing.
        """
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
        """
        Returns 1 if red has two in a row, 2 if blue has two in a row, and 0 if neither player has two in a row.
        
        Args:
        None
        
        Returns:
        1 if red has two in a row, 2 if blue has two in a row, and 0 if neither player has two in a row.
        """
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
        """
        Clears the board.
        
        Args:
        None
        
        Returns:
        None
        """

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
        """
        Returns 1 if red has two in a row and one empty space, 2 if blue has two in a row and one empty space,
        and 0 if neither player has two in a row.
        
        Args:
        None
        
        Returns:
        1 if red has two in a row and one empty space, 2 if blue has two in a row and one empty space, and 0 if neither player has two in a row.
        """
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
    
    def check_line(self):
        """
        Returns 0 if the top row is full, 1 if the middle row is full, 2 if the bottom row is full, 3 if the left column is full,
        4 if the middle column is full, 5 if the right column is full, 6 if the left diagonal is full, 7 if the right diagonal is full,
        and -1 if no line is full.
        
        Args:
        None
        
        Returns:
        0 if the top row is full, 1 if the middle row is full, 2 if the bottom row is full, 3 if the left column is full,
        4 if the middle column is full, 5 if the right column is full, 6 if the left diagonal is full, 7 if the right diagonal is full,
        and -1 if no line is full.
        """
        l = self.board_list
        if l[0] == [1,1,1] or l[0] == [2,2,2]:
            return 0
        elif l[1] == [1,1,1] or l[1] == [2,2,2]:
            return 1
        elif l[2] == [1,1,1] or l[2] == [2,2,2]:
            return 2
        elif [l[0][0], l[1][0], l[2][0]] == [1,1,1] or [l[0][0], l[1][0], l[2][0]] == [2,2,2]:
            return 3
        elif [l[0][1], l[1][1], l[2][1]] == [1,1,1] or [l[0][1], l[1][1], l[2][1]] == [2,2,2]:
            return 4
        elif [l[0][2], l[1][2], l[2][2]] == [1,1,1] or [l[0][2], l[1][2], l[2][2]] == [2,2,2]:
            return 5
        elif [l[0][0], l[1][1], l[2][2]] == [1,1,1] or [l[0][0], l[1][1], l[2][2]] == [2,2,2]:
            return 6
        elif [l[0][2], l[1][1], l[2][0]] == [1,1,1] or [l[0][2], l[1][1], l[2][0]] == [2,2,2]:
            return 7