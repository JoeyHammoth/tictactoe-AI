from Board import Board
from Random import Random
from Minimax import Minimax
from MCTS import Mcts
from Neural import Nueral

import copy
import csv
import threading

class Master:
    #red = Random()
    blue = Random()
    game_board = Board()

    def __init__(self, type=0, max=-1, c=-1, iterations=1000):
        if type == 0:
            self.blue = Mcts(True, c, iterations)
        elif type == 1:
            self.blue = Minimax(True, max)
        elif type == 2:
            self.blue = Nueral()
        else:
            self.human_move = (-1,-1)
            self.condition = threading.Condition()
            self.opp_move = (-1,-1)
        
        self.type = type
        
    def turn(self, player):
        valid = False
        while valid == False:
            g_board = copy.deepcopy(self.game_board)
            answer = player.generate_answer(g_board)
            if (self.game_board.is_valid_move(answer[0], answer[1]) == True):
                valid = True
        return answer

    def run(self, filename=0):
        win = 0 
        self.game_board.clear()
        count = 0
        with self.condition:
            while win == 0:
                if self.type == 3:
                    print("yes")
                    if count > 0:
                        self.condition.wait()
                    self.game_board.flip(True, self.human_move[1], self.human_move[0])
                    self.game_board.print_board()
                    win = self.game_board.check_board()
                else:
                    red_answer = self.turn(self.red)
                    self.game_board.flip(True, red_answer[0], red_answer[1])
                    self.game_board.print_board()
                    win = self.game_board.check_board()

                if (win != 0):
                    break

                blue_answer = self.turn(self.blue)
                if self.type == 3:
                    result = (blue_answer[1], blue_answer[0])
                    self.opp_move = result
                    self.condition.notify()

                self.game_board.flip(False, blue_answer[0], blue_answer[1])
                self.game_board.print_board()
                win = self.game_board.check_board()
                count += 1

        if self.type == 3:
            with self.condition:
                self.condition.notify()

        if filename != 0:
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([win])