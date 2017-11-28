from tkinter import Frame , Label , Toplevel
from PIL import Image, ImageTk
import eventlog as log
class File(Frame):
	def __init__(self, parent, name , format = "" ):
		super().__init__(parent, width = 100, height = 100 , bg = 'white')
		self.root = parent
		self.name = name
		self.format = format
		self.initUI()
		#self.image = ImageTk.PhotoImage(Image.open('Images/' + name))

	def initUI(self):

		icon = ImageTk.PhotoImage(Image.open('Images/file.png'))
		icon_sel = ImageTk.PhotoImage(Image.open('Images/fileselected.png'))
		self.img = Label(self , image = icon , bg = 'white')
		self.lbl = Label(self, text = self.name , bg = 'white')
		self.img.image = icon
		self.img.pack()
		self.lbl.pack()

		self.img.bind('<Button-1>' , self.onClick )
		self.lbl.bind('<Button-1>' , self.onClick)


	def onClick(self,event):
		itemName = event.widget.master.name
		log.writeEvent('Click on ' + itemName + ' File')
		for item in self.root.master.selected:
			if type(item).__name__ == 'Folder':
				icon = ImageTk.PhotoImage(Image.open('Images/folder.png'))
				item.img.configure(image = icon)
				item.img.image = icon
				item.lbl.configure(fg = '#000')
			if type(item).__name__ == 'File':
				icon = ImageTk.PhotoImage(Image.open('Images/file.png'))
				item.img.configure(image = icon)
				item.img.image = icon
				item.lbl.configure(fg = '#000')
		icon_sel = ImageTk.PhotoImage(Image.open('Images/fileselected.png'))
		self.img.configure(image = icon_sel)
		self.img.image = icon_sel
		self.lbl.configure(fg = '#103c74')
		self.root.master.selected.add(event.widget.master)






