from tkinter import *


class wholeFrame(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)

		self.master = master
		self.init_window()

	def init_window(self):

		self.master.title("STS Team Sorting and Managing")
		self.pack(fill=BOTH, expand=1)
		quitButton = Button()

root = Tk()
app = wholeFrame(root)
root.mainloop()