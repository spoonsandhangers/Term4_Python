"""
Same game but using a class
"""
import tkinter as tk
import random as rd

class DiceGame(tk.Frame):
	def __init__(self, the_window):
		super().__init__()  # this invokes the constructor of the super class Frame
		self["width"] = 300  # sets the width of the greenFrame instance to 300
		self["height"] = 300  # sets the height of the greenframe instance to 300
		self["relief"] = "sunken"  # sets the relief of the greenframe instance to sunken
		self["border"] = 8
		self["bg"] = "green"
		self["padx"] = 8
		self["pady"] = 120  # changing the value of the padx and pady will change the label position.
		self.lbl_one = tk.Label(self, text="Not yet randomised")
		self.addLabel()
		self.btn_play = tk.Button(self, text="Randomise",
		                          command=self.roll,
		                          padx=5, pady=5,
		                          height=20)
		self.addButton()

		# this method creates a label and adds it to the frame.
	def addLabel(self):
		self.lbl_one.pack()

	def addButton(self):
		self.btn_play.pack()

	def roll(self):
		self.result = rd.randint(1,6)
		self.lbl_one.config(text=str(self.result))



window = tk.Tk()  # creates new base window.

window.title("My window")
window.geometry("300x300")  # width x height

# creates an instance of the ExampleFrame class
a_frame = DiceGame(window)
# adds the frame to the base window
a_frame.pack(expand=1, fill=tk.X)
window.mainloop()



