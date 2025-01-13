import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe")

root.geometry("600x600")

canvas_board = tk.Canvas(root, width=300, height=300)
canvas_board.pack()
canvas_board.create_rectangle(0, 0, 100, 100, fill="black")
canvas_board.create_rectangle(100, 0, 200, 100, fill="white")
canvas_board.create_rectangle(200, 0, 300, 100, fill="black")

canvas_board.create_rectangle(100, 100, 200, 200, fill="black")
canvas_board.create_rectangle(100, 200, 200, 300, fill="white")

canvas_board.create_rectangle(200, 100, 300, 200, fill="white")
canvas_board.create_rectangle(200, 200, 300, 300, fill="black")

canvas_board.create_rectangle(0, 100, 100, 200, fill="white")
canvas_board.create_rectangle(0, 200, 100, 300, fill="black")

# Crosses

# First Row
cross_1_1 = canvas_board.create_line(20, 20, 80, 80, fill="white", width=7, state="hidden")
cross_1_2 = canvas_board.create_line(20, 80, 80, 20, fill="white", width=7, state="hidden")

cross_2_1 = canvas_board.create_line(120, 20, 180, 80, fill="black", width=7, state="hidden")
cross_2_2 = canvas_board.create_line(120, 80, 180, 20, fill="black", width=7, state="hidden")

cross_3_1 = canvas_board.create_line(220, 20, 280, 80, fill="white", width=7, state="hidden")
cross_3_2 = canvas_board.create_line(220, 80, 280, 20, fill="white", width=7, state="hidden")

# Second Row
cross_4_1 = canvas_board.create_line(20, 120, 80, 180, fill="black", width=7, state="hidden")
cross_4_2 = canvas_board.create_line(20, 180, 80, 120, fill="black", width=7, state="hidden")

cross_5_1 = canvas_board.create_line(120, 120, 180, 180, fill="white", width=7, state="hidden")
cross_5_2 = canvas_board.create_line(120, 180, 180, 120, fill="white", width=7, state="hidden")

cross_6_1 = canvas_board.create_line(220, 120, 280, 180, fill="black", width=7, state="hidden")
cross_6_2 = canvas_board.create_line(220, 180, 280, 120, fill="black", width=7, state="hidden")

# Third Row
cross_7_1 = canvas_board.create_line(20, 220, 80, 280, fill="white", width=7, state="hidden")
cross_7_2 = canvas_board.create_line(20, 280, 80, 220, fill="white", width=7, state="hidden")

cross_8_1 = canvas_board.create_line(120, 220, 180, 280, fill="black", width=7, state="hidden")
cross_8_2 = canvas_board.create_line(120, 280, 180, 220, fill="black", width=7, state="hidden")

cross_9_1 = canvas_board.create_line(220, 220, 280, 280, fill="white", width=7, state="hidden")
cross_9_2 = canvas_board.create_line(220, 280, 280, 220, fill="white", width=7, state="hidden")

# Circles

# First Row
circle_1 = canvas_board.create_oval(20, 20, 80, 80, outline="white", width=7, fill="", state="hidden")
circle_2 = canvas_board.create_oval(120, 20, 180, 80, outline="black", width=7, fill="", state="hidden")
circle_3 = canvas_board.create_oval(220, 20, 280, 80, outline="white", width=7, fill="", state="hidden")

# Second Row
circle_4 = canvas_board.create_oval(20, 120, 80, 180, outline="black", width=7, fill="", state="hidden")
circle_5 = canvas_board.create_oval(120, 120, 180, 180, outline="white", width=7, fill="", state="hidden")
circle_6 = canvas_board.create_oval(220, 120, 280, 180, outline="black", width=7, fill="", state="hidden")

# Third Row
circle_7 = canvas_board.create_oval(20, 220, 80, 280, outline="white", width=7, fill="", state="hidden")
circle_8 = canvas_board.create_oval(120, 220, 180, 280, outline="black", width=7, fill="", state="hidden")
circle_9 = canvas_board.create_oval(220, 220, 280, 280, outline="white", width=7, fill="", state="hidden")

# Lines

# Row
line_1 = canvas_board.create_line(50, 20, 50, 280, fill="red", width=7, state="hidden")
line_2 = canvas_board.create_line(150, 20, 150, 280, fill="red", width=7, state="hidden")
line_3 = canvas_board.create_line(250, 20, 250, 280, fill="red", width=7, state="hidden")

# Column
line_4 = canvas_board.create_line(20, 50, 280, 50, fill="red", width=7, state="hidden")
line_5 = canvas_board.create_line(20, 150, 280, 150, fill="red", width=7, state="hidden")
line_6 = canvas_board.create_line(20, 250, 280, 250, fill="red", width=7, state="hidden")

# Diagonal
line_7 = canvas_board.create_line(20, 20, 280, 280, fill="red", width=7, state="hidden")
line_8 = canvas_board.create_line(20, 280, 280, 20, fill="red", width=7, state="hidden")

root.mainloop()