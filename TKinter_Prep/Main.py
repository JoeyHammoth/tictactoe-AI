import tkinter
from tkinter import *


# Create an event function to print something when a button is pressed
def on_button_pressed(event):
    print("The button has been pressed!")


# Tk to create the main window for application
# className is name of the window title
m = tkinter.Tk(className="Testing")

# Tkinter widgets to put into the app

# Label: display box to display text or images
Title = Label(m, text="Welcome to my application!")
# Title.pack()

Label_One = Label(m, text="Please press the button below")

# Button: A clickable button that can trigger an action
Press = Button(m, text="Press Me Hard!", width=25, command = Title.destroy)
# Press.pack()
# Button-1 refers to left mouse click
Press.bind("<Button-1>", on_button_pressed)

# Grid organizes the widgets in grid
Title.grid(row=0, column=0)
Label_One.grid(row=0, column=1)
Press.grid(row=1, column=0)

# Infinite loop to run the app when it's ready.
# Infinite loop to wait for events to occur. 
# Stops when window is closed. 
m.mainloop()