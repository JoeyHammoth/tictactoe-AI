from tic_tac_toe.main_assets.Board import Board
from tic_tac_toe.ai_models.Random import Random
from tic_tac_toe.ai_models.Minimax import Minimax
from tic_tac_toe.ai_models.MCTS import Mcts
from tic_tac_toe.ai_models.Neural import Nueral

import copy
import csv
import threading

class Master:
    """
    Master class that controls the game and the AI players in the game
    
    Attributes:
    - game_board: Board object that represents the game board
    - game_history: List of the game board at each turn
    - type: Type of AI player
    - max: Maximum depth of Minimax
    - c: Exploration constant for MCTS
    - iterations: Number of iterations for MCTS
    - ai_player: Boolean that represents if the AI player is the first player
    - opp_type: Type of the opponent AI player
    - opp_max: Maximum depth of Minimax for the opponent
    - opp_c: Exploration constant for MCTS for the opponent
    - opp_iterations: Number of iterations for MCTS for the opponent
    - games: Number of games for the Nueral network
    - opp_games: Number of games for the opponent's Nueral network
    - human_move: Tuple that represents the move of the human player
    - condition: Condition object for threading
    - opp_move: Tuple that represents the move of the opponent

    Methods:
    - turn: Generates a move for the player
    - switch_order_human: Switches the order of the AI players
    - run_human: Runs the game with a human player
    - run: Runs the game with two AI players
    
    """
    game_board = Board()
    game_history = []

    def __init__(self, type=0, max=-1, c=-1, iterations=1000, ai_player=False, opp_type=0, opp_max=-1, opp_c=-1, 
                 opp_iterations=1000, games=100000, opp_games=100000):
        # If ai_player is False, Main Player is first, Opp is second
        # Main Player
        if type == -1: # Random
            if ai_player:
                self.blue = Random()
            else:
                self.red = Random()
        elif type == 0: #MCTS
            if ai_player:
                self.blue = Mcts(True, c, iterations)
            else:
                self.red = Mcts(True, c, iterations)
        elif type == 1: #MINIMAX
            if ai_player:
                self.blue = Minimax(True, max)
            else:
                self.red = Minimax(True, max)
        elif type == 2: #MLP
            if ai_player:
                self.blue = Nueral(games)
            else:
                self.red = Nueral(games)
        else: #HUMAN
            self.human_move = (-1,-1)
            self.condition = threading.Condition()
            self.opp_move = (-1,-1)
        
        # Opponent
        if opp_type == 0:
            if ai_player:
                self.red = Random()
            else:
                self.blue = Random()
        elif opp_type == 1:
            if ai_player:
                self.red = Mcts(True, opp_c, opp_iterations)
            else:
                self.blue = Mcts(True, opp_c, opp_iterations)
        elif opp_type == 2:
            if ai_player:
                self.red = Minimax(True, opp_max)
            else:
                self.blue = Minimax(True, opp_max)
        else:
            if ai_player:
                self.red = Nueral(opp_games)
            else:
                self.blue = Nueral(opp_games)

        self.type = type
        self.ai_player = ai_player
        self.opp_type = opp_type
        
    def turn(self, player):
        """
        Generates a move for the player
        
        Args:
        player: AI player object
        
        Returns:
        answer: Tuple that represents the move of the player
        """
        valid = False
        while valid == False:
            g_board = copy.deepcopy(self.game_board)
            answer = player.generate_answer(g_board)
            if (self.game_board.is_valid_move(answer[0], answer[1]) == True):
                valid = True
        return answer
    
    def switch_order_human(self, ai_player):
        """
        Switches the order of the AI players and updates the game board accordingly
        
        Args:
        ai_player: Boolean that represents if the AI player is the first player

        Returns:
        None

        """
        # input ai_player is the NEW order
        if ai_player:
            new_blue = copy.deepcopy(self.red)
            self.blue = new_blue
        else:
            new_red = copy.deepcopy(self.blue)
            self.red = new_red
        self.ai_player = ai_player
    
    def run_human(self):
        """
        Runs the game with a human player
        
        Args:
        None
        
        Returns:
        None
        """
        # Only use this if type == 3
        win = 0 
        self.game_board.clear()
        count = 0
        with self.condition:
            if not self.ai_player:
                while win == 0:
                    if count > 0:
                        self.condition.wait()
                    self.game_board.flip(True, self.human_move[1], self.human_move[0])
                    #self.game_board.print_board()
                    win = self.game_board.check_board()

                    if (win != 0):
                        break

                    blue_answer = self.turn(self.blue)

                    result = (blue_answer[1], blue_answer[0])
                    self.opp_move = result
                    self.condition.notify()

                    self.game_board.flip(False, blue_answer[0], blue_answer[1])
                    #self.game_board.print_board()
                    win = self.game_board.check_board()
                    count += 1
            else:
                while win == 0:

                    red_answer = self.turn(self.red)

                    result = (red_answer[1], red_answer[0])
                    self.opp_move = result
                    self.condition.notify()

                    self.game_board.flip(True, red_answer[0], red_answer[1])
                    #self.game_board.print_board()
                    win = self.game_board.check_board()

                    if (win != 0):
                        break

                    self.condition.wait()
                    self.game_board.flip(False, self.human_move[1], self.human_move[0])
                    #self.game_board.print_board()
                    win = self.game_board.check_board()

            self.condition.notify()
    

    def run(self, filename=0):
        """
        Runs the game with two AI players and writes the results to a file if a filename is provided
        
        Args:
        filename: Name of the file to write the results to
        
        Returns:
        None
        """
        win = 0 
        self.game_board.clear()
        self.game_history = []
        while win == 0:
            red_answer = self.turn(self.red)
            self.game_board.flip(True, red_answer[0], red_answer[1])
            #self.game_board.print_board()
            self.game_history.append(copy.deepcopy(self.game_board.board_list))
            win = self.game_board.check_board()

            if (win != 0):
                break

            blue_answer = self.turn(self.blue)
            self.game_board.flip(False, blue_answer[0], blue_answer[1])
            #self.game_board.print_board()
            self.game_history.append(copy.deepcopy(self.game_board.board_list))
            win = self.game_board.check_board()

        if filename != 0:
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([win])