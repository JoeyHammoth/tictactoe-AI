from Board import Board
from Random import Random
from Minimax import Minimax
from MCTS import Mcts
from Neural import Nueral

import copy
import csv

class Master:
    red = Random()
    game_board = Board()

    def __init__(self, type=0, max=-1, c=-1, iterations=1000):
        if type == 0:
            self.blue = Mcts(True, c, iterations)
        elif type == 1:
            self.blue = Minimax(True, max)
        else:
            self.blue = Nueral()
        
    def turn(self, player):
        valid = False
        while valid == False:
            g_board = copy.deepcopy(self.game_board)
            answer = player.generate_answer(g_board)
            if (self.game_board.is_valid_move(answer[0], answer[1]) == True):
                valid = True
        return answer

    def run(self, filename):
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

        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([win])