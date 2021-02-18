"""
Usually a GUI is just to create the presentational features (frontend)
All functional code will be stored in other classes (backend)
However for the next task use a single class/ or functions to create a working game
There are several opportunities to extend the game if such an opportunity interests you.

Set an amount of credit
set the cost of a stake
generate 3 text symbols randomly out of (cherry, bell, lemon, star and 7s)
Extension - use images instead of text as the symbols.
"""
"""
Same game but using a class
"""
import tkinter as tk
from random import choice


class Fruity(tk.Frame):
	def __init__(self, the_window):
		super().__init__()  # this invokes the constructor of the super class Frame
		self["width"] = 300  # sets the width of the greenFrame instance to 300
		self["height"] = 300  # sets the height of the greenframe instance to 300
		self["relief"] = "sunken"  # sets the relief of the greenframe instance to sunken
		self["border"] = 8
		self["bg"] = "green"
		self["padx"] = 8
		self["pady"] = 120  # changing the value of the padx and pady will change the label position.
		self.lbl_one = tk.Label(self, text="Reel 1", bg="yellow", width=10)
		self.lbl_two = tk.Label(self, text="Reel 2", bg="pink", width=10)
		self.lbl_three = tk.Label(self, text="Reel 3", bg="yellow", width=10)
		self.lbl_result = tk.Label(self, text="result", bg="red", width=10)
		self.addLabels()
		self.btn_play = tk.Button(self, text="Play",
		                          command=self.roll,
		                          padx=5, pady=5)
		self.addButton()
		self.icons = ["cherry", "bell", "lemon", "orange", "star", "seven"]
		self.credit = 100


	def addLabels(self):
		self.lbl_one.grid(row=1, column=1)
		self.lbl_two.grid(row=1, column=2)
		self.lbl_three.grid(row=1, column=3)
		self.lbl_result.grid(row=2, column=2)

	def addButton(self):
		self.btn_play.grid(row=1, column=4)

	def roll(self):
		if self.credit >= 10:
			self.result1 = choice(self.icons)
			self.lbl_one.config(text=str(self.result1))
			self.result2 = choice(self.icons)
			self.lbl_two.config(text=str(self.result2))
			self.result3 = choice(self.icons)
			self.lbl_three.config(text=str(self.result3))
			self.check4win()
			self.credit -= 10
		else:
			self.lbl_result.config(text="No credit!")

	def check4win(self):
		if self.result1 == self.result2:
			if self.result3 == self.result2:
				self.lbl_result.config(text="Winner! + 50 credits")
				self.credit += 50
		else:
			self.lbl_result.config(text="No Match!")




window = tk.Tk()  # creates new base window.

window.title("My window")
window.geometry("300x300")  # width x height

# creates an instance of the ExampleFrame class
a_frame = Fruity(window)
# adds the frame to the base window
a_frame.pack(expand=1, fill=tk.X)
window.mainloop()



