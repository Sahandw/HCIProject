from tkinter import Toplevel , Button , Frame , BOTH
from File import File
from PIL import Image, ImageTk
class Explorer(Toplevel):
	def __init__(self , folder):
		super().__init__(bg = 'white')
		self.f = folder
		self.title(self.f.name)
		self.selected = set()
		self.fr = Frame(self, bg = 'white')
		self.fr.pack(fill = BOTH , expand = True)
		for i,f in enumerate(folder.fileList):
			name = f.split('.')[0]
			format = f.split('.')[1]
			newFile = File(self.fr, name, format)
			k = int(i / 5)
			j = int( i % 5)
			newFile.grid(row = k , column = j , padx = 15 , columnspan = 1)


		self.attributes('-topmost' , 'true')

		self.fr.bind('<Button-1>' , self.onClick)


	def onClick(self ,event):
		for item in self.selected:
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

