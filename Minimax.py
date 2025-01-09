import math

class Minimax:
    def __init__(self, red):
        self.red = red
        pass

    def evaluate(self, board):
        if (board.check_board() == 1):
            return 10
        elif (board.check_board() == 2):
            return -10
        elif (board.check_twos() == 1):
            return 5
        elif (board.check_twos() == 2):
            return -5
        else:
            return 0
    
    def minimax(self, board, depth, isMax):
        score = self.evaluate(board)
        if score == 10 or score == -10 or board.check_board() == 3:
            return score
        if depth > 2:
             if score == 10 or score == -10 or score == 5 or score == -5 or board.check_board() == 3:
                 return score
        if isMax:
            best = -math.inf
            for y in range(3):
                for x in range(3):
                    if board.is_valid_move(x, y):
                        board.flip(self.red, x, y)
                        best = max(best, self.minimax(board, depth + 1, not self.red))
                        board.undo(x, y)
            return best
        else:
            best = math.inf
            for y in range(3):
                for x in range(3):
                    if board.is_valid_move(x, y):
                        board.flip(not self.red, x, y)
                        best = min(best, self.minimax(board, depth + 1, self.red))
                        board.undo(x, y)
            return best
    
    def generate_answer(self, board):
        best_move = (-1, -1)
        if self.red:
            best_value = -math.inf
            for y in range(3):
                for x in range(3):
                    if board.is_valid_move(x, y):
                        board.flip(self.red, x, y)
                        move_value = self.minimax(board,  0, not self.red)
                        board.undo(x, y)
                        if move_value > best_value:
                            best_value = move_value
                            best_move = (x, y)
            return best_move
        else:
            best_value = math.inf
            for y in range(3):
                for x in range(3):
                    if board.is_valid_move(x, y):
                        board.flip(not self.red, x, y)
                        move_value = self.minimax(board,  0, self.red)
                        board.undo(x, y)
                        if move_value < best_value:
                            best_value = move_value
                            best_move = (x, y)
            return best_move