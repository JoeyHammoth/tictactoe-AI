import tkinter as tk
from Board import Board

class AppBoard:
    def __init__(self, root):
        self.game_board = Board()
        self.move = (-1, -1)
        self.state = 1 # 0 = not playing, 1 = playing
        self.red = True
        self.move_done = False

        self.canvas_board = tk.Canvas(root, width=300, height=300)

        self.rect_1 = self.canvas_board.create_rectangle(0, 0, 100, 100, fill="black")
        self.rect_2 = self.canvas_board.create_rectangle(100, 0, 200, 100, fill="white")
        self.rect_3 = self.canvas_board.create_rectangle(200, 0, 300, 100, fill="black")

        self.rect_4 = self.canvas_board.create_rectangle(0, 100, 100, 200, fill="white")
        self.rect_5 = self.canvas_board.create_rectangle(100, 100, 200, 200, fill="black")
        self.rect_6 = self.canvas_board.create_rectangle(200, 100, 300, 200, fill="white")

        self.rect_7 = self.canvas_board.create_rectangle(0, 200, 100, 300, fill="black")
        self.rect_8 = self.canvas_board.create_rectangle(100, 200, 200, 300, fill="white")
        self.rect_9 = self.canvas_board.create_rectangle(200, 200, 300, 300, fill="black")

        self.canvas_board.tag_bind(self.rect_1, "<Button-1>", self.pressed_1)
        self.canvas_board.tag_bind(self.rect_2, "<Button-1>", self.pressed_2)
        self.canvas_board.tag_bind(self.rect_3, "<Button-1>", self.pressed_3)
        self.canvas_board.tag_bind(self.rect_4, "<Button-1>", self.pressed_4)
        self.canvas_board.tag_bind(self.rect_5, "<Button-1>", self.pressed_5)
        self.canvas_board.tag_bind(self.rect_6, "<Button-1>", self.pressed_6)
        self.canvas_board.tag_bind(self.rect_7, "<Button-1>", self.pressed_7)
        self.canvas_board.tag_bind(self.rect_8, "<Button-1>", self.pressed_8)
        self.canvas_board.tag_bind(self.rect_9, "<Button-1>", self.pressed_9)

        self.cross_list = [[],[],[]]
        self.circle_list = [[],[],[]]
        self.line_list = []

        # Crosses

        # First Row
        self.cross_1_1 = self.canvas_board.create_line(20, 20, 80, 80, fill="white", width=7, state="hidden")
        self.cross_list[0].append(self.cross_1_1)
        self.cross_1_2 = self.canvas_board.create_line(20, 80, 80, 20, fill="white", width=7, state="hidden")
        self.cross_list[0].append(self.cross_1_2)

        self.cross_2_1 = self.canvas_board.create_line(120, 20, 180, 80, fill="black", width=7, state="hidden")
        self.cross_list[0].append(self.cross_2_1)
        self.cross_2_2 = self.canvas_board.create_line(120, 80, 180, 20, fill="black", width=7, state="hidden")
        self.cross_list[0].append(self.cross_2_2)

        self.cross_3_1 = self.canvas_board.create_line(220, 20, 280, 80, fill="white", width=7, state="hidden")
        self.cross_list[0].append(self.cross_3_1)
        self.cross_3_2 = self.canvas_board.create_line(220, 80, 280, 20, fill="white", width=7, state="hidden")
        self.cross_list[0].append(self.cross_3_2)

        # Second Row
        self.cross_4_1 = self.canvas_board.create_line(20, 120, 80, 180, fill="black", width=7, state="hidden")
        self.cross_list[1].append(self.cross_4_1)
        self.cross_4_2 = self.canvas_board.create_line(20, 180, 80, 120, fill="black", width=7, state="hidden")
        self.cross_list[1].append(self.cross_4_2)

        self.cross_5_1 = self.canvas_board.create_line(120, 120, 180, 180, fill="white", width=7, state="hidden")
        self.cross_list[1].append(self.cross_5_1)
        self.cross_5_2 = self.canvas_board.create_line(120, 180, 180, 120, fill="white", width=7, state="hidden")
        self.cross_list[1].append(self.cross_5_2)

        self.cross_6_1 = self.canvas_board.create_line(220, 120, 280, 180, fill="black", width=7, state="hidden")
        self.cross_list[1].append(self.cross_6_1)
        self.cross_6_2 = self.canvas_board.create_line(220, 180, 280, 120, fill="black", width=7, state="hidden")
        self.cross_list[1].append(self.cross_6_2)

        # Third Row
        self.cross_7_1 = self.canvas_board.create_line(20, 220, 80, 280, fill="white", width=7, state="hidden")
        self.cross_list[2].append(self.cross_7_1)
        self.cross_7_2 = self.canvas_board.create_line(20, 280, 80, 220, fill="white", width=7, state="hidden")
        self.cross_list[2].append(self.cross_7_2)

        self.cross_8_1 = self.canvas_board.create_line(120, 220, 180, 280, fill="black", width=7, state="hidden")
        self.cross_list[2].append(self.cross_8_1)
        self.cross_8_2 = self.canvas_board.create_line(120, 280, 180, 220, fill="black", width=7, state="hidden")
        self.cross_list[2].append(self.cross_8_2)

        self.cross_9_1 = self.canvas_board.create_line(220, 220, 280, 280, fill="white", width=7, state="hidden")
        self.cross_list[2].append(self.cross_9_1)
        self.cross_9_2 = self.canvas_board.create_line(220, 280, 280, 220, fill="white", width=7, state="hidden")
        self.cross_list[2].append(self.cross_9_2)

        # Circles

        # First Row
        self.circle_1 = self.canvas_board.create_oval(20, 20, 80, 80, outline="white", width=7, fill="", state="hidden")
        self.circle_list[0].append(self.circle_1)
        self.circle_2 = self.canvas_board.create_oval(120, 20, 180, 80, outline="black", width=7, fill="", state="hidden")
        self.circle_list[0].append(self.circle_2)
        self.circle_3 = self.canvas_board.create_oval(220, 20, 280, 80, outline="white", width=7, fill="", state="hidden")
        self.circle_list[0].append(self.circle_3)

        # Second Row
        self.circle_4 = self.canvas_board.create_oval(20, 120, 80, 180, outline="black", width=7, fill="", state="hidden")
        self.circle_list[1].append(self.circle_4)
        self.circle_5 = self.canvas_board.create_oval(120, 120, 180, 180, outline="white", width=7, fill="", state="hidden")
        self.circle_list[1].append(self.circle_5)
        self.circle_6 = self.canvas_board.create_oval(220, 120, 280, 180, outline="black", width=7, fill="", state="hidden")
        self.circle_list[1].append(self.circle_6)

        # Third Row
        self.circle_7 = self.canvas_board.create_oval(20, 220, 80, 280, outline="white", width=7, fill="", state="hidden")
        self.circle_list[2].append(self.circle_7)
        self.circle_8 = self.canvas_board.create_oval(120, 220, 180, 280, outline="black", width=7, fill="", state="hidden")
        self.circle_list[2].append(self.circle_8)
        self.circle_9 = self.canvas_board.create_oval(220, 220, 280, 280, outline="white", width=7, fill="", state="hidden")
        self.circle_list[2].append(self.circle_9)

        # Lines

        # Row
        self.line_1 = self.canvas_board.create_line(50, 20, 50, 280, fill="red", width=7, state="hidden")
        self.line_list.append(self.line_1)
        self.line_2 = self.canvas_board.create_line(150, 20, 150, 280, fill="red", width=7, state="hidden")
        self.line_list.append(self.line_2)
        self.line_3 = self.canvas_board.create_line(250, 20, 250, 280, fill="red", width=7, state="hidden")
        self.line_list.append(self.line_3)

        # Column
        self.line_4 = self.canvas_board.create_line(20, 50, 280, 50, fill="red", width=7, state="hidden")
        self.line_list.append(self.line_4)
        self.line_5 = self.canvas_board.create_line(20, 150, 280, 150, fill="red", width=7, state="hidden")
        self.line_list.append(self.line_5)
        self.line_6 = self.canvas_board.create_line(20, 250, 280, 250, fill="red", width=7, state="hidden")
        self.line_list.append(self.line_6)

        # Diagonal
        self.line_7 = self.canvas_board.create_line(20, 20, 280, 280, fill="red", width=7, state="hidden")
        self.line_list.append(self.line_7)
        self.line_8 = self.canvas_board.create_line(20, 280, 280, 20, fill="red", width=7, state="hidden")
        self.line_list.append(self.line_8)
    
    def hide_all(self):
        # Crosses and Cricles
        for y in range(0,3):
            for x in range(0,3):
                 self.canvas_board.itemconfig(self.circle_list[y][x], state="hidden")
        
        for y in range(0,3):
            for x in range(0,6):
                 self.canvas_board.itemconfig(self.cross_list[y][x], state="hidden")
        
        # Lines
        for l in self.line_list:
            self.canvas_board.itemconfig(l, state="hidden")
        
    
    def flip_board(self, coord, red):
        if red:
            self.canvas_board.itemconfig(self.circle_list[coord[0]][coord[1]], state="normal")
        else:
            self.canvas_board.itemconfig(self.cross_list[coord[0]][2 * coord[1]], state="normal")
            self.canvas_board.itemconfig(self.cross_list[coord[0]][2 * coord[1] + 1], state="normal")
    
    def cross_line(self, num):
        self.canvas_board.itemconfig(self.line_list[num], state="normal")

    def pressed_1(self, event):
        if self.state == 1 and self.game_board.is_valid_move(0,0):
            self.move = (0,0)
            self.flip_board((0,0), self.red)
            self.move_done = True
    
    def pressed_2(self, event):
        if self.state == 1 and self.game_board.is_valid_move(1,0):
            self.move = (0,1)
            self.flip_board((0,1), self.red)
            self.move_done = True
    
    def pressed_3(self, event):
        if self.state == 1 and self.game_board.is_valid_move(2,0):
            self.move = (0,2)
            self.flip_board((0,2), self.red)
            self.move_done = True
    
    def pressed_4(self, event):
        if self.state == 1 and self.game_board.is_valid_move(0,1):
            self.move = (1,0)
            self.flip_board((1,0), self.red)
            self.move_done = True
    
    def pressed_5(self, event):
        if self.state == 1 and self.game_board.is_valid_move(1,1):
            self.move = (1,1)
            self.flip_board((1,1), self.red)
            self.move_done = True
    
    def pressed_6(self, event):
        if self.state == 1 and self.game_board.is_valid_move(2,1):
            self.move = (1,2)
            self.flip_board((1,2), self.red)
            self.move_done = True

    def pressed_7(self, event):
        if self.state == 1 and self.game_board.is_valid_move(0,2):
            self.move = (2,0)
            self.flip_board((2,0), self.red)
            self.move_done = True
    
    def pressed_8(self, event):
        if self.state == 1 and self.game_board.is_valid_move(1,2):
            self.move = (2,1)
            self.flip_board((2,1), self.red)
            self.move_done = True
    
    def pressed_9(self, event):
        if self.state == 1 and self.game_board.is_valid_move(2,2):
            self.move = (2,2)
            self.flip_board((2,2), self.red)
            self.move_done = True
    
    def create_line(self, num):
        match num:
            case 0:
                self.canvas_board.itemconfig(self.line_list[3], state="normal")
            case 1:
                self.canvas_board.itemconfig(self.line_list[4], state="normal")
            case 2:
                self.canvas_board.itemconfig(self.line_list[5], state="normal")
            case 3:
                self.canvas_board.itemconfig(self.line_list[0], state="normal")
            case 4:
                self.canvas_board.itemconfig(self.line_list[1], state="normal")
            case 5:
                self.canvas_board.itemconfig(self.line_list[2], state="normal")
            case 6:
                self.canvas_board.itemconfig(self.line_list[6], state="normal")
            case 7:
                self.canvas_board.itemconfig(self.line_list[7], state="normal")

    def draw_board(self, board_list):
        for y in range(0, 3):
            for x in range(0, 3):
                if board_list[y][x] == 1:
                    self.canvas_board.itemconfig(self.circle_list[y][x], state="normal")
                if board_list[y][x] == 2:
                    self.canvas_board.itemconfig(self.cross_list[y][2 * x], state="normal")
                    self.canvas_board.itemconfig(self.cross_list[y][2 * x + 1], state="normal")
