"""
A GUI creates an event driven environment.
The application window created listens for events e.g. a button press.
Declare the widgets (frames/labels/buttons etc.) that are needed
use a layout manager to add them to their parent element.
This is a functional solution not OOP

Dice GUI

declare a base window
declare a button with the text "Randomise"
declare a label with the text "Not yet randomised".
Add functionality to the button so it generates a random number between
1 and 6 inclusive when pressed.
When the button is clicked update the label with the value which is generated.

Extension - Change the label so that instead of using text to display
the number, it displays an image of a dice with the relevant number
"""
import tkinter as tk
import random as rd

root = tk.Tk()
root.title("Dice Game")

def roll():
	rollResult = rd.randint(1,6)
	lbl_result.config(text=str(rollResult))


lbl_result = tk.Label(root,
                      text="Not yet randomised")

btn_roll = tk.Button(root,
                     text="Randomise",
                     command=roll)

lbl_result.pack()
btn_roll.pack()

root.mainloop()


