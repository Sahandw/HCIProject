from tkinter import Tk ,RIGHT, BOTH, RAISED , LEFT ,X , N , E, W,S, \
    Text , BooleanVar,  Canvas
from tkinter.ttk import Frame , Button , Style , Label , Entry , Checkbutton


class App(Frame):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        self.master.title("Application")
        self.pack(fill =BOTH , expand = 1)
        self.centerWindow()

        self.style = Style()
        self.style.theme_use('clam')

        # absolute positioning
        #quitbutton = Button(self, text = "Quit" , command= self.quit)
        #quitbutton.place(x = 50 , y = 50)

        # pack layout manager
        '''
        self.master.title("Review")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Title", width=7)
        lbl1.pack(side=LEFT, padx=10, pady=10)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=10, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Author", width=7)
        lbl2.pack(side=LEFT, padx=10, pady=10)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=10, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=7)
        lbl3.pack(side=LEFT, anchor=N, padx=10, pady=10)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=10, padx=10, expand=True)
        '''



        # Grid layout manager
        '''
        self.master.title('Window')
        self.pack(fill = BOTH , expand = True)


        self.columnconfigure(1, weight =1 )
        self.columnconfigure(3, pad = 7)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(5, pad = 7)

        lbl = Label(self, text = 'Window')
        lbl.grid(sticky = W , pady = 4 , padx = 5)

        area = Text(self)
        area.grid(row = 1 , column = 0 , columnspan = 2 , rowspan = 4 ,
                  padx = 5 , sticky = E + W + S + N)

        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text="Help")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=3)
        '''

        # CheckBox
        '''
        self.master.title("Checkbutton")

        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()

        cb = Checkbutton(self, text="Show title",
            variable=self.var, command=self.onClick)

        cb.place(x=50, y=50)
        '''


        # drawing
        '''
        canvas = Canvas(self)
        canvas.create_line(15,25, 200,25)


        canvas.create_line(300, 35, 300, 200, dash=(14, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        canvas.pack(fill=BOTH, expand=1)

        canvas.create_rectangle(30, 10, 120, 80,
            outline="#fb0", fill="#fb0")
        canvas.create_rectangle(150, 10, 240, 80,
            outline="#f50", fill="#f50")
        canvas.create_rectangle(270, 10, 370, 80,
            outline="#05f", fill="#05f")
        canvas.pack(fill=BOTH, expand=1)

        canvas.create_oval(10, 10, 80, 80, outline="#f11",
            fill="#1f1", width=2)
        canvas.create_oval(110, 10, 210, 80, outline="#f11",
            fill="#1f1", width=2)
        canvas.create_rectangle(230, 10, 290, 60,
            outline="#f11", fill="#1f1", width=2)
        canvas.create_arc(30, 200, 90, 100, start=0,
            extent=210, outline="#f11", fill="#1f1", width=2)

        points = [150, 100, 200, 120, 240, 180, 210,
            200, 150, 150, 100, 200]
        canvas.create_polygon(points, outline='#f11',
            fill='#1f1', width=2)

        canvas.create_text(20, 30, anchor=W, font="Purisa",
            text="Most relationships seem so transitory")
        canvas.create_text(20, 60, anchor=W, font="Purisa",
            text="They're good but not the permanent one")
        canvas.create_text(20, 130, anchor=W, font="Purisa",
            text="Who doesn't long for someone to hold")
        canvas.create_text(20, 160, anchor=W, font="Purisa",
            text="Who knows how to love without being told")
        canvas.create_text(20, 190, anchor=W, font="Purisa",
            text="Somebody tell me why I'm on my own")
        canvas.create_text(20, 220, anchor=W, font="Purisa",
            text="If there's a soulmate for everyone")
        canvas.pack(fill=BOTH, expand=1)
        '''
    def onClick(self):
        if self.var.get() == True:
            self.master.title("Checkbutton")
        else:
            self.master.title("")

    def centerWindow(self , w= 500 , h = 500):
        sw =  self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2

        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))





def main():
    root = Tk()
    app = App()
    root.mainloop()











if __name__ == '__main__':
    main()