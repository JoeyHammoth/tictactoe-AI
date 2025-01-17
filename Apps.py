import threading
import tkinter as tk
import webbrowser

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
sim_status = False
sim_first_ai_att = []
sim_second_ai_att = []
is_updating = False

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
    if not sim_status:
        # Stop the current game (threads)
        stop_event.set()
        root.after(100, lambda: start_game(master, appBoard))

# TODO: Fix bug where alg switch does not work with toggling player order
def toggle_player_order():
    global player_first, master
    if player_first: # if player is first, new order is second
        player_first = False
        #master = Master(type=3, ai_player=True)
        master.switch_order_human(False)
    else:
        player_first = True
        #master = Master(type=3, ai_player=False)
        master.switch_order_human(True)
    # TKinter labels don't automatically reflect changes in external variables—they 
    # need to be explicitly updated
    order_label.config(text=f"Player is first: {player_first}") 

def switch_alg(type, isOpp=False):
    global master, player_first, sim_status
    try:
        if not sim_status:
            if type == 0:
                master = Master(type=3, ai_player=not player_first)
                ai_type_label.config(text="AI Algorithm Used: Random")
            elif type == 1:
                c = int(c_entry.get())
                iter= int(iter_entry.get())
            
                master = Master(type=3, ai_player=not player_first, opp_type=1, opp_c=c, opp_iterations=iter)
                ai_type_label.config(text="AI Algorithm Used: MCTS")
            elif type == 2:
                max_d = int(max_depth_entry.get())

                master = Master(type=3, ai_player=not player_first, opp_type=2, opp_max=max_d)
                ai_type_label.config(text="AI Algorithm Used: Minimax")
            elif type == 3:
                games = int(mlp_games_entry.get())

                master = Master(type=3, ai_player=not player_first, opp_type=3, opp_games=games)
                ai_type_label.config(text="AI Algorithm Used: Neural Network")
        else: # Sim att list format = [type, c, iter, maxd, games]
            if not isOpp:
                sim_first_ai_att.clear()
                if type == 0:
                    sim_first_ai_att.append(-1)
                    sim_first_ai_att.append(0)
                    sim_first_ai_att.append(0)
                    sim_first_ai_att.append(0)
                    sim_first_ai_att.append(0)
                    ai_type_label.config(text="AI Algorithm Used: Random")
                elif type == 1:
                    c = int(c_entry.get())
                    iter= int(iter_entry.get())
                    sim_first_ai_att.append(0)
                    sim_first_ai_att.append(c)
                    sim_first_ai_att.append(iter)
                    sim_first_ai_att.append(0)
                    sim_first_ai_att.append(0)
                    ai_type_label.config(text="AI Algorithm Used: MCTS")
                elif type == 2:
                    max_d = int(max_depth_entry.get())
                    sim_first_ai_att.append(1)
                    sim_first_ai_att.append(0)
                    sim_first_ai_att.append(0)
                    sim_first_ai_att.append(max_d)
                    sim_first_ai_att.append(0)
                    ai_type_label.config(text="AI Algorithm Used: Minimax")
                elif type == 3:
                    games = int(mlp_games_entry.get())
                    sim_first_ai_att.append(2)
                    sim_first_ai_att.append(0)
                    sim_first_ai_att.append(0)
                    sim_first_ai_att.append(0)
                    sim_first_ai_att.append(games)
                    ai_type_label.config(text="AI Algorithm Used: Neural Network")
            else:
                sim_second_ai_att.clear()
                if type == 0:
                    sim_second_ai_att.append(0)
                    sim_second_ai_att.append(0)
                    sim_second_ai_att.append(0)
                    sim_second_ai_att.append(0)
                    sim_second_ai_att.append(0)
                    opp_ai_type_label.config(text="Opponent AI Algorithm Used: Random")
                elif type == 1:
                    c = int(opp_c_entry.get())
                    iter= int(opp_iter_entry.get())
                    sim_second_ai_att.append(1)
                    sim_second_ai_att.append(c)
                    sim_second_ai_att.append(iter)
                    sim_second_ai_att.append(0)
                    sim_second_ai_att.append(0)
                    opp_ai_type_label.config(text="Opponent AI Algorithm Used: MCTS")
                elif type == 2:
                    max_d = int(opp_max_depth_entry.get())
                    sim_second_ai_att.append(2)
                    sim_second_ai_att.append(0)
                    sim_second_ai_att.append(0)
                    sim_second_ai_att.append(max_d)
                    sim_second_ai_att.append(0)
                    opp_ai_type_label.config(text="Opponent AI Algorithm Used: Minimax")
                elif type == 3:
                    games = int(opp_mlp_games_entry.get())
                    sim_second_ai_att.append(3)
                    sim_second_ai_att.append(0)
                    sim_second_ai_att.append(0)
                    sim_second_ai_att.append(0)
                    sim_second_ai_att.append(games)
                    opp_ai_type_label.config(text="Opponent AI Algorithm Used: Neural Network") 
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer!")

def clear_score():
    global human_score, ai_score, draw_score
    human_score = 0
    ai_score = 0
    draw_score = 0
    score_text.config(text=f"Wins: {human_score}     Losses: {ai_score}     Draws: {draw_score}")

def toggle_sim_status(app):
    global sim_status, human_score, ai_score, draw_score, master
    app.state = 0
    app.hide_all()
    master.game_board.clear()
    if sim_status:
        sim_status = False
        status_text.config(text="Player mode activated", fg='white') 
    else:
        sim_status = True
        status_text.config(text="Simulation mode activated", fg='white') 
    sim_label.config(text=f"AI simulation status: {sim_status}")
    clear_score()

def run_sim(app):
    # Sim att list format = [type, c, iter, maxd, games]
    global sim_status, sim_first_ai_att, sim_second_ai_att, human_score, ai_score, draw_score, player_first, is_updating
    if sim_status and not is_updating:
        print(sim_first_ai_att)
        print(sim_second_ai_att)
        new_master = Master(type=sim_first_ai_att[0], c=sim_first_ai_att[1], iterations=sim_first_ai_att[2], max=sim_first_ai_att[3],
                            games=sim_first_ai_att[4], opp_type=sim_second_ai_att[0], opp_c=sim_second_ai_att[1], opp_iterations=sim_second_ai_att[2],
                            opp_max=sim_second_ai_att[3], opp_games=sim_second_ai_att[4], ai_player=not player_first)
        app.state = 0
        app.hide_all()
        new_master.run()
        

        # TODO: Change this so that instead of trying to change it live using a while loop, have Master keep a list
        # of the game states, wait till the game is done and draw each game state with a pause in between.
        # while new_master.game_board.check_board() == 0:
        #     #app.hide_all()
        #     # app.game_board = new_master.game_board
        #     # app.draw_board()
        #     pass

        print(new_master.game_history)

        def update(index):
            global is_updating, human_score, ai_score, draw_score, player_first
            if index == 0:
                is_updating = True
            if index < len(new_master.game_history):
                print("ping")
                print(new_master.game_history[index])
                app.draw_board(new_master.game_history[index])  # Draw the current board
                root.after(100, update, index + 1)  # Schedule the next update after 2000 ms
            else:
                app.create_line(master.game_board.check_line()) 
                if player_first:
                    if new_master.game_board.check_board() == 1:
                        human_score += 1
                    elif new_master.game_board.check_board() == 2:
                        ai_score += 1
                    elif new_master.game_board.check_board() == 3:
                        draw_score +=1
                else:
                    if new_master.game_board.check_board() == 1:
                        ai_score += 1
                    elif new_master.game_board.check_board() == 2:
                        human_score += 1
                    elif new_master.game_board.check_board() == 3:
                        draw_score +=1
                score_text.config(text=f"Wins: {human_score}     Losses: {ai_score}     Draws: {draw_score}")
                is_updating = False
                
        update(0)

def open_webpage(type):
    match type:
        case 0:
            url = "https://github.com/JoeyHammoth/tictactoe-AI" 
        case 1:
            url = "https://github.com/JoeyHammoth/tictactoe-AI/wiki"
    webbrowser.open(url)

def exit():
    root.destroy()

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x900")

master = Master(type=3, ai_player=True)
appBoard = AppBoard(root)

status_text = Label(root)

button_replay =  Button(root, text="Replay", width=25, command=lambda: reset_game())

score_text = Label(root, text=f"Wins: {human_score}     Losses: {ai_score}     Draws: {draw_score}")

button_clear = Button(root, text="Clear Score", width=25, command=clear_score)

sim_label = Label(root, text=f"AI simulation status: {sim_status}")

button_toggle_sim = Button(root, text="Toggle Simulation", width=25, command=lambda: toggle_sim_status(appBoard))

button_run_sim = Button(root, text="Run Simulation", width=25, command=lambda: run_sim(appBoard))

button_repo = Button(root, text="Open Project Repo", width=25, command=lambda: open_webpage(0))

button_wiki = Button(root, text="Open Project Wiki", width=25, command=lambda: open_webpage(1))

button_exit = Button(root, text="Exit", width=25, command=exit)

icon = PhotoImage(file="icon.png")  

icon = icon.subsample(9, 9)

icon_label = Label(root, image=icon)

end_label = Label(root, text="JoeyHammoth 2025")

# Player

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

# Opponent

opp_ai_type_label = Label(root, text="Opponent AI Algorithm Used: Random")

opp_max_depth_label = Label(root, text="Opponent Max Depth")

opp_max_depth_entry = Entry(root)

opp_c_label = Label(root, text="Opponent Exploration Parameter")

opp_c_entry = Entry(root)

opp_iter_label = Label(root, text="Opponent MCTS Iterations")

opp_iter_entry = Entry(root)

opp_mlp_games_label = Label(root, text="Opponent NN No. of Games")

opp_mlp_games_entry = Entry(root)

opp_random_button = Button(root, text="Switch Opponent AI to Random", width=25, command=lambda: switch_alg(0, isOpp=True))

opp_mcts_button = Button(root, text="Switch Opponent AI to MCTS", width=25, command=lambda: switch_alg(1, isOpp=True))

opp_mm_button = Button(root, text="Switch Opponent AI to Minimax", width=25, command=lambda: switch_alg(2, isOpp=True))

opp_nn_button = Button(root, text="Switch Opponent AI to Neural Network", width=25, command=lambda: switch_alg(3, isOpp=True))

appBoard.canvas_board.grid(row=0, column=0, rowspan=10)
status_text.grid(row=11, column=0)
button_replay.grid(row=12, column=0)
score_text.grid(row=13, column=0)
button_clear.grid(row=14, column=0)
sim_label.grid(row=15, column=0, pady=(5,5))
button_toggle_sim.grid(row=16, column=0,pady=(5,5))
button_run_sim.grid(row=17, column=0,pady=(5,5))
button_repo.grid(row=18, column=0, pady=(5,5))
button_wiki.grid(row=19, column=0, pady=(5,5))
button_exit.grid(row=20, column=0, pady=(5,5))
icon_label.grid(row=21, column=0, rowspan=5, pady=(0,0))
end_label.grid(row=26, column=0, pady=(0,0))

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
opp_ai_type_label.grid(row=15, column=1, pady=(0,0))
opp_max_depth_label.grid(row=16, column=1, pady=(0,0))
opp_max_depth_entry.grid(row=17, column=1, pady=(0,0))
opp_c_label.grid(row=18, column=1, pady=(0,0))
opp_c_entry.grid(row=19, column=1, pady=(0,0))
opp_iter_label.grid(row=20, column=1, pady=(0,0))
opp_iter_entry.grid(row=21, column=1, pady=(0,0))
opp_mlp_games_label.grid(row=22, column=1, pady=(0,0))
opp_mlp_games_entry.grid(row=23, column=1, pady=(0,0))
opp_random_button.grid(row=24, column=1, pady=(5,5))
opp_mcts_button.grid(row=25, column=1, pady=(5,5))
opp_mm_button.grid(row=26, column=1, pady=(5,5))
opp_nn_button.grid(row=27, column=1, pady=(5,5))


# Initial game threads running
root.after(100, start_game, master, appBoard)

root.mainloop()