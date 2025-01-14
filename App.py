import tkinter as tk
from AppBoard import AppBoard

root = tk.Tk()
root.title("Tic-Tac-Toe")

root.geometry("600x600")

appBoard = AppBoard(root)

appBoard.flip_board((0, 1), True)

root.mainloop()