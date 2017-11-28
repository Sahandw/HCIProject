from tkinter import Frame , Label , Toplevel
from PIL import Image, ImageTk
from explorer import Explorer
from File import File
import eventlog as log
class Folder(Frame):

	def __init__(self, parent, name , fileList = None):
		super().__init__(parent , width = 100, height = 100 , bg = 'white')
		self.root = parent
		self.name = name
		self.explorerList = set()
		if fileList == None:
			self.fileList = sorted(['The Terminal.mkv', 'The Godfather.mp4' ,
						 'Forrest Gump.mkv' , 'Departed.mp4' ,
						 'The LOR.mkv' , 'Twelve Angry Men.mp4' ,
						 'The planet earth.mp4'])
		else:
			self.fileList = fileList


		self.initUI()


	def initUI(self):

		icon = ImageTk.PhotoImage(Image.open('Images/folder.png'))
		icon_sel = ImageTk.PhotoImage(Image.open('Images/folderselected.png'))
		self.img = Label(self , image = icon , bg = 'white')
		self.lbl = Label(self, text = self.name , bg = 'white')
		self.img.image = icon
		self.img.pack()
		self.lbl.pack()
		self.img.bind('<Button-1>' , self.onClick )
		self.lbl.bind('<Button-1>' , self.onClick)
		self.img.bind('<Double-Button-1>' , self.onDoubleClick)
		self.lbl.bind('<Double-Button-1>' , self.onDoubleClick)

	def onDoubleClick(self, event):
		itemName = event.widget.master.name
		log.writeEvent('DoubleClick on ' + itemName + ' Folder')
		top = Explorer(self)
		self.root.topwindows.add(top)
		self.explorerList.add(top)
		top.mainloop()


	def onClick(self,event):
		itemName = event.widget.master.name
		log.writeEvent('Click on ' + itemName + ' Folder')

		for item in self.root.selected:
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
		icon_sel = ImageTk.PhotoImage(Image.open('Images/folderselected.png'))
		self.img.configure(image = icon_sel)
		self.img.image = icon_sel
		self.lbl.configure(fg = '#103c74')
		self.root.selected.add(event.widget.master)
		#print(self.root.selected)





