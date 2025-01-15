import threading
import tkinter as tk
from tkinter import Button
from AppBoard import AppBoard
from Master import Master

# Global Stop Event 
stop_event = threading.Event()

def run_game(master, app):
    with master.condition:
        while not stop_event.is_set() and master.game_board.check_board() == 0:
            app.state = 1
            app.move_done = False
            while not stop_event.is_set() and app.move_done == False:
                stop_event.wait(0.1)
            if stop_event.is_set():
                print("it is")
                break
            master.human_move = app.move
            print(master.human_move)
            master.condition.notify()
            app.state = 0
            master.condition.wait()
            if stop_event.is_set():
                break
            app.flip_board(master.opp_move, False)

def start_game(master, app):
    app.hide_all()
    master.game_board.clear()
    stop_event.clear()
    threading.Thread(target=run_game, args=(master, app), daemon=True).start()
    threading.Thread(target=master.run, daemon=True).start()

def reset_game():
    stop_event.set()
    print("helps")
    root.after(100, lambda: start_game(master, appBoard))

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x600")

master = Master(type=3)
appBoard = AppBoard(root)

button_replay =  Button(root, text="Replay", width=25, command=lambda: reset_game())
button_replay.pack()

button_clear = Button(root, text="Kill", width=25, command=appBoard.hide_all)
button_clear.pack()

# Start threads after tkinter is running
root.after(100, start_game, master, appBoard)

root.mainloop()
