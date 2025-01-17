import math

class Minimax:
    """
    Minimax AI algorithm for tic-tac-toe. It decides the best move for the current player by predicting the opponent’s moves.

    Methods:
    - evaluate(board): Used internally as the evaluation function for scoring moves. Returns the score for a move.
    - minimax(board, depth, isMax): Internally used recursion function that navigates the minimax tree. Returns the best score for a move state.
    - generate_answer(board): Provide the move coord with the best score.
    """

    def __init__(self, red, max_depth):
        self.red = red
        self.max_depth = max_depth
        pass

    def evaluate(self, board):
        """
        Returns the score for a move based on whether move results in win/lose/draw/strategic position.

        Args:
        board (Board): Master game board object.

        Returns:
        int: Score of the move.
        """
        
        if (board.check_board() == 1):
            return 10
        elif (board.check_board() == 2):
            return -10
        elif (board.check_twos() == 1 or board.check_defence() == 1):
            return 5
        elif (board.check_twos() == 2 or board.check_defence() == 2):
            return -5
        else:
            return 0
    
    def minimax(self, board, depth, isMax):
        """
        Iterate through the minimax tree and return the best score possible for a move state chosen by the 
        generate_answer method.

        Args:
        - board (Board): Master game board object.
        - depth (int): Current depth of the minimax tree.
        - isMax (boolean): Is maximizing player or not.

        Returns:
        int: Best score of the move state.
        """

        score = self.evaluate(board)
        if score == 10 or score == -10 or board.check_board() == 3:
            return score
        if depth > self.max_depth:
             if score == 10 or score == -10 or score == 5 or score == -5 or board.check_board() == 3:
                 return score
        if isMax: # Maximizing player
            best = -math.inf
            # Iterate over every possible move
            for y in range(3):
                for x in range(3):
                    if board.is_valid_move(x, y): # Check if move is valid
                        board.flip(self.red, x, y) # Make move in current board
                        best = max(best, self.minimax(board, depth + 1, not self.red)) # Check if move leads to a win or strategic position
                        board.undo(x, y) # Undo the move to reset to initial board for next move check
            return best
        else:
            best = math.inf # Opponent (Minimizing the score of the player)
            for y in range(3):
                for x in range(3):
                    if board.is_valid_move(x, y):
                        board.flip(not self.red, x, y)
                        best = min(best, self.minimax(board, depth + 1, self.red))
                        board.undo(x, y)
            return best
    
    ## generate_answer 
    def generate_answer(self, board):
        """
        Iterate through all the possible moves and create a move state based on these moves to determine which
        move leads to the best move state using minimax method. 

        Args:
        board (Board): Master game board object.

        Returns:
        tuple: Move with best score.
        """

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