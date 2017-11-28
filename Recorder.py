from tkinter import Toplevel , Button , TOP , \
    BOTTOM , RIGHT , S , Frame , BOTH, Listbox, \
    StringVar, END , Label , Entry , messagebox , MULTIPLE
from tkinter.ttk import Style
import eventlog as log
import os



class ScenarioList(Frame):
    def __init__(self , parent):
        super().__init__(parent )

        self.initUI()

    def initUI(self):
        self.style = Style()
        self.style.theme_use('clam')
        self.acts = []
        self.selected = []
        self.scDir = 'Scenarios/'


        listFrame = Frame(self)
        listFrame.pack(pady = 15)



        self.lb = Listbox(listFrame)
        self.lb.grid(row = 0 , column = 0 , columnspan = 2 ,padx = 5)
        self.lb.bind("<<ListboxSelect>>", self.onSelect)
        self.updateList()

        deleteBtn = Button(listFrame, text = 'Delete' )
        deleteBtn.grid(row= 0 , column = 2 , padx = 1)
        deleteBtn.bind('<ButtonRelease-1>', self.onDeleteClick)


        self.lbl = Label(self, text = 'Scenario Name: ')
        self.lbl.pack()
        self.scName = Entry(self , width = 25)
        self.scName.pack()
        self.recBtn = Button(self, text = 'Record' , width = 10 , height = 1)
        self.recBtn.pack(pady = 10)
        self.recBtn.bind('<ButtonRelease-1>' , self.onButtonClick)

    def onButtonClick(self , event):
        if self.recBtn['text'] == 'Record':
            if self.scName.get() != "":
                Recorder.RecorderFileName = self.scName.get()
                log.writeEvent('Record')
                Recorder.RecorderState = 'recording'
                self.recBtn['text'] = 'Save'
            else:
                messagebox.showerror("No Scenario Name" , " You Should Specify a Name for your Scenario" +
                                     " before starting to record")
                return
        else:
            if self.scName.get() == "":
                messagebox.showerror("No Scenario Name" , " You Should Specify a Name for your Scenario" )
                return
            log.writeEvent('Save')
            self.recBtn['text'] = 'Record'
            log.saveRecordedScenario(self.scName.get())
            self.updateList()
            scenarioEvents = log.getScenarioEvents(self.scName.get())
            scc= ScenarioCenter(self ,scenarioEvents , self.scName.get() )
            scc.mainloop()


    def updateList(self):
        self.lb.delete(0,END)
        self.acts = []
        for file in os.listdir(self.scDir):
            self.acts.append(file.split('.')[0])
        for i in self.acts:
            self.lb.insert(END, i)

    def onSelect(self, val):
        self.selected = self.lb.curselection()

    def onDeleteClick(self, event):

        log.deleteScenarioFile(self.acts[self.selected[0]])
        self.updateList()



class ScenarioCenter(Toplevel):
    def __init__(self , parent , scEvents ,scName ):
        super().__init__(parent , height = 100)
        self.parent = parent
        self.attributes('-topmost', 'true')
        self.resizable(width=False, height=False)
        self.title('Scenario Center')
        self.scEvents = scEvents
        self.scName = scName
        editListFrame = Frame(self)
        editListFrame.pack()
        self.currentSelection = []


        self.lb = Listbox(editListFrame , selectmode = MULTIPLE)
        for i in self.scEvents:
            self.lb.insert(END, i)


        self.lb.bind("<<ListboxSelect>>", self.onSelect)
        self.lb.grid(row = 0 , column = 0 , columnspan = 2)

        self.DeleteBtn = Button(editListFrame, text = 'Delete' , width = 12 , height = 1)
        self.DeleteBtn.grid(row = 0 , column = 2 , padx = 5)
        self.DeleteBtn.bind('<ButtonRelease-1>' , self.onDeleteClick)

        self.cancelBtn = Button(editListFrame, text = 'Cancel' , width = 12 , height = 1)
        self.cancelBtn.grid(row = 1 , column = 1 , pady = 2)
        self.cancelBtn.bind('<ButtonRelease-1>' , self.onCancelClick)
        self.okBtn = Button(editListFrame, text = 'OK' , width = 12 , height = 1)
        self.okBtn.grid(row = 1 , column = 2 , padx = 1 , pady = 2)
        self.okBtn.bind('<ButtonRelease-1>' , self.onOkClick)

    def onCancelClick(self,event):
        log.deleteScenarioFile(self.scName)
        self.parent.updateList()
        self.destroy()

    def onDeleteClick(self,event):
        print(self.scEvents)
        self.lb.delete(0,END)
        for idx in self.currentSelection[::-1]:
            del self.scEvents[idx]
        for i in self.scEvents:
            self.lb.insert(END, i)

    def onOkClick(self, event):
        log.saveSelectedScenario(self.scName,self.scEvents)
        self.destroy()

    def onSelect(self,event):
        self.currentSelection = list(self.lb.curselection())
class Recorder(Toplevel):
    RecorderState = 'close'
    RecorderFileName = ''
    def __init__(self , parent ):
        super().__init__(parent)
        self.parent = parent
        self.attributes('-topmost', 'true')
        self.resizable(width=False, height=False)
        self.position()
        self.title('AutoPilot')
        self.protocol('WM_DELETE_WINDOW', self.onClose)
        self.scenarioList = ScenarioList(self)
        self.scenarioList.pack()
        self.ActionList = []

    def position(self):
        x = self.parent.winfo_screenwidth()
        y = self.parent.winfo_screenheight()
        w = 200
        h = 300
        self.geometry("%dx%d+%d+%d" % (w,h, x - w, 0 ))
        self.resizable(width=False, height=False)

    def onClose(self):
        self.withdraw()
        Recorder.RecorderState = 'hidden'





