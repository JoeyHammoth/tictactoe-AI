import random

class Random:
    """
    Random AI algorithm for tic-tac-toe. Randomly chooses a move on the game board. Does not have valid move check.

    Methods:
        generate_answer(board): Return a random move coordinate tuple.
    """
     
    def __init__(self):
        pass

    def generate_answer(self, board=None):
        """
        Generates a random tuple based on game board size.

        Args:
        board (Board): Master game board object.

        Returns:
        tuple: Random move coord.
        """

        return (random.randint(0,2), random.randint(0,2))