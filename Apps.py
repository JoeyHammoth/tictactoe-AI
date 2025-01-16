import threading
import tkinter as tk
from tkinter import *
from AppBoard import AppBoard
from Master import Master
from tkinter import messagebox

# Global Stop Event 
stop_event = threading.Event()
player_first = False
master = None
human_score = 0
ai_score = 0
draw_score = 0

def run_game(master, app):
    global human_score, ai_score, draw_score
    with master.condition:
        if player_first:
            app.red = True
            while not stop_event.is_set() and master.game_board.check_board() == 0:
                app.state = 1
                app.game_board = master.game_board
                status_text.config(text="Your turn", fg='white') 
                app.move_done = False
                while not stop_event.is_set() and app.move_done == False:
                    stop_event.wait(0.1)
                if stop_event.is_set():
                    break
                master.human_move = app.move
                master.condition.notify()
                app.state = 0
                status_text.config(text="AI's turn", fg='white') 
                master.condition.wait()
                if stop_event.is_set():
                    break
                app.flip_board(master.opp_move, False)
            if master.game_board.check_board() == 2:
                status_text.config(text="You Loose!", fg='red') 
                ai_score += 1
            elif master.game_board.check_board() == 1:
                status_text.config(text="You Win!", fg='green') 
                human_score += 1
            elif master.game_board.check_board() == 3:
                status_text.config(text="It's a Draw!", fg='#ADD8E6') 
                draw_score += 1
        else:
            app.red = False
            while not stop_event.is_set() and master.game_board.check_board() == 0:
                master.condition.notify()
                app.state = 0
                status_text.config(text="AI's turn", fg='white') 
                master.condition.wait()
                if stop_event.is_set():
                    break
                app.flip_board(master.opp_move, True)
                if master.game_board.check_board() != 0:
                    break
                app.state = 1
                app.game_board = master.game_board
                status_text.config(text="Your turn", fg='white') 
                app.move_done = False
                while not stop_event.is_set() and app.move_done == False:
                    stop_event.wait(0.1)
                if stop_event.is_set():
                    break
                master.human_move = app.move
            app.state = 0
            if master.game_board.check_board() == 1:
                status_text.config(text="You Loose!", fg='red') 
                ai_score += 1
            elif master.game_board.check_board() == 2:
                status_text.config(text="You Win!", fg='green') 
                human_score += 1
            elif master.game_board.check_board() == 3:
                status_text.config(text="It's a Draw!", fg='#ADD8E6') 
                draw_score += 1
        if master.game_board.check_board() != 0:
            app.create_line(master.game_board.check_line()) 
            score_text.config(text=f"Wins: {human_score}     Losses: {ai_score}     Draws: {draw_score}")

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

def switch_alg(type):
    global master
    try:
        if type == 0:
            master = Master(type=3, ai_player=True)
            ai_type_label.config(text="AI Algorithm Used: Random")
        elif type == 1:
            c = int(c_entry.get())
            iter= int(iter_entry.get())
        
            master = Master(type=3, ai_player=True, opp_type=1, opp_c=c, opp_iterations=iter)
            ai_type_label.config(text="AI Algorithm Used: MCTS")
        elif type == 2:
            max_d = int(max_depth_entry.get())

            master = Master(type=3, ai_player=True, opp_type=2, opp_max=max_d)
            ai_type_label.config(text="AI Algorithm Used: Minimax")
        elif type == 3:
            games = int(mlp_games_entry.get())

            master = Master(type=3, ai_player=True, opp_type=3, opp_games=games)
            ai_type_label.config(text="AI Algorithm Used: Neural Network")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer!")

def clear_score():
    global human_score, ai_score, draw_score
    human_score = 0
    ai_score = 0
    draw_score = 0
    score_text.config(text=f"Wins: {human_score}     Losses: {ai_score}     Draws: {draw_score}")

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x600")

master = Master(type=3, ai_player=True)
appBoard = AppBoard(root)

status_text = Label(root)

button_replay =  Button(root, text="Replay", width=25, command=lambda: reset_game())

score_text = Label(root, text=f"Wins: {human_score}     Losses: {ai_score}     Draws: {draw_score}")

button_clear = Button(root, text="Clear Score", width=25, command=clear_score)

order_label = Label(root, text=f"Player is first: {player_first}")

button_order = Button(root, text="Change Order", width=25, command=lambda: toggle_player_order())

ai_type_label = Label(root, text="AI Algorithm Used: Random")

max_depth_label = Label(root, text="Max Depth")

max_depth_entry = Entry(root)

c_label = Label(root, text="Exploration Parameter")

c_entry = Entry(root)

iter_label = Label(root, text="MCTS Iterations")

iter_entry = Entry(root)

mlp_games_label = Label(root, text="NN No. of Games")

mlp_games_entry = Entry(root)

random_button = Button(root, text="Switch AI to Random", width=25, command=lambda: switch_alg(0))

mcts_button = Button(root, text="Switch AI to MCTS", width=25, command=lambda: switch_alg(1))

mm_button = Button(root, text="Switch AI to Minimax", width=25, command=lambda: switch_alg(2))

nn_button = Button(root, text="Switch AI to Neural Network", width=25, command=lambda: switch_alg(3))

appBoard.canvas_board.grid(row=0, column=0, rowspan=10)
status_text.grid(row=11, column=0)
button_replay.grid(row=12, column=0)
score_text.grid(row=13, column=0)
button_clear.grid(row=14, column=0)

order_label.grid(row=0, column=1, pady=(0,0))
button_order.grid(row=1, column=1, pady=(0,0))
ai_type_label.grid(row=2, column=1, pady=(0,0))
max_depth_label.grid(row=3, column=1, pady=(0,0))
max_depth_entry.grid(row=4, column=1, pady=(0,0))
c_label.grid(row=5, column=1, pady=(0,0))
c_entry.grid(row=6, column=1, pady=(0,0))
iter_label.grid(row=7, column=1, pady=(0,0))
iter_entry.grid(row=8, column=1, pady=(0,0))
mlp_games_label.grid(row=9, column=1, pady=(0,0))
mlp_games_entry.grid(row=10, column=1, pady=(0,0))
random_button.grid(row=11, column=1, pady=(5,5))
mcts_button.grid(row=12, column=1, pady=(5,5))
mm_button.grid(row=13, column=1, pady=(5,5))
nn_button.grid(row=14, column=1, pady=(5,5))


# Initial game threads running
root.after(100, start_game, master, appBoard)

root.mainloop()
