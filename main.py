from tkinter import Tk , BOTH , Frame , Toplevel , LEFT , RIGHT ,N ,X
from tkinter.ttk import Button
from PIL import Image, ImageTk
from Folder import Folder
from File import File
from Taskbar import Taskbar
import eventlog as log
from Recorder import Recorder

class OS(Frame):
    def __init__(self):
        super().__init__(bg = 'white')

        self.initUI()

        self.selected = set()
        self.topwindows = set()

        self.master.attributes('-topmost' , 'false')
    def initUI(self):
        self.master.attributes('-fullscreen' , True)
        self.pack(fill =BOTH , expand = 1)
        f = Folder(self,'images' , sorted(['cat.jpeg' , 'icon.png' , 'smile.jpg' , 'sky.jpg' , 'mountain.tiff',
                                    'sound.jpg' , 'os.jpg' , 'ml.jpg' , 'data.png' , 'logo.tiff']))
        f.grid(row = 0 , column = 0 , padx = 20 , pady = 5)

        f2 = Folder(self,'Movies')
        f2.grid(row = 1 , column = 0 , padx = 20 , pady = 5)

        f3 = Folder(self, 'Documents' , sorted(['HCI_course.pdf' , 'Assignment_P1.pdf' ,
                                         'P2.pdf' , 'CHI2016.pdf' , 'ICWSM17.pdf' ]))
        f3.grid(row = 2, column = 0 , padx = 20 , pady = 5)

        self.bind('<Button-1>' , self.onClick)



        taskbar = Taskbar(self)



    def onClick(self ,event):
        log.writeEvent('Click on Desktop')
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



def main():
    root = Tk()
    log.createFile()
    os = OS()
    print(Recorder.RecorderState)
    root.mainloop()

if __name__ == '__main__':
    main()
