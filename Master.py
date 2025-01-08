from Board import Board
from Random import Random

red = Random()
blue = Random()
game_board = Board()
win = 0

def turn(player):
    valid = False
    while valid == False:
        answer = player.generate_answer()
        if (game_board.is_valid_move(answer[0], answer[1]) == True):
            valid = True
    return answer
        

while win == 0:
    red_answer = turn(red)
    game_board.flip(True, red_answer[0], red_answer[1])
    game_board.print_board()
    win = game_board.check_board()

    if (win != 0):
        break

    blue_answer = turn(blue)
    game_board.flip(False, blue_answer[0], blue_answer[1])
    game_board.print_board()
    win = game_board.check_board()

print(win)

        