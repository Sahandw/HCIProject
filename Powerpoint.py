from tkinter import Toplevel , Frame , E, S, N , W , Text ,\
	BOTH , Canvas , Label , RIDGE , Button
from PIL import Image, ImageTk
from Scrollbar import ScrollBar
import eventlog as log
class PPT(Toplevel):
	def __init__(self , parent ):
		super().__init__(parent)
		self.attributes('-topmost', 'true')
		self.resizable(width=False , height= False)
		self.minsize(750, 500)
		self.maxsize(750, 550)
		mainFrame = Frame(self , width = 500 ,height = 500 )
		mainFrame.grid(row = 0 , column = 0 , columnspan = 2)

		mainFrame.columnconfigure(0, weight = 1)
		mainFrame.columnconfigure(1, weight = 1)
		mainFrame.columnconfigure(0, pad = 20)

		sideBar = Frame(mainFrame)
		slides = Frame(mainFrame )
		sideBar.grid(row = 0, column = 0)
		slides.grid(row = 0 ,column = 1 )


		lbl = Label(slides )
		lbl.grid(row = 0 ,column = 1 , columnspan  =1  , sticky = N , padx = 50 , pady = 20)
		ScrollBar(sideBar , lbl , self).pack(side="top", fill="both", expand=True )

		self.protocol('WM_DELETE_WINDOW', self.onClose)


	def onClose(self):
		log.writeEvent('Close PPT')
		self.destroy()
