from Board import Board
from Random import Random
from Minimax import Minimax
from MCTS import Mcts
from Neural import Nueral

import copy
import csv
import threading

class Master:
    game_board = Board()

    def __init__(self, type=0, max=-1, c=-1, iterations=1000, ai_player=False, opp_type=0, opp_max=-1, opp_c=-1, opp_iterations=1000):
        # If ai_player is False, Main Player is first, Opp is second
        # Main Player
        if type == 0: #MCTS
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
                self.blue = Nueral()
            else:
                self.red = Nueral()
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
                self.red = Nueral()
            else:
                self.blue = Nueral()

        self.type = type
        self.ai_player = ai_player
        self.opp_type = opp_type
        
    def turn(self, player):
        valid = False
        while valid == False:
            g_board = copy.deepcopy(self.game_board)
            answer = player.generate_answer(g_board)
            if (self.game_board.is_valid_move(answer[0], answer[1]) == True):
                valid = True
        return answer
    
    def run_human(self):
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
                    self.game_board.print_board()
                    win = self.game_board.check_board()

                    if (win != 0):
                        break

                    blue_answer = self.turn(self.blue)

                    result = (blue_answer[1], blue_answer[0])
                    self.opp_move = result
                    self.condition.notify()

                    self.game_board.flip(False, blue_answer[0], blue_answer[1])
                    self.game_board.print_board()
                    win = self.game_board.check_board()
                    count += 1
            else:
                while win == 0:

                    red_answer = self.turn(self.red)

                    result = (red_answer[1], red_answer[0])
                    self.opp_move = result
                    self.condition.notify()

                    self.game_board.flip(True, red_answer[0], red_answer[1])
                    self.game_board.print_board()
                    win = self.game_board.check_board()

                    if (win != 0):
                        break

                    self.condition.wait()
                    self.game_board.flip(False, self.human_move[1], self.human_move[0])
                    self.game_board.print_board()
                    win = self.game_board.check_board()

            self.condition.notify()
    

    def run(self, filename=0):
        win = 0 
        self.game_board.clear()
        while win == 0:
            red_answer = self.turn(self.red)
            self.game_board.flip(True, red_answer[0], red_answer[1])
            self.game_board.print_board()
            win = self.game_board.check_board()

            if (win != 0):
                break

            blue_answer = self.turn(self.blue)
            self.game_board.flip(False, blue_answer[0], blue_answer[1])
            self.game_board.print_board()
            win = self.game_board.check_board()

        if filename != 0:
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([win])