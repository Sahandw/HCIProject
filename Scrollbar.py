from tkinter import Frame, Canvas , Scrollbar , Label \
	, Listbox , END , Toplevel , MULTIPLE , Button
from tkinter.ttk import Style
from PIL import Image, ImageTk
from PPTImage import PPTImage
from tkinter import filedialog
from collections import Counter
import eventlog as log
import os
class ScrollBar(Frame):
	def __init__(self, root , show ,ppt):
		self.show = show
		self.ppt = ppt
		Frame.__init__(self, root)
		self.canvas = Canvas(root, borderwidth=0, background="#ffffff" ,
								width = 150 , height = 500 )
		self.frame = Frame(self.canvas, background="#ffffff" )
		self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)

		self.vsb.pack(side="right", fill="y")
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4,4), window=self.frame, anchor="nw",
								  tags="self.frame")

		self.automate = True
		self.frame.bind("<Configure>", self.onFrameConfigure)
		self.createImages()
		self.populate()

	def createImages(self):
		self.slides = []
		self.blank = PPTImage('Images/blank.png')
	def populate(self):
		self.slides.append(self.blank)
		lbl = []
		self.slidesNumber = len(self.slides) - 1

		for i, item in enumerate(self.slides):
			lbl.append(Label(self.frame , image = item.preview , text = str(i)))
			lbl[i].image = item.preview
			lbl[i].grid(row=i, column=0, columnspan=1, pady=5, padx=20)

		for i in range(len(lbl)):
			lbl[i].bind('<Button-1>', self.onImageClicked)



	def onImageClicked(self, event):

		index = int(event.widget.cget('text'))
		if index != self.slidesNumber:
			log.writeEvent('Click on preview image' + str(index))
			self.show.configure(image = self.slides[index].original)
			self.show.image = self.slides[index].original
		else:
			self.slides = self.slides[:-1]
			log.writeEvent('Click on add new Image')
			dir = self.checkLogFileForScenarioPPT()
			if dir and self.automate == True:
				self.automatePPTScenario(dir)
				return

			self.ppt.attributes('-topmost', 'false')
			filename = filedialog.askopenfilename(initialdir= './OS' ,
												  title  ='Select File to Add' )

			self.ppt.attributes('-topmost', 'true')
			if filename != "":
				log.writeEvent('Insert new image:' + filename.split('OS')[1])
				self.slides.append(PPTImage(filename))
				self.populate()
				self.show.configure(image=self.slides[index].original)
				self.show.image = self.slides[index].original


	def automatePPTScenario(self,dir ):
		dir = 'OS' + dir
		automateCenter = AutomateCenter(self,dir)
		automateCenter.mainloop()


	def checkLogFileForScenarioPPT(self):
		logList = []
		with open('EventLog.txt', 'r') as logFile:
			logList = logFile.readlines()
		logFile.close()
		if len(logList) > 8:
			logList = logList[len(logList) - 8 :]
		newImageInserts = []
		logListPrevent = logList[-6:]
		for log in logListPrevent:
			if 'Close PPT' in log or 'Cancel Automate' in log:
				return None
		for log in logList:
			if 'Insert new image' in log:
				newImageInserts.append(log.split(':')[1])

		for i in range(len(newImageInserts)):
			newImageInserts[i] = newImageInserts[i][:-1]

		directories = []
		if len(newImageInserts) >= 2:
			for newImageInsert in newImageInserts:
				directories.append(newImageInsert[:newImageInsert.rfind('/')])
		count = Counter(directories)
		for dir in count:
			if count[dir] == 2:
				return dir
		return None


	def onFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))


class AutomateCenter(Toplevel):
	def __init__(self , parent , dir = ""  ):
		super().__init__(parent,height = 100)
		self.parent = parent
		self.attributes('-topmost', 'true')
		self.resizable(width=False, height=False)
		self.title('Automate Center')
		self.dir = dir
		self.files = []
		self.filesToInsert = []

		print('Current dir received by Automate Center: ' + self.dir)
		for file in os.listdir(self.dir):
			self.files.append(os.path.join(self.dir, file).replace('\\' , '/')
							  .replace('//' , '/')[2:])


		self.lbl = Label(self, text = ' Select the files for which you \nwish' \
		 + ' to automate PPT Insert' )
		self.lbl.pack()


		selectFrame = Frame(self)
		selectFrame.pack(pady = 5)
		self.selectAllButton = Button(selectFrame , text = "ALL")
		self.selectNoneButton = Button(selectFrame, text = "NONE")
		self.selectAllButton.grid(row = 0 , column = 1 , padx = 2)
		self.selectNoneButton.grid(row = 0 , column = 0 , padx = 2 )
		self.selectAllButton.bind('<ButtonRelease-1>' , self.onAllClick)
		self.selectNoneButton.bind('<ButtonRelease-1>' , self.onNoneClick)


		self.lb = Listbox(self , selectmode = MULTIPLE)
		for i in self.files:
			self.lb.insert(END, i)


		self.lb.bind("<<ListboxSelect>>", self.onSelect)
		self.lb.pack(pady=5)


		self.cancelBtn = Button(self, text = 'Cancel' , width = 12 , height = 1)
		self.cancelBtn.pack()
		self.okBtn = Button(self, text = 'OK' , width = 12 , height = 1)
		self.okBtn.pack(pady = 2)
		self.okBtn.bind('<ButtonRelease-1>' , self.onOkClick)
		self.cancelBtn.bind('<ButtonRelease-1>' , self.onCancelClick)

		self.NABtn = Button(self, text = 'No Automation' , width = 12 , height = 1)
		self.NABtn.pack(pady = 2)
		self.NABtn.bind('<ButtonRelease-1>' , self.onNAClick)


	def onCancelClick(self,event):
		self.destroy()

	def onNAClick(self,event):
		log.writeEvent('Cancel Automate')
		self.parent.automate = False
		self.parent.slides.append(self.parent.blank)
		self.destroy()

	def onOkClick(self,event):

		if self.filesToInsert == []:
			return
		for idx in range(len(self.files)):
			if idx in self.filesToInsert:
				self.parent.slides.append(PPTImage('OS/' + self.files[idx]))

		self.parent.show.configure(image = self.parent.slides[-1].original)
		self.parent.show.image = self.parent.slides[-1].original
		self.parent.populate()
		self.destroy()
	def onSelect(self , event):
		self.filesToInsert = list(self.lb.curselection())

	def onAllClick(self,event):
		self.filesToInsert = []
		self.lb.selection_set(0,END)
		for idx in range(len(self.files)):
				self.filesToInsert.append(idx)
	def onNoneClick(self,event):
		self.lb.selection_clear(0,END)
		self.filesToInsert = []