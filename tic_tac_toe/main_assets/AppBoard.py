import tkinter as tk
from tic_tac_toe.main_assets.Board import Board

class AppBoard:
    """
    Class that represents the Tkinter UI board of the game. 

    Attributes:
    - game_board (Board): The game board.
    - move (tuple): The move that the player wants to make.
    - state (int): The state of the game. 0 = not playing, 1 = playing.
    - red (bool): The color of the player.
    - move_done (bool): If the move has been done or not.
    - canvas_board (Canvas): The canvas of the board.
    - rect_1 (Rectangle): The rectangle of the first cell.
    - rect_2 (Rectangle): The rectangle of the second cell.
    - rect_3 (Rectangle): The rectangle of the third cell.
    - rect_4 (Rectangle): The rectangle of the fourth cell.
    - rect_5 (Rectangle): The rectangle of the fifth cell.
    - rect_6 (Rectangle): The rectangle of the sixth cell.
    - rect_7 (Rectangle): The rectangle of the seventh cell.
    - rect_8 (Rectangle): The rectangle of the eighth cell.
    - rect_9 (Rectangle): The rectangle of the ninth cell.
    - cross_list (list): The list of crosses.
    - circle_list (list): The list of circles.
    - line_list (list): The list of lines.
    - cross_1_1 (Line): The first line as part of the cross in the first cell.
    - cross_1_2 (Line): The second line as part of the cross in the first cell.
    - cross_2_1 (Line): The first line as part of the cross in the second cell.
    - cross_2_2 (Line): The second line as part of the cross in the second cell.
    - cross_3_1 (Line): The first line as part of the cross in the third cell.
    - cross_3_2 (Line): The second line as part of the cross in the third cell.
    - cross_4_1 (Line): The first line as part of the cross in the fourth cell.
    - cross_4_2 (Line): The second line as part of the cross in the fourth cell.
    - cross_5_1 (Line): The first line as part of the cross in the fifth cell.
    - cross_5_2 (Line): The second line as part of the cross in the fifth cell.
    - cross_6_1 (Line): The first line as part of the cross in the sixth cell.
    - cross_6_2 (Line): The second line as part of the cross in the sixth cell.
    - cross_7_1 (Line): The first line as part of the cross in the seventh cell.
    - cross_7_2 (Line): The second line as part of the cross in the seventh cell.
    - cross_8_1 (Line): The first line as part of the cross in the eighth cell.
    - cross_8_2 (Line): The second line as part of the cross in the eighth cell.
    - cross_9_1 (Line): The first line as part of the cross in the ninth cell.
    - cross_9_2 (Line): The second line as part of the cross in the ninth cell.
    - circle_1 (Oval): The circle in the first cell.
    - circle_2 (Oval): The circle in the second cell.
    - circle_3 (Oval): The circle in the third cell.
    - circle_4 (Oval): The circle in the fourth cell.
    - circle_5 (Oval): The circle in the fifth cell.
    - circle_6 (Oval): The circle in the sixth cell.
    - circle_7 (Oval): The circle in the seventh cell.
    - circle_8 (Oval): The circle in the eighth cell.
    - circle_9 (Oval): The circle in the ninth cell.
    - line_1 (Line): The line in the first row.
    - line_2 (Line): The line in the second row.
    - line_3 (Line): The line in the third row.
    - line_4 (Line): The line in the first column.
    - line_5 (Line): The line in the second column.
    - line_6 (Line): The line in the third column.
    - line_7 (Line): The line in the first diagonal.
    - line_8 (Line): The line in the second diagonal.

    Methods:
    - hide_all: Hides all the crosses, circles and lines.
    - flip_board: Flips the board.
    - cross_line: Draws a line.
    - pressed_1: Event handler for the first cell.
    - pressed_2: Event handler for the second cell.
    - pressed_3: Event handler for the third cell.
    - pressed_4: Event handler for the fourth cell.
    - pressed_5: Event handler for the fifth cell.
    - pressed_6: Event handler for the sixth cell.
    - pressed_7: Event handler for the seventh cell.
    - pressed_8: Event handler for the eighth cell.
    - pressed_9: Event handler for the ninth cell.
    - create_line: Draws a line.
    - draw_board: Draws the board.
    """
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
        """
        Hides all the crosses, circles and lines. 

        Args:
        None

        Returns:
        None
        
        """
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
        """
        Turn a specified cell in the Tkinter UI game board into a circle or cross. 

        Args:
        - coord (tuple): The coordinates of the cell.
        - red (bool): The color of the player.

        Returns:
        None
        """
        if red:
            self.canvas_board.itemconfig(self.circle_list[coord[0]][coord[1]], state="normal")
        else:
            self.canvas_board.itemconfig(self.cross_list[coord[0]][2 * coord[1]], state="normal")
            self.canvas_board.itemconfig(self.cross_list[coord[0]][2 * coord[1] + 1], state="normal")
    
    def cross_line(self, num):
        """
        Draws a line in the Tkinter UI game board.

        Args:
        num (int): The number of the line.

        Returns:
        None
        
        """
        self.canvas_board.itemconfig(self.line_list[num], state="normal")

    def pressed_1(self, event):
        """
        Event handler for the first cell. 

        Args:
        event: The event.

        Returns:
        None
        """
        if self.state == 1 and self.game_board.is_valid_move(0,0):
            self.move = (0,0)
            self.flip_board((0,0), self.red)
            self.move_done = True
    
    def pressed_2(self, event):
        """
        Event handler for the second cell.
        
        Args:
        event: The event.
        
        Returns:
        None
        """
        if self.state == 1 and self.game_board.is_valid_move(1,0):
            self.move = (0,1)
            self.flip_board((0,1), self.red)
            self.move_done = True
    
    def pressed_3(self, event):
        """
        Event handler for the third cell.
        
        Args:
        event: The event.
        
        Returns:
        None
        
        """
        if self.state == 1 and self.game_board.is_valid_move(2,0):
            self.move = (0,2)
            self.flip_board((0,2), self.red)
            self.move_done = True
    
    def pressed_4(self, event):
        """
        Event handler for the fourth cell.
        
        Args:
        event: The event.
        
        Returns:
        None
        """
        if self.state == 1 and self.game_board.is_valid_move(0,1):
            self.move = (1,0)
            self.flip_board((1,0), self.red)
            self.move_done = True
    
    def pressed_5(self, event):
        """
        Event handler for the fifth cell.
        
        Args:
        event: The event.
        
        Returns:
        None
        """
        if self.state == 1 and self.game_board.is_valid_move(1,1):
            self.move = (1,1)
            self.flip_board((1,1), self.red)
            self.move_done = True
    
    def pressed_6(self, event):
        """
        Event handler for the sixth cell.
        
        Args:
        event: The event.
        
        Returns:
        None
        """
        if self.state == 1 and self.game_board.is_valid_move(2,1):
            self.move = (1,2)
            self.flip_board((1,2), self.red)
            self.move_done = True

    def pressed_7(self, event):
        """
        Event handler for the seventh cell.
        
        Args:
        event: The event.
        
        Returns:
        None
        """
        if self.state == 1 and self.game_board.is_valid_move(0,2):
            self.move = (2,0)
            self.flip_board((2,0), self.red)
            self.move_done = True
    
    def pressed_8(self, event):
        """
        Event handler for the eighth cell.
        
        Args:
        event: The event.
        
        Returns:
        None
        """
        if self.state == 1 and self.game_board.is_valid_move(1,2):
            self.move = (2,1)
            self.flip_board((2,1), self.red)
            self.move_done = True
    
    def pressed_9(self, event):
        """
        Event handler for the ninth cell.
        
        Args:
        event: The event.
        
        Returns:
        None
        """
        if self.state == 1 and self.game_board.is_valid_move(2,2):
            self.move = (2,2)
            self.flip_board((2,2), self.red)
            self.move_done = True
    
    def create_line(self, num):
        """
        Draws a line in the Tkinter UI game board.
        
        Args:
        num (int): The number of the line.
        
        Returns:
        None
        """
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
        """
        Draws the board in the Tkinter UI game board from a provided 2D board list representing 
        game board from a Board object.
        
        Args:
        board_list (list): The 2D board list.
        
        Returns:
        None
        """
        for y in range(0, 3):
            for x in range(0, 3):
                if board_list[y][x] == 1:
                    self.canvas_board.itemconfig(self.circle_list[y][x], state="normal")
                if board_list[y][x] == 2:
                    self.canvas_board.itemconfig(self.cross_list[y][2 * x], state="normal")
                    self.canvas_board.itemconfig(self.cross_list[y][2 * x + 1], state="normal")
