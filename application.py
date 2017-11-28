from tkinter import Label
from PIL import Image, ImageTk


class Application(Label):
	def __init__(self , parent , icon, icon_sel):
		super().__init__(parent)
		self.icon = ImageTk.PhotoImage(Image.open(icon))
		self.icon_sel = ImageTk.PhotoImage(Image.open(icon_sel))

		self.configure(image = self.icon)
		self.image = self.icon

		self.bind('<Enter>' , self.onEnter)
		self.bind('<Leave>' , self.onLeave)

	def onEnter(self, event):
		self.configure(image = self.icon_sel)
		self.image = self.icon_sel
	def onLeave(self , event):
		self.configure(image = self.icon)
		self.image = self.icon