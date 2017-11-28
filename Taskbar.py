from tkinter import Frame , Label , LEFT , RAISED
from application import Application
from Powerpoint import PPT
from Recorder import Recorder
import eventlog as log
class Taskbar(Frame):
	def __init__(self , parent , w = 400, h = 70 ):
		super().__init__(parent , width = w , height = h , borderwidth = 2 )
		self.parent = parent

		self.centerTaskbar(w = w , h = h)

		self.recorderWindow = None

		ppt = Application(self, 'Images/presentation.png' , 'Images/presentationsel.png')
		browser = Application(self, 'Images/browser.png' , 'Images/browsersel.png')
		self.recorder = Application(self, 'Images/recorder.png' , 'Images/recordersel.png')
		ppt.grid(row = 0 , column = 0 , padx = 10)
		browser.grid(row = 0 , column = 1 , padx = 10)
		self.recorder.grid(row = 0, column = 2 , padx = 10)


		ppt.bind('<Button-1>' , self.openPowerPoint)
		self.recorder.bind('<Button-1>' , self.openRecorder)

	def openPowerPoint(self , event):
		log.writeEvent('Open PPT')
		ppt = PPT(self.parent)
		ppt.mainloop()

	def openRecorder(self, event):
		if self.recorderWindow == None:
			self.recorderWindow = Recorder(self.parent)
			self.recorderWindow.mainloop()
			Recorder.RecorderState = 'Running'
		else:
			self.recorderWindow.deiconify()
			Recorder.RecorderState=  'Visible'


	def centerTaskbar(self  , w , h):
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = ( sw - w )/ 2
		y =  sh - h

		self.place(x = x,y = y)

