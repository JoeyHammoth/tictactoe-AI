import threading
import tkinter as tk
from tkinter import Button
from AppBoard import AppBoard
from Master import Master

def run_game(master, app):
    while master.game_board.check_board() == 0:
        with master.condition:
            app.state = 1
            app.move_done = False
            while app.move_done == False:
                pass
            master.human_move = app.move
            print(master.human_move)
            master.condition.notify()
            app.state = 0
            master.condition.wait()
            app.flip_board(master.opp_move, False)
    print("DONE!")

def start_game(master, app):
    app.hide_all()
    master.game_board.clear()
    threading.Thread(target=run_game, args=(master, app)).start()
    threading.Thread(target=master.run).start()

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x600")

master = Master(type=3)
appBoard = AppBoard(root)

button_replay =  Button(root, text="Replay", width=25, command=lambda: root.after(100, start_game, master, appBoard))
button_replay.pack()

button_clear = Button(root, text="Kill", width=25, command=appBoard.hide_all)
button_clear.pack()

# Start threads after tkinter is running
root.after(100, start_game, master, appBoard)

root.mainloop()
