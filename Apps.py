import threading
import tkinter as tk
from tkinter import *
from AppBoard import AppBoard
from Master import Master

# Global Stop Event 
stop_event = threading.Event()
player_first = False
master = None

def run_game(master, app):
    with master.condition:
        if player_first:
            app.red = True
            while not stop_event.is_set() and master.game_board.check_board() == 0:
                app.state = 1
                app.move_done = False
                while not stop_event.is_set() and app.move_done == False:
                    stop_event.wait(0.1)
                if stop_event.is_set():
                    break
                master.human_move = app.move
                master.condition.notify()
                app.state = 0
                master.condition.wait()
                if stop_event.is_set():
                    break
                app.flip_board(master.opp_move, False)
        else:
            app.red = False
            while not stop_event.is_set() and master.game_board.check_board() == 0:
                master.condition.notify()
                app.state = 0
                master.condition.wait()
                if stop_event.is_set():
                    break
                app.flip_board(master.opp_move, True)
                if master.game_board.check_board() != 0:
                    break
                app.state = 1
                app.move_done = False
                while not stop_event.is_set() and app.move_done == False:
                    stop_event.wait(0.1)
                if stop_event.is_set():
                    break
                master.human_move = app.move
            app.state = 0
        if master.game_board.check_board() != 0:
            app.create_line(master.game_board.check_line())

def start_game(master, app):
    # Reset all the boards and restart threads
    app.hide_all()
    master.game_board.clear()
    stop_event.clear()

    # daemon to keep track of threads
    threading.Thread(target=run_game, args=(master, app), daemon=True).start()
    threading.Thread(target=master.run_human, daemon=True).start()

def reset_game():
    # Stop the current game (threads)
    stop_event.set()
    root.after(100, lambda: start_game(master, appBoard))

def toggle_player_order():
    global player_first, master
    if player_first:
        player_first = False
        master = Master(type=3, ai_player=True)
    else:
        player_first = True
        master = Master(type=3, ai_player=False)
    # TKinter labels don't automatically reflect changes in external variables—they 
    # need to be explicitly updated
    order_label.config(text=f"Player is first: {player_first}") 

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x600")

master = Master(type=3, ai_player=True)
appBoard = AppBoard(root)

button_replay =  Button(root, text="Replay", width=25, command=lambda: reset_game())
button_replay.pack()

button_clear = Button(root, text="Kill", width=25, command=appBoard.hide_all)
button_clear.pack()

order_label = Label(root, text=f"Player is first: {player_first}")
order_label.pack()

button_order = Button(root, text="Change Order", width=25, command=lambda: toggle_player_order())
button_order.pack()

# Initial game threads running
root.after(100, start_game, master, appBoard)

root.mainloop()
