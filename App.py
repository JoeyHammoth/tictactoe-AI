import threading
import tkinter as tk
from tkinter import *
from AppBoard import AppBoard
from Master import Master

def run_game(master, app):
    while master.game_board.check_board() == 0:
        with master.condition:
            app.state = 1
            # While loop can stop everything else
            app.move_done = False
            while app.move_done == True:
                pass
            master.human_move = app.move
            master.condition.notify()
            app.state = 0
            master.condition.wait()
            app.flip_board(master.opp_move, False)

root = tk.Tk()
root.title("Tic-Tac-Toe")

root.geometry("600x600")

master = Master(type=3)
appBoard = AppBoard(root)
button_clear = Button(root, text="Kill", width=25, command=appBoard.hide_all)
button_clear.pack()

# Create threads for the method and the script
method_thread = threading.Thread(target=master.run)
script_thread = threading.Thread(target=run_game, args=(master, appBoard,))

# Start the threads
method_thread.start()
script_thread.start()

# Wait for both threads to finish
method_thread.join()
script_thread.join()

root.mainloop()